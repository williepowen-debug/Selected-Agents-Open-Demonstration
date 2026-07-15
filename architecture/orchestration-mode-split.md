# Orchestration Mode Split

Multi-agent work has two different shapes. Treating them as one creates unnecessary cost, context pressure, and coordination failure.

| | Fan-out execution | Live orchestration |
|---|---|---|
| Best for | Independent, templated tasks | Tasks with mid-flight dependencies or decisions |
| Coordinator's job | Specify, collect, verify | Route, interpret, decide, and iterate |
| Interaction | Results can return together | Later steps depend on earlier findings |
| Main risk | Poorly specified bulk work | Context saturation and coordination overhead |

## Fan-out test

Use fan-out when all of the following are true:

- tasks are independent;
- prompts are substantially similar;
- no human decision is required between sub-steps;
- collection and synthesis can be specified in advance.

If any condition is false, the decision spine requires live orchestration.

## The common hybrid

Most sessions are hybrid:

1. scope the work and identify owners;
2. fan out independent inventory or verification tasks;
3. collect results into a common format;
4. live-orchestrate only the contradictions, dependencies, and human decisions;
5. verify consequential claims before changing canonical state.

## Verification tiers

Not every claim warrants the same rework.

- Claims that change canonical state or trigger consequential action require primary-source verification.
- Domain judgments are reviewed for reasoning and checked more deeply when surprising or load-bearing.
- Mechanical claims are verified through artifact and version evidence rather than by repeating the work.

## Record versus reality

A routed request is not a built artifact. A generated artifact is not a consumed obligation. A detected condition is not an executed action. The system records these as different events because collapsing them makes reliability look better while preventing diagnosis.
