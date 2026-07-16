# PROME Example State

> Demonstration only. This is fictional task state, not a current system docket.

## Task

| Field | Example |
|---|---|
| Task ID | `DEMO-001` |
| Objective | Test whether two reports provide independent support for one mechanism |
| Owner | NEXUS |
| Reviewer | RED |
| State | `ACTIVE` |
| Completion evidence | Antecedent map, confidence revision, and routed conclusion |
| Human decision | None unless reviewers disagree after two rounds |

## Lifecycle

1. PROME converts the request into `DEMO-001`.
2. NEXUS maps both reports to their causal roots.
3. RED tests whether the independence claim survives.
4. NEXUS returns `DONE`, `PARTIAL`, or `BLOCKED` with evidence.
5. PROME records the result and creates follow-up only if an unresolved decision remains.

## Example completion

```text
STATUS: DONE
TASK_ID: DEMO-001
RESULT: The two reports share one antecedent and count as one evidentiary leg.
CHANGED: synthesis/DEMO-001.md
GAPS: A second independent observation has not been identified.
HUMAN_DECISION: none
FOLLOW_UP: Reassess only if a separately sourced observation arrives.
```
