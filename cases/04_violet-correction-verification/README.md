# Case 4 — VIOLET: When a correction needs its own regression test

**A repair can preserve the appearance of verification while failing to preserve the fact being verified.** This September 6, 2026 case follows a data-authority repair through two incomplete versions and a third version that satisfies the supplied regression cases.

The result is deliberately narrow: seven synthetic scenarios distinguish three historical implementations. It is not a benchmark of agent intelligence, proof of lower fleet error rates, or evidence of trading performance.

## The failure in plain language

VIOLET's backfill tool combines a publisher-of-record feed with a secondary feed. Its ledger can label a row `SETTLE`, which downstream readers treat as an authoritative basis. A secondary value could be written into that row without removing the label. A successful exit then concealed a mismatch between the value's provenance and the row's asserted authority.

The public demonstration uses invented dates and values: the authoritative fixture says **120**, the secondary fixture says **110**. These are test inputs, not historical market observations. `SETTLE` is a legacy software label; matching a designated publisher is not independent verification of the publisher's accuracy.

## What changed, and what still failed

| Version | Repair present | Remaining demonstrated failure |
|---|---|---|
| A: transport-only | Fetch the publisher first; withhold secondary writes for a failed series; return a nonzero status on failure | HTTP 200 with an HTML body is treated as valid absence. A valid CSV missing the target date also permits an overwrite. A provisional fill can acquire `SETTLE`. |
| B: per-run guard | Validate CSV headers; protect occupied and already-labelled destinations; track provisional writes during this run | On the second run the provisional value is already on disk. No new provisional write is recorded, so the row can acquire `SETTLE`. |
| C: stateless guard | Before adding `SETTLE`, require every nonblank spot column to have a publisher value for that date, alongside the existing completion/fetch conditions | None of the seven supplied cases violates its expected contract. Other inputs and other writers remain outside this result. |

The useful simplification was to remove the per-run bookkeeping, not persist another ledger. The authoritative pass reconciles values first; the stamp condition then asks whether the row still contains a nonblank column that the publisher did not confirm for that date. This describes the new-stamp check, not a guarantee that all pre-existing labels are valid.

## Why the earlier verification was insufficient

The original test suite reported twelve passing checks. It called a hand-transcribed version of the provisional write gate, supplied already-parsed publisher data, and inspected source strings. It did exercise parts of the authoritative pass, but did not run the complete parser-to-write path. The green result did not cover the missing failure cases.

A later end-to-end suite ran the actual entry point, but its historical comparison initially loaded `HEAD`. Committing the repair moved that reference to the repaired code. The intended defective baseline disappeared from the comparison. The operational suite subsequently pinned its reference; this public package includes frozen snapshots so it needs neither the private repository nor a moving Git reference.

These historical test-suite observations are source-backed editorial findings. The [provenance record](PROVENANCE.md) separates them from the behavior reproduced by the bundled code.

## Run the evidence

With the declared dependency installed, from the repository root:

```bash
python3 -B cases/04_violet-correction-verification/reproduction/run_checks.py --selftest
```

See [setup, expected output, and test boundaries](reproduction/README.md). The harness executes source-derived `main(["--spot-only"])`, including the parser, both write passes, exit status, and temporary ledger readback. It does not transcribe the write gate.

The repeated-run case is the most informative contrast:

| Snapshot | After run 1 | After run 2 |
|---|---|---|
| A | `110 / SETTLE / rc=0` | `110 / SETTLE / rc=0` |
| B | `110 / blank basis / rc=0` | `110 / SETTLE / rc=0` |
| C | `110 / blank basis / rc=0` | `110 / blank basis / rc=0` |

The recovery control then supplies the missing authoritative value. All three versions finish at `120 / SETTLE / rc=0`. Refusing all updates is therefore not an acceptable repair. The harness checks the intermediate states as well as that terminal recovery.

## Why this matters for research productivity

The episode exposes work that a count of completed agent tasks would miss: external review, attempted repairs, re-review, and verification of the verification tool itself. Those are candidates for measuring the cost of obtaining a usable result, not evidence of a measured productivity loss or gain here.

The research question is whether a workflow's reliability benefit outweighs its model usage, coordination, human review, and rework costs. The separate [pilot protocol](../../experiments/research-quality-pilot.md) proposes how to begin testing that question. It has not been run.

The companion [VULCAN case](../07_vulcan-test-harness-false-pass/) isolates another verification failure: the test harness accepted unsuccessful control runs. Its offline reproduction checks historical scoring behavior using specified subprocess exits.

## Contributions and limits

- **Will:** designed and operates the broader system, commissioned the external review, and selected and authorized this portfolio addition. This is not a claim that he manually authored every implementation detail.
- **VIOLET / Claude-based workflow:** produced the operational implementation, repairs, and internal tests documented in the source history.
- **Codex external review:** supplied adversarial checks during the correction cycle and prepared this source-derived public reproduction and explanation under Will's direction. External review also requires verification; this is not a controlled comparison of vendors.

This is a retrospectively selected case, not a random sample. Tests use controlled adapters, not live vendor services. They do not evaluate the separate leading-edge writer (`thresholds.py`), downstream trading decisions, every ledger column, every malformed input, or future changes. A case-specific repair is demonstrated; system-wide prevention, economic gains, and multi-agent superiority remain unproven.
