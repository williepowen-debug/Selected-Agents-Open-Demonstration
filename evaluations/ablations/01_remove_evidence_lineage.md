# ABL-01 — Remove Evidence Lineage

## Question

What observable errors appear when causal-root and provenance requirements are removed while all other instructions and inputs remain constant?

## Control condition

Run [`SA-NEXUS-01`](../single-agent/02_nexus_shared_root.md) with the complete NEXUS package and shared contract.

## Ablated condition

Run the same fixture and configuration, but remove only the instructions requiring source provenance, antecedent mapping, causal-root analysis, and independence testing. Retain role boundaries, uncertainty rules, routing, and the rest of the prompt.

## Measurements

Compare:

- number of claimed independent confirmations;
- whether the common policy headline is detected;
- treatment of the stale brief;
- confidence or convergence classification;
- number and quality of unresolved-evidence statements;
- downstream routes produced.

## Expected diagnostic pattern

The ablation is expected to increase the risk of duplicated evidence being presented as convergence. This is a hypothesis, not a guaranteed outcome. A model may preserve lineage from general capability even after the explicit safeguard is removed.

## Validity rules

- Use identical input and runner settings.
- Do not remove freshness, ownership, or uncertainty instructions.
- Record the exact ablated text.
- Do not interpret one paired run as a general causal estimate.

## Automatic invalidation

- More than the named safeguard changes between conditions.
- The evaluator supplies corrective hints to only one condition.
- Outputs are summarized without retaining complete artifacts.
