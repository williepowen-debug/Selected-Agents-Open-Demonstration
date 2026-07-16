# Selected Research-Agent Case Studies

> A curated public selection from a larger fleet of 28+ specialized research agents.

This repository presents selected case studies and architectural artifacts from a larger research-agent system. It documents how persistent domain agents form and revise beliefs, test claims adversarially, coordinate evidence, track calibration, and alter procedures after failure.

It is a curated demonstration—not a complete release of the underlying system.

The broader system's July 2026 canonical roster contains 28 active specialized agents, alongside on-demand, dormant, and architectural roles. It also contains shared research infrastructure, live state, and private operational material. Rather than publishing a few agent directories without their history or context, this repository focuses on the artifacts and episodes that best reveal how the system reasons and changes over time.

## What this repository is trying to show

Many agent demonstrations begin with a prompt and end with a polished answer. That makes it difficult to see whether the agent:

- distinguished strong evidence from merely relevant evidence;
- preserved the actual disagreement between competing positions;
- revised a prior belief rather than rewriting its conclusion after the fact;
- respected criteria established before seeing the outcome;
- detected that apparently independent sources shared one causal root;
- recognized when its evidence or proposed action had become stale;
- exposed an operational failure instead of smoothing it over;
- changed the surrounding system in response to that failure.

The cases collected here emphasize those intermediate processes.

Together, they tell a larger story:

> Agents are most useful as research partners when their beliefs, evidence, disagreements, decisions, failures, and revisions are represented as inspectable state—not hidden inside a single conversational response.

## Why case studies instead of complete agent folders?

The strongest evidence of an agent’s quality is often distributed across time:

- a prediction made before an event;
- a later evaluation against preregistered criteria;
- an adversarial challenge from another agent;
- a confidence revision;
- a gate that fired but did not reach execution;
- a postmortem that changed monitoring procedures;
- a cross-domain brief that preserved the mechanism behind a finding.

Publishing an entire working directory would expose a great deal of live operational state while making these episodes harder to understand. It would also encourage readers to evaluate the agents primarily as character prompts.

This repository therefore reconstructs several bounded cases using sanitized evidence, dated artifacts, explanatory notes, and reusable templates. The goal is to make the underlying epistemic and operational mechanisms legible.

## Public agent packages

The [`agents/`](agents/) directory adds a second view: six source-derived, public-safe agent packages for PROME, NEXUS, SAM, RED, BRENT, and VIOLET.

Each package contains:

- a role and ownership boundary;
- sanitized operating instructions;
- a public state schema;
- an explicitly non-live example state.

These are traceable semantic reconstructions rather than raw directory copies. They show how an agent boots, reasons, writes back, communicates, and preserves state while withholding current research, private memory, live thresholds, positions, data adapters, and operational infrastructure.

## Behavioral evaluation layer

The [`evaluations/`](evaluations/) directory adds controlled fictional tests for the public contracts. It includes one role-fidelity fixture per agent, two multi-agent handoff tests, two component ablations, a shared rubric, and a reproducible result-record template.

The fixtures define expected observable properties and automatic failure conditions. They are evaluation specifications, not claimed benchmark results, and they do not use live market data.

## The five-part demonstration

### 1. PROME — orchestration and institutional state

PROME manages priorities, task lifecycle, action-gate state, operator decisions, and completion processing. Its inclusion prevents the cases from appearing to be several sophisticated but unrelated agents.

The important boundary is explicit: PROME coordinates domain work without replacing domain judgment. See [PROME orchestration](architecture/prome-orchestration/).

### 2. NEXUS — cross-domain connective tissue

NEXUS compares standardized briefs to preserve causal mechanisms, uncertainty, sending edges, and waiting dependencies across specialties. It is the analytical synthesis layer, not the operational orchestrator.

See the [NEXUS brief schema](architecture/nexus-brief-schema.md).

### 3. SAM ⇄ RED — governed adversarial reasoning

Six preregistered challenges produced explicit concessions, a confidence downgrade from **MEDIUM-HIGH** to **MEDIUM**, a fixed falsification window, a retired mechanism, and a decision not to propagate two more complex options.

> Can an adversarial interaction apply criteria fixed in advance and produce accountable belief revision rather than theatrical debate?

See the [SAM–RED case](cases/01_sam-red-adversarial-dialogue/).

### 4. BRENT — calibration and evidentiary restraint

A headline price condition passed, but BRENT returned **DENY** because only one of two required fresh independent evidentiary legs fired. The case shows how freshness, causal-root, and no-double-counting rules can block apparent confirmation.

