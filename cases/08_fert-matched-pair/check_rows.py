#!/usr/bin/env python3
"""Check the FERT matched-pair evidence: public hashes, dates, the absence of probabilities, and the magnitude arithmetic.

Standard library only. Verifies the bundled files against the manifest and the claims the case README makes about them.
It does not open the private repository, re-source the graded outcomes, or rerun any agent.
"""
import csv, hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
EV = HERE / "evidence"

def sha256(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)

def main() -> int:
    manifest = json.loads((EV / "manifest.json").read_text(encoding="utf-8"))
    for rel, want in manifest["public_sha256"].items():
        got = sha256(HERE / rel)
        if got != want:
            fail(f"{rel} sha256 {got[:12]} != manifest {want[:12]}")
    print(f"PASS: {len(manifest['public_sha256'])} bundled evidence files match their manifest hashes.")

    with (EV / "rows.tsv").open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    by_id = {r["ID"]: r for r in rows}
    if set(by_id) != {"FERT-08", "FERT-10"}:
        fail(f"unexpected row set {sorted(by_id)}")

    for rid, r in by_id.items():
        if r["Date"] != "2026-03-20":
            fail(f"{rid} Date {r['Date']} != 2026-03-20")
        if r["Date_Resolved"] != "2026-08-17":
            fail(f"{rid} Date_Resolved {r['Date_Resolved']} != 2026-08-17")
        if "%" in r["Confidence"]:
            fail(f"{rid} Confidence cell carries a percentage: {r['Confidence']!r}")
    if by_id["FERT-08"]["Status"] != "MISS" or by_id["FERT-10"]["Status"] != "HIT":
        fail("statuses are not MISS (FERT-08) and HIT (FERT-10)")
    print("PASS: both rows dated 2026-03-20, both graded 2026-08-17, one HIT and one MISS.")
    print("PASS: neither Confidence cell is a probability (convergence scores: "
          f"{by_id['FERT-08']['Confidence']!r}, {by_id['FERT-10']['Confidence']!r}).")

    if by_id["FERT-08"]["Resolve_By"] != by_id["FERT-08"]["Date_Resolved"]:
        fail("FERT-08 Resolve_By was expected to equal its grade date")
    print("NOTE: FERT-08 Resolve_By equals its grade date; the row was registered and resolved in one sitting.")

    claimed, actual = 77.0, 12.8
    ratio = claimed / actual
    if not (5.9 < ratio < 6.1):
        fail(f"77 / 12.8 = {ratio:.2f}, README says about six times")
    outcome = by_id["FERT-08"]["Outcome"]
    if "12.8 mtpa" not in outcome or "~6x" not in outcome:
        fail("FERT-08 outcome text does not carry the 12.8 mtpa figure and the ~6x magnitude")
    print(f"PASS: 77 / 12.8 = {ratio:.2f}; the grade's '~6x' magnitude is arithmetic on figures the row itself states.")

    march = (EV / "march_claims.md").read_text(encoding="utf-8")
    for needle in ("77 mtpa", "India emergency purchases | 3 |", "Qatar LNG → fertilizer production | 4 |"):
        if needle not in march:
            fail(f"March excerpt lacks {needle!r}")
    print("PASS: March excerpt carries the 77 mtpa claim and both convergence-vector scores (4 and 3).")
    fc = manifest["fleet_context"]
    print(f"Context: {fc['rows_with_bare_HIT_token'] + fc['rows_with_bare_MISS_token']} rows across "
          f"{fc['ledgers_named_PREDICTIONS.tsv']} ledgers carry a bare HIT or MISS token at the pinned commit.")
    print("Not checked here: the graded outcomes' cited figures (IPL tender, QatarEnergy update) were not re-sourced for this portfolio.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
