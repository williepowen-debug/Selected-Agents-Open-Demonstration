# Portfolio notes and evidence boundaries

**Editorial revision: September 6, 2026.** This is background for the [portfolio landing page](README.md), not an additional experiment or a current operating dashboard.

## Operator decisions and attribution

The following choices come from Will's external-review brief, supplied in conversation. Short verbatim excerpts are retained with editorial explanations.

### 1. Review first; implementation requires permission

> Start read-only. Do not edit, commit, route messages, or change agent-owned files until I explicitly ask for implementation.

Will defined the reviewer as an external second pair of eyes rather than a permanent research agent. The chosen boundary allowed criticism across the system without granting authority to change the owners' records. Will later authorized the public portfolio additions separately.

The [VIOLET provenance](cases/04_violet-correction-verification/PROVENANCE.md) distinguishes the agent's operational repairs from Codex's review, public extraction, and new fixture harness. The [WALTER provenance](cases/05_walter-instruction-pilot/PROVENANCE.md) discloses that Codex advised on the protocol and reviewed the results; external to the desk did not mean blind or uninvolved.

### 2. Check the application of a correction

> A receipt proves delivery or triage, not necessarily application.

> Verify another desk's state at its owner artifact.

These requirements distinguish an acknowledged request from a changed canonical claim. Will also asked the review to separate detection, diagnosis, owner correction, propagation, closure, recurrence, time, coordination burden, and added complexity.

The public [gate lifecycle](architecture/prome-orchestration/task-lifecycle.md) preserves the distinction between an unresolved obligation and verified closure. Missing timestamps identify documentation gaps; they cannot alone establish that the underlying action never occurred.

### 3. Prefer a smaller enforceable fix

> Prefer a small enforceable invariant over another monitoring layer.

> Do not recommend a new mechanism until you identify the measured failure that existing mechanisms cannot handle.

Will made simplification an explicit constraint on recommendations. In the selected episodes, VIOLET removed per-run bookkeeping and DAEDALUS withdrew an invalid ratio. The diagnoses and remedies themselves came from agent work and external review.

The separate July [incident reconstruction](cases/03_violet-detection-to-execution-failure/incident-report.md) records human review classifying a missed action as lapsed rather than replaying it after conditions changed.

### Division of work

Will designed and operates the broader system, set review requirements, selected work and public cases, and authorized implementation and publication scope. Agents generated research, candidate protocols, code, tests, and proposed corrections. Codex reviewed claims and prepared the September public prose, source extractions, test harness, and synthetic illustration under his direction.

These records support an account of human-directed, AI-assisted work, not sole-human authorship of the technical details.

## Historical operating record

The table below preserves figures **reported as of July 26, 2026**, in public-repository commit `2c7bb55e4839be9747eef98f5a1e7821a0078c37` (`README.md`). That commit anchors what was published, not an independently reproduced private-repository census.

| Metric | Value | Historical command |
|---|---|---|
| First commit | 2026-02-01 | `git log --reverse --format=%ad --date=short \| head -1` |
| Days with commits | **172 of 176** | `git log --format=%ad --date=short \| sort -u \| wc -l` |
| Total commits | 5,117 | `git rev-list --count HEAD` |
| Agents with live state files | 38 | `ls AGENTS/*/STATUS.md \| wc -l` |
| Catalogued failure findings | **208** | `ls memory/auto/finding_*.md \| wc -l` |
| Registered predictions | **411** across 42 ledgers | `find AGENTS -name PREDICTIONS.tsv -exec awk 'FNR>1 && $0!~/^#/ && NF>2' {} \; \| wc -l` |
| Daily session notes | 128 | `ls memory/2*.md \| wc -l` |

**Measurement limits:** the July commands did not pin a private revision, so the July inputs cannot be re-derived. The September refresh in the [README](README.md#operating-record) pins the private commit it was measured at.

The prediction command counts non-comment data rows in files named exactly `PREDICTIONS.tsv`; it does not separately calculate the reported 42-ledger count. The commit-day command calculates the numerator, not the elapsed-calendar-day denominator. Other ledger names and different inclusion rules produce different populations.

The roster's active count and the count of agent directories with state files use different definitions. Findings, rows, and commits are activity measures, not prevented errors or hours saved, and they can fall as records are archived.

## Evidence forms and dates

| Material | Date or snapshot | What a public reader can check |
|---|---|---|
| Cases 1–3 | June/July 2026 episodes; public reconstructions introduced July 15 | Stated logic, chronology, concessions, and consequences; underlying private records are not bundled for independent regrading |
| Architecture and six agent packages | July 15 public reconstruction; September editorial clarifications | Role boundaries and normalized interfaces, not a September audit of the live runtime |
| Case 4: VIOLET repair | September 6 historical implementations | Frozen source-derived code under declared adapters and synthetic regression tests |
| Case 5: WALTER pilot | September 6 recorded runs | Exact instruction files, sanitized tool records, rubric chronology, and editorial behavior grades; not a fresh model run |
| Case 6: DAEDALUS withdrawal | September 5 correction | Selected pinned report/code excerpts plus a new synthetic illustration; not a full historical census |
| Case 7: VULCAN test-harness repair | September 6 historical suite revisions | Source-derived suite logic with controlled subprocess exits; not a rerun of the GPU validator or production crashes |
| Research-quality protocol | September 6 draft | A prospective design only; no results or frozen preregistration |

The older cases' source descriptions and sanitization notes remain in their READMEs. Exact operational dates or thresholds withheld in July remain withheld; their exclusion does not imply that the same gates are still live in September. The new cases' hashes support comparison with supplied artifacts, not independent authentication of their private origin.

Public task/gate interfaces are normalized teaching examples. Their vocabulary is defined at the [public lifecycle](architecture/prome-orchestration/task-lifecycle.md), not an instruction to migrate private agent files. A written contract describes required behavior; it does not establish that every operational session complied.

## Why selected cases rather than complete folders?

Important evidence is distributed across time: a claim, its original test, a challenge, a revision, and the downstream consequence. These cases collect those steps without exposing current positions, private messages, paid-source text, credentials, or operational integrations.

The selection is deliberately instructive, not representative. It includes failures and retained uncertainty, but cannot estimate their frequency. Architecture and templates provide context; the case-specific artifacts support the narrower results. Domain conclusions are historical research examples, not current recommendations.

## Evaluation boundaries

The system's incremental value over a well-prompted single model remains unproven. Persistent state may retain errors; multiple agents can share sources and model errors; extra review can add costs and new mistakes. The operating record has no matched baseline, and model versions, procedures, and operator experience changed together.

The [planned research-quality comparison](experiments/research-quality-pilot.md) would measure a smaller workflow contrast prospectively. A finding favoring the simpler workflow would be useful. No evidence here establishes autonomous trading performance, production security, or generalized reliability.