> Can a domain agent resist confirmation when the evidentiary structure preregistered before the outcome has not been satisfied?

See the [BRENT case](cases/02_brent-calibration-and-deny/).

### 5. VIOLET — detection, execution failure, and adaptation

Two gates fired, but the required packet disappeared for seven days. The action was ruled lapsed, an owner-independent gate ledger was introduced, and a later fresh look concluded **NO-FIRE** against changed conditions.

> Can an agent system distinguish noticing, communicating, deciding, and acting—and redesign itself when those stages fail to connect?

See the [VIOLET case](cases/03_violet-detection-to-execution-failure/).

## Repository structure

```text
research-agent-case-study/
├── README.md
├── SYSTEM_OVERVIEW.md
├── architecture/
│   ├── persistent-domain-ownership.md
│   ├── prome-orchestration/
│   ├── nexus-brief-schema.md
│   └── orchestration-mode-split.md
├── cases/
│   ├── 01_sam-red-adversarial-dialogue/
│   ├── 02_brent-calibration-and-deny/
│   └── 03_violet-detection-to-execution-failure/
├── agents/
│   ├── shared/
│   ├── PROME/
│   ├── NEXUS/
│   ├── SAM/
│   ├── RED/
│   ├── BRENT/
│   └── VIOLET/
├── evaluations/
│   ├── single-agent/
│   ├── integration/
│   └── ablations/
├── templates/
│   ├── domain-agent-instructions.md
│   ├── prediction-ledger.tsv
│   ├── nexus-brief.md
│   └── adversarial-dialogue.md
└── LESSONS_LEARNED.md
```

The repository can be read in two ways:

### Short path

For a rapid overview:

1. Read this file.
2. Read [`SYSTEM_OVERVIEW.md`](SYSTEM_OVERVIEW.md).
3. Browse the [public agent packages](agents/).
4. Review the [evaluation inventory](evaluations/).
5. Review the summary page inside each case directory.
6. Finish with [`LESSONS_LEARNED.md`](LESSONS_LEARNED.md).

### Technical path

For architecture and implementation:

1. Begin with [`architecture/persistent-domain-ownership.md`](architecture/persistent-domain-ownership.md).
2. Review [PROME orchestration](architecture/prome-orchestration/) and its task lifecycle.
3. Review the [NEXUS brief schema](architecture/nexus-brief-schema.md).
4. Compare the [agent packages](agents/) and their state schemas.
5. Inspect the [evaluation methodology and fixtures](evaluations/).
6. Inspect each case’s dated artifacts and reconstruction notes.
7. Compare the public templates with the mechanisms demonstrated in the cases.

## Design principles

### Persistent domain ownership

Agents maintain responsibility for a domain across sessions rather than being recreated as disposable personas for each question. Persistence makes it possible to accumulate:

- forecasts;
- unresolved questions;
- calibration findings;
- evidence standards;
- known failure modes;
- monitoring obligations;
- changes in confidence.

Persistence is valuable only when state remains inspectable and correctable. Accumulated context without disciplined state can preserve errors as easily as knowledge.

### Preregistration before outcome

Where possible, decision criteria are written before the relevant evidence arrives. Survival bars, falsification windows, gate thresholds, and sustain tests reduce the ability to reinterpret an outcome opportunistically.

Preregistration does not eliminate judgment. It makes changes in judgment visible.

### Evidence lineage and independence

The number of citations is not the number of independent confirmations. Several reports may descend from one original observation, share an incentive, or arise from the same causal event.

The system therefore attempts to preserve:

- source provenance;
- freshness;
- causal root;
- ownership;
- dependence between observations;
- the distinction between evidence of a mechanism and evidence that a threshold has been crossed.

### Belief revision as state

A revised conclusion should not erase its predecessor. Mature research state records:

- the earlier position;
- its confidence;
- the evidence that changed;
- concessions made;
- the new position;
- remaining uncertainty;
- downstream consequences.

This makes “changing one’s mind” an inspectable event rather than a difference between two disconnected answers.

### Failure visibility

The system distinguishes epistemic success from operational success.

An agent can correctly detect a condition while the surrounding workflow fails to deliver, route, review, or execute it. Hiding that distinction would make the system appear more reliable while preventing it from improving.

The VIOLET case is included because the failure is evidence: it reveals where the architecture’s original boundaries were incorrectly drawn.

### Human authority

These agents support research judgment; they do not replace responsibility for it.

Human control remains necessary for:

- selecting consequential questions;
- approving changes to system architecture;
- reviewing sensitive or high-impact conclusions;
- determining whether evidence is sufficient for action;
- resolving conflicts the system cannot adjudicate;
- deciding what may be published.

