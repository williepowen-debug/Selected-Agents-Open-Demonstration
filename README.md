# Selected Research-Agent Case Studies

This repository presents selected case studies and architectural artifacts from a larger research-agent system. It documents how persistent domain agents form and revise beliefs, test claims adversarially, coordinate evidence, track calibration, and alter procedures after failure.

It is a curated demonstration—not a complete release of the underlying system.

The broader system contains a substantially larger fleet of specialized agents, shared research infrastructure, live state, and private operational material. Rather than publishing a few agent directories without their history or context, this repository focuses on the artifacts and episodes that best reveal how the system reasons and changes over time.

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

## The four-part demonstration

### 1. SAM ⇄ RED — governed adversarial reasoning

The SAM–RED dialogue is the principal demonstration of argumentation and belief revision.

The case includes:

- steelmanning before criticism;
- preregistered survival criteria;
- bounded argumentative rounds;
- explicit concessions;
- separation of objections from decisive falsifiers;
- a forced confidence downgrade from **MEDIUM-HIGH** to **MEDIUM**;
- a dated falsification window;
- a consequential decision not to propagate a more complex strategy.

The important result is not that two agents generated opposing viewpoints. The result is that the dialogue was governed by rules strong enough to produce a visible change in belief and a downstream decision.

This case asks:

> Can an adversarial agent interaction preserve the strongest version of a claim, apply criteria fixed in advance, and produce accountable belief revision rather than theatrical debate?

See: [`cases/01_sam-red-adversarial-dialogue/`](cases/01_sam-red-adversarial-dialogue/)

### 2. BRENT — calibration and evidentiary restraint

BRENT is the most complete example of a mature persistent domain agent.

Its prediction ledger identifies recurring calibration patterns, including:

- underconfidence on direct physical constraints;
- overconfidence on third-order transmission chains;
- confusion between the presence of a mechanism and the crossing of a decision threshold;
- increasing uncertainty as additional intermediating actors introduce optionality;
- the need for a pre-flight test before accepting future predictions.

The featured sustain-test episode is especially important. A headline price condition passed, but BRENT returned **DENY** because the full test required two independent evidentiary legs and only one had fired.

In reaching that decision, the agent:

- refused to count stale evidence;
- refused to double-count related observations as independent confirmation;
- excluded evidence arising from the wrong causal root;
- distinguished a visible market outcome from proof of the proposed mechanism;
- preserved the preregistered test despite pressure from a partially confirming headline.

This case asks:

> Can a domain agent resist apparent confirmation when the causal and evidentiary structure required by its earlier test has not actually been satisfied?

See: [`cases/02_brent-calibration-and-deny/`](cases/02_brent-calibration-and-deny/)

### 3. VIOLET — detection, execution failure, and procedural adaptation

VIOLET is the repository’s principal failure-and-learning case.

The original monitoring architecture correctly detected two gates. The downstream execution packet was nevertheless dropped for seven days. The system did not retroactively pretend that the intended action had occurred or that the delayed action remained valid.

Instead:

- the failure was acknowledged explicitly;
- the original action was ruled lapsed;
- the difference between detection and delivery was formalized;
- an owner-independent gate ledger was introduced;
- staleness controls were added;
- a preregistered canary map was built;
- monitoring failures themselves became mechanically detectable.

The canary map distinguishes among:

- live calibrated instruments;
- instruments that exist but lack calibrated thresholds;
- externally owned signals;
- observed successes and false negatives;
- expected pull cadence;
- “dark canaries” that have gone unobserved beyond their allowed interval.

A later fresh-look memorandum provides a second form of revision. VIOLET determined that the premise queued for investigation had become stale, reconstructed the current evidence, changed the interpretation, and concluded **NO-FIRE**.

This case asks:

> Can an agent system represent the difference between noticing, communicating, deciding, and acting—and then redesign itself when those stages fail to connect?

See: [`cases/03_violet-detection-to-execution-failure/`](cases/03_violet-detection-to-execution-failure/)

### 4. NEXUS — the connective architecture

NEXUS provides the grammar that makes the other cases parts of a system rather than isolated agent performances.

The NEXUS brief schema distinguishes:

- within-domain reasoning from cross-domain transmission;
- observations from causal mechanisms;
- sending edges from waiting edges;
- active claims from unresolved questions;
- agreement from calibrated divergence;
- concise cross-agent messages from selective drill-down into raw state.

The architecture is designed to transmit more than conclusions. A useful message should preserve why a finding matters, which causal channel it may enter, how uncertain it is, and what another domain agent should watch next.

This case asks:

> What information must survive when specialized agents exchange findings across disciplinary and causal boundaries?

See: [`architecture/nexus-brief-schema.md`](architecture/nexus-brief-schema.md)

## Repository structure

```text
research-agent-case-study/
├── README.md
├── SYSTEM_OVERVIEW.md
├── architecture/
│   ├── persistent-domain-ownership.md
│   ├── nexus-brief-schema.md
│   └── orchestration-mode-split.md
├── cases/
│   ├── 01_sam-red-adversarial-dialogue/
│   ├── 02_brent-calibration-and-deny/
│   └── 03_violet-detection-to-execution-failure/
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
3. Review the summary page inside each case directory.
4. Finish with [`LESSONS_LEARNED.md`](LESSONS_LEARNED.md).

### Technical path

For architecture and implementation:

1. Begin with [`architecture/persistent-domain-ownership.md`](architecture/persistent-domain-ownership.md).
2. Review the NEXUS brief schema.
3. Inspect each case’s dated artifacts and reconstruction notes.
4. Compare the public templates with the mechanisms demonstrated in the cases.

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
- complete directories whose internal dependencies would be misleading when removed from the larger system;
- HENRY and other agents whose value is better demonstrated in a deeper architectural follow-up.

The omissions are not intended to make the cases look cleaner than they were. Each case should preserve material uncertainty, contrary evidence, concessions, and relevant failures. Sanitization removes sensitive operational content, not the difficulty of the reasoning problem.

## How to evaluate the cases

Readers are encouraged to look beyond whether they agree with a case’s substantive conclusion.

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
- Multi-agent disagreement can become performative if concessions and decision rules are not enforced.
- Procedural adaptation is not equivalent to autonomous model-weight learning.
- Results from one domain may not generalize to another.
- Some evidence and operational context have been removed for privacy, security, and scope.

Where possible, the repository separates direct artifacts from retrospective explanation so readers can distinguish what existed at the time from what was learned afterward.

## Current status

This repository is being assembled in stages. The planned initial release contains:

- a system overview;
- three sanitized case studies;
- the NEXUS communication schema;
- selected reusable templates;
- a lessons-learned synthesis.

Future additions may include controlled component ablations, evaluation rubrics, and deeper architectural notes. Additional private agents may be introduced only when their context can be presented without exposing live operational state or reducing them to decontextualized prompt folders.

## Central takeaway

The purpose of this repository is not to argue that these agents never fail. The opposite is more important.

The cases show a system attempting to make reasoning and failure inspectable:

- SAM and RED preserve disagreement strongly enough to force belief revision.
- BRENT denies apparent confirmation when the required evidence is not causally independent.
- VIOLET reveals that correct detection can still die in delivery, then changes the monitoring architecture in response.
- NEXUS defines how those local findings can move through a larger network without losing their mechanism or uncertainty.

The resulting story is not simply “here are some agents.” It is:

> Here is how persistent research agents form beliefs, challenge them, coordinate evidence, fail operationally, and alter the surrounding system in response.
