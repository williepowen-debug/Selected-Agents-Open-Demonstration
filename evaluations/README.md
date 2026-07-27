# Evaluation Layer

This directory turns the public agent packages into inspectable behavioral tests. It evaluates whether an agent preserves ownership, evidence lineage, uncertainty, state transitions, and human authority—not whether it produces a particular paragraph.

All inputs are fictional. They are not current research, operational signals, forecasts, or financial advice.

## Contents

- [`METHODOLOGY.md`](METHODOLOGY.md) — how to run, score, and report an evaluation;
- [`RUBRIC.md`](RUBRIC.md) — shared scoring dimensions and automatic failure conditions;
- [`COVERAGE_MATRIX.md`](COVERAGE_MATRIX.md) — fixture coverage across contract dimensions and safeguards;
- [`RESULT_RECORD_TEMPLATE.md`](RESULT_RECORD_TEMPLATE.md) — one reproducible record per run;
- [`single-agent/`](single-agent/) — one bounded role-fidelity test for each public package;
- [`integration/`](integration/) — two multi-agent handoff tests;
- [`ablations/`](ablations/) — two controlled comparisons that remove a system safeguard.

## Evaluation inventory

| ID | Type | Primary behavior under test |
|---|---|---|
| [`SA-PROME-01`](single-agent/01_prome_task_reconciliation.md) | Single agent | Task reconciliation and authority boundaries |
| [`SA-NEXUS-01`](single-agent/02_nexus_shared_root.md) | Single agent | Shared-root detection without forced convergence |
| [`SA-SAM-01`](single-agent/03_sam_transmission_boundary.md) | Single agent | Transmission-family separation and domain boundary |
| [`SA-RED-01`](single-agent/04_red_survival_bar.md) | Single agent | Preregistered adversarial challenge |
| [`SA-BRENT-01`](single-agent/05_brent_deny.md) | Single agent | Denial despite a passing headline condition |
| [`SA-VIOLET-01`](single-agent/06_violet_lapsed_gate.md) | Single agent | Lapsed-gate handling and fresh-premise requirement |
| [`INT-01`](integration/01_transmission_handoff.md) | Integration | SAM → VIOLET → NEXUS → PROME handoff integrity |
| [`INT-02`](integration/02_challenge_reconciliation.md) | Integration | BRENT ↔ RED → PROME disagreement preservation |
| [`ABL-01`](ablations/01_remove_evidence_lineage.md) | Ablation | Effect of removing evidence lineage |
| [`ABL-02`](ablations/02_collapse_action_stages.md) | Ablation | Effect of collapsing detection into execution |

## What counts as evidence

The suite scores only observable artifacts: the response, proposed state changes, routes, decision requests, and any files the runner records. An evaluator must not award credit for hidden reasoning or infer that an omitted step probably occurred.

## What this suite does not establish

Passing these fixtures does not establish factual market skill, production safety, model independence, profitability, or suitability for consequential autonomous action. The suite tests public behavioral contracts under small fictional scenarios.
