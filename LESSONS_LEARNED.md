# Lessons Learned

The selected cases do not show a system that avoids failure. They show a system attempting to make failure classifiable and useful.

## 1. A challenge needs a decision rule

Debate becomes accountable when survival criteria are fixed before the exchange, rounds are bounded, concessions remain visible, and the verdict has a downstream consequence. SAM–RED is valuable because it changed the grade and removed options, not because it generated opposing prose.

## 2. A visible outcome does not prove the mechanism

BRENT's headline condition passed, but the full test failed. Freshness, causal roots, and evidential independence prevented a tempting but under-supported confirmation.

## 3. Detection, delivery, judgment, and action are different events

VIOLET detected its conditions correctly. The required packet still disappeared for seven days. Treating detection as execution would have hidden the actual failure.

## 4. Late execution can be worse than explicit lapse

When the environment changed, the system refused to build the original packet retroactively. It recorded the action as lapsed and required a fresh look. This preserved the meaning of the original gate.

## 5. Persistent state requires subtraction

A larger memory is not automatically a better memory. Stale status, duplicated claims, dead protocols, and unresolved obligations can make persistence misleading. Archival, canonical ownership, staleness markers, and maintenance logs are part of reasoning quality.

## 6. Cross-agent agreement is not automatically independent evidence

Several agents can repeat one causal root. NEXUS and the domain cases therefore track source lineage, shared antecedents, and whether apparently different observations are genuinely independent.

## 7. Orchestration should preserve domain authority

PROME coordinates tasks and decisions; NEXUS synthesizes; RED challenges; WALTER filters external signals; domain agents retain analytical ownership. Blurring these roles creates silent overrides and unclear accountability.

## 8. Human authority remains part of the architecture

The system can make evidence, disagreement, and failure more legible. It does not eliminate responsibility for consequential choices, public claims, or system design.

## 9. Corrections need tests that survive the next run

[Case 4](cases/04_violet-correction-verification/) shows a repair whose safeguard depended on per-run memory while the provisional data persisted on disk. A second run exposed the mismatch. The final repair removed that bookkeeping and checked publisher coverage for each nonblank spot cell before adding an authoritative label. The useful evidence is the executed contrast against frozen defective versions, including recovery controls—not the existence of another rule or a green test count alone. That local improvement does not establish a falling system-wide error rate.

[Case 7](cases/07_vulcan-test-harness-false-pass/) examines the test's own verdict: a control returning an unsuccessful status was accepted because it did not return the one code reserved for a detected defect. Requiring the exact expected code preserved valid runs and rejected the injected failures. Verification includes checking how tests handle unexpected outcomes and distinguishing intended detection from a broken test setup.

## 10. A comparison need not produce a winner

[Case 5](cases/05_walter-instruction-pilot/) tested whether a shorter instruction preserved required behavior. Both versions met the rubric on one fixture. That limited success did not establish general equivalence, explain which sentence caused it, or measure maintenance costs. Captured tool records also exposed omissions in the models' requested command reports. The lesson is to preserve the objective and inspect execution evidence, not select a new objective because the result is unexciting.

## 11. Correct arithmetic can conceal an invalid measure

[Case 6](cases/06_daedalus-measurement-validity/) withdrew a ratio whose inputs counted different populations without establishing decision timing. Neither a zero in a correction register nor a large number of detected defects measures error prevention by itself. Separately defined raw counts were more defensible than the composite. Withdrawing the interpretation was progress; it did not make every surviving label valid or establish better system performance.

## Open research questions

- How should message consumption and integration be measured without producing compliance theater?
- Which agent behaviors survive controlled ablation?
- When does persistent specialization outperform a fresh, well-scoped single agent?
- How much apparent multi-agent diversity comes from prompts rather than independent evidence?
- Which procedural improvements generalize beyond financial research?
- How should coordination bottlenecks be measured before they become operational failures?
- Does a review workflow's reliability benefit outweigh verification and rework costs? The [pilot protocol](experiments/research-quality-pilot.md) is planned, not completed.
