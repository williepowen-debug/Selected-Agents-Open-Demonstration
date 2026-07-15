# Canary Map — Public Reconstruction

After the dropped-packet incident, VIOLET assembled an explicit map of which instruments could provide early warning for different stress channels.

This public version preserves the ownership and calibration logic but removes current thresholds and action routes.

## Three tiers

### Tier 1 — Owned and live

| Canary class | Intended lead | Historical evidence |
|---|---|---|
| Rates volatility | Duration and auction stress | Rose during an auction-stress window while headline equity volatility reversed |
| Lower-quality credit dispersion | Credit-to-vol transmission | Crossed its registered band before headline volatility responded |
| Volatility-curve shape | Peak marker rather than onset detector | Correctly refused to call a peak during a short-lived shock |
| Volatility of volatility | Formal stress confirmation | Remained quiet and prevented a false formal fire |
| Tail-skew sustain | Durable tail-bid regime | Two short runs failed the sustain count and were rejected |
| Positioning | Crowding and supply context | Flagged an extreme configuration but remained contextual rather than action-gating |

### Tier 2 — Scoped, uncalibrated, or dark

| Canary class | Gap made explicit |
|---|---|
| Currency volatility | Proxy selected, but the automated instrument was not yet built |
| Oil volatility | Instrument existed, but no defensible numerical line had been calibrated |
| Single-stock versus index protection | Signal observed through external intake; repeatable source and threshold missing |
| Index-dispersion volatility | Historical anchors existed, but one coincidence was insufficient calibration |

### Tier 3 — Referenced but owned elsewhere

The map also included signals maintained by other agents and one offshore stress signal with no clear owner. Naming the ownership gap was part of the design; assigning a decorative owner would have hidden it.

## Dark-canary rule

A canary becomes `DARK` when it has not been observed within twice its stated cadence. Darkness is not a bearish or bullish signal. It is a monitoring failure that prevents the system from claiming coverage.

## Calibration discipline

- No threshold is invented merely to fill an empty cell.
- Every line must cite a registered source or remain `TBD`.
- Worked, failed, and true-negative instances are appended over time.
- Repeated false fires demote a canary pending recalibration.
- Percentile-based lines are re-derived rather than treated as permanent constants.

## Connection to the incident

Before the map, several early-warning instruments had worked but were discovered or routed ad hoc. The map attempted to convert isolated detection wins into an inspectable routing and staleness system.
