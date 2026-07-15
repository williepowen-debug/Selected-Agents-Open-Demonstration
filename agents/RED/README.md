# RED — Adversarial Review Agent

RED is the system's dedicated honesty mechanism. It reconstructs the strongest version of a claim, searches for genuine disconfirming evidence, tests causal independence, and forces explicit dispositions when a thesis weakens.

RED does not own domain data and cannot edit another agent's canonical judgment. It challenges through inspectable reports, survival criteria, and bounded dialogue.

## Package contents

- [Instructions](INSTRUCTIONS.md)
- [State schema](STATE_SCHEMA.md)
- [Example state](EXAMPLE_STATE.md)
- [Shared contract](../shared/PUBLIC_AGENT_CONTRACT.md)

## Related evidence

- [SAM–RED adversarial dialogue](../../cases/01_sam-red-adversarial-dialogue/)
- [Adversarial-dialogue template](../../templates/adversarial-dialogue.md)

## Publication note

This package preserves RED's steelman, challenge, weighting, prediction, and write-back rules. It excludes current theses, active challenges, portfolio context, live triggers, private reports, and internal routing state.
