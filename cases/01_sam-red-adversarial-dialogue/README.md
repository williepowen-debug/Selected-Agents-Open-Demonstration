# Case 1 — SAM ⇄ RED: Governed Adversarial Reasoning

This case documents a bounded adversarial exchange between SAM, the domain owner for Japan and carry dynamics, and RED, the system's adversarial reviewer.

The exchange accompanied a major thesis revision. Six challenges were registered before the dialogue. Several included explicit survival criteria, the number of rounds was capped, concessions remained in the record, and each verdict had to name what evidence would reverse it.

## Result

The thesis did not simply “win” or “lose.” It survived at a lower grade:

- confidence fell from `MEDIUM-HIGH` to `MEDIUM`;
- the expected-value claim failed its original survival bar;
- the dominant failure surface became a two-part test rather than a single condition;
- a fixed eligibility window was imposed;
- a weak causal channel was retired rather than left indefinitely “deferred”;
- two more complex implementation options were not propagated downstream.

The consequential behavior was subtraction: a weaker grade, a bounded clock, one retired mechanism, and fewer implementation choices.

## Why this is evidence

A generic debate can generate objections without changing either participant. This dialogue forced SAM to concede that its own expected-value table did not support the original confidence grade and that its first formulation named only half of the thesis's failure surface.

RED also accepted several parts of SAM's case. The result was not blanket opposition; it was a more falsifiable surviving claim.

## Files

- [`dialogue.md`](dialogue.md) — curated six-challenge transcript
- [`falsification-window.md`](falsification-window.md) — how the verdict became forward tests
- [`../../templates/adversarial-dialogue.md`](../../templates/adversarial-dialogue.md) — reusable protocol

## Editorial note

The source was a 273-line internal dialogue dated June 22, 2026. This public reconstruction preserves the participant roles, challenge order, survival bars, concessions, confidence change, and decision consequences.

Removed or generalized:

- personal and operator identifiers;
- holdings, cost basis, stops, and implementation sizing;
- live market levels and private repository paths;
- an exact future gate date that remained operationally live when this release was prepared.

The reader may infer that the protocol changed the recorded thesis and downstream choice. The reader should not infer that this selected case proves the reliability of every adversarial exchange in the larger system.
