# Case 5 — WALTER: Testing a shorter instruction without inventing a win

**Both versions met the required behaviors on one fixture. The prepared revised instruction was 187 bytes smaller. Reference dependence and maintenance cost were not established.** That is the result of this September 6, 2026 pilot—not evidence that shorter instructions are generally better or that the two versions are reliably equivalent.

WALTER is the system's signal-routing agent. Its boot procedure requires checking whether carried obligations are still true before repeating them to the operator. A proposed rewrite separated the trigger, action, failure behavior, and reference from incident history. The question was whether the candidate preserved useful behavior, not whether it could beat the original at any cost.

## The exercise

Two separate subagent sessions received the same small fixture, one with the original instruction and one with the candidate. Both session records report `claude-sonnet-5`; that is an archived model identifier, not a pinned reproducible model build. Each was asked to perform the step and produce a boot reply, not explain what the instruction meant.

| Carried item | Evidence available in the fixture | Required disposition |
|---|---|---|
| A: a signal still lacks a status header | The signal file has that header | Withdraw the obsolete complaint |
| B: a recipient and a note still need adding | The registry still lacks both | Preserve the open obligation |
| C: three items remain unrouted | The named evidence file is absent | Retain uncertainty; neither assert nor silently drop the claim |

These are fictionalized test obligations, not current research or routing instructions. The fixture is deliberately small and includes an explicit explanatory note for B. This makes the observed success interpretable but limits how far it can generalize.

## What the records support

Scoring was checked against tool calls/results and final answers, not the author's condensed summaries. The [evidence guide](EVIDENCE.md) points to each relevant record section.

| Required behavior | Original | Revised |
|---|---|---|
| Inspect evidence for all three items, including an absence check for C | Pass | Pass |
| Withdraw A | Pass | Pass |
| Preserve B | Pass | Pass |
| Retain C as unverified, naming the missing evidence | Pass | Pass |

The original inspected the containing directory and established the file's absence. The revised also attempted to open the file and received an error. Both final replies retained the uncertainty. These four rubric items are related checks on **one exercise**, not four independent trials per condition.

The two prepared instruction files measure **1,724 and 1,537 UTF-8 bytes**, including the revised file's relocated general principle and its wrapper. They are retained unchanged so that count can be rechecked. This is not a token count, total transmitted-prompt measurement, runtime saving, or reduction already deployed across the system.

## The useful result included withdrawing interpretations

| Initial interpretation | Why it did not follow | Bounded conclusion |
|---|---|---|
| Both passing means the fixture was inadequate | The objective was preservation, not necessarily superiority | Both met the bar on this fixture; adequacy for broader claims is unresolved |
| The original reader credited narrative, so removed history was necessary | The credited sentence remained in both versions; self-attribution would not establish causation anyway | No causal contribution of the removed history was isolated |
| A smaller instruction created three times the maintenance burden | Three locations need not all change together; the proposed history block was not implemented | Maintenance cost was unmeasured |
| Neither reader needed the reference document | The reference was unavailable in the fixture | Reference dependence was not tested |

Testing additional tasks can be valuable if the next question and sampling plan are specified. Selecting tasks until the candidate appears to win would answer a different question. The pilot was closed without claiming superiority or adopting the candidate into WALTER's live charter.

## A second observation: requested logs are not execution records

Both prompts explicitly required exact commands and literal outputs. Both models nevertheless abbreviated their final command reports. The revised final report omitted its first directory-listing call; the original shortened commands and reproduced a directory-listing detail differently. The separately captured tool records retained the observations needed for scoring.

This supports a practical distinction: **collect execution records directly rather than relying on a model to reconstruct them in its answer.** It does not prove the recording system is infallible. The public records are sanitized copies of committed extractions, and the [provenance](PROVENANCE.md) specifies their boundary.

## Design limitations that travel with the result

- One fixture, one run per condition, retrospectively selected for this portfolio. No equivalence test, effect-size estimate, or general reliability claim.
- The candidate adds an explicit instruction for unreachable evidence. It is a combined wording/content change, not pure compression.
- Both prompts demanded command logs, which may itself encourage verification. This does not isolate the boot instruction's effect in ordinary sessions.
- The core rubric was committed **before** execution. A later addendum clarifying acceptance and documenting the asymmetry was committed **during** execution, before the recorded final replies. Do not describe the entire protocol as frozen before either run.
- Codex both advised on the protocol and later reviewed the results. It was external to WALTER, but not an uninvolved blind evaluator.
- The candidate was not deployed at closeout. Reference-reading costs, maintenance costs, and operational savings remain unknown.

## Inspect the evidence

- [Evidence guide and scoring anchors](EVIDENCE.md)
- [Original instruction](evidence/instruction_original.txt) and [candidate instruction](evidence/instruction_revised.txt)
- [Original-arm execution record](evidence/record_control.md) and [revised-arm execution record](evidence/record_revised.md)
- [Core rubric committed before the runs](evidence/rubric_before_runs.md)
- [Fixture handoff](fixture/AGENTS/WALTER/LAST_COMPLETION.md)
- [Provenance and chronological limits](PROVENANCE.md)

From the repository root, this standard-library-only command checks archived artifact hashes, instruction sizes, and chronology:

```bash
python3 -B cases/05_walter-instruction-pilot/check_artifacts.py
```

It does **not** rerun the models or automatically certify the behavior grades. The separate [48-run research-quality protocol](../../experiments/research-quality-pilot.md) remains planned and has not been executed; this earlier two-run instruction pilot is a different exercise.

Will directed the broader system and authorized the pilot and public selection. WALTER produced the candidate, ran the sessions, and interpreted them; Codex contributed protocol review, challenged overclaims, checked the records, and prepared this public case under Will's direction. The value of the episode is disciplined interpretation of limited evidence, not a victory for a particular agent or vendor.
