# Case 8 — FERT: Right about India, wrong about Qatar by six times, from the same page

**On March 20, 2026, a newly bootstrapped fertilizer desk wrote two load-bearing claims into its status file.** India, which sourced about half its nitrogen from the Gulf, would be forced into emergency purchasing. Qatar's LNG outage had removed 77 million tonnes a year of capacity, permanently, and fertilizer production ran on the same gas.

Five months later the desk graded both on the same day. India's IPL had taken 2.5 million tonnes in a single emergency tender, about a quarter of its annual import requirement, at roughly twice the price of two months earlier. Qatar's actual outage was 12.8 million tonnes a year. The 77 was the country's total nameplate capacity, and the true figure had been published by QatarEnergy on the same day the desk wrote 77.

This is the portfolio's one case where the subject is the world rather than the system's own plumbing. It is also honest about two things a ledger row can hide.

## The two rows

Verbatim from the desk's prediction ledger at the pinned revision ([rows.tsv](evidence/rows.tsv)):

| | FERT-10 | FERT-08 |
|---|---|---|
| Claim | India enters emergency/panic purchasing on Gulf supply loss (49% nitrogen from Gulf) | Qatar 77 mtpa LNG offline = fertilizer capacity physically destroyed |
| Confidence cell | `3/5 convergence score` | `(scored 4/5 as convergence vector 3)` |
| Dated | 2026-03-20 | 2026-03-20 |
| Graded | 2026-08-17 **HIT** | 2026-08-17 **MISS** |
| Outcome, as graded | IPL emergency tender April 2026: 2.5 Mt in one tender, ~¼ of annual imports, $935/mt CFR west and $959/mt CFR east, ~2× the rate of two months earlier | Refuted on magnitude ~6×: actual 12.8 mtpa (Trains 4 and 6, Ras Laffan), ~17% of Qatar export capacity, per a QatarEnergy update dated 3/20/26. Repair timeline and cause confirmed. No primary links the LNG damage to ammonia or urea output |
| If falsified, do | n/a | Delete unevidenced mechanism inferences; state them as open questions |
| Desk's note | The March desk's single best call: it named the mechanism, the geography and the trigger, and all three landed | The 6× error sat directly under the thesis's load-bearing word, "structural". The inference "fertilizer production depends on same gas" is deleted from the rebuilt STATUS rather than carried |

## What the March page actually said

The claims exist in the March 20 commit, in the desk's status and instruction files, not in its ledger. [Verbatim lines](evidence/march_claims.md), two of them:

```text
L29: | 3 | Qatar LNG → fertilizer production | 4 | 🔴 | 77 mtpa offline, 3-5yr repair = permanent capacity loss | Confirmed plant closures |
L31: | 5 | India emergency purchases | 3 | 🟠 | 49% nitrogen from Gulf. Not yet confirmed but structural trigger | Official announcement |
```

These are rows of a convergence table. Each carries a score from 1 to 5 for how much it supports the desk's thesis. Neither carries a probability, a resolve-by date, or a falsification condition. The India row says so itself: "Not yet confirmed but structural trigger."

## The two things a ledger row can hide

**The rows were entered on August 17, not March 20.** The ledger was a bare column header in March. The desk was re-chartered on August 16 with a requirement that graded rows land at the first live session, so on August 17 it wrote the March claims into the ledger, dated them to the claims, and graded them in the same sitting. FERT-08's resolve-by date equals its grade date for that reason. The ledger's own header records that the March calendar never entered it. The pre-outcome evidence is the March commit; the ledger is where the grade landed.

**Neither claim had a probability.** The confidence column holds the March convergence score. A claim without a probability can be right without being calibrated, and FERT-10 is a correct call, not a calibration observation. The desk's next rows, registered in September, carry probabilities (72%, 78%), resolve-by dates, and a stated action on falsification. That change is the repair.

## Why the miss is the more useful half

The 77 was a denominator recorded as a numerator, and it sat under the word the whole thesis rested on. The refuting figure was public on the day the claim was written. The desk's response followed its own falsified-action cell: the mechanism inference it could not evidence was deleted rather than carried, and the thesis was rebuilt on the 12.8.

## Run the check

From the repository root, standard library only:

```bash
python3 -B cases/08_fert-matched-pair/check_rows.py
```

It verifies the bundled rows and March excerpt against their manifest hashes, the March and August dates, the absence of a percentage in either confidence cell, that the "~6×" magnitude is arithmetic on figures the row itself states, and that the March excerpt carries both convergence scores.

## Boundary

The graded outcomes' cited figures, the IPL tender and the QatarEnergy update, are the desk's record and were not re-sourced for this portfolio. Across the private repository's 44 prediction ledgers, 27 rows carry a bare HIT or MISS status token at the pinned commit; most grading lives on cards with other vocabularies. This pair comes from the ledger with the cleanest matched record, and it is a sample, not the fleet's scorecard. Pinned revisions, hashes, and attribution: [PROVENANCE.md](PROVENANCE.md).
