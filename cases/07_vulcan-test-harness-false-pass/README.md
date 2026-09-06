# Case 7 — VULCAN: When the regression test accepts a failed validator

**A regression suite rejected known invalid inputs but accepted unsuccessful control runs.** When ten otherwise-valid controls were made to return exit code `1`, the original suite still reported `WRONG: 0` and exited successfully. The repaired suite reported ten failures and exited `1` under the same injection.

This September 6, 2026 episode is a companion to [VIOLET's correction-verification case](../04_violet-correction-verification/). It examines the test harness's definition of success. The public reproduction runs historical suite logic with controlled subprocess results; it does not run the underlying GPU validator or measure research productivity.

## How the test became the subject

VULCAN maintains research on AI capital spending and its transmission through related markets. External review found that its workbook validator accepted values forbidden by its declared schema, including negative GPU prices and invalid category names. VULCAN repaired those checks and created a retained regression suite.

The new suite isolated each case in a fresh temporary tree. This addressed an earlier testing mistake in which one modified ledger contaminated later cases. Its 31 cases included 21 deliberately invalid inputs and ten valid controls. On the actual repaired validator, all 31 returned their expected statuses.

That successful run did not establish that the suite would correctly classify other outcomes. Its scoring line was:

```python
ok = (rc == 2) == must_catch
```

For an invalid input, it required the validator's error code `2`. For a valid control, however, it accepted **any other code**. Exit code `1` could indicate a warning or a Python exception, but the control was still labelled successful. A process failure could therefore become a passing test.

## The discriminating check

The review kept the baseline clean and the 21 negative cases unchanged, then replaced the ten control results with `1`. These were deliberately injected statuses, not ten observed production crashes.

| Supplied results | Original suite | Repaired suite |
|---|---|---|
| Baseline `0`; negatives `2`; controls `0` | Zero wrong; exit `0` | Zero wrong; exit `0` |
| Baseline `0`; negatives `2`; controls `1` | **Zero wrong; exit `0` — false pass** | **Ten wrong; exit `1`** |
| Baseline `1` | Stops before case execution; exit `1` | Stops before case execution; exit `1` |

The repair specifies the expected status directly:

```python
want = 2 if must_catch else 0
ok = rc == want
```

An unexpected control status now produces a diagnostic naming the observed and expected codes. The change preserves successful controls and expected negative results. It adds neither a new ledger nor another reviewing agent.

## Run the evidence

From the repository root, using Python 3.10 or newer:

```bash
python3 -B cases/07_vulcan-test-harness-false-pass/reproduction/run_checks.py --selftest
```

The runner checks six version/scenario traces and two controls on the reproduction itself. One rejects replacing the historical baseline with repaired code. The other ensures that a setup exception cannot masquerade as successful fault detection. See [setup and substitutions](reproduction/README.md) and [source provenance](PROVENANCE.md).

## What the case contributes

A test's result is another claim to verify. Here, a correct validator repair and a passing suite coexisted with an incorrect definition of control success. The decisive evidence was the changed behavior under an unexpected result, alongside preservation of the valid path.

The episode also makes review and rework visible. It does not measure their net cost or establish that adding review always pays. The test was designed retrospectively with knowledge of the defect; there was no blind evaluator or matched workflow comparison. The [planned research-quality pilot](../../experiments/research-quality-pilot.md) addresses that broader question separately and remains unrun.

Will directed the external review and commissioned this portfolio addition. VULCAN produced the operational validator repairs and regression suite. Codex identified the control-exit defect, verified its repair, and prepared this source-derived demonstration under Will's direction. Private market records and operational integrations are excluded. The demonstrated result is one repaired test-harness failure, not comprehensive validation of VULCAN or the research system.
