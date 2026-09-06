# Provenance and evidence boundary

Prepared September 6, 2026. This is a source-derived public reconstruction of a private operating-repository episode, not a raw export or independent certification. The public files preserve the selected behavior while excluding live research state.

## Historical source anchors

All three implementations come from `AGENTS/VIOLET/scripts/backfill.py` in the private operating repository. Full commit IDs, source-file SHA-256 hashes, snapshot hashes, and line spans for every selected definition are in the bundled [manifest](reproduction/snapshots/manifest.json).

| Public snapshot | Private commit | Selected behavior |
|---|---|---|
| [transport_only.py](reproduction/snapshots/transport_only.py) | `7b746e269163d84d0bec02cf1c3e58839e17552c` | Initial write-authority/transport repair |
| [per_run_guard.py](reproduction/snapshots/per_run_guard.py) | `1e8ae5d00162f3b4b92309ccd3ccd76f7dbab347` | Parser/destination repair, with per-run provisional bookkeeping |
| [stateless_guard.py](reproduction/snapshots/stateless_guard.py) | `8eec88a841e6ade5096abaeb9a8aa21bc31db3e4` | Stateless stamp condition; per-run bookkeeping removed |

These are fixed historical versions, not a claim about whichever code is currently deployed. The transport-only version already contains a repair; the earlier unguarded implementation is not bundled.

## Extraction method

The extraction parsed each pinned file with Python's `ast` module and selected these definitions:

- Functions: `load_existing`, `write_merged`, `backfill_spot`, `fetch_cboe_history`, `fetch_all_cboe`, `backfill_spot_cboe`, `main`.
- Constants: `TICKERS`, `CBOE_HISTORY_URL`, `CBOE_SERIES`, `CBOE_TOL`.

Only leading function docstrings were removed from the selected syntax trees. `ast.unparse` produced the public code, dropping comments and normalizing formatting. The resulting definitions were checked against the originals using `ast.dump(..., include_attributes=False)` after the same docstring removal. **All eleven definitions matched for each version.** There was no manual reimplementation of the gate, parser, merge, or entry-point control flow.

The harness supplies standard-library imports, a frozen clock, a temporary ledger path, and synthetic requests/yfinance adapters. It retains actual pandas operations. The unrelated regime helper returns a constant `OMITTED`; its original classification thresholds are not published. The futures functions and original standalone launcher are excluded. A rejecting stub guards the unused futures branch of the retained `main`.

The fixture deliberately changes original observation dates and numbers to invented values. It retains series names, column semantics, and the public endpoint shape so the existing parser and mapping paths run unchanged. There are no positions, active gates, credentials, private absolute paths, real ledger rows, or live data downloads in the package.

## What readers can reproduce here

- All seven scenarios against all three snapshots: **21 matching expected traces**, including defective outcomes.
- The intermediate snapshot's first-run/second-run difference.
- Successful authoritative recovery, including the value, label, and exit status.
- Rejection of fixed-code substitution for the historical baseline and of a disabled writer.
- Snapshot hash checks and temporary-ledger assertions described in the reproduction README.

This package is portable without private history. Hashes make local changes detectable against this manifest; because the manifest ships with the code, they do not independently authenticate the private origin.

## Additional preparation checks, not bundled historical suites

During preparation, the full original `backfill.py` modules were run against the same synthetic fixtures, retaining their actual regime helper but grading only the public contract fields. All seven traces matched for each version. This verifies the chosen extraction boundary for these fixtures; the same harness was used, so it is not independent verification of the test design.

The original `test_backfill_authority.py` at `7b746e269` was also rerun against its original source and returned **12 passing checks**. Source inspection confirms that `run_yf_pass` transcribes the provisional gate and that the suite does not call `backfill.main()`. It exercises portions of the authoritative pass directly. One assertion checks for a counter name in ledger-row text:

```python
"settle_stamped" not in str(rows)
```

That clause does not measure the stamping counter in those fixtures. Neither this excerpt nor the historical suite's green count establishes that all of its tests were useless; the narrower issue is that its coverage missed the demonstrated defects.

At `1e8ae5d00`, `test_backfill_endtoend.py` loads its baseline using:

```python
["git", "show", "HEAD:AGENTS/VIOLET/scripts/backfill.py"]
```

That committed reference points at the repaired file, not an immutable defective baseline. The subsequent `8eec88a84` revision pins the reference to `1e8ae5d00^`. The public harness avoids the private Git dependency entirely by bundling all three snapshots and always running the contrast.

These historical suite observations were verified locally from private source. The suites themselves are not bundled; a public reader can reproduce the implementation failures above but cannot independently rerun those historical suite counts from this package alone. Private artifacts are available for review on request under the repository's existing access policy.

## Attribution and uncertainty

Will designed and operates the broader system, commissioned review, and authorized this addition. The operational repairs/tests were agent-produced; Codex prepared the public extraction, new fixture harness, prose, and prospective protocol under his direction. The public test design adapts the original seven scenarios, strengthens exact persisted-state checks, and adds two harness controls. It is a retrospective reconstruction, not a preregistered or blind evaluation.

No inference is made here about publisher accuracy, the frequency of the defects in live operation, financial effects, human hours saved, general improvement over time, or cross-vendor superiority. The separate `thresholds.py` writer and its leading-edge policy are excluded, not implicitly cleared by this case.
