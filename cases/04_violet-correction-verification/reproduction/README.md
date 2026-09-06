# Offline reproduction

This directory runs seven scenarios against three frozen source-derived snapshots. All prices and observation dates are synthetic. The historical version dates in the provenance are real repository dates.

## Setup and run

Requires Python 3.11 or newer. Verified locally with **Python 3.12.3 and pandas 3.0.3** on September 6, 2026. Other Python versions have not been tested for this package.

From the repository root, a separate environment can be prepared with:

```bash
python3 -m venv .venv-demo
.venv-demo/bin/python -m pip install -r cases/04_violet-correction-verification/reproduction/requirements.txt
.venv-demo/bin/python -B cases/04_violet-correction-verification/reproduction/run_checks.py --selftest
```

Dependency installation may require network access. **The test run itself is offline:** requests and yfinance are fixture adapters; real pandas performs the alignment operations. No API keys, model calls, market downloads, private repository, or Git executable are required. The runner writes synthetic ledgers only inside automatically cleaned temporary directories. `.venv-demo/` is ignored by Git.

If the dependency is already installed, the single `python3 -B .../run_checks.py --selftest` command is sufficient.

## Expected result

`HOLDS` means the case satisfies the tested authority behavior; `DEFECT` means the historical defect is reproduced. For the recovery control it describes the terminal recovery, with the earlier step checked separately. The harness additionally checks **exact value, basis, and exit-code traces**, not just these table labels.

| Case | Transport-only | Per-run guard | Stateless guard |
|---|---|---|---|
| 1. Publisher HTTP 503 | HOLDS | HOLDS | HOLDS |
| 2. Publisher HTTP 200, HTML body | DEFECT | HOLDS | HOLDS |
| 3. Valid CSV missing target date, occupied labelled row | DEFECT | HOLDS | HOLDS |
| 4. Complete publisher control | HOLDS | HOLDS | HOLDS |
| 5. Missing date, blank unlabelled cell | DEFECT | HOLDS | HOLDS |
| 6. Same missing-date fixture run twice on the same ledger | DEFECT | DEFECT | HOLDS |
| 7. Missing date followed by authoritative recovery | HOLDS | HOLDS | HOLDS |

The expected summary is:

```text
PASS: 21/21 expected case-version traces reproduced (including expected defects).
REJECTED as required: fixed code substituted for historical baseline
REJECTED as required: ledger writer disabled
PASS: 2/2 harness negative controls rejected.
```

An expected historical defect is **not** an error in the reproduction. Any mismatch with its exact expected trace, unexpected exception, or failed control causes exit code **1**; the complete expected contrast exits **0**. In cases 1 and 2, the repaired program's own exit code is **2**. In case 3 it is **0**: a missing date in a structurally valid file is not a failed fetch.

The runner also checks that each execution queried all six fixture series from both sources, retained the row identity/header, preserved an unrelated field, and retained the five non-SKEW control values and two derived ratios. It checks file contents after each run, not a log message claiming a write occurred.

## What is real, and what is substituted?

- **Retained:** seven production functions, including `main`, the CSV parser, provisional/authoritative passes, and ledger read/write functions; four relevant constants. Their executable syntax trees match the selected historical definitions after removing docstrings.
- **Supplied by the harness:** imports, a fixed clock, a temporary ledger path, fixture network/data adapters, and a constant `OMITTED` regime label.
- **Excluded:** unrelated futures computation, actual regime classification thresholds, live state, deployment setup, and the standalone command-line launcher. The retained main's non-spot branch calls a rejecting stub if reached.
- **Frozen:** snapshot hashes in [the manifest](snapshots/manifest.json) are checked before execution. The files are local evidence, not a claim of cryptographic authentication by a third party. Preserve them; adapt the harness if dependencies change.

The full original modules were also run privately against these same fixtures during preparation; all seven traces per version matched. That is an extraction check using the same harness, **not an independent test design**. See [provenance](../PROVENANCE.md) for exact revisions and source spans.

This is an end-to-end test of the selected spot-only path within declared substitutions, not a production deployment, exhaustive validation, or live-data accuracy test. The expected results and adapters were authored with knowledge of the defects; there is no blind evaluation here.
