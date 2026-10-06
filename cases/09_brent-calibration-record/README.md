# Case 9 — BRENT: A calibration record, scored on the first call

**Thirty-one dated forecasts, the earliest dated February 18 and the rest from March 6, 2026 onward, with first calls from 40% to 88% and current marks up to 95%. Seventeen have resolved yes or no: thirteen scored as right, four as wrong. One of the seventeen was written into the ledger two days after its own outcome date, so this case scores sixteen. Brier 0.1911 on the marks the desk first wrote down, 0.1697 on the cells as they read today, against 0.25 for always saying 50%. A stricter comparator, always forecasting the 75% of scored rows that came true, scores 0.1875: the first calls do not beat it, the current cells do.** The gap between the two desk scores is the point of the case, and it widened as the ledger grew.

*Revised October 5, 2026. The September 6 version scored fourteen rows: 0.1707 current, 0.1854 first call, against a base rate of 0.1684, which neither score beat. Since then BRT-26 resolved yes on a mark raised as its window closed, and BRT-29 failed on its first call. The previous pin is recorded in the [manifest](evidence/manifest.json).*

BRENT is the system's oil and energy desk. In the private repository, commits touch its directory on 161 of the 214 days from March 6 to October 5, and 60 commits touch this ledger; those two counts are in the manifest as context and are not something the bundle can prove. Twenty-three rows were committed on their stated date and five the next day. The three exceptions are below.

Four terms, used throughout: a **mark** is a probability written in the Confidence cell; the **first call** is the mark in the row's earliest commit; a **re-mark** is any later change; **CONFIRMED** and **FAILED** are the desk's outcome tokens through May and **HIT** the token on its one grade after that, so CONFIRMED and HIT score alike here.

## The record

Verbatim from the ledger at the pinned revision ([rows.tsv](evidence/rows.tsv)), five position phrases and one sentence about credential configuration redacted and marked:

