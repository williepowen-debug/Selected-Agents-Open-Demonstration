# Case 6 — DAEDALUS: Withdrawing a metric the logs could not support

**The arithmetic was right; the measurement was not.** A coordination scorecard reported `correction_efficiency = 28 / (28 + 0) = 1.00`. Review found that its terms counted different populations and did not establish whether errors were caught before or after decisions. DAEDALUS withdrew the ratio from the specification, renderer, and published scorecard on September 5, 2026.

DAEDALUS is the system's architecture and process-design agent. This case illustrates measurement validity—not a measured improvement in prevention, productivity, or overall research quality.

## What the calculation actually counted

| Historical label | Operational definition | Published count |
|---|---|---|
| `catches_pre_decision` | Coordinator touches with at least one recorded brief defect | 28 touches; 32 defects summed |
| `corrections_post_decision` | Correction-register entries dated in the window, plus queue amendment stamps | 0 entries + 0 stamps |
| `correction_efficiency` | First count divided by the sum of both | 1.00 |

The [source excerpts](evidence/source-excerpts.md) preserve both published rows and the counting code. A touch containing several defects contributes **one**, while a register entry or amendment is a different unit. The inputs provide neither a shared error identity nor complete coverage of a common error population. Their labels also do not establish decision timing.

Consequently, zero registered corrections does not establish zero post-decision errors. A perfect-looking ratio could reflect incomplete registration, different inclusion rules, or different units. It cannot distinguish these explanations from effective prevention. Calling the ratio descriptive rather than decision-driving does not repair its meaning.

## A small counterexample

Suppose the same visible logs contain two defect-bearing touches and one correction entry. The formula gives `2/3`.

- In one possible underlying history, the two touched errors were caught before a decision and the registered error afterward: two of three were caught before the decision.
- In another, all three were discovered afterward: zero of three were caught before the decision.

The recorded fields are identical; the quantity one might want to measure differs. This is a **constructed illustration**, not a reconstruction of the historical 28 touches. It shows why the logs alone cannot identify that quantity—even after granting one distinct error per touch for simplicity.

Run it with standard-library Python from the repository root:

```bash
python3 -B cases/06_daedalus-measurement-validity/counterexample.py
```

The script checks the archived excerpt's hash and the illustrative arithmetic. It does not execute the production scorecard or independently recount the private logs.

## The correction—and its boundary

The useful change was subtraction: retire the unsupported ratio, retain separately defined raw counts, and explain the incompatibility where the result had been published. No replacement dashboard or composite score was needed to stop this particular overclaim.

The repair was scoped. The historical raw-column names still say “pre-decision” and “post-decision”; the excerpts retain those names rather than silently improving the record. Their chronology remains unestablished. Withdrawing the ratio does **not** validate every surviving scorecard label.

This episode matters because activity records are tempting substitutes for outcomes. Before interpreting any efficiency measure, define its unit, population, coverage, and timing—and verify that its components actually measure those definitions. Sometimes the defensible result is to publish less.

See [provenance](PROVENANCE.md) for pinned revisions and attribution. Will directed and authorized the system's review; Codex challenged the metric; DAEDALUS made the operational withdrawal. Codex prepared this public explanation and synthetic illustration under Will's direction. No controlled system-level benefit is claimed.
