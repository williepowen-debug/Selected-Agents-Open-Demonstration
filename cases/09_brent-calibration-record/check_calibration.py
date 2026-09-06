#!/usr/bin/env python3
"""Check the BRENT calibration-record evidence: hashes, status counts, both Brier scores, the moved marks, the dates, the redactions.

Standard library only. Everything is recomputed from the bundled files; the private repository is not opened,
no outcome is re-sourced, and no agent is run.
"""
import csv, hashlib, json, pathlib, re, sys
from collections import Counter, defaultdict

HERE = pathlib.Path(__file__).resolve().parent
EV = HERE / "evidence"
TSV = dict(delimiter="\t", quoting=csv.QUOTE_NONE)

def fail(msg):
    print(f"FAIL: {msg}"); sys.exit(1)

def marks(cell):
    """Every percentage in a Confidence cell, in order. Bare cells have one; the desk's newer compound cells carry a trail."""
    return [float(x) / 100 for x in re.findall(r"(\d+(?:\.\d+)?)%", cell)]

def head(status):
    return status.split(" ")[0].split("(")[0]

def main():
    manifest = json.loads((EV / "manifest.json").read_text(encoding="utf-8"))
    for rel, want in manifest["public_sha256"].items():
        got = hashlib.sha256((HERE / rel).read_bytes()).hexdigest()
        if got != want:
            fail(f"{rel} sha256 {got[:12]} != manifest {want[:12]}")
    print(f"PASS: {len(manifest['public_sha256'])} bundled evidence files match their manifest hashes.")

    with (EV / "rows.tsv").open(encoding="utf-8", newline="") as fh:
        rows = {r["Pred_ID"]: r for r in csv.DictReader(fh, **TSV)}
    if len(rows) != 30:
        fail(f"expected 30 rows, found {len(rows)}")
    counts = Counter(head(r["Status"]) for r in rows.values())
    want = {"CONFIRMED": 11, "HIT": 1, "FAILED": 3, "RESOLVED": 4, "NOT-FIRED-PRECONDITION": 3,
            "PARTIAL": 1, "VOID": 1, "RETIRED-OUT-OF-LANE": 1, "OPEN": 5}
    if dict(counts) != want:
        fail(f"status counts {dict(counts)} != {want}")
    print("PASS: 30 rows; 11 CONFIRMED + 1 HIT, 3 FAILED, 4 RESOLVED with a qualifier, 3 NOT-FIRED-PRECONDITION, 1 PARTIAL, 1 VOID, 1 RETIRED, 5 OPEN.")

    hdr = (EV / "ledger_header_2026-06-01.txt").read_text(encoding="utf-8")
    for needle in ("(3 excluded from calibration math", "No FAILED above 70% conf"):
        if needle not in hdr:
            fail(f"June 1 header lacks {needle!r}")
    print("PASS: the June 1 ledger header is bundled; it states the exclusion rule and the since-refuted 'No FAILED above 70% conf' finding.")

    hist = defaultdict(list)
    with (EV / "mark_history.tsv").open(encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh, **TSV):
            hist[r["id"]].append(r)
    if set(hist) != set(rows):
        fail("mark_history ids do not match rows.tsv")
    with (EV / "contemporaneity.tsv").open(encoding="utf-8", newline="") as fh:
        ct = {r["id"]: r for r in csv.DictReader(fh, **TSV)}

    excluded = {rid for rid, r in rows.items() if r["Date_Resolved"] and r["Date_Resolved"] < ct[rid]["first_commit_date"]}
    if excluded != {"BRT-06"} or rows["BRT-06"]["Date_Made"] != "2026-02-18" or rows["BRT-06"]["Date_Resolved"] != "2026-03-04":
        fail(f"expected only BRT-06 (dated 2026-02-18, resolved 2026-03-04, committed 2026-03-06) to resolve before registration; got {excluded}")
    print("PASS: exactly one row, BRT-06, resolved before it was first committed; it is excluded from this case's score (the desk counts it).")

    binary = []
    for rid, r in rows.items():
        s = head(r["Status"]); y = 1 if s in ("CONFIRMED", "HIT") else 0 if s == "FAILED" else None
        if y is None or rid in excluded:
            continue
        now, first = marks(r["Confidence"]), marks(hist[rid][0]["confidence_cell"])
        if not now or not first:
            fail(f"{rid}: no percentage in a confidence cell")
        binary.append((rid, now[-1], first[0], y))
    n = len(binary)
    b_now = sum((p - y) ** 2 for _, p, _, y in binary) / n
    b_first = sum((p - y) ** 2 for _, _, p, y in binary) / n
    sc = manifest["scoring"]
    if n != sc["n_binary"] or abs(b_now - sc["brier_current_cells"]) > 5e-4 or abs(b_first - sc["brier_first_call"]) > 5e-4:
        fail(f"Brier recomputed n={n} now={b_now:.4f} first={b_first:.4f} vs manifest")
    print(f"PASS: Brier over {n} scored rows = {b_now:.4f} on the latest marks, {b_first:.4f} on the first calls; gap {b_first - b_now:.4f}; always-0.5 = 0.25.")

    moved = {rid for rid, h in hist.items() if len({m for x in h for m in marks(x["confidence_cell"])}) > 1 or len(marks(rows[rid]["Confidence"])) > 1}
    if moved != {"BRT-02", "BRT-03", "BRT-04", "BRT-05", "BRT-15", "BRT-26", "BRT-28"}:
        fail(f"moved-mark set {sorted(moved)} unexpected")
    last = {rid: hist[rid][-1]["date"] for rid in moved}
    window_end = {"BRT-02": "2026-03-20", "BRT-03": "2026-03-31", "BRT-05": "2026-03-31"}
    for rid, end in window_end.items():
        if not (last[rid] <= end and last[rid] <= "2026-03-07"):
            fail(f"{rid}: last mark change {last[rid]} is not on or before 2026-03-07 and its window end {end}")
    if not (last["BRT-15"] == "2026-03-07" and last["BRT-15"] < rows["BRT-15"]["Date_Resolved"]):
        fail("BRT-15: expected its only re-mark on 2026-03-07, before its 2026-06-20 grade")
    b04 = hist["BRT-04"][-1]
    if not (b04["date"] == "2026-04-16" and marks(b04["confidence_cell"]) == [0.95] and rows["BRT-04"]["Timeframe"] == "Q1 2026"
            and "2026-03-31" < b04["date"] < rows["BRT-04"]["Date_Resolved"] and "UPGRADED 93→95% on 2026-04-16" in b04["notes_at_that_commit"]):
        fail("BRT-04: expected the 95% mark dated 2026-04-16 with its reason in the notes, after the Q1 2026 window and before the 2026-05-31 grade")
    if not (last["BRT-28"] == "2026-06-08" == rows["BRT-28"]["Date_Made"] and marks(hist["BRT-28"][0]["confidence_cell"]) == [0.45]):
        fail("BRT-28: expected 45% at first commit and a 2026-06-08 change matching its stated date")
    m26 = marks(rows["BRT-26"]["Confidence"])
    if not (m26 == [0.60, 0.58, 0.85] and "re-marked 2026-09-06" in rows["BRT-26"]["Confidence"] and head(rows["BRT-26"]["Status"]) == "OPEN"):
        fail("BRT-26: expected an open row whose cell carries 60% -> 58% -> 85% with a 2026-09-06 re-mark")
    if "UPGRADED from 70%. Day-by-day model confirms" not in "".join(x["notes_at_that_commit"] for x in hist["BRT-02"]):
        fail("BRT-02: the March 7 note quoted in the README is not in mark_history")
    h05 = hist["BRT-05"]
    if not (len(h05) == 3 and marks(h05[1]["confidence_cell"]) == [0.82] and marks(h05[2]["confidence_cell"]) == [0.85]
            and h05[1]["notes_at_that_commit"] == h05[2]["notes_at_that_commit"] and "Upgraded from 70%" in h05[2]["notes_at_that_commit"]):
        fail("BRT-05: expected 70 -> 82 -> 85 with the 85% note unchanged from the 82% note and still reading 'Upgraded from 70%'")
    print("PASS: seven rows moved a mark. BRT-02/03/05/15 settled by 2026-03-07 inside their windows; BRT-04's last two points moved 2026-04-16, after its Q1 window and before its grade; BRT-28 moved on its stated date; BRT-26 (open) carries three dated marks in its cell; BRT-05's 82->85 step carries no new note.")

    late = {rid: (r["date_made"], r["first_commit_date"]) for rid, r in ct.items() if r["date_made"] != r["first_commit_date"]}
    next_day = {rid for rid, (dm, fc) in late.items() if dm == "2026-03-06" and fc == "2026-03-07"}
    others = {rid for rid in late if rid not in next_day}
    if others != {"BRT-06", "BRT-27", "BRT-28"} or ct["BRT-27"]["first_call_confidence"] != "55%" or ct["BRT-28"]["first_call_confidence"] != "45%":
        fail(f"contemporaneity exceptions {sorted(others)} or first calls unexpected")
    print(f"PASS: {30 - len(late)} rows committed on their stated date, {len(next_day)} the next day; exceptions BRT-06 (dated 2026-02-18, committed 2026-03-06), BRT-27 (55%) and BRT-28 (45%) first committed 2026-06-01 and dated 2026-06-08.")

    marker = manifest["redactions"]["marker"]; text = (EV / "rows.tsv").read_text(encoding="utf-8")
    if text.count(marker) != manifest["redactions"]["count"]:
        fail(f"redaction marker count {text.count(marker)} != {manifest['redactions']['count']}")
    cells = Counter((i["row"], i["column"]) for i in manifest["redactions"]["items"])
    for (rid, col), k in cells.items():
        line = next(l for l in text.splitlines() if l.startswith(rid + "\t")).split("\t")
        if line[col - 1].count(marker) != k:
            fail(f"{rid} column {col}: {line[col - 1].count(marker)} markers, manifest says {k}")
    print(f"PASS: {manifest['redactions']['count']} position-reference redaction markers in {len(cells)} cells, as the manifest lists them.")
    b23 = rows["BRT-23"]
    print(f"NOTE: BRT-23 status is {head(b23['Status'])}; its outcome text {'also says' if 'NOT-FIRED' in b23['Outcome'] else 'does not say'} NOT-FIRED. This case scores the Status column.")
    print("Not checked here: the outcomes' cited sources, the desk-context counts in the manifest, or any private file.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
