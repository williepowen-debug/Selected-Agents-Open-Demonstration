# Provenance and evidence boundary

Prepared September 6, 2026. This package contains historical source-derived suite logic and a new, controlled reproduction. It is not an export of a production run or an independent certification of the private repository.

## Source anchors

Source path in the private operating repository: `AGENTS/VULCAN/scripts/test_validate_workbook.py`.

| Snapshot | Private commit | Behavior |
|---|---|---|
| [Before](reproduction/snapshots/before.py) | `ffefbafea9ce384c11b50fda88f76593a28df060` | A valid control passes on any status other than `2` |
| [After](reproduction/snapshots/after.py) | `8c33df2d26958c782b0d097847ebb9599e9f6f8b` | Each case requires its exact expected status |

The [manifest](reproduction/snapshots/manifest.json) records full-source hashes, public-snapshot hashes, and the selected source spans. Fixed revisions prevent a later commit from silently replacing the defective baseline.

## Extraction and adapters

The public snapshots retain the `CASES` assignment and the complete `run` and `main` definitions. Extraction used Python's `ast` module and `ast.unparse`, removing comments and any leading function docstrings. Each selected executable syntax tree was compared with its pinned original after the same transformation; all three selections matched in both versions. The case labels, field names, and test literals come from the historical suite; they are test inputs, not exported market observations.

The runner supplies imports and two adapters:

- `build_sandbox` creates a temporary Python exit-code probe and a JSON fixture, in place of copying the private workbook and validator.
- `apply_case` records the case arguments and assigns the subprocess status specified by the scenario. It does not decide whether a GPU price or ledger value is valid.

The retained `run` function launches a real subprocess and returns its actual exit code. The retained `main` controls baseline handling, temporary-directory cleanup, case iteration, scoring, printed diagnostics, and final suite status. It creates a fresh case directory each time. There is no manual transcription of the defective or repaired scoring predicate in the runner.

The reference expectations are declared independently: 21 negative results, ten control results, exact baseline and suite statuses, expected summary, and the repaired unexpected-exit diagnostics. The historical summary's phrase “defects injected” is retained in captured output; in this public exercise the adapter supplies process results rather than injecting defects into a real validator.

During preparation, both full historical modules were also executed with these same adapters. Their stdout, exit codes, case results, and fixture records matched their extracted counterparts for all three scenarios. This checks the extraction boundary using the same fixtures, not an independent test design.

## Historical observation versus public reproduction

The operational suite was run against the real repaired ledgers during review and returned the expected 31 results. A separate review probe changed the ten clean control statuses to `1`, leaving the clean baseline and negative cases unchanged: the old suite passed and the repaired suite failed with ten unexpected-exit diagnostics.

The public package reproduces that scoring contrast using deterministic process fixtures. It does not independently rerun the original validator's schema checks, publish the real ledgers, reproduce the agents' full sessions, or establish that any production process actually crashed. A failed reproduction setup is treated as an error, never evidence that the repaired suite detected the intended condition.

Hashes support comparison with these supplied artifacts. A manifest distributed beside its own files does not independently authenticate their private origin. Private-source review remains subject to the portfolio's existing access arrangements.

## Attribution and limits

Will directed the read-only external review, selected the episode, and commissioned preparation of this addition. VULCAN implemented the operational repairs and test suite. Codex identified and checked the exit-code defect and prepared the public extraction, adapters, explanation, and reproduction controls under Will's direction.

This is a selected, retrospective case with defect-aware expectations. It does not measure frequency, financial effects, hours saved, generalized research reliability, or the comparative effectiveness of agents or vendors. The separate prospective research-quality protocol has not been executed by preparing this case.
