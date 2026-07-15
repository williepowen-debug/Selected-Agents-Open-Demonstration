# VIOLET State Schema

> Public interface note: source-aligned filenames are retained where they clarify VIOLET's real operating model. The external gate-ledger row preserves the owner-independent boundary introduced after the historical incident; it is not a VIOLET-owned private file export.

## Selected public state surfaces

| File | Purpose |
|---|---|
| `STATUS.md` | Current volatility regime, fresh observations, mechanism grades, and unresolved conditions |
| `SCRATCH.md` | Compact current state, dark coverage, and next work |
| `MEMORY.md` | Durable agent-specific methods, definitions, and calibration lessons |
| `CALENDAR.md` | Human-readable catalyst view, reconciled to the structured catalyst ledger |
| `thesis/VIX_THESIS.md` | Durable regime definitions, transmission framework, and calibrated tests |
| `thesis/CHANGELOG.md` | Material old view → new view changes |
| `CANARY_MAP.md` | Instrument, owner, cadence, calibration status, and route coverage |
| `workbook/CATALYSTS.tsv` | Dated events and expected evidence checks |
| `workbook/KB.tsv` | Durable sourced facts and calibration outcomes |
| `workbook/VX_DAILY.tsv` | Dated volatility-surface observations |
| `SIGNAL_INTAKE.md` | Durable external-signal scope and registered routing categories; no live observations |
| `MAINTENANCE.md` | Structural changes to documents, schemas, protocols, and tools |
| PROME-owned gate ledger | Owner-independent condition-to-consequence lifecycle; VIOLET supplies detection and evidence |
| `NEXUS_BRIEF.md` | Cross-domain sending and waiting edges |

## Canary record

The record below is a normalized public interface for the canary map, not a literal copy of the private file's schema.

```text
canary_id	instrument_class	owner	purpose	cadence	last_observed	calibration_state	threshold_ref	route	coverage_state
```

Allowed calibration states: `CALIBRATED`, `PROVISIONAL`, `UNCALIBRATED`, `EXTERNAL`.

Allowed coverage states: `LIVE`, `DARK`, `MISSING_OWNER`, `STALE`, `RETIRED`.

## Gate record

The record below expresses the cross-agent gate contract. The canonical ledger remains owner-independent rather than VIOLET-owned.

```text
gate_id	condition	detected_at	delivered_at	reviewed_at	decided_at	executed_at	state	disposition
```

Empty timestamps are evidence. They identify the stage at which the workflow stopped.
