# Provenance — DAEDALUS measurement-validity case

Prepared September 6, 2026. This is a source-based account of a metric withdrawal, accompanied by a new synthetic illustration—not a new historical census or model experiment.

## Historical anchors

- Before withdrawal: `eb6a80d8cbb0d540de0376fa528cf37cad856682`.
- Withdrawal: `0923f5816ff62423200901c15d931c96f9590104` (September 5, 2026).
- Renderer: `AGENTS/DAEDALUS/scripts/scorecard.py`.
- Published report: `AGENTS/DAEDALUS/scorecards/2026-09-04.md`.
- Specification also inspected: `AGENTS/DAEDALUS/design/2026-08-28_coordination_scorecard_v1.md`.

The [manifest](evidence/manifest.json) records full-file SHA-256 hashes for the renderer and report at both revisions, plus the public excerpt hash. The [excerpt bundle](evidence/source-excerpts.md) contains selected table rows, two complete counting-function definitions, and selected calculation/output statements. These passages are verbatim; headings and scope notes are editorial. Omitted helpers and data inputs mean the code excerpts are not a standalone program.

The published 28/0 counts were checked against the archived report and their definitions against the renderer. They were **not independently recomputed from every underlying log** for this portfolio. The source code establishes the measurement mismatch without requiring that census. The raw labels that imply pre/post decision order survive in the historical artifacts and are explicitly not certified here.

Hashes make copies comparable; a manifest shipped beside its own evidence does not independently authenticate its private origin. The private source remains available for review on request under the repository's existing policy.

## New illustration and attribution

`counterexample.py` was written for this public case. Its two-touch/one-entry histories are synthetic. They demonstrate that identical observable records can accompany different decision timing; they are not claims about what happened in the operating system. Its hash check verifies the local excerpt, not the full private renderer, all scorecard outputs, or the correctness of every surviving metric.

Will designed and operated the broader system, commissioned review, and authorized this public selection. DAEDALUS authored and withdrew the operational metric. Codex identified the validity problem and prepared the public narrative, excerpts, and illustration under Will's direction. This is evidence of a particular correction and its limits, not an estimate of review effectiveness or system-wide improvement.
