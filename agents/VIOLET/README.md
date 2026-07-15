# VIOLET — Volatility-Regime Monitoring Agent

VIOLET owns volatility-regime evidence: implied-volatility structure, volatility of volatility, skew, curve shape, positioning context, and the timing of transmission from other stress channels into volatility markets.

VIOLET is also the clearest example of an operational lesson: correct detection is not the same as delivery, review, decision, or execution.

## Package contents

- [Instructions](INSTRUCTIONS.md)
- [State schema](STATE_SCHEMA.md)
- [Example state](EXAMPLE_STATE.md)
- [Shared contract](../shared/PUBLIC_AGENT_CONTRACT.md)

## Related evidence

- [Detection-to-execution failure case](../../cases/03_violet-detection-to-execution-failure/)
- [Canary-map reconstruction](../../cases/03_violet-detection-to-execution-failure/canary-map.md)

## Publication note

This package preserves VIOLET's domain, staleness, canary-coverage, and action-gate separation. It excludes live volatility levels, current thresholds, positions, private tools, active gates, current routes, and working research state.
