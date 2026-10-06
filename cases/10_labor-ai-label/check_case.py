#!/usr/bin/env python3
"""Check the LABOR AI-label case: hashes, every figure against the verbatim desk rows, the exact ratios,
the pre-committed demote rule and its outcome, and the dates that make the rule and card prior to the data.

Standard library only. The private repository is not opened and Challenger's reports are not re-read;
the figures are checked against the desk's verbatim records of them, not against the publisher.
"""
import datetime, hashlib, json, pathlib, sys
from fractions import Fraction as F

HERE = pathlib.Path(__file__).resolve().parent
EV = HERE / "evidence"

def fail(msg):
    print(f"FAIL: {msg}"); sys.exit(1)

def main():
    man = json.loads((EV / "manifest.json").read_text(encoding="utf-8"))
    for name, meta in man["files"].items():
        if hashlib.sha256((EV / name).read_bytes()).hexdigest() != meta["public_sha256"]:
            fail(f"{name}: hash mismatch")
    print(f"PASS: {len(man['files'])} evidence files match their manifest hashes.")

    kb = {l.split("\t")[0]: l for l in (EV / "kb_rows.tsv").read_text(encoding="utf-8").splitlines()[1:]}
    # month: (KB row, announced cuts, AI-cited cuts, tech YTD 2026, tech YTD 2025 base or None)
    months = {
        "Jun": ("KB-LAB-108", "45,849", "14,029", "139,156", None),
        "Jul": ("KB-LAB-137", "33,429", "10,970", "149,023", "89,251"),
        "Aug": ("KB-LAB-194", "52,881", "3,462", "155,126", "102,239"),
        "Sep": ("KB-LAB-201", "43,281", "3,961", "165,925", "107,878"),
    }
    num = lambda s: int(s.replace(",", ""))
    share, growth = {}, {}
    for m, (rid, cuts, ai, t26, t25) in months.items():
        for fig in (cuts, ai, t26) + ((t25,) if t25 else ()):
            if fig not in kb[rid]:
                fail(f"{m}: {fig} not in {rid}")
        share[m] = F(num(ai), num(cuts))
        if t25:
            growth[m] = F(num(t26), num(t25)) - 1
    print("PASS: every figure below appears verbatim in the desk's knowledge-base row for its month.")
    for m in months:
        g = f"; tech YTD {float(growth[m]):+.1%}" if m in growth else "; tech YTD +83% (as stated; 2025 base not in the row)"
        print(f"      {m}: AI-cited share {float(share[m]):.2%}{g}")
    if "+83% YoY" not in kb["KB-LAB-108"]:
        fail("June tech growth text not in KB-LAB-108")
    if "116,175 + 3,961 = 120,136" not in kb["KB-LAB-201"]:
        fail("September AI YTD reconciliation not in KB-LAB-201")
    if 116175 + 3961 != 120136:
        fail("AI YTD does not reconcile")
    print("PASS: AI-cited YTD reconciles: 116,175 (Aug) + 3,961 (Sep) = 120,136.")

    rule = (EV / "rule_2026-07-02.txt").read_text(encoding="utf-8")
    if "AI share <20% ×2 mo + tech YTD growth <+20% → demote to 2" not in rule:
        fail("demote rule text not in the July 2 excerpt")
    tl = man["timeline"]
    rule_t = datetime.datetime.fromisoformat(tl["rule_first_committed"]["time"])
    if not rule_t.date() < datetime.date.fromisoformat(tl["august_report_release"]):
        fail("rule not committed before the August report")
    print(f"PASS: the demote rule (share <20% for two months AND tech YTD growth <+20%) was first committed {rule_t.date()}, before the August report.")

    share_leg = share["Aug"] < F(1, 5) and share["Sep"] < F(1, 5)
    tech_leg = growth["Sep"] < F(1, 5)
    if not (share_leg and not tech_leg):
        fail("expected the share leg met and the tech leg not met")
    card = (EV / "grading_card_2026-10-01.md").read_text(encoding="utf-8")
    for needle in ("**v5 HOLDS at 4.**", "I will not read a share move as a change in displacement in either direction.",
                   "I will not attribute any September AI-share or tech-cut move to the EO"):
        if needle not in card:
            fail(f"card lacks {needle[:50]!r}")
    print("PASS: share leg met (Aug 6.55%, Sep 9.15%, both < 20%); tech leg not met (+53.8% >= +20%); the card grades v5 HOLDS, as the rule requires.")

    t = {k: datetime.datetime.fromisoformat(v["time"]) for k, v in tl.items() if isinstance(v, dict)}
    release = datetime.datetime.fromisoformat(tl["september_report_release"])
    if not (t["card_first_committed"] < t["card_amendment_1_committed"] < release < t["card_graded_committed"]):
        fail("card, amendment, release and grade are not in that order")
    print("PASS: card committed 2026-09-29 13:11 ET and amended 13:26 ET, both before the 2026-10-01 05:30 ET release; graded 12:23 ET that day.")
    if "`s = 0.1996` displays \"20.0%\" but is <20%" not in card:
        fail("Amendment 1's rounding example not in the card")
    print("NOTE: Amendment 1 grades on exact ratios: a share of 19.96% displays as 20.0% but is below the 20% bar.")

    lag = (datetime.date.fromisoformat(tl["august_report_captured"]) - datetime.date.fromisoformat(tl["august_report_release"])).days
    if lag != 26 or "Captured 26 days late" not in kb["KB-LAB-194"]:
        fail("August capture lag")
    print("PASS: the August report (released 2026-09-03) was captured 2026-09-29, 26 days late, as its row records.")

    lab = (EV / "lab11_row.tsv").read_text(encoding="utf-8").splitlines()[1].split("\t")
    if not (lab[0] == "LAB-11" and lab[3].startswith("50% (was 55%") and lab[5] == "OPEN" and "2026-07-31 CUT 55->50" in lab[8]):
        fail("LAB-11 row not as described")
    print("PASS: LAB-11 'AI narrative shield breaks' is OPEN at 50%, cut from 55% on 2026-07-31; no later re-mark is recorded in the row.")
    print("Not checked here: the figures against Challenger's own reports, or any private file.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
