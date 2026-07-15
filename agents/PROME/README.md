# PROME — Orchestration Agent

PROME is the system's chief-of-staff layer. It turns human requests into bounded work, assigns analytical ownership, tracks task and decision state, processes completions, and keeps unresolved obligations visible.

PROME is not a market-domain expert and does not replace another agent's judgment. Its central design problem is coordination without silent analytical override.

## Package contents

- [Instructions](INSTRUCTIONS.md)
- [State schema](STATE_SCHEMA.md)
- [Example state](EXAMPLE_STATE.md)
- [Shared contract](../shared/PUBLIC_AGENT_CONTRACT.md)

## Related architecture

- [PROME orchestration](../../architecture/prome-orchestration/)
- [Task lifecycle](../../architecture/prome-orchestration/task-lifecycle.md)
- [Orchestration-mode split](../../architecture/orchestration-mode-split.md)

## Publication note

This package reconstructs PROME's stable role and task-state model. It excludes operator correspondence, current priorities, live decisions, machine and repository procedures, messaging internals, credentials, and system-health records.
