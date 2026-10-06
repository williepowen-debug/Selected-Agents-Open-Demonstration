# Provenance — LABOR AI-label case

Prepared October 5, 2026. This case bundles four records from the labor desk verbatim, at pinned revisions of the private operating repository, plus a checker. No agent session was run to prepare it, and Challenger's reports were not re-read.

## Pinned revisions

| Role | Private commit | Time (ET) | What it holds |
|---|---|---|---|
| Demote rule first committed | `b50c6adad3b14f392a5c8cd55c719fe7bcda99e4` | 2026-07-02 10:49 | The AI-displacement row of the desk's status matrix, with the demote rule |
| Grading card first committed | `b0e1f8b5fff0d5f9f032b540a178e7ac7a11fc6c` | 2026-09-29 13:11 | The frozen September card |
| Amendment 1 committed | `d09db5fe4d16a524a65adb1722d76f54afebfb52` | 2026-09-29 13:26 | Exact-ratio grading and corrected release time |
| September report released | — | 2026-10-01 05:30 | Challenger's own release calendar, as the card records it |
| Card graded | `5a339a6db1dae7c87feac6c7f258f7420adb1e5b` | 2026-10-01 12:23 | The grade and the card's move to `graded/` |
| Current | `7d15d5c9200e802d0c702884c6655f6e6d53ef7d` | 2026-10-05 18:13 | The knowledge-base rows, the LAB-11 row and the graded card as bundled |

The [manifest](evidence/manifest.json) records, for each bundled file, the private commit and path it came from, the SHA-256 of that private file at that commit, and the SHA-256 of the public file. A reviewer with access can compare them; the bundle cannot authenticate its private origin on its own. The private repository is available for review on request.

## What is bundled

- [rule_2026-07-02.txt](evidence/rule_2026-07-02.txt): the header and the AI-displacement row of the status file's matrix as first committed on July 2, verbatim.
- [kb_rows.tsv](evidence/kb_rows.tsv): the header and four knowledge-base rows (KB-LAB-108, -137, -194, -201) recording the June to September Challenger reports, verbatim at the current pin. Each row names its source file and, for August and September, the date the report was captured and how its figures were checked.
- [lab11_row.tsv](evidence/lab11_row.tsv): the header and the LAB-11 row of the desk's prediction ledger, verbatim at the current pin.
- [grading_card_2026-10-01.md](evidence/grading_card_2026-10-01.md): the September grading card, whole, including its superseded sections, Amendment 1 and the grade.

Nothing was redacted. The bundled files were searched for positions, trade references, sizes, credentials and local paths before publication, and none were found. Internal routing names (other desks, a coordinating agent) and internal rule numbers are left as written.

## What was not done

Challenger's reports were not re-read and the figures were not re-sourced; the desk's rows record that each August and September figure was checked against the report's extracted text, and that claim is the desk's. The June row cites the report by its date; the July row cites the issuer's release as retrieved on August 7. Neither records a text-extraction check. The case's statement that part of LAB-11's supporting evidence lapsed is the case's own reading of the bundled records: the row's notes cite AI's run as the top-cited reason, and the knowledge-base rows show that run ending in August. The desk's status file, which notes the same lapse, is not bundled.

## Attribution

LABOR wrote the rule, the knowledge-base rows, the prediction row and the grading card; a reviewer found the card's release-time and rounding defects before the release. Will designed and operates the system and authorized this case. Claude Code selected the records, wrote the case and the checker, and prepared this package under Will's direction on October 5, 2026; the private repository was read, not modified.