## Relationship to humanities-derived methods

Several procedures in this repository resemble practices cultivated in the humanities:

- **source criticism** appears in provenance, freshness, incentive, and independence checks;
- **argument reconstruction** appears in explicit premises, survival criteria, and adversarial dialogue;
- **interpretive charity** appears in steelmanning before criticism;
- **historical contextualization** appears in dated evidence and stale-premise review;
- **hermeneutic iteration** appears in versioned interpretation and belief revision;
- **dialectic** appears in bounded disagreement, concession, and synthesis;
- **rhetorical analysis** appears in attention to source purpose and interested testimony.

This repository does not claim that humanities training automatically produces better AI systems or that these methods belong exclusively to the humanities. It demonstrates that epistemic practices can be translated into agent procedures and evaluated through their artifacts and failure modes.

## What is intentionally not included

The initial public release excludes:

- the complete private agent fleet;
- full live agent status files;
- current trade files, live gates, and position surfaces;
- credentials, private data sources, or proprietary access details;
- operational state that could expose active research decisions;
- raw working directories whose live state and internal dependencies would be misleading outside the larger system;
- HENRY and other agents whose value is better demonstrated in a deeper architectural follow-up.

The omissions are not intended to make the cases look cleaner than they were. Each case should preserve material uncertainty, contrary evidence, concessions, and relevant failures. Sanitization removes sensitive operational content, not the difficulty of the reasoning problem.

## How to evaluate the cases

Readers are encouraged to look beyond whether they agree with a case’s substantive conclusion.

The [public evaluation layer](evaluations/) turns several of these questions into frozen fictional fixtures with explicit scoring rules. It evaluates observable artifacts and does not claim access to hidden model reasoning.

More useful questions include:

- Were the decision criteria defined before the result?
- Does the case distinguish causal mechanisms from surface correlation?
- Are apparently independent sources actually independent?
- Can the agent state what evidence would change its view?
- Does contrary evidence produce an explicit concession or confidence update?
- Are stale evidence and lapsed actions handled consistently?
- Can a failure be traced to detection, delivery, judgment, or execution?
- Did the postmortem produce a durable procedural change?
- Can the mechanism be removed and tested through an ablation?

## Limitations

This is a curated case-study repository, not a controlled scientific evaluation of the entire system.

- The selected cases were chosen because they are unusually legible and informative.
- The underlying language models remain probabilistic and can generate unsupported claims.
- Persistent state can accumulate errors as well as insights.
- Agent names and role definitions do not themselves guarantee independent reasoning.
- The public agent packages are reconstructed specifications, not self-contained production deployments.
- Multi-agent disagreement can become performative if concessions and decision rules are not enforced.
- Procedural adaptation is not equivalent to autonomous model-weight learning.
- Results from one domain may not generalize to another.
- Some evidence and operational context have been removed for privacy, security, and scope.

Where possible, the repository separates direct artifacts from retrospective explanation so readers can distinguish what existed at the time from what was learned afterward.

## Current status

The initial release contains:

- a system overview;
- PROME and NEXUS architectural layers;
- three sanitized case studies;
- the NEXUS communication schema;
- selected reusable templates;
- a lessons-learned synthesis.

The second release layer adds public-safe packages for PROME, NEXUS, SAM, RED, BRENT, and VIOLET. The packages expose operating contracts and state models without publishing the agents' current working directories.

The third release layer adds a controlled evaluation specification: six single-agent fixtures, two multi-agent handoff tests, two component ablations, a shared rubric, and a result-record template. No benchmark results are claimed until a runner configuration and complete run artifacts are published.

Future additions may include replicated evaluation results and deeper architectural notes. Additional private agents may be introduced only when their context can be presented without exposing live operational state or reducing them to decontextualized prompt folders.

## Central takeaway

The purpose of this repository is not to argue that these agents never fail. The opposite is more important.

The cases show a system attempting to make reasoning and failure inspectable:

- PROME keeps priorities, obligations, and human decisions distinct from domain judgment.
- NEXUS preserves mechanisms and uncertainty as evidence moves across domains.
- SAM and RED preserve disagreement strongly enough to force belief revision.
- BRENT denies apparent confirmation when the required evidence is not causally independent.
- VIOLET reveals that correct detection can still die in delivery, then changes the monitoring architecture in response.

The resulting story is not simply “here are some agents.” It is:

> Here is how persistent research agents form beliefs, challenge them, coordinate evidence, fail operationally, and alter the surrounding system in response.
