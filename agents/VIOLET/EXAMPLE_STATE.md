# VIOLET Example State

> Resolved historical demonstration only. No current thresholds or actionable signals are included.

## Gate lifecycle

| Stage | Historical reconstruction |
|---|---|
| Detection | Two registered conditions fired |
| Delivery | Required review packet absent |
| Review | Failure discovered seven days later |
| Decision | Original action classified `LAPSED` |
| Execution | None |
| Fresh analysis | Queued premise no longer held; `NO-FIRE` |

## Remediation state

```text
GATE STATE: LAPSED
OWNER-INDEPENDENT RECORD: CREATED
FIRED-UNRESOLVED CHECK: BLOCKING
STALE-PREMISE REPLAY: PROHIBITED
CANARY COVERAGE: EXPLICITLY MAPPED
DARK-CANARY RULE: ENABLED
CURRENT ACTION: NONE
```

See the [incident report](../../cases/03_violet-detection-to-execution-failure/incident-report.md) and [fresh look](../../cases/03_violet-detection-to-execution-failure/fresh-look.md).
