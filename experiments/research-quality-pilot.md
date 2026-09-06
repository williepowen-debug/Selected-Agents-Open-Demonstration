# Research-quality pilot: benefit after verification and rework

**Status: PLANNED — not run.** This is a prospective protocol draft, not a preregistration, benchmark result, or claim that the existing fleet is superior. Freeze the task set, prompts, model configuration, rubric, and budget before an evaluation run; any development runs use separate practice tasks.

## Question

Does separating analysis and review improve the reliability of a research deliverable relative to a well-prompted single agent with an equal opportunity to self-review? What additional model usage and human effort does either workflow require?

The [operating record](../README.md#operating-record) generates hypotheses, but supplies no matched counterfactual. [Case 4](../cases/04_violet-correction-verification/) supplies a reproducible mechanism failure, not an estimate of its prevalence or economic impact.

The completed [WALTER instruction pilot](../cases/05_walter-instruction-pilot/) is a different, two-run exercise—not an execution of this protocol. Its limited comparison and mid-run protocol addendum reinforce the need to freeze this study before running it. The [DAEDALUS metric withdrawal](../cases/06_daedalus-measurement-validity/) motivates explicit units and shared populations for quality/cost measures; historical activity counts cannot substitute for these prospective observations.

## Smallest useful first comparison

Use **12 constructed tasks**, four in each of three families, with **two repetitions per task per condition: 48 task-condition runs**. These counts define a feasibility pilot, not a statistically powered effectiveness study. Repetitions are nested within tasks, not 48 independent research problems.

| Element | Single-agent condition | Separated-review condition |
|---|---|---|
| Model | Same pinned model version and settings | Same pinned model version and settings |
| Call 1 | Analyst drafts a structured answer | Analyst drafts the same deliverable |
| Call 2 | Same agent self-reviews against a supplied checklist | Separate reviewer session critiques against that same checklist |
| Call 3 | Agent revises its answer | Analyst receives critique and revises its answer |
| Evidence and prior work | Same corpus, task-local state, and visible prior outputs | Same corpus, task-local state, and visible prior outputs |
| Budget | At most three model calls and the same total token ceiling | At most three model calls and the same total token ceiling |
| External tools | No web or outside retrieval | No web or outside retrieval |

Both conditions receive the same evidence updates at the same step. No condition receives hidden answers or an extra factual hint. The reviewer can differ in role instruction, not access to evidence. Save the full messages to make that distinction auditable.

Choose a common token ceiling on separate practice tasks and record the numerical value before freezing the evaluation. Count all input/output tokens, including role instructions, replayed context, review, and coordination. Record separately any provider-reported reasoning/cached tokens and actual charges. If the budget cannot accommodate the next call, record budget exhaustion and grade the last deliverable; do not quietly grant an extra call. Randomize condition order within task pairs.

This contrast tests a **role-separated review package**, not persistent specialization, memory, a whole fleet, or causal independence between agents. Both conditions share one model and may share its errors. Later component ablations are warranted only if the pilot and available resources justify them.

## Tasks and ground truth

1. **Source dependence:** apparently separate reports share an explicitly documented original source. Grade whether the answer preserves the number and scope of independent evidentiary roots.
2. **Supersession:** an update changes a number, population, or qualification. Grade whether the final answer uses the current evidence without discarding still-valid historical context.
3. **Correction application:** start both conditions with the same seeded error and require an update to both a canonical record and a downstream summary. Grade the actual fields, not a statement that the correction was made.

Each task includes a small synthetic document bundle, an evidence map, and an answer key withheld from both conditions. Some documents contain ambiguity where the correct response is uncertainty rather than an invented resolution. Include matched no-change controls so mechanically rejecting every claim cannot earn a good score.

Task-local state persists across the three calls; all state resets between tasks. No live financial data, positions, private fleet context, or memorized event outcome is required. Constructed evidence reduces historical-answer leakage but does not establish transfer to real research. If AI assists corpus construction, disclose that and independently check every answer key before freezing it.

## Measurements fixed before running

Report first-draft and final-deliverable scores separately:

- Citation support and correct source dependence.
- Preservation of population, date, units, and uncertainty.
- Correct application of superseding evidence to each required surface.
- Remaining seeded errors, newly introduced errors, and damage to initially correct claims.
- Review flags: valid, invalid, acted on, and ignored, each checked against the key.
- Tokens, charges, wall-clock time, and human intervention minutes per task, including failures.

Do not silently combine these into an overall score. Define a task-level acceptable-deliverable criterion in advance: all mandatory factual/state checks satisfied, with no critical unsupported claim. Report acceptable deliverables per total run cost alongside the component scores. If none qualify, report that outcome rather than an undefined efficiency ratio.

Use anonymized output IDs and randomized grading order where practical. A human grader checks the fixed rubric; ambiguous cases receive an explicit adjudication note. If an AI grader is used, preserve its outputs separately and verify consequential judgments against the key. Neither agent agreement nor the same model grading its own prose establishes accuracy. Disclose when style or context could reveal the condition; do not call the evaluation blind if masking fails.

## Human cost and research cost are different

Measure operator intervention during runs prospectively. After scoring the unassisted outputs, optionally perform a separately timed human-assisted correction pass under the same predeclared time limit for both conditions. Preserve both pre- and post-repair deliverables; do not overwrite the primary results with the repaired version.

Report task/corpus construction and experimental grading labor separately from the human verification labor an operational workflow would require. Do not infer either from commit timestamps or narrated session durations. For any wage-based cost scenario, expose the assumed hourly rate and model prices; do not present one assumed wage as an observed economic fact.

## Analysis, stopping, and limitations

- Publish all task pairs, including timeouts, budget exhaustion, failed runs, and adverse findings. Permit retries only for predeclared infrastructure failures; keep both attempts and their costs.
- Show paired differences and per-family results. With twelve tasks, use descriptive results and explicit uncertainty; avoid claims of broad statistical superiority.
- Freeze this pilot before seeing results. Any prompt or rubric adjustment begins a separately labelled follow-up, not a replacement of an inconvenient run.
- If review adds cost without useful correction, the simpler workflow remains the practical default. Do not respond automatically by adding another reviewer.
- If the rubric is ambiguous or the workflows receive unequal information, repair the experimental design before drawing a performance conclusion.

The planned output is a compact methods/results note with prompts, synthetic corpus, grading rubric, per-run outputs, and cost accounting. None of those pilot results exists in this repository yet. Ablations of persistent state, adversarial review, and coordination remain longer-term research directions, not what this initial two-condition pilot can establish.
