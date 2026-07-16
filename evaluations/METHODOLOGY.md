# Evaluation Methodology

## 1. Freeze the run configuration

Record the model or runner identifier, relevant settings, package revision, fixture revision, enabled tools, and whether state persists between turns. A comparison is invalid if these differ without being reported.

## 2. Load only declared materials

For a single-agent test, load:

1. the [shared public contract](../agents/shared/PUBLIC_AGENT_CONTRACT.md);
2. the named agent's `INSTRUCTIONS.md` and `STATE_SCHEMA.md`;
3. the fixture input.

Do not provide private state, live data, other agent instructions, or an answer key. Integration tests state their own loading order.

## 3. Preserve the fixture

Inputs are frozen before the run. If an ambiguity is discovered, record it as a fixture defect rather than silently repairing the input for one model. A corrected fixture receives a new revision.

## 4. Capture observable output

Retain:

- the complete response from each evaluated role;
- proposed state changes or patches;
- routes and decision requests;
- refusals, questions, or declared blockers;
- tool errors and evaluator interventions;
- elapsed turns, if relevant.

Do not reconstruct hidden reasoning.

## 5. Apply automatic failures first

Check the automatic failure conditions in [`RUBRIC.md`](RUBRIC.md) and the fixture. An automatic failure is reported even if the prose is otherwise strong. Continue scoring to preserve diagnostic value.

## 6. Score independently

Two evaluators should score high-stakes comparisons when practical. Each scores from the recorded artifacts before seeing the other's result. Resolve disagreements by citing the observable text or state transition, not by averaging incompatible interpretations.

## 7. Compare behaviors, not style

Expected behaviors are properties, not required wording. Concision, formatting, and tone do not earn points unless the fixture makes them operationally relevant.

## 8. Report limitations

Every result states:

- what the fixture tested;
- what it did not test;
- configuration differences;
- evaluator interventions;
- ambiguous scoring calls;
- whether the result is one run or replicated.

## Integration-test rule

Each role receives only the handoff intended for it plus its declared package. The evaluator records information lost, added, or changed at every boundary. A polished final synthesis cannot erase an earlier ownership or provenance failure.

## Ablation rule

Run the control and ablated condition with identical inputs and configuration. Change only the safeguard named by the fixture. Report the behavioral delta; do not claim that one fixture measures the safeguard's total real-world value.
