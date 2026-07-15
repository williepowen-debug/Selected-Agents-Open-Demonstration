# Calibration Extract

This is a public reconstruction of the durable calibration findings in BRENT's private prediction ledger. It excludes open predictions and current market state.

## Pattern 1 — Underconfidence on direct constraints

Predictions grounded in storage arithmetic, physical capacity, or chokepoint geometry repeatedly resolved more strongly than BRENT's assigned confidence suggested.

**Lesson:** When the constraint is direct and binding, confidence should be anchored higher than when the claim depends on discretionary behavior.

## Pattern 2 — Overconfidence on third-order transmission

Two historical failures followed the same structure:

```text
energy condition → input cost → intermediate actor → industrial outcome
```

In one case, policy intervention produced the observed outcome through a different mechanism. In another, an alternative supply channel prevented the expected consequence.

**Lesson:** Each intermediating actor introduces options, substitutions, and mitigation. Confidence should fall as optionality rises.

## Pattern 3 — Mechanism and threshold can separate

One resolved prediction correctly identified a transmission mechanism, but the numerical threshold could not be tested from the available evidence.

**Lesson:** Grade the mechanism and the threshold separately. Do not turn “mechanism supported” into “prediction confirmed” when the decisive number is unavailable.

## Pattern 4 — Precondition failure is not an ordinary miss

Some predictions depended on an upstream event that never occurred. Treating those as ordinary directional failures would contaminate calibration.

**Lesson:** Register the precondition explicitly and resolve `NOT-FIRED-PRECONDITION` when appropriate.

## Pre-flight check derived from the ledger

Before registering a new prediction:

1. Could the upstream condition fail to occur entirely?
2. Could the prediction become true for a different reason?
3. Could the mechanism be right while the threshold remains untestable?
4. How many actors can substitute, delay, or mitigate the chain?
5. Is the evidence fresh enough to grade the stated window?

The sustain test applies all five questions.
