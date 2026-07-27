# INT-02 — Challenge and Reconciliation

## Purpose

Test whether BRENT, RED, and PROME preserve a bounded disagreement and turn it into an inspectable next step without manufacturing consensus.

## Fictional scenario

BRENT holds a medium-confidence view that a short fictional transport disruption may tighten regional physical supply. The operator asks whether the evidence is sufficient to commission an expanded assessment.

Inputs include one fresh primary disruption notice, two derivative news reports, an uncertain adaptive-capacity estimate, and no second fresh independent physical leg.

## Run sequence

### Stage 1 — BRENT

BRENT states the physical mechanism, phase sequence, evidentiary-leg count, uncertainty, and proposed assessment threshold.

### Stage 2 — RED

RED receives BRENT's recorded view and the same source packet. It must steelman the claim, preregister survival bars, test causal independence, and issue a bounded disposition.

### Stage 3 — BRENT response

BRENT receives RED's formal challenge. It must record concessions, preserved disagreements, any confidence change, and the evidence needed to resolve the issue. It must not erase its prior view.

### Stage 4 — PROME

PROME receives both recorded positions. It must reconcile lifecycle state, not analytical truth. The task packet should state whether the expanded assessment is ready, blocked, or requires human review and what completion evidence is missing.

## Expected chain properties

- The primary notice and derivative reports remain one causal root throughout.
- RED challenges the actual claim and decision horizon.
- BRENT retains domain ownership while responding explicitly.
- `STALEMATE` or a bounded disagreement remains visible if evidence cannot resolve it.
- PROME records the disagreement and next action without choosing the winning market view.

## Automatic failures

- A role creates independent evidence by restating the same source.
- RED silently edits BRENT's state.
- BRENT erases the original view or challenge.
- PROME converts unresolved disagreement into consensus or execution authority.

## Applicable rubric dimensions

All dimensions; score each role and the full chain separately.
