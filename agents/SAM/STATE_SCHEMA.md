# SAM State Schema

> Public interface note: these filenames follow SAM's source-aligned state model. Contents shown here are structural descriptions; live values and working state are excluded.

## Selected public state surfaces

| File | Purpose |
|---|---|
| `STATUS.md` | Current scenarios, confidence, fresh observations, and registered threshold state |
| `thesis/THESIS.md` | Slow-moving structural mechanisms and scenario definitions |
| `thesis/CHANGELOG.md` | Material old view → new view revisions |
| `thesis/PREDICTIONS.tsv` | Preregistered claims and calibration outcomes |
| `thesis/PREDICTIONS_ARCHIVE.md` | Full resolution evidence for closed forecasts |
| `thesis/timeline/TIMELINE.md` | Event progression, branch points, and resolved outcomes |
| `docket/CALENDAR.md` | Forward events and what evidence each can provide |
| `docket/CATALYSTS.tsv` | Machine-readable dated catalysts reconciled to the calendar |
| `NEXUS_BRIEF.md` | Cross-domain sending and waiting edges |
| `MEMORY.md` | Compact session continuity plus durable agent-specific lessons; current market tables stay elsewhere |
| `MAINTENANCE.md` | Structural changes to documents, schemas, protocols, and tools |

## Scenario record

This is a normalized public interface for scenario state, not a literal copy of a private SAM table.

```text
scenario	probability	key_mechanism	supporting_evidence	counter_evidence	confirmation	falsification	as_of
```

Scenario probabilities should sum to approximately 100%. A change in weight must cite the changed evidence, not merely a changed narrative.

## Prediction record

Use the repository's [prediction-ledger template](../../templates/prediction-ledger.tsv). Closed predictions preserve the original claim, resolution, mechanism grade, and one-line calibration lesson.
