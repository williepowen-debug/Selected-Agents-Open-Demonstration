# NEXUS Brief Schema

NEXUS compares standardized agent briefs to detect cross-domain mechanisms, contradictions, and waiting dependencies. The brief is designed for connective-tissue detection, not merely token reduction.

## Priority under compression

1. Cross-domain sending and waiting edges
2. Calibration, divergence, and known tensions
3. Current domain view
4. Next decision point
5. Forward catalysts

The cross-domain section is protected because it contains the graph NEXUS is trying to reconstruct.

## Public schema

```markdown
# <AGENT> — NEXUS Brief

**Status:** <one primary claim>
**Domain:** <scope and transmission edges>
**Recent thesis pivot:** <old view> → <new view> — <reason>
**As of:** <date> | Canonical-state version: <identifier>

## VIEW
- Three to five compressed domain claims.

## CALIBRATION
- Conviction and its decomposition, when meaningful
- Divergence from the prevailing view, with framing
- Cross-agent tensions
- Material uncertainty
- Known failure patterns, referenced rather than duplicated

## CROSS-DOMAIN
### SENDING
| To | Signal | Priority | Mechanism in recipient's domain |

### WAITING FOR
| From | Input | Expected by | Why it matters | How it changes my view |

## NEXT DECISION POINT
- What
- When
- What would falsify the trigger

## FORWARD CATALYSTS
| Date | Event | Threshold or interpretation |
```

## Maintenance rules

- Refresh the brief at session closeout.
- Reference canonical ledgers rather than restating them.
- Leave tables empty when no edge exists; do not manufacture activity.
- Preserve the mechanism, not only the conclusion.
- Name when an expected input is overdue.
- Fall back to full domain state when the brief is stale, when two briefs imply an unnamed convergence, or when one agent's uncertainty belongs to another domain.

A reusable version appears in [`templates/nexus-brief.md`](../templates/nexus-brief.md).
