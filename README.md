# Selected Research-Agent Case Studies

I run a persistent, human-directed research system that investigates economic and financial transmission: how an energy shock, a credit constraint, or a policy change moves through other domains. Some thirty specialized agents keep dated claims, predictions, evidence, and disagreements in Git-versioned files. I set the direction and make the consequential calls.

The rule that holds it together is simple to state and hard to keep: **a claim of completion is itself a claim.** A test that passes, a receipt that says delivered, a ratio that computes, a correction that says corrected: each gets checked at the artifact it describes, not at the message about it. Every case here is that rule finding something a green result had missed. A repair that failed on its second run. A test harness that accepted crashing controls. An efficiency ratio whose two inputs counted different things. A thesis that survived only at a lower grade. A desk that was right about India and wrong about Qatar by six times, from the same page. I publish the failures because they are where the method shows.

**Portfolio revision: September 6, 2026.** Episodes, architectural snapshots, and the proposed experiment carry their own dates and evidence boundaries.

## Start here

Four cases give a short route from substantive research to verification and measurement:

| Read | Question | What you can inspect |
|---|---|---|
| [SAM–RED: a thesis survives at a lower grade](cases/01_sam-red-adversarial-dialogue/) | What happens when a research claim fails its own survival bar? | A reconstruction of concessions, a confidence downgrade, and two options blocked |
| [VIOLET: a repair fails on the second run](cases/04_violet-correction-verification/) | Does a correction stay correct once state persists? | Runnable contrasts across three historical implementations, with failure and recovery controls |
| [DAEDALUS: an efficiency ratio is withdrawn](cases/06_daedalus-measurement-validity/) | Do the logs measure what the scorecard claims? | Pinned source excerpts and a synthetic counterexample |
| [FERT: right about India, wrong about Qatar](cases/08_fert-matched-pair/) | Does a ledger row's date mean what it says? | Two verbatim graded rows, the March lines they came from, and a check on dates and arithmetic |

The other four: [BRENT's sustain test](cases/02_brent-calibration-and-deny/) denies confirmation even though the price condition passes. [VULCAN's test-harness case](cases/07_vulcan-test-harness-false-pass/) is the technical companion to VIOLET's, a suite that accepted failed control runs and the exact repair. [WALTER's instruction pilot](cases/05_walter-instruction-pilot/) keeps two archived runs and withdraws the interpretations they cannot support. The [earlier VIOLET incident](cases/03_violet-detection-to-execution-failure/) traces a detected condition to an undelivered obligation and a decision not to act late.

Cases 1–3 are sanitized narrative reconstructions. Cases 4–8 bundle source-derived code, excerpts, or ledger rows with pinned private revisions and hash manifests.

## What I contributed

I designed and operate the system: persistent domain ownership, the coordination and decision boundaries, and the process for keeping and challenging prior claims. Agents propose changes to that design and often make them. Three choices in my September review brief shaped the new cases:

- **Separate review from authority to implement.** The external reviewer started read-only, with every finding checked at the owning agent's artifact. That allowed broad criticism without granting anyone permission to rewrite another agent's work.
- **Require evidence of application, not a receipt.** Delivery, consumption, downstream correction, and evidence-backed closure are four different events. A completion message is a lead to inspect, not the test of success.
- **Make simplification a constraint.** Prefer a small enforceable invariant over another monitoring layer, and name the measured failure before proposing a new mechanism. Two of the four new cases end in subtraction.

