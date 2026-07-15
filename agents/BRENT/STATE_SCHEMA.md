# BRENT State Schema

> Public interface note: these filenames follow BRENT's source-aligned state model. Positions, trade surfaces, current values, live catalysts, and private data integrations are excluded.

## Selected public state surfaces

| File | Purpose |
|---|---|
| `STATUS.md` | Current physical evidence, mechanism grade, threshold grade, and scenario state |
| `SCRATCH.md` | Compact next-session state and due work |
| `MEMORY.md` | Durable agent-specific calibration and process lessons |
| `LESSONS.md` | Named mistake patterns to check before new analysis, when maintained |
| `thesis/THESIS.md` | Structural supply, demand, sequencing, and transmission mechanisms |
| `thesis/CHANGELOG.md` | Material old view → new view changes |
| `thesis/PREDICTIONS.tsv` | Preregistered forecasts and calibration outcomes |
| `thesis/PREDICTIONS_ARCHIVE.md` | Full resolution evidence for closed forecasts |
| `domain/REFERENCE_TABLES.md` | Slow-moving definitions and physical reference data |
| `docket/CATALYSTS.tsv` | Dated events and registered evidence checks |
| `NEXUS_BRIEF.md` | Cross-domain sending and waiting edges |
| `MAINTENANCE.md` | Structural changes to documents, schemas, protocols, and tools |

## Evidence-leg record

This is a normalized public interface for evaluating evidence legs, not the literal schema of a private BRENT file.

```text
leg_id	claim	source	observed_at	fresh_until	causal_root	independent_of	grade	note
```

Allowed grades: `FIRED`, `NOT_FIRED`, `STALE`, `DEPENDENT`, `WRONG_ROOT`, `UNVERIFIED`.

## Prediction record

Use the repository's [prediction-ledger template](../../templates/prediction-ledger.tsv). Resolution must separately grade the observed outcome and the proposed mechanism.
