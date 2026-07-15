# Case 3 — VIOLET: Detection, Delivery Failure, and Adaptation

This case documents an operational failure in a volatility and credit-to-vol monitoring agent.

The underlying detectors worked. Two preregistered conditions fired. The same-session review packet required by the gate was not built, delivered, or recorded. The failure remained undiscovered for seven days.

## Result

The system did not retroactively claim success or execute a week-old instruction against changed conditions.

Instead, it:

- acknowledged the missing packet;
- classified the original action as lapsed;
- created an owner-independent action-gate ledger;
- made fired-but-unexecuted obligations blocking;
- added freshness and staleness checks;
- required a fresh analysis of the changed environment;
- later built a canary map that made missing coverage and dark instruments visible.

## Files

- [`incident-report.md`](incident-report.md) — chronology, cause, and remediation
- [`canary-map.md`](canary-map.md) — publication-safe reconstruction of the early-warning map
- [`fresh-look.md`](fresh-look.md) — changed premise and `NO-FIRE` conclusion

## Editorial note

The source artifacts included a July 9, 2026 backfill memorandum, the historical action-gate row, selected evidence-ledger entries, a maintenance log, a July 11 fresh-look memorandum, and the current canary map.

Removed or generalized:

- implementation sizing and instrument construction;
- current live thresholds and routing actions;
- private paths, inbox filenames, and operator identifiers;
- unrelated current market conclusions.

The chronology and system changes are preserved. The public files do not provide a current trading or monitoring surface.
