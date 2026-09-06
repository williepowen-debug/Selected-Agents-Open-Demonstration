# Provenance — BRENT calibration record

Prepared September 6, 2026. This case bundles the desk's prediction ledger verbatim at one pinned revision, plus two tables derived by walking the ledger's commit history. No agent session was run to prepare it; the only code executed is the bundled checker.

## Pinned revisions

| Role | Private commit | Date | What it holds |
|---|---|---|---|
| First rows | `dec1eff0d5418cf0e3e81442281bd08a19da2ed7` | 2026-03-06 20:02 UTC | Desk bootstrapped; BRT-01 to BRT-06 registered with probabilities in `workbook/PREDICTIONS.tsv` |
| March 7 raises | `82a3c5644b716817be3a4370f83a944a4af95aa6` | 2026-03-07 05:20 UTC | BRT-02 70→85, BRT-03 60→80, BRT-05 82→85, BRT-15 85→90, each with a reason in the row |
| April 16 raise | `b2d8e67755c6eb50e22a3722492e72fbab47e6d0` | 2026-04-16 14:50 ET | BRT-04 93→95 after its Q1 window, with a dated reason in the row |
| Resolution pass | `03dd65f47ebf59dee539b70b7ead6cc784c04c44` | 2026-05-31 13:35 ET | Six date-passed rows resolved |
| Ledger re-homed | `3fcce675a406cbea2ef55f7c715f1e014dd22dad` | 2026-06-01 17:28 ET | Ledger moves from `workbook/` to `thesis/`; probabilities carried unchanged |
| Current | `7a0a32ffc18c5e817f06b5cd99ec3f8aa912e246` | 2026-09-06 16:26 ET | The 30 rows in `rows.tsv` |

The [manifest](evidence/manifest.json) records SHA-256 hashes of the private ledger at the first four pinned revisions and at the current one, the public files' hashes, the redaction log, the scoring inputs, and two desk-context counts (days with commits, ledger commits walked) that are offered as scale and are not bundled evidence. A manifest shipped beside its own evidence supports comparison with these files, not independent authentication of their private origin. The private repository is available for review on request.

## How the two derived tables were built

The history walk ran `git log --reverse` over both ledger paths together, so that same-day commits are ordered by commit sequence rather than by hash (an earlier pass ordered by hash and produced false oscillations; it was discarded). At each commit the file was parsed into rows keyed by ID, and:

- [mark_history.tsv](evidence/mark_history.tsv) records every commit at which a row's Confidence cell differed from its previous value, with the cell text, the row's status, and the row's Notes cell at that commit. Rows that never changed appear once. The desk's newer compound cells carry several marks; the case reads the last percentage as the current mark and the first percentage in the earliest commit as the first call.
- [ledger_header_2026-06-01.txt](evidence/ledger_header_2026-06-01.txt) is the ledger's comment header at the June 1 revision, verbatim, which states the desk's exclusion rule.
- [contemporaneity.tsv](evidence/contemporaneity.tsv) records each row's stated `Date_Made`, the first commit containing the row, that commit's date, and the Confidence cell at that commit, which the case calls the first call.

Forty-six commits touch the two paths. The scoring rule (CONFIRMED or HIT scores 1, FAILED scores 0, every other status is excluded) follows the ledger's own June 1 header. This case adds one exclusion of its own: a row whose Date_Resolved precedes its first commit is not a forecast and is not scored. That removes BRT-06 (dated February 18, resolved March 4, committed March 6), which the desk itself counts. Brier is the mean squared difference between probability and outcome over the fourteen remaining rows. The window ends the checker uses for BRT-02, BRT-03 and BRT-05 (March 20, 31, 31) are the case's reading of the rows' Timeframe cells ("By Mar 20", "By Mar 31", "Q2 2026" on a claim that ends with the first quarter); they are hardcoded, not parsed.

## Verbatim, redacted, and editorial

- `rows.tsv` is the ledger's header and thirty rows at the current revision, ten columns, in ledger order. Five phrases are replaced with `[redacted: position reference]`: two in BRT-06 (a percentage move measured from an entry price) and three in BRT-15 (an equity-position status, an entry-quality remark, and an entry decision). The manifest lists each by row, column name, and character count. Market prices, claims, resolvers, outcomes, and the operator's and coordinator's names are verbatim.
- The README's tables restate ledger cells in prose for readability; `rows.tsv` and `mark_history.tsv` govern where they differ.
- The BRT-15 claim itself, which names an exit signal for a tanker equity, is published as written. It describes a March trigger design, not a current holding.

## What was not done

The outcomes' cited sources (Kpler storage data, EIA weekly reports, a QatarEnergy update, TSMC's quarterly report, a Taiwanese ministerial statement, and others named in the rows) were not re-sourced for this portfolio. The case reports the desk's grades as recorded. Fourteen scored outcomes from one desk show the method and the gap between the two scores; they do not estimate the desk's calibration precisely, and no trade, position size, or account is described.

## Declared residue after two blind cold reads

Two blind reads preceded publication. The first found eleven contradictions between the page and its own bundle, every one leaning in the desk's favor: a February-dated row scored as a forecast, a seventh moved mark the checker could not see because it read only the leading percentage, the wrong falsified mechanism named for BRT-23, two wrong placeholder percentages, and a quoted cell missing its latest re-mark. The second found two: "every move was written into the row with a reason" was false for BRT-05's second step, and the redaction count named cells where it should have named markers. All thirteen were fixed in the page, the checker, or the evidence. Declared rather than fixed: the desk-context counts are not bundled; the redaction rule leaves ticker and price visible by design; "verbatim" is a statement about the pinned private file that this bundle cannot authenticate; the checker's window ends are hardcoded for three rows and it checks two of the page's quotations, not all; BRT-26's "Moved" column gives commit dates where the cell dates its own re-marks differently, and the page says so in the cell; and the exclusion of sixteen rows extends a header rule that names three, which the page states as its own extension. The page was closed after the second correction pass, with one later one-word change (the marker count is five markers in three cells; the second pass had written four, from the reader's summary rather than the checker); a third read was not taken.

## Attribution

BRENT wrote, re-marked, and graded every row, and documented each re-mark in the row. Will designed and operates the system and authorized this case. PROME, the system's coordinating agent, walked the history, built the two derived tables and the checker, chose the redactions under Will's rule, and prepared this package on September 6, 2026.
