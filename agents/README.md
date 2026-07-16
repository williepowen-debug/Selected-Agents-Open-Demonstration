# Public Agent Packages

This directory contains public-safe packages for six representative agents from the larger research system.

They are closer to the working agents than a character profile or a single prompt: each package defines domain ownership, operating rules, public state, handoff behavior, and an inspectable example. They are still reconstructions. Private working memory, live research state, current thresholds, operational tooling, and internal messaging infrastructure are deliberately absent.

## Package index

| Agent | Function | Package | Related evidence |
|---|---|---|---|
| PROME | Orchestration and task lifecycle | [PROME](PROME/) | [Architecture](../architecture/prome-orchestration/) |
| NEXUS | Cross-domain synthesis | [NEXUS](NEXUS/) | [Brief schema](../architecture/nexus-brief-schema.md) |
| SAM | Japan macro and carry transmission | [SAM](SAM/) | [SAM–RED case](../cases/01_sam-red-adversarial-dialogue/) |
| RED | Adversarial review | [RED](RED/) | [SAM–RED case](../cases/01_sam-red-adversarial-dialogue/) |
| BRENT | Oil and energy-market research | [BRENT](BRENT/) | [Calibration case](../cases/02_brent-calibration-and-deny/) |
| VIOLET | Volatility-regime monitoring | [VIOLET](VIOLET/) | [Failure-and-learning case](../cases/03_violet-detection-to-execution-failure/) |

## Common layout

Every package contains:

- `README.md` — purpose and boundaries;
- `INSTRUCTIONS.md` — the public operating contract;
- `STATE_SCHEMA.md` — a public interface preserving the function of the agent's state; filenames are retained where useful and normalized where disclosure or portability warrants it;
- `EXAMPLE_STATE.md` — non-live demonstration state.

All six inherit the [public agent contract](shared/PUBLIC_AGENT_CONTRACT.md).

## How to use these packages

A file-capable agent runner can load the shared contract and one agent's instructions, then create a state directory conforming to that package's public schema. The runner must supply research tools and data adapters separately.

These packages do not authorize autonomous trading, public posting, external messaging, credential use, or changes outside the agent's owned state. Consequential actions remain human-controlled.

## What these packages are not

They are not raw exports, current market views, self-contained production services, or proof that six language-model sessions are independent sources. The strongest claims in this repository remain tied to the dated cases and their observable artifacts.
