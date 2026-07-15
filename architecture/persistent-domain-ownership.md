# Persistent Domain Ownership

A persistent domain agent is responsible for a bounded research area across sessions. It is not recreated from scratch for each question, and its earlier beliefs are not supposed to disappear when a new answer is generated.

## The ownership contract

A domain owner is expected to:

- maintain the canonical evidence and judgment for its specialty;
- distinguish observations, mechanisms, thresholds, and conclusions;
- date important claims and identify their sources;
- register what would change its view;
- resolve predictions against their original terms;
- record uncertainty, failed assumptions, and procedural lessons;
- route cross-domain implications without editing another owner's judgment.

PROME may assign or prioritize work, NEXUS may synthesize it, and RED may challenge it. None of those roles silently becomes the domain owner.

## State, not conversational memory

The system's basic rule is that durable claims live in files. Conversational recall is too easy to distort, omit, or overwrite. A typical state layout includes:

| Surface | Function |
|---|---|
| Current state | The agent's present view, uncertainty, and next decision point |
| Thesis and changelog | Versioned explanation of what changed and why |
| Prediction ledger | Claims, confidence, time window, invalidation, and resolution |
| Evidence ledger | Source lineage, freshness, epistemic status, and cross-links |
| Cross-domain brief | Signals being sent, inputs being awaited, and causal mechanisms |
| Inbox and outbox | Explicit obligations and handoffs |
| Maintenance log | Changes to tools, schemas, monitoring, and procedures |

The exact filenames vary. The important property is that each kind of state has a named owner and a canonical home.

## Belief revision

A revision should preserve:

1. the earlier claim and confidence;
2. the new evidence or argument;
3. any explicit concessions;
4. the revised claim and confidence;
5. the downstream consequence;
6. the conditions that could reverse the revision.

This turns “changing one's mind” into an inspectable event rather than a difference between two disconnected outputs.

## Calibration as institutional memory

Resolved predictions are useful only if the result changes future behavior. Mature ledgers therefore retain patterns such as:

- systematic underconfidence on direct physical constraints;
- overconfidence when a causal chain contains several actors with optionality;
- thresholds reached for the wrong causal reason;
- predictions that were literally correct but operationally unhelpful;
- missed windows caused by stale or unconsumed evidence.

The BRENT case demonstrates how those patterns become a pre-flight check for new predictions.

## Boundaries and failure modes

Persistence can preserve errors as easily as knowledge. Common failure modes include stale status surfaces, duplicated canonical claims, unconsumed messages, overgrown agent scope, and a false sense of independence between agents that rely on the same source or causal root.

Persistent ownership therefore requires subtraction and maintenance: archive resolved material, mark stale evidence, reconcile mirrors to canonical sources, and retire rules whose operating substrate no longer exists.
