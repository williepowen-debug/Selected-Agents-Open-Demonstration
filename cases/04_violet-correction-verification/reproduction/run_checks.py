#!/usr/bin/env python3
"""Offline regression contrast over three frozen, source-derived snapshots.

This harness supplies I/O and synthetic evidence; it does not implement a write
gate, parser, basis-stamping rule, or replacement main(). See PROVENANCE.md.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import socket
import sys
import tempfile
import types
from contextlib import redirect_stdout
from datetime import date, datetime
from pathlib import Path
from unittest.mock import patch

import pandas as pd

HERE = Path(__file__).resolve().parent
TARGET = "2001-01-04"
REFERENCE = {"vix": 20.0, "vix9d": 18.0, "vix3m": 24.0,
             "vix6m": 26.0, "vvix": 90.0, "skew": 120.0}
MIRROR_SKEW = 110.0
HEADER = ["date", *REFERENCE, "basis", "vix3m_vix_ratio",
          "vix9d_vix_ratio", "regime", "unrelated_note"]
VERSIONS = ("transport_only", "per_run_guard", "stateless_guard")
CASES = (
    ("1_transport_503", False, ("503",)),
    ("2_html_200", False, ("html",)),
    ("3_missing_date", False, ("missing",)),
    ("4_complete_control", False, ("good",)),
    ("5_provisional_fill", True, ("missing",)),
    ("6_repeat_run", True, ("missing", "missing")),
    ("7_recovery_control", True, ("missing", "good")),
)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


class FrozenDate(date):
    @classmethod
    def today(cls):
        return cls(2001, 1, 5)


def unavailable(*args, **kwargs):
    raise RuntimeError("Outside the offline spot-only reproduction boundary")


def load_snapshot(version):
    manifest = json.loads((HERE / "snapshots" / "manifest.json").read_text())
    path = HERE / "snapshots" / f"{version}.py"
    source = path.read_bytes()
    require(hashlib.sha256(source).hexdigest() == manifest[version]["snapshot_sha256"],
            f"Snapshot changed: {version}; preserve historical versions")
    module = types.ModuleType(version)
    module.__dict__.update(argparse=argparse, csv=csv, io=io,
                           date=FrozenDate, datetime=datetime,
                           determine_regime=lambda value: "OMITTED",
                           backfill_m1m2=unavailable)
    exec(compile(source, str(path), "exec"), module.__dict__)
    return module


def publisher_csv(symbol, include_target):
    value = REFERENCE[symbol.lower()]
    if symbol in ("SKEW", "VVIX"):
        header = f"DATE,{symbol}\n"
        row = lambda day: f"{day},{value}\n"
    else:
        header = "DATE,OPEN,HIGH,LOW,CLOSE\n"
        row = lambda day: f"{day},{value},{value},{value},{value}\n"
    return header + row("01/03/2001") + (row("01/04/2001") if include_target else "")


def external_sources(mode):
    """Use real pandas, but replace requests/yfinance with strict fixture adapters."""
    calls = {"publisher": [], "mirror": []}
    requests = types.ModuleType("requests")
    requests.RequestException = RuntimeError

    def get(url, timeout=None, headers=None):
        prefix = "https://cdn.cboe.com/api/global/us_indices/daily_prices/"
        require(url.startswith(prefix) and url.endswith("_History.csv"),
                f"Unexpected request: {url}")
        symbol = url[len(prefix):-len("_History.csv")]
        require(symbol.lower() in REFERENCE, f"Unexpected series: {symbol}")
        calls["publisher"].append(symbol.lower())
        if symbol == "SKEW" and mode == "503":
            return types.SimpleNamespace(status_code=503, text="unavailable")
        if symbol == "SKEW" and mode == "html":
            return types.SimpleNamespace(status_code=200, text="<!DOCTYPE html><html>Error</html>")
        return types.SimpleNamespace(status_code=200, text=publisher_csv(
            symbol, not (symbol == "SKEW" and mode == "missing")))

    requests.get = get
    yf = types.ModuleType("yfinance")

    class Ticker:
        def __init__(self, symbol):
            require(symbol.startswith("^") and symbol[1:].lower() in REFERENCE,
                    f"Unexpected mirror ticker: {symbol}")
            self.key = symbol[1:].lower()

        def history(self, period=None, auto_adjust=False):
            calls["mirror"].append(self.key)
            value = MIRROR_SKEW if self.key == "skew" else REFERENCE[self.key]
            return pd.DataFrame({"Close": [value]}, index=pd.to_datetime([TARGET]))

    yf.Ticker = Ticker
    return requests, yf, calls


def run_case(module, blank, modes):
    """Execute source main() and inspect the persisted row after EVERY step."""
    row = {"date": TARGET, **REFERENCE, "basis": "SETTLE",
           "vix3m_vix_ratio": 1.2, "vix9d_vix_ratio": 0.9,
           "regime": "OMITTED", "unrelated_note": "preserve-me"}
    if blank:
        row.update(skew="", basis="")
    observed = []
    with tempfile.TemporaryDirectory(prefix="violet-demo-") as tmp:
        ledger = Path(tmp) / "synthetic.tsv"
        with ledger.open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=HEADER, delimiter="\t")
            writer.writeheader()
            writer.writerow(row)
        module.DAILY_LOG = ledger
        for mode in modes:
            requests, yf, calls = external_sources(mode)
            module.requests = requests
            with patch.dict(sys.modules, {"requests": requests, "yfinance": yf}), \
                    patch.object(socket.socket, "connect", unavailable), \
                    patch.object(socket, "create_connection", unavailable), \
                    redirect_stdout(io.StringIO()):
                rc = module.main(["--spot-only"])
            require(sorted(calls["publisher"]) == sorted(REFERENCE), "Publisher path was not exercised")
            require(sorted(calls["mirror"]) == sorted(REFERENCE), "Mirror path was not exercised")
            with ledger.open(newline="") as stream:
                reader = csv.DictReader(stream, delimiter="\t")
                saved = list(reader)
                require(reader.fieldnames == HEADER, "Header changed")
            require(len(saved) == 1 and saved[0]["date"] == TARGET, "Row identity/count changed")
            saved = saved[0]
            require(saved["unrelated_note"] == "preserve-me", "Unrelated state changed")
            for key, value in REFERENCE.items():
                if key != "skew":
                    require(float(saved[key]) == value, f"Control column changed: {key}")
            require(float(saved["vix3m_vix_ratio"]) == 1.2 and
                    float(saved["vix9d_vix_ratio"]) == 0.9, "Derived control changed")
            require(saved["skew"].strip() != "", "Missing persisted SKEW value")
            observed.append((float(saved["skew"]), saved["basis"], rc))
    return observed


def expected_trace(version, index):
    """Explicit expected historical outputs, NOT a copy of the production gate."""
    settled = (120.0, "SETTLE", 0)
    provisional = (110.0, "", 0)
    bad = (110.0, "SETTLE", 0)
    transport = (120.0, "SETTLE", 2)
    first = bad if version == "transport_only" else provisional
    second = provisional if version == "stateless_guard" else bad
    return (
        [transport],
        [bad] if version == "transport_only" else [transport],
        [bad] if version == "transport_only" else [settled],
        [settled],
        [first],
        [first, second],
        [first, settled],
    )[index]


def verify_version(module, version):
    results = []
    for index, (name, blank, modes) in enumerate(CASES):
        trace = run_case(module, blank, modes)
        want = expected_trace(version, index)
        require(trace == want, f"{version}/{name}: got {trace}, expected {want}")
        # For recovery, report the terminal control separately; earlier steps
        # are still checked against the exact historical trace above.
        checked = trace[-1:] if index == 6 else trace
        safe = all(not (value == MIRROR_SKEW and basis == "SETTLE")
                   for value, basis, rc in checked)
        results.append("HOLDS" if safe else "DEFECT")
    return results


def selftest():
    """Reject a moving baseline and a 'repair' that stops writing altogether."""
    controls = []
    controls.append(("fixed code substituted for historical baseline",
                     load_snapshot("stateless_guard"), "transport_only",
                     "transport_only/2_html_200"))
    inert = load_snapshot("stateless_guard")
    inert.write_merged = lambda header, rows: None
    controls.append(("ledger writer disabled", inert, "stateless_guard",
                     "Missing persisted SKEW value"))
    for label, module, version, expected_error in controls:
        try:
            verify_version(module, version)
        except AssertionError as error:
            require(expected_error in str(error), f"Wrong rejection for {label}: {error}")
            print(f"REJECTED as required: {label}")
        else:
            raise AssertionError(f"Harness failed to reject: {label}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selftest", action="store_true", help="also test two harness negative controls")
    args = parser.parse_args()
    results = {version: verify_version(load_snapshot(version), version) for version in VERSIONS}
    print(f"Python {sys.version.split()[0]}; pandas {pd.__version__}; synthetic data only")
    print(f"{'case':25s} {'transport_only':17s} {'per_run_guard':17s} stateless_guard")
    for index, (name, _, _) in enumerate(CASES):
        print(f"{name:25s} " + " ".join(f"{results[v][index]:17s}" for v in VERSIONS))
    print("PASS: 21/21 expected case-version traces reproduced (including expected defects).")
    if args.selftest:
        selftest()
        print("PASS: 2/2 harness negative controls rejected.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}", file=sys.stderr)
        raise SystemExit(1)
