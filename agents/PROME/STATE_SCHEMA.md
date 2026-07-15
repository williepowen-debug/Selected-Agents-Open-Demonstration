# PROME State Schema

> Public interface note: this preserves PROME's task, decision, gate, completion, and continuity functions. `HANDOFF.md`, `SCRATCH.md`, `ACTIVE_DECISIONS.md`, and `STATUS.md` are source-aligned names; the tabular task interface below is a normalized public representation rather than a literal private-directory inventory.

## Selected public state surfaces

| File | Purpose | Required discipline |
|---|---|---|
| `TASKS.tsv` | Work lifecycle | One row per stable task ID; never overwrite history silently |
| `GATES.tsv` | Conditions that require review or action | Distinguish armed, fired, reviewed, executed, lapsed, and cancelled |
| `COMPLETIONS/` | Agent completion records | Preserve result, changed artifacts, gaps, and follow-up |
| `HANDOFF.md` | Compact next-session continuity | Only current risks, decisions, and next actions |
| `SCRATCH.md` | Immediate working continuity | Short-lived next-session state, distinct from durable decisions |
| `ACTIVE_DECISIONS.md` | Current decision rail | Pending, decided, superseded, and lapsed decisions |
| `STATUS.md` | Current orchestration posture | Concise current state; details remain in owner files |
| `MAINTENANCE.md` | Structural coordination changes | Record why the orchestration design changed |

## `TASKS.tsv`

```text
task_id	created_at	owner	reviewer	objective	state	depends_on	deadline_or_trigger	completion_evidence	human_decision	updated_at
```

Allowed task states:

`PROPOSED`, `READY`, `ACTIVE`, `BLOCKED`, `PARTIAL`, `DONE`, `CANCELLED`, `LAPSED`.

## `GATES.tsv`

```text
gate_id	owner	condition	required_consequence	state	last_checked	evidence_ref	disposition
```

A gate's condition and required consequence are registered before it fires. `FIRED_UNRESOLVED` is blocking. `LAPSED` requires a new analysis rather than replay of the original action.

## Completion record

```text
STATUS: DONE | PARTIAL | BLOCKED
TASK_ID: <stable identifier>
RESULT: <concrete outcome>
CHANGED: <canonical artifacts>
GAPS: <remaining uncertainty or missing work>
HUMAN_DECISION: <question or none>
FOLLOW_UP: <next bounded action or none>
```