| Status | Rows | Scored |
|---|---|---|
| CONFIRMED or HIT | 13 | 12 as a 1; BRT-06 excluded, see below |
| FAILED | 4 | 4 as a 0 |
| RESOLVED with a qualifier: mechanism or direction confirmed while the threshold was unreached, moot, or untestable, or the lead-lag incomplete | 4 | no |
| NOT-FIRED-PRECONDITION: the if-clause never occurred | 3 | no |
| PARTIAL, VOID (unsatisfiable or defective as specified), RETIRED (out of the desk's lane) | 4 | no |
| OPEN | 3 | not yet |

The exclusion rule is the desk's own. Its ledger header of June 1, 2026, bundled verbatim as [ledger_header_2026-06-01.txt](evidence/ledger_header_2026-06-01.txt), reads "3 excluded from calibration math: BRT-18 RETIRED + BRT-20/25 NOT-FIRED-PRECONDITION". The header names three exclusions; this case applies the same rule to the mechanism-only resolutions and unfired preconditions registered after June 1, which makes fifteen of thirty-one unscored, three of them still open. A claim like "Brent reaches $100 before Hormuz reopens" (65%, confirmed April 17) scores. A claim whose mechanism arrived without its threshold, or whose precondition never fired, is listed and counted neither way. The same header also states a calibration finding, "No FAILED above 70% conf — high-conviction predictions are reliable. Trust 85%+ calls", which the desk's 90% call refuted nineteen days later. One more sentence a reader is owed: the four largest raises, +15 to +20 points on BRT-02 through BRT-05, were all on rows that later confirmed; of the four rows that failed, only BRT-15 ever moved, up five.

## The four failures

- **BRT-15, 90%:** the tanker-equity exit signal would fire on a naval-escort or ceasefire announcement, not on physical reopening. The June 17 signing tripped the trigger and the stock rose 5.79% on the week instead of falling the 10% the test required. Graded FAILED June 20. It is the highest-confidence failure in the ledger, and the row that refuted the header's "Trust 85%+ calls".
- **BRT-23, 70%:** "at least one major DRC SX-EW copper/cobalt operator announces force majeure or significant curtailment" within the window. Glencore did, but the row records that it was driven by the DRC's February cobalt export ban and quotas, "NOT by sulphur feedstock cost making SX-EW uneconomic", the mechanism the prediction tested; cobalt prices rose about 160% on policy scarcity, the opposite of the cost squeeze modeled. The status column says FAILED and the outcome text also says "Marked NOT-FIRED (mechanism falsified)."; this case scores the status column, which keeps the row in the denominator as a 0.
- **BRT-24, 65%:** Taiwan initiates industrial power rationing if the closure exceeds 30 days. No Stage 2 or higher load shedding occurred by the late-April deadline; Taiwan covered the gap with spot LNG, Australian term contracts, and record US LNG. Graded FAILED May 31.
- **BRT-29, 55%:** a demand test on US gasoline, requiring its four-week year-on-year change to fall to −3.0% or below; the EIA weekly report for the week of September 25 showed +0.26%. Graded FAILED September 30, on the mark first written and never moved.

## Seven rows moved a mark, and where the two Brier scores come from

Every change to a probability cell, with its commit, date, status, and the row's note at that commit, is in [mark_history.tsv](evidence/mark_history.tsv). Seven rows moved:

| Row | First call | Now | Moved | Window closes | Graded |
|---|---|---|---|---|---|
| BRT-02 Kuwait full curtailment within 14 days | 70% | 85% | Mar 7 | Mar 20 | Apr 16, confirmed |
| BRT-03 UAE curtailment within 25 days | 60% | 80% | Mar 7 | Mar 31 | Apr 16, confirmed |
| BRT-04 US shale does not respond in Q1 | 80% | 95% | Mar 6 to 93%, **Apr 16 to 95%** | Mar 31 | May 31, confirmed |
| BRT-05 demand destruction not visible before Q2 | 70% | 85% | Mar 6 to 82%, Mar 7 to 85% | Mar 31 (the row's cell says Q2 2026; the claim ends with Q1) | Apr 16, confirmed |
| BRT-15 tanker exit-signal timing | 85% | 90% | Mar 7 | event-keyed | Jun 20, failed |
| BRT-26 US oil rig count stays below 457 by end-Q3 | 60% | 60% → 58% → 85% in one cell | Aug 28, Sep 6 (the cell dates its own re-marks Jul 28 and Sep 6) | Sep 30 | Sep 25, confirmed (455 against 457) |
| BRT-28 second-chokepoint premium bleeds out | 45% | 70% | Jun 8, when the claim was restructured | Jul 3 | Jul 1, mechanism only, unscored |

Six of the seven moves were written into the row with a reason; BRT-02's March 7 note begins "UPGRADED from 70%. Day-by-day model confirms: 51.60M bbl effective capacity, 2.58 mbpd fill rate, Mar 20 = tank tops". The exception is BRT-05's second step, 82% to 85% on March 7, whose note is unchanged from the day before and still reads "Upgraded from 70%." Of the five March rows, four settled by March 7, before their own outcomes. BRT-04 moved once more: its last two percentage points were added on April 16, sixteen days after its first-quarter window had closed, with a note citing an April 14 report and the April 10 rig count. That is a documented, reasoned re-mark, and it is also a mark raised on evidence the window itself had already produced. BRT-28's two marks are on two propositions: the June 8 note records the claim being restructured from an event to a price consequence, with the stated date moved to match. BRT-26 is the desk's newer form, three dated marks kept in one cell.

For the March rows the Confidence column holds only the latest mark. The first call survives in the current note for BRT-02, BRT-03 and BRT-15 ("upgraded from 70%") and only in the history for BRT-04 and BRT-05. Scored on the latest marks the sixteen resolved rows give 0.1697; scored on the first calls, 0.1911; a gap of 0.021 in the desk's favor, up from 0.015 at fourteen rows. Both beat the 0.25 baseline. The widening comes from one row: BRT-26 was first called at 60%, re-marked to 58% in July, and raised to 85% on September 6, nineteen days before the rig count confirmed it and twenty-four before its window closed. The cell calls that a window-shrink re-mark, dated and reasoned, and it is also a mark raised as the remaining time to fail ran out.

The 0.25 baseline is a low bar for a desk whose scored marks run from 55% to 95% and whose scored rows mostly came true. Twelve of the sixteen resolved yes, 75%, and a forecaster who wrote 75% on every row would score 0.1875. The current cells sit 0.018 below that, better; the first calls 0.004 above it, worse. Scoring BRT-26 at its July 58% instead of its September 85% gives 0.1793, still 0.008 better than the base rate, so the current-cell margin does not rest on that one re-mark alone. At fourteen rows on September 6 neither score beat the base rate (0.1707 and 0.1854 against 0.1684). The desk beats a coin; it beats its own hit rate only on the marks as they stand, not on the marks as first made. Two cautions cut in opposite directions: the base rate is known only in hindsight, so the comparator is stricter than any forecaster could have used in March; and a ledger that registers mostly claims its author expects to come true earns a high hit rate without discrimination, which is what this comparator detects. The test that would settle it is the forecasts the desk got right and wrong at different marks, and sixteen rows are too few to show that. A market-implied probability, where one exists, would be the fairer comparator still.

BRT-26 shows the cell form that would make the gap visible without a history walk: "60% [Date_Made 2026-05-31; first-call calibration, retained] → 58% [re-marked 2026-07-28 …] → 85% [re-marked 2026-09-06 — WINDOW-SHRINK re-mark …]".

## Three rows whose dates need a sentence

BRT-06 is dated February 18, before the desk existed, resolved March 4, and first committed March 6: a claim entered already confirmed, at 55%. The desk counts it; its June 1 header cites it as the call that "overshot threshold by ~2000%". This case does not score it, because a row written after its outcome is not a forecast by the case's own standard. BRT-27 (55%, unchanged since) and BRT-28 (45% at first commit) first appear in a June 1 commit and carry a stated date of June 8, the day BRT-28 was restructured and both were marked as made. The full table is [contemporaneity.tsv](evidence/contemporaneity.tsv).

## Run the check

From the repository root, standard library only:

```bash
python3 -B cases/09_brent-calibration-record/check_calibration.py
```

It verifies the four evidence files against their manifest hashes; the status counts; that the June 1 header carries the exclusion rule; that exactly one row resolved before its first commit; both Brier scores recomputed from the bundled rows and history, and the always-the-base-rate score beside them, and the current-cell score with BRT-26 at 58%; the set of seven moved rows; that BRT-02, BRT-03 and BRT-05 last moved on or before March 7 and inside the window ends the case assigns them (March 20, 31, 31), that BRT-15 moved before its grade, that BRT-04's 95% is dated April 16 with its reason in the note, after March 31 and before May 31, that BRT-28 moved on its stated date, that BRT-26's cell holds three marks with its 85% committed September 6 and graded September 25, and that BRT-31's several percentages are one first call, not a re-mark; that BRT-02's and BRT-04's quoted notes are in the bundle and BRT-05's note did not change between its 82% and 85% commits; the contemporaneity exceptions and their first calls; five position redaction markers in three cells; and one credential-configuration marker in BRT-29. It does not read window ends from the Timeframe cells, and it does not check the other quotations on this page.

## Boundary

The outcomes' cited sources are the desk's record and were not re-sourced for this portfolio. Five phrases describing a position or an entry decision are replaced with `[redacted: position reference]`; the manifest lists each by row and column. One sentence in BRT-29's notes, saying where a data-service credential file lives and which machines hold it, is replaced with `[redacted: credential configuration]`; no key value was in it. The surrounding note, in which the desk reports that it had wrongly told the operator the data was unreadable, is published as written. The BRT-15 claim is published as written, so a reader sees the ticker and the price and not the size; that is the rule chosen, not an oversight. Every other cell is as the ledger holds it at the pinned revision, which a reviewer with access can compare against the manifest's private hash and this bundle cannot prove on its own. Sixteen scored rows from one desk show the method and the gap, not the desk's calibration to any precision finer than the gap itself. Pinned revisions, the history-walk method, and attribution: [PROVENANCE.md](PROVENANCE.md).
