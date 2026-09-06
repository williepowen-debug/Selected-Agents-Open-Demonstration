# Selected historical source and report excerpts

These are excerpts, not a complete renderer or independently recomputed census.
Surviving pre/post labels are historical names; their chronology is not established.


## Before withdrawal

Source: `AGENTS/DAEDALUS/scorecards/2026-09-04.md` at `eb6a80d8cbb0d540de0376fa528cf37cad856682`.

| # | Column | Value | Both terms / note |
|---|---|---|---|
| 3 | `catches_pre_decision` | **28** | ORCH_LOG touches with `brief_defect_count`≥1 (defects summed: 32) · 12 scored 0 · 0 prose-only UNSCORED |
| 4 | `corrections_post_decision` | **0** | CORRECTIONS.tsv rows dated in window 0 + WQ amendment stamps 0 |
| 8 | `correction_efficiency` | 28/28 = 1.00 | pre ÷ (pre + post) |

## After withdrawal

Source: `AGENTS/DAEDALUS/scorecards/2026-09-04.md` at `0923f5816ff62423200901c15d931c96f9590104`.

| # | Column | Value | Both terms / note |
|---|---|---|---|
| 3 | `catches_pre_decision` | **28** | ORCH_LOG touches with `brief_defect_count`≥1 (defects summed: 32) · 12 scored 0 · 0 prose-only UNSCORED |
| 4 | `corrections_post_decision` | **0** | CORRECTIONS.tsv rows dated in window 0 + WQ amendment stamps 0 |
| 8 | `correction_efficiency` | ~~28/28 = 1.00~~ **WITHDRAWN** (see §8 note added 2026-09-05) | pre ÷ (pre + post) — NOT a valid ratio (Codex) |

## Counting functions

Verbatim definitions from the pre-withdrawal renderer. Helpers and input files are omitted; this is not executable standalone code.


```python
def col3_catches(touches):
    caught, unscored_prose, scored_zero = [], [], 0
    for r in touches:
        ok, v = orch_log.int_or_empty(r["brief_defect_count"])
        if ok and v is not None and v >= 1:
            caught.append((r["date"], r["desk"], r["touch"], v))
        elif ok and v == 0:
            scored_zero += 1
        elif r["brief_defects"].strip() and r["brief_defects"].strip() not in ("—", "-"):
            unscored_prose.append((r["date"], r["desk"], r["touch"]))
    return caught, scored_zero, unscored_prose
```

```python
def col4_corrections(start, end):
    rows = tsv_rows(CORR)
    if not rows:
        return None, []
    h = rows[0][1]
    for c in ("correction_id", "date", "corrector", "targets"):
        if c not in h:
            print(f"rc=2 CANNOT-EVALUATE: CORRECTIONS.tsv header lacks {c}")
            sys.exit(2)
    ci, di, ki, ti = (h.index(c) for c in ("correction_id", "date", "corrector", "targets"))
    out = []
    for ln, f in rows[1:]:
        if len(f) <= max(ci, di, ki, ti):
            continue
        if in_window(f[di].strip(), start, end):
            out.append((f[ci], f[di], f[ki], f[ti][:40], ln))
    return len(rows) - 1, out
```

## Calculation before withdrawal

```python
pre, post = len(caught), len(corr) + len(amended)
P(f"| 8 | `correction_efficiency` | {ratio(pre, pre + post)} | pre ÷ (pre + post) |")
```

## Renderer after withdrawal

```python
P(f"| 8 | `correction_efficiency` | **WITHDRAWN — not a ratio** | pre={pre} (col 3, ORCH_LOG brief-defects) and post={post} (col 4, CORRECTIONS+WQ) are DIFFERENT populations, no shared event identity — see §8 |")
```
