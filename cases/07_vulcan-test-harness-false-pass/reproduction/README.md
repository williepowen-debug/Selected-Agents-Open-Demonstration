# Offline reproduction

Run from the repository root:

```bash
python3 -B cases/07_vulcan-test-harness-false-pass/reproduction/run_checks.py --selftest
```

Requires Python 3.10 or newer and only its standard library. Verified with **Python 3.12.3** on September 6, 2026; other versions have not been tested. No dependency installation, network, model calls, credentials, private repository, or Git executable is needed. The runner writes only to automatically cleaned temporary directories and invokes the same Python interpreter for child processes.

## What runs

Two frozen source-derived snapshots retain the historical suite's 31 case definitions, subprocess runner, and complete `main` function. The public runner supplies a deterministic exit-code program in place of the real validator. This isolates **how the suite interprets process results**, not whether the underlying schema checks work.

Three scenarios run against both versions:

1. Baseline `0`, 21 negatives `2`, ten controls `0`: both suites report zero wrong and return `0`.
2. Baseline `0`, 21 negatives `2`, ten controls `1`: the original falsely reports zero wrong and returns `0`; the repaired suite names ten unexpected exits and returns `1`.
3. Baseline `1`: both return `1` before applying or scoring any case.

These are six expected traces of the supplied process conditions, not six independent research trials. The outer runner returns `0` only when all traces match, including the expected historical defect. An unexpected exception or mismatched trace returns `1`.

## Expected output

```text
PASS: both source-derived snapshots match their manifest hashes.
Fixture boundary: real subprocess exits; no GPU validator or market data.
PASS: before expected_results   baseline=0 cases=31 suite_rc=0
PASS: before controls_exit_1    baseline=0 cases=31 suite_rc=0
PASS: before baseline_exit_1    baseline=1 cases=0 suite_rc=1
PASS: after  expected_results   baseline=0 cases=31 suite_rc=0
PASS: after  controls_exit_1    baseline=0 cases=31 suite_rc=1
PASS: after  baseline_exit_1    baseline=1 cases=0 suite_rc=1
PASS: 6/6 expected version/scenario traces reproduced, including the historical false pass.
REJECTED as required: repaired code substituted for historical baseline.
REJECTED as required: setup exception is not a successful fault-detection trace.
PASS: 2/2 reproduction controls rejected.
```

Without `--selftest`, the runner checks the same six traces and hashes but omits the two reproduction controls. The baseline-substitution control tests the behavioral contrast after normal snapshot integrity checks; a changed snapshot on disk is rejected separately by its hash.

## Scope

Case labels and test literals are retained from the source. Their ledger fields are recorded in temporary JSON fixtures but are not evaluated as market or schema data. The adapters neither open nor copy private ledgers. The scripts print a summary instead of reproducing all historical agent commentary.

The source-derived snapshots intentionally depend on the runner's supplied environment; use `run_checks.py` rather than executing them individually. [Provenance](../PROVENANCE.md) describes extraction, full-module comparison, attribution, and the limits of the shipped hashes.
