# Evaluation Coverage Matrix

This matrix shows the public-contract behaviors each fixture directly tests. A check means the behavior has explicit input, expected evidence, and a failure condition; it does not mean the behavior has already passed.

## Rubric dimensions

| Fixture | Role fidelity | Evidence discipline | Uncertainty | State lifecycle | Handoff quality | Human authority |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| `SA-PROME-01` | ✓ |  | ✓ | ✓ | ✓ | ✓ |
| `SA-NEXUS-01` | ✓ | ✓ | ✓ |  | ✓ |  |
| `SA-SAM-01` | ✓ | ✓ | ✓ |  | ✓ | ✓ |
| `SA-RED-01` | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| `SA-BRENT-01` | ✓ | ✓ | ✓ | ✓ |  |  |
| `SA-VIOLET-01` | ✓ | ✓ |  | ✓ | ✓ | ✓ |
| `INT-01` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `INT-02` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `ABL-01` |  | ✓ | ✓ |  | ✓ |  |
| `ABL-02` |  |  |  | ✓ | ✓ | ✓ |

## System safeguards

| Safeguard | Primary fixtures |
|---|---|
| Bounded domain ownership | `SA-PROME-01`, `SA-NEXUS-01`, `SA-SAM-01`, `INT-01`, `INT-02` |
| Source freshness | `SA-NEXUS-01`, `SA-SAM-01`, `SA-RED-01` |
| Causal-root independence | `SA-NEXUS-01`, `SA-RED-01`, `SA-BRENT-01`, `INT-02`, `ABL-01` |
| Observation vs mechanism vs threshold | `SA-NEXUS-01`, `SA-SAM-01`, `SA-BRENT-01`, `INT-01` |
| Preregistered tests | `SA-RED-01`, `SA-BRENT-01` |
| Prior-view preservation | `SA-RED-01`, `SA-BRENT-01`, `INT-02` |
| Detection-to-execution separation | `SA-PROME-01`, `SA-VIOLET-01`, `INT-01`, `ABL-02` |
| Lapse and fresh-premise handling | `SA-VIOLET-01`, `ABL-02` |
| Partial or unresolved completion | `SA-PROME-01`, `SA-NEXUS-01`, `INT-02` |
| Human consequential-action boundary | `SA-PROME-01`, `SA-SAM-01`, `SA-VIOLET-01`, `INT-01`, `INT-02`, `ABL-02` |

## Deliberate exclusions

The initial suite does not directly evaluate live data retrieval, long-horizon calibration, scheduler reliability, credential isolation, external delivery infrastructure, profitability, or factual forecasting accuracy. Those require different fixtures, runtime controls, and—where live systems are involved—additional safety review.
