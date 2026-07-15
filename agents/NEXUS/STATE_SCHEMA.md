# NEXUS State Schema

> Public interface note: the filenames below preserve NEXUS's source-aligned canonical surfaces. The tabular record examples normalize Markdown structures into compact public schemas; they are not claims that the private files are TSVs.

## Selected public state surfaces

| File | Purpose |
|---|---|
| `STATUS.md` | Active convergence matrix, tensions, antecedents, transmission chains, and narrative gaps |
| `PREDICTIONS_MONITOR.md` | Falsifiable cross-domain predictions and resolution grades |
| `CONFIRMED.md` | Resolved, durable syntheses with evidence references |
| `BRIEFS_MAP.md` | Input coverage, freshness, and drill-down status |
| `SIGNALS.md` | Unresolved inputs not yet absorbed into a synthesis |
| `inbox/` | Routed signals awaiting synthesis or disposition |
| `outbox/` | Questions and findings sent to owners, RED, or PROME |
| `signals_archive/` | Consumed or resolved signals mapped to the resulting synthesis |
| `brief_fallback_log.tsv` | Why raw state was consulted instead of a brief |
| `templates/` | NEXUS-owned brief schema and template |
| `research/` | Archived synthesis reports and deep-dive analysis |
| `LAST_COMPLETION.md` | Compact pass result, files read and changed, gaps, and next synthesis action |

## Convergence record

```text
convergence_id	claim	inputs	shared_antecedents	independent_legs	mechanism_grade	threshold_grade	confidence	confidence_delta_pp	last_material_update	last_full_review	flip_condition
```

## Brief-health record

```text
agent	brief_as_of	state_as_of	status	fallback_reason	note
```

Allowed `status` values: `FRESH`, `STALE`, `MISSING`, `DRILLDOWN_REQUIRED`.

Allowed fallback reasons: `stale`, `convergence`, `uncertainty`, `brief-gap`.

High drill-down volume is not automatically a defect. A repeated `brief-gap` is the stronger signal that a brief has become ceremonial rather than useful.
