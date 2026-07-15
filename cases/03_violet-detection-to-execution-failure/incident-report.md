# Incident Report — Detection Succeeded, Required Packet Disappeared

## Summary

On July 2, 2026, two independently registered conditions in VIOLET's credit-to-vol framework fired. Either condition was sufficient to require a same-session review packet. No packet was created. The omission was discovered during a July 9 backfill.

The original action was declared lapsed because the environment had materially changed. The incident produced an owner-independent gate ledger and boot-time checks for orphaned and stale obligations.

## Timeline

| Date | Event |
|---|---|
| July 1 | The action rule was registered: any qualifying gate required a same-session packet for human review. |
| July 2, morning | A persistence-and-dispersion condition crossed both of its preregistered lines. |
| July 2, morning | A separate breadth assessment had already arrived and supported the non-idiosyncratic interpretation. |
| July 2, later | VIOLET's current-state surface stopped updating. The breadth assessment remained unread. |
| July 4 | A proposed staleness guard arrived but was not consumed. |
| July 2–8 | No packet artifact appeared in the owner, downstream-construction, or orchestration histories. |
| July 9 | Backfill found that both gates had fired and that no packet existed. |
| July 9 | Human review classified the original action as `LAPSED`; no retroactive packet was built. |
| July 9 | PROME created an owner-independent action-gate ledger and blocking fired-unexecuted state. |
| July 11 | VIOLET applied the staleness guard, ran a fresh analysis, and later created a canary map. |

## What worked

- The quantitative condition was computable from data already held by the agent.
- The independent breadth assessment had been completed.
- Both gates were recorded strongly enough to reconstruct the miss.
- Git history made it possible to test whether the packet artifact existed.
- The agent surfaced the failure instead of silently acting late.

## What failed

### 1. Detection was owner-local

The gate logic lived with VIOLET, and the same agent's state froze as the conditions resolved. No independent surface was checking whether the required consequence occurred.

### 2. Delivery was mistaken for consumption

The breadth assessment reached an inbox but remained unread. File presence did not prove integration.

### 3. The action lacked an owner-independent obligation

The system could reconstruct “the condition fired” and “the artifact does not exist,” but it had no standing ledger that treated the gap itself as blocking.

### 4. Staleness was visible but not mechanically decisive

The frozen state and unconsumed repair packet were both discoverable. Nothing promoted them into an exception that interrupted normal work.

## Why the action lapsed

A packet built seven days later would not have represented the decision approved on July 1. Volatility, energy prices, and credit evidence had changed. One original gate would not have re-fired against the latest available observation.

The system therefore separated two conclusions:

1. the original monitoring and delivery workflow failed; and
2. the original market action was no longer authorized.

This distinction prevented a process postmortem from becoming a pretext for stale action.

## Remediation

### Owner-independent gate ledger

Every preregistered condition whose fire requires an action receives a stable record containing its owner, condition, consequence, state, last-checked date, and canonical source.

### Blocking exception state

`FIRED-UNEXECUTED` blocks unrelated new work until the obligation is cleared or escalated.

### Freshness scan

Live gates that have not been checked within their allowed interval are refreshed or explicitly flagged.

### Owner-side staleness guard

The agent's boot process checks whether core evidence and state surfaces have stopped updating.

### Fresh-look requirement

A lapsed action cannot be revived by replaying the original packet. A new analysis must establish a new premise and new conditions.

## Residual limitation

The ledger improves visibility but does not, by itself, prove that a delivered message was understood or incorporated into downstream judgment. Consumption and integration remain separate measurement problems.
