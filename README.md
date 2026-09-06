# Selected Research-Agent Case Studies

I built and operate a persistent, human-directed research system for investigating economic and financial transmission: how an energy shock, credit constraint, or policy change moves through other domains. Agents maintain dated claims, predictions, evidence, and disagreements in Git-versioned files. Human judgment controls research direction and consequential decisions.

This portfolio shows selected research decisions, failures, and repairs—not a complete agent runtime or a claim of investment performance. Its central question is whether structured AI research produces more dependable results **after accounting for verification, coordination, and rework**.

**Portfolio revision: September 6, 2026.** Episodes, architectural snapshots, and proposed experiments have separate dates and evidence boundaries.

## Start here

These three cases offer a short route from substantive research to verification and measurement:

| Read | Question | What you can inspect |
|---|---|---|
| [SAM–RED: a thesis survives at a lower grade](cases/01_sam-red-adversarial-dialogue/) | What happens when a research claim fails its own survival bar? | A historical reconstruction of concessions, a confidence downgrade, and two complex options blocked |
| [VIOLET: a repair fails on the second run](cases/04_violet-correction-verification/) | Does a correction remain correct after state persists? | Runnable contrasts across three historical implementations, including failure and recovery controls |
| [DAEDALUS: an efficiency ratio is withdrawn](cases/06_daedalus-measurement-validity/) | Do the logs measure the outcome the scorecard claims? | Pinned source excerpts and a synthetic counterexample, not a measured prevention rate |

For another substantive research example, [BRENT's sustain test](cases/02_brent-calibration-and-deny/) denies confirmation even though the price condition passes. For experimental judgment, [WALTER's instruction pilot](cases/05_walter-instruction-pilot/) preserves two archived runs and withdraws interpretations they cannot support. The [earlier VIOLET incident](cases/03_violet-detection-to-execution-failure/) traces a detected condition to an undelivered obligation and a decision not to act late.

For a technical companion to VIOLET, [VULCAN's test-harness case](cases/07_vulcan-test-harness-false-pass/) reproduces a suite that accepted unsuccessful control runs, followed by an exact-exit-code repair.

Cases 1–3 are sanitized narrative reconstructions. Cases 4–7 add source-derived code or excerpts and explicitly distinguish historical records from new tests and illustrations. These are different evidence forms, not seven equivalent experiments.

## What I contributed

I designed and operate the system: persistent domain ownership, coordination and decision boundaries, and the process for retaining and challenging prior claims. Agents also propose changes to that design. My contribution is research direction, system design, and operational judgment—not a claim that I manually wrote every rule, analysis, or program.

Three concrete choices in my September review brief shaped the work:

- **Separate review from authority to implement.** I asked for an external second pair of eyes, beginning read-only, with findings checked at canonical owner artifacts. That allowed broad criticism without granting the reviewer permission to rewrite other agents' work.
- **Require evidence of application, not a receipt.** I explicitly distinguished delivery, consumption, downstream correction, and evidence-backed closure. A completion message was a lead to inspect, not the test of success.
- **Make simplification a constraint.** I asked reviewers to prefer a small enforceable invariant over another monitoring layer and to identify a measured failure before proposing a new mechanism. The cases show both repairs and decisions to withdraw unsupported interpretations.

These choices are documented in [operator decisions and attribution](PORTFOLIO_NOTES.md#operator-decisions-and-attribution), with short excerpts from the review brief supplied in conversation. They describe my requirements, not proof that the system always followed them.

The operational agents produced analysis, code, repairs, and tests. Codex contributed external review and prepared the September public evidence packages and explanations under my direction. Each new case identifies its specific contributions and limits. I selected and authorized publication of these failures as well as their outcomes; the failures in the system and in how I built it are also mine.

## What is demonstrated

VIOLET's offline reproduction executes the selected production path using synthetic data. Seven scenarios across three snapshots reproduce **21 expected traces**, including historical defects. Two negative controls reject an incorrectly substituted baseline and a disabled writer.

With the declared dependency installed, run from the repository root:

```bash
python3 -B cases/04_violet-correction-verification/reproduction/run_checks.py --selftest
```

[Setup and scope](cases/04_violet-correction-verification/reproduction/) explain the dependency, source extraction, adapters, and excluded behavior. This is a local regression result, not exhaustive software validation.

WALTER's two runs both meet the behavior rubric on one fixture. Its artifact checker does not rerun models or establish general equivalence. DAEDALUS's illustration shows why incompatible counts cannot identify the desired quantity; it does not recount the private logs.

VULCAN's offline companion executes historical suite logic with specified subprocess results. It reproduces a false pass and its repair; it does not run the underlying GPU validator or measure research productivity.

## Open research question

**Does separating analysis and review improve research quality enough to justify its additional costs?**

The [prospective pilot](experiments/research-quality-pilot.md) compares analyst self-review with a role-separated analyst/reviewer workflow using the same model, evidence, call limit, and token ceiling. It proposes 12 constructed tasks, two conditions, and two repetitions: 48 runs. Quality, model usage, human verification, and rework would be recorded separately.

**That pilot has not been run.** It is distinct from WALTER's completed instruction exercise. Persistent-memory and coordination ablations remain later questions, not demonstrated benefits.

The operating history supplies useful hypotheses but no matched system-level counterfactual. Models, protocols, and operator experience changed together. The cases were selected for instructiveness, not randomly sampled. Neither agent count nor corrections found establishes productivity, prevention, or superiority over a simpler workflow. A result favoring the simpler workflow would be useful.

## Operating record

The private system has been operated since February 2026. A July 26 portfolio snapshot reported 172 commit-days out of 176 and 208 catalogued failure findings. These are **previously reported activity counts**, not September measurements or independently reproduced performance results.

The [historical count table and measurement limits](PORTFOLIO_NOTES.md#historical-operating-record) preserve the original figures and commands. The old commands lack a pinned private snapshot; running them now would produce a new inventory, not reproduce July.

## Architecture and further reading

[System overview](SYSTEM_OVERVIEW.md) explains the role boundaries: domain agents own analysis, PROME coordinates, NEXUS synthesizes, and RED challenges. The [public agent packages](agents/) provide six reconstructed operating contracts, schemas, and non-live examples—not self-contained production deployments.

For more detail:

- [Persistent domain ownership](architecture/persistent-domain-ownership.md), [task and gate lifecycle](architecture/prome-orchestration/task-lifecycle.md), and [orchestration modes](architecture/orchestration-mode-split.md).
- [Cross-domain brief schema](architecture/nexus-brief-schema.md) and [reusable templates](templates/).
- [Lessons learned](LESSONS_LEARNED.md) and [portfolio background, attribution, and evidence boundaries](PORTFOLIO_NOTES.md).

Private working state, positions, credentials, and operational integrations are excluded. Private source artifacts are available for review on request under appropriate access arrangements. The public material supports inspection of particular reasoning and failure mechanisms; it does not establish production-grade runtime reliability or financial returns.
