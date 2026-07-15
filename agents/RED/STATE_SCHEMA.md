# RED State Schema

> Public interface note: these filenames follow RED's source-aligned state model. Live challenges, workbook rows, current hypotheses, and routing records are excluded.

## Selected public state surfaces

| File | Purpose |
|---|---|
| `STATUS.md` | Active challenges, hypothesis weights, counter-signals, and falsification status |
| `MEMORY.md` | Durable methodology and calibration lessons |
| `CALENDAR.md` | Narrative catalyst and falsification windows |
| `docket/CATALYSTS.tsv` | Structured forward-catalyst backbone |
| `workbook/CHALLENGES.tsv` | Challenge terms, survival bars, outcomes, and concessions |
| `workbook/PREDICTIONS.tsv` | RED's own falsifiable claims and calibration |
| `workbook/VX.tsv` | Standing counter-evidence vectors with explicit weights and flip conditions |
| `workbook/VX_HISTORY.tsv` | Audit trail for counter-evidence weight changes |
| `workbook/KB.tsv` | Sourced facts with confidence and staleness state |
| `workbook/FLOW.tsv` | Transmission pathways and break conditions |
| `thesis/FRAMEWORK.md` | Stable adversarial methodology |
| `thesis/CHANGELOG.md` | Material assessment revisions |
| `reports/` | Detailed challenge reports and bounded dialogues |
| `OUTBOX.md` | Challenges and findings presented for orchestration and domain-owner review |
| `SCRATCH.md` | Current unresolved threads and next review action |
| `MAINTENANCE.md` | Structural changes to documents, schemas, protocols, and tools |

## Challenge record

The record below combines fields distributed across RED's public state model. It is a normalized interface, not the literal private `CHALLENGES.tsv` schema.

```text
challenge_id	target	claim	decision_affected	survival_bar	counter_evidence	strength	verdict	concession	confidence_before	confidence_after	flip_condition	resolved_at
```

Allowed verdicts: `ACTIVE`, `SURVIVES`, `BROKEN`, `CONVERGED`, `STALEMATE_HUMAN_REVIEW`, `RETIRED`.

An expired `ACTIVE` challenge must be resolved, re-armed with a reason, or retired. It may not remain silently stale.
