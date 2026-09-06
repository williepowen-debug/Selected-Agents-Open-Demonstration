#!/usr/bin/env python3
"""Offline contrast of historical suite grading; the validator is an exit-code fixture."""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCENARIOS = ("expected_results", "controls_exit_1", "baseline_exit_1")
PROBE = "import json, pathlib, sys\nsys.exit(json.loads(pathlib.Path(__file__).with_suffix('.json').read_text())['exit_code'])\n"


class CheckFailure(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise CheckFailure(message)


def load_snapshot(name):
    manifest = json.loads((HERE / "snapshots/manifest.json").read_text())
    path = HERE / "snapshots" / f"{name}.py"
    data = path.read_bytes()
    require(hashlib.sha256(data).hexdigest() == manifest["snapshots"][name]["public_sha256"],
            f"{name}: snapshot hash mismatch")
    return data.decode()


@dataclass
class Trace:
    exit_code: int
    stdout: str
    baseline_code: int
    case_codes: list[int]
    fixtures: list[dict]


def execute(source, scenario, *, break_setup=False):
    """Execute retained main/run with explicit adapters; exceptions are never verdicts."""
    require(scenario in SCENARIOS, "unknown scenario")
    namespace = {
        "__name__": "historical_suite", "__file__": str(HERE / "snapshots/source.py"),
        "Path": Path, "shutil": shutil, "subprocess": subprocess,
        "sys": sys, "tempfile": tempfile,
    }
    exec(compile(source, "historical_suite", "exec"), namespace)
    cases = namespace["CASES"]
    fixtures = []

    def build_sandbox(tmp):
        if break_setup:
            raise FileNotFoundError("deliberately unavailable fixture input")
        script = tmp / "exit_probe.py"
        script.write_text(PROBE, encoding="utf-8")
        code = 1 if scenario == "baseline_exit_1" else 0
        script.with_suffix(".json").write_text(json.dumps({"exit_code": code}))
        return script

    def apply_case(tmp, ledger, column, value):
        index = len(fixtures)
        require(index < len(cases), "unexpected extra case")
        label, expected_ledger, expected_column, expected_value, negative = cases[index]
        require((ledger, column, value) == (expected_ledger, expected_column, expected_value),
                f"case order/arguments changed at {index}")
        code = 2 if negative else (1 if scenario == "controls_exit_1" else 0)
        # These are declared process results, not results calculated from the cell value.
        fixture = {"label": label, "ledger": ledger, "column": column,
                   "value": value, "negative": negative, "exit_code": code}
        (tmp / "exit_probe.json").write_text(json.dumps(fixture))
        fixtures.append(fixture)

    namespace.update(build_sandbox=build_sandbox, apply_case=apply_case)
    output = io.StringIO()
    try:
        with contextlib.redirect_stdout(output):
            code = namespace["main"]()
    except Exception as error:
        raise CheckFailure(f"fixture/suite execution failed before a valid trace: {error}") from error
    text = output.getvalue()
    baseline = re.findall(r"BASELINE.*?rc=(-?\d+)", text)
    require(len(baseline) == 1, "missing or duplicate baseline diagnostic")
    case_codes = [int(m) for m in re.findall(r"^.*?rc=(-?\d+)\s+(?:CATCH|PASS)\s", text, re.M)]
    return Trace(code, text, int(baseline[0]), case_codes, fixtures)


def check_trace(version, scenario, trace):
    """An independent, explicit expected trace; no reuse of the historical predicate."""
    if scenario == "baseline_exit_1":
        require(trace.baseline_code == 1 and trace.exit_code == 1,
                f"{version}: baseline failure not propagated")
        require(not trace.case_codes and not trace.fixtures and "WRONG:" not in trace.stdout,
                f"{version}: cases ran or were scored after a failed baseline")
        require("SANDBOX DIRTY" in trace.stdout, "baseline diagnostic missing")
        return
    require(trace.baseline_code == 0, "comparison requires a clean baseline")
    require(len(trace.case_codes) == len(trace.fixtures) == 31, "expected 31 executed cases")
    negative_codes = [code for code, f in zip(trace.case_codes, trace.fixtures) if f["negative"]]
    control_codes = [code for code, f in zip(trace.case_codes, trace.fixtures) if not f["negative"]]
    require(negative_codes == [2] * 21, "negative cases did not retain expected status")
    expected_control = 1 if scenario == "controls_exit_1" else 0
    require(control_codes == [expected_control] * 10, "wrong control statuses")
    expected_wrong = 10 if version == "after" and scenario == "controls_exit_1" else 0
    summaries = re.findall(r"31 cases — 21 defects injected, 10 real-form controls — WRONG: (\d+)", trace.stdout)
    require(summaries == [str(expected_wrong)], f"{version}/{scenario}: wrong scoring summary")
    require(trace.exit_code == (1 if expected_wrong else 0), f"{version}/{scenario}: wrong suite exit")
    require(trace.stdout.count("UNEXPECTED EXIT 1 (want 0)") == expected_wrong,
            f"{version}/{scenario}: wrong number of unexpected-exit diagnostics")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selftest", action="store_true", help="also reject two invalid reproduction controls")
    args = parser.parse_args()
    snapshots = {name: load_snapshot(name) for name in ("before", "after")}
    print("PASS: both source-derived snapshots match their manifest hashes.")
    print("Fixture boundary: real subprocess exits; no GPU validator or market data.")
    for name, source in snapshots.items():
        for scenario in SCENARIOS:
            trace = execute(source, scenario)
            check_trace(name, scenario, trace)
            print(f"PASS: {name:6} {scenario:18} baseline={trace.baseline_code} "
                  f"cases={len(trace.case_codes)} suite_rc={trace.exit_code}")
    print("PASS: 6/6 expected version/scenario traces reproduced, including the historical false pass.")
    if args.selftest:
        try:
            check_trace("before", "controls_exit_1", execute(snapshots["after"], "controls_exit_1"))
        except CheckFailure:
            print("REJECTED as required: repaired code substituted for historical baseline.")
        else:
            raise CheckFailure("self-test accepted a repaired historical baseline")
        try:
            execute(snapshots["after"], "controls_exit_1", break_setup=True)
        except CheckFailure as error:
            require(isinstance(error.__cause__, FileNotFoundError), "setup control failed for the wrong reason")
            print("REJECTED as required: setup exception is not a successful fault-detection trace.")
        else:
            raise CheckFailure("self-test accepted a broken setup")
        print("PASS: 2/2 reproduction controls rejected.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
