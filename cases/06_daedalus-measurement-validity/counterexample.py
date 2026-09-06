"""Synthetic non-identification illustration; no private logs or model calls."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path


def require(condition, message):
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def project_to_logs(world):
    # The historical count fields do not encode the decision timing below.
    return {
        "touches": tuple((key, 1) for key in world if key in ("A", "B")),
        "correction_entries": ("C",),
        "amendment_stamps": (),
    }


def main():
    evidence = Path(__file__).resolve().parent / "evidence"
    manifest = json.loads((evidence / "manifest.json").read_text())
    expected = manifest["public_sha256"]["source-excerpts.md"]
    actual = hashlib.sha256((evidence / "source-excerpts.md").read_bytes()).hexdigest()
    require(actual == expected, "archived source excerpt hash differs")

    worlds = (
        {"A": "before", "B": "before", "C": "after"},
        {"A": "after", "B": "after", "C": "after"},
    )
    logs = [project_to_logs(world) for world in worlds]
    require(logs[0] == logs[1], "illustration needs identical observed logs")
    observed = logs[0]
    touches = len(observed["touches"])
    corrections = len(observed["correction_entries"]) + len(observed["amendment_stamps"])
    ratio = Fraction(touches, touches + corrections)
    true_shares = [Fraction(list(world.values()).count("before"), len(world)) for world in worlds]
    require(ratio == Fraction(2, 3), "unexpected illustrative ratio")
    require(true_shares == [Fraction(2, 3), Fraction(0)], "unexpected underlying shares")
    require(true_shares[0] != true_shares[1], "histories must differ on target quantity")

    print("PASS: archived excerpt matches its public hash.")
    print(f"Same synthetic logs: 2 defect-bearing touches + 1 correction entry; ratio {ratio}.")
    print(f"Possible pre-decision shares: {true_shares[0]} versus {true_shares[1]}.")
    print("Illustration only: no production renderer, private-log census, or model experiment run.")


if __name__ == "__main__":
    main()
