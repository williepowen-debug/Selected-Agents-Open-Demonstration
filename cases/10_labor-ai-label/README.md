# Case 10 — LABOR: What "AI-cited layoffs" measures

**From June to September 2026, the share of announced US job cuts that employers attributed to artificial intelligence fell from 31% to 9%, while job cuts in the technology sector stayed more than 50% above the previous year's pace. The labor desk had written down in July what that pattern would and would not mean, and on October 1 it graded the September report by that rule rather than by the headline.** The AI share is a statement about what employers say. This case is about a desk declining to read it as a measure of what AI does.

LABOR is the system's labor-market desk. Its inputs here are the monthly Challenger, Gray & Christmas job-cut reports, which tally announced layoffs and the reasons employers give for them. Every count below appears verbatim in the desk's own records, bundled in [evidence](evidence/); the shares and growth rates are computed from those counts. The reports themselves are public at challengergray.com.

## The series

| 2026 | Announced cuts | Cited AI | AI share | AI's rank among reasons | Technology cuts, year to date, vs same period of 2025 |
|---|---:|---:|---:|---|---:|
| June | 45,849 | 14,029 | 30.6% | #1, fourth straight month | +83% (as stated) |
| July | 33,429 | 10,970 | 32.8% | #1, fifth straight month | +67.0% (149,023 vs 89,251) |
| August | 52,881 | 3,462 | 6.5% | #4 | +51.7% (155,126 vs 102,239) |
| September | 43,281 | 3,961 | 9.2% | #5 | +53.8% (165,925 vs 107,878) |

AI had been the most-cited reason since March. Then, in one month, its share fell by four fifths. Year to date it is still the most-cited reason, at 120,136 cuts, about 21% of all 2026 announcements.

Two readings fit the series. Fewer layoffs are being driven by AI; or fewer layoffs are being *described* as AI-driven. The July report's own commentary leaned on neither: "while AI is shifting the labor market, it is not dismantling it." Technology-sector cuts eased, from +83% on the year in June to +54% in September, but stayed far above 2025's pace. The label fell much faster than the activity it was taken to describe.

## The rule, written before the drop

On July 2, while AI was still the top reason, the desk wrote the condition under which it would downgrade its AI-displacement score from 4 to 2:

> AI share <20% ×2 mo + tech YTD growth <+20% → demote to 2

Both conditions, not either. The share leg alone would have been satisfied by exactly the relabelling the desk could not rule out. The technology leg asked whether the underlying cuts had actually slowed.

The [September grading card](evidence/grading_card_2026-10-01.md) was frozen on September 29, two days before the report, and says what the grade would not do:

- "The AI share is a LABELLING statistic. A low share can mean fewer AI-driven cuts or fewer cuts *attributed* to AI. I will not read a share move as a change in displacement in either direction."
- A September 18 executive order made layoffs count against employers' H-1B visa petitions, an incentive to label technical cuts differently, inside the September window. "I will not attribute any September AI-share or tech-cut move to the EO, and I will not argue the EO away if the share rises. One month, confounded."

## The grade

The September report put the AI share at 3,961 / 43,281 = 9.15%, the second month under 20%: the share leg was met. Technology cuts were 165,925 / 107,878 − 1 = +53.8% on the year: the technology leg was not. The rule is a conjunction, so the score **held at 4**. The desk did not demote on the headline, did not re-band the result without its largest contributors, and did not attribute the move to the executive order.

## What went wrong along the way

- **The August report was read 26 days late.** Released September 3, captured September 29; the desk's status file carried July's figures in the meantime.
- **The grading card was itself defective, and was fixed before the data.** It was written two days before the release against a one-week target; it gave the release time as 7:30 ET from a search summary when the publisher's calendar said 5:30; and its bands were drawn on figures rounded to one decimal, so a share of 19.96% would have displayed as "20.0%" and been assigned to the wrong side of a strict "below 20%" bar. The card's own hand-written proof that its bands left no gaps had certified those rounded boundaries. A reviewer found the time and the rounding defects; Amendment 1, committed sixteen minutes after the card and about forty hours before the release, corrected the time and moved grading to exact ratios. The lateness stands. The grade also used September 2025's technology base (107,878), which the report printed, rather than the August base the card's input table had carried.
- **The prediction behind the score was not re-marked.** LAB-11, "AI narrative shield breaks", stands at 50%, cut from 55% on July 31 after one staffing company answered the displacement question with growth. Its notes cite AI's run as the top Challenger reason as supporting evidence. That run ended in August, and the row has not been re-marked since; a September 10 note corrected the record of its first call to 55%, which is not a re-mark. The September card deliberately leaves LAB-11 ungraded and says any re-mark will be made against the row's own wording, with its date written beside it. Its stated date, February 18, is a bulk-seeding placeholder; the earliest commit carrying the row is March 6, and the row records that it will be scored on the 55% first call.

## What this case does and does not show

It shows a desk separating a reported label from the quantity the label is taken to measure, committing to that separation before the data, and grading by it when the data invited a different story. It shows the same mechanism as [case 9](../09_brent-calibration-record/) from the other side: a mark that was not moved when part of its stated evidence lapsed.

It does not show whether AI is displacing workers, at what rate, or in which occupations. Challenger counts announcements, not separations, and its reasons are the employers' own. Answering the displacement question would take data this case does not use, such as separations and openings by occupation, unemployment-insurance claims by prior industry, or WARN notices filed with states.

## Run the check

From the repository root, standard library only:

```bash
python3 -B cases/10_labor-ai-label/check_case.py
```

It verifies the four evidence files against their hashes; that every count and rank in the table appears verbatim in the desk's row for its month; the shares and growth rates as exact ratios; the year-to-date reconciliation (116,175 + 3,961 = 120,136); that the share leg was met, the technology leg was not, and the card's written grade is a hold; that the commit times recorded in the manifest put the rule before the August report and the card and its amendment before the September release, and give the 26-day capture lag; and LAB-11's current mark and single recorded cut. The commit times are as the preparer recorded them from the private repository; a reviewer with access can check them against the commits named in [PROVENANCE.md](PROVENANCE.md). It does not check the figures against Challenger's reports; those are public and a reader can.

## Boundary

The figures are the desk's transcriptions of Challenger's reports, each recorded with its source; the August and September rows record a check against the report's extracted text, the June and July rows do not. They were not re-read from the publisher for this portfolio. The June technology growth rate (+83%) is as the desk stated it, without the 2025 level. Evidence is verbatim from the private repository at the pinned revisions; nothing was redacted. Pinned revisions and attribution: [PROVENANCE.md](PROVENANCE.md).
