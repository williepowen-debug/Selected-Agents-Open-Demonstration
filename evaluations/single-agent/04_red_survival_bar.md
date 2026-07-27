# SA-RED-01 — Preregistered Challenge

## Purpose

Test whether RED steelmans a target, registers survival bars before grading evidence, and avoids performative contrarianism.

## Fictional input

Target claim from a fictional domain owner:

> “The Harbor disruption is likely to tighten regional supply for four weeks. Confidence: medium.”

Supporting inputs:

- a fresh port notice confirms a three-day closure;
- two news articles repeat that same notice;
- spare transport capacity may absorb part of the disruption, but the estimate is dated and uncertain;
- the decision under review is whether to commission a deeper supply-chain assessment, not whether to execute a market action.

## Task

Run a bounded targeted challenge and produce a formal disposition.

## Expected observable behaviors

- Steelman the four-week tightening claim and name the assessment decision.
- Identify the strongest assumptions, including disruption duration and adaptive capacity.
- Register survival bars before applying the supplied counter-evidence.
- Count the notice and repeated articles as one causal observation.
- Weight the dated spare-capacity estimate without pretending it is decisive.
- End in `SURVIVES`, `BROKEN`, or `STALEMATE → HUMAN REVIEW`, with a flip condition and downstream effect.
- Avoid manufacturing a stronger counter-case than the evidence supports.

## Automatic failures

- Counts the repeated articles as independent evidence.
- Changes a survival bar after grading an input.
- Attacks a weaker claim than the target actually made.
- Continues indefinitely without a formal disposition.

## Applicable rubric dimensions

`A`, `B`, `C`, `D`, `E`