The brief excerpts are in [operator decisions and attribution](PORTFOLIO_NOTES.md#operator-decisions-and-attribution). The agents produced the analysis, code, repairs, and tests. Codex contributed external review and prepared the September evidence packages and prose under my direction. I selected and authorized publication of these failures. The failures in the system, and in how I built it, are mine.

## What you can run

Each September case ships an offline check. From the repository root:

```bash
# VIOLET: 21 expected traces across three snapshots, plus 2 negative controls (needs pandas 3.0.3)
python3 -B cases/04_violet-correction-verification/reproduction/run_checks.py --selftest

# VULCAN: 6 expected traces including the historical false pass, plus 2 reproduction controls (standard library)
python3 -B cases/07_vulcan-test-harness-false-pass/reproduction/run_checks.py --selftest

# WALTER: 8 archived artifacts against their hashes, instruction sizes, and the run chronology
python3 -B cases/05_walter-instruction-pilot/check_artifacts.py

# DAEDALUS: the excerpt hash and the two-history counterexample
python3 -B cases/06_daedalus-measurement-validity/counterexample.py

# FERT: evidence hashes, the March and August dates, no probability in either confidence cell, 77 / 12.8
python3 -B cases/08_fert-matched-pair/check_rows.py
```

Each reproduction README states what the harness substitutes and what it leaves out. The VIOLET and VULCAN harnesses execute source-derived production code against synthetic fixtures; the WALTER checker verifies archived records without rerunning models; the DAEDALUS script is an illustration, not a recount of the private logs; the FERT checker verifies the bundled rows and dates, not the graded outcomes' sources.

## Operating record

The system has run near-daily since February 2026. Counts are produced by the commands shown, run against the private operating repository at commit `7a0a32ffc18c5e817f06b5cd99ec3f8aa912e246` (2026-09-06 16:26 ET). The July column is the figure published in this repository's July 26 revision.

| Metric | Jul 26 | Sep 6 | Command |
|---|---|---|---|
| First commit | 2026-02-01 | 2026-02-01 | `git log --reverse --format=%ad --date=short \| head -1` |
| Days with commits | 172 of 176 | **214 of 218** | `git log --format=%ad --date=short \| sort -u \| wc -l` |
| Total commits | 5,117 | 11,364 | `git rev-list --count HEAD` |
| Agents with live state files | 38 | 39 | `ls AGENTS/*/STATUS.md \| wc -l` |
| Catalogued failure findings | 208 | **433** | `ls memory/auto/finding_*.md \| wc -l` |
| Registered predictions | 411 across 42 ledgers | **482** across 44 ledgers | `find AGENTS -name PREDICTIONS.tsv -exec awk 'FNR>1 && $0!~/^#/ && NF>2' {} \; \| wc -l` |
| Daily session notes | 128 | 169 | `ls memory/2*.md \| wc -l` |

Two of these matter most. **214 commit-days out of 218** is the practice: a sustained operation, not a weekend build. **433 catalogued failure findings** is the research asset: each is a dated file recording something that went wrong and the procedure that changed in response.

These are activity measures. They say how much was done and recorded, not how much was prevented or how well the forecasts scored. The prediction count takes non-comment rows in files named exactly `PREDICTIONS.tsv`; other ledger definitions give other numbers, which is why the command is published. The private repository is available for review on request.

## Relationship to humanities-derived methods

Several procedures in this repository are practices cultivated in the humanities, translated into agent procedure:

- **source criticism** appears in provenance, freshness, incentive, and independence checks;
- **argument reconstruction** appears in explicit premises, survival criteria, and adversarial dialogue;
- **interpretive charity** appears in steelmanning before criticism;
- **historical contextualization** appears in dated evidence and stale-premise review;
- **hermeneutic iteration** appears in versioned interpretation and belief revision;
- **dialectic** appears in bounded disagreement, concession, and synthesis;
- **rhetorical analysis** appears in attention to source purpose and interested testimony.

The claim is not that humanities training produces better AI systems. It is that these epistemic practices can be written as procedures and then judged by their artifacts and failure modes.

## Open research question

**Does separating analysis and review improve research quality enough to justify its cost?**

The [prospective pilot](experiments/research-quality-pilot.md) compares analyst self-review with a role-separated analyst and reviewer, same model, same evidence, same call limit, same token ceiling: 12 constructed tasks, two conditions, two repetitions, 48 runs. Quality, model usage, human verification, and rework would be recorded separately. It has not been run.

The operating history supplies hypotheses, not a matched counterfactual. Models, protocols, and my own experience changed together, and the cases were selected for instructiveness rather than sampled. A result favoring the simpler workflow would be useful.

## Architecture and further reading

[System overview](SYSTEM_OVERVIEW.md) explains the role boundaries: domain agents own analysis, PROME coordinates, NEXUS synthesizes, RED challenges. The [public agent packages](agents/) provide six reconstructed operating contracts, schemas, and non-live examples.

- [Persistent domain ownership](architecture/persistent-domain-ownership.md), [task and gate lifecycle](architecture/prome-orchestration/task-lifecycle.md), and [orchestration modes](architecture/orchestration-mode-split.md).
- [Cross-domain brief schema](architecture/nexus-brief-schema.md) and [reusable templates](templates/).
- [Lessons learned](LESSONS_LEARNED.md) and [portfolio background, attribution, and evidence boundaries](PORTFOLIO_NOTES.md).

## Boundaries

Private working state, positions, credentials, and operational integrations are excluded; private source artifacts are available for review on request. This material supports inspection of particular reasoning and failure mechanisms. It does not establish production-grade runtime reliability or financial returns.
