# Task and Action-Gate Lifecycle

This document reconstructs the system's task and action-gate protocols without publishing live operational state.

## Completion record

Every delegated task should end with a compact completion record:

```text
STATUS: DONE | PARTIAL | BLOCKED
CHANGED: artifacts created or modified
RESULT: concrete outcome, including counts where useful
GAPS: what could not be completed and why
OPERATOR_NEEDS: decisions or access only the operator can provide
FOLLOW_UP: the next bounded action, or none
```

The record is both a summary and a routing surface. `PARTIAL` is a valid result. A gap without a reason is not actionable, and an operator request should be reserved for things that genuinely require human authority or access.

## Action-gate ledger

Some preregistered conditions require an action when they fire. Those conditions are indexed separately from ordinary predictions.

| Field | Meaning |
|---|---|
| Gate ID | Stable identity for the obligation |
| Registered | When the gate became authoritative |
| Owner | Agent responsible for evaluating it |
| Condition | Precommitted firing rule |
| Consequence | Required action or escalation |
| State | Live, fired-unexecuted, resolved, lapsed, or retired |
| Last checked | Freshness control |
| Source | Canonical full logic |

### State definitions

- `LIVE`: the condition is active and being checked.
- `FIRED-UNEXECUTED`: the condition fired but the required action is not evidenced. This blocks unrelated new work until resolved or escalated.
- `RESOLVED`: the condition was evaluated and its consequence or stand-down was recorded.
- `LAPSED`: the original action is no longer valid because time or context changed.
- `RETIRED`: the gate no longer belongs to the active system.

## Fictional example

```text
GATE-DEMO-01
Condition: two independent sensors cross their preregistered lines within 24 hours
Consequence: open a same-session review packet for human approval
State: LAPSED — detected three days late; environment materially changed
Remediation: add owner-independent ledger and freshness scan
```

The example's important feature is not the sensor. It is the refusal to pretend that a late action is equivalent to the action originally approved.
