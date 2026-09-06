# Provenance — FERT matched pair

Prepared September 6, 2026. This case bundles verbatim ledger rows and verbatim status-file lines from the private operating repository at three pinned revisions. No code is executed beyond the bundled checker; no agent session was run to prepare it.

## Pinned revisions

| Role | Private commit | Date | What it holds |
|---|---|---|---|
| March snapshot | `0087ee84eb4b53cd4c03118bfdc7d9f1ce6bae1b` | 2026-03-20 01:15 UTC | The commit that bootstrapped the FERT desk. `STATUS.md` and `CLAUDE.md` carry the two claims; `workbook/PREDICTIONS.tsv` is a bare column header |
| Registration and grade | `aa3e057fdf8b82488510451e6e3b3410b38a3a23` | 2026-08-17 11:30 ET | The desk's first live session under its 2026-08-16 re-charter. FERT-08 and FERT-10 enter the ledger, dated 2026-03-20, and are graded |
| Current | `7a0a32ffc18c5e817f06b5cd99ec3f8aa912e246` | 2026-09-06 16:26 ET | The two rows are byte-identical to the registration commit |

The [manifest](evidence/manifest.json) records SHA-256 hashes of the private files at each revision, the public files' hashes, and the selected line numbers. Because the manifest ships beside the evidence, it supports comparison with these files, not independent authentication of their private origin. The private repository is available for review on request.

## What is verbatim and what is editorial

- [rows.tsv](evidence/rows.tsv): the ledger's column header and the FERT-08 and FERT-10 rows, byte-for-byte from the current revision. Eleven columns; nothing removed or reordered.
- [march_claims.md](evidence/march_claims.md): ten lines from the March snapshot's `STATUS.md` and `CLAUDE.md`, each prefixed with its line number. The file's headings and one framing sentence are editorial; the fenced lines are not altered.
- The case README's two-column table restates the rows in prose for readability. The `rows.tsv` file governs where they differ.
- The fleet-context count (27 rows with a bare HIT or MISS token across 44 ledgers) was produced by a tab-delimited grep over files named exactly `PREDICTIONS.tsv` at the current revision. It ignores other status vocabularies and grades recorded on cards, so it understates the fleet's graded work and is offered only as scale.

## What was not done

The outcome figures the desk cites, the April 2026 IPL tender and the QatarEnergy production update dated 2026-03-20, were not re-sourced for this portfolio. The case reports the desk's grade and the evidence it recorded; it does not certify those figures independently. No trade, position, or gate is described.

## Attribution

The FERT desk wrote the March claims, registered and graded the rows in August, and executed its own falsified-action cell. Will designed and operates the system and authorized this case. PROME, the system's coordinating agent, selected the pair, traced the rows to their March source in the private history, and prepared this package and its checker at Will's direction on September 6, 2026.
