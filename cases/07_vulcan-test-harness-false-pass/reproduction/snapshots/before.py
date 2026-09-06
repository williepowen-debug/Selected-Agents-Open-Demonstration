# Source-derived snapshot. See ../README.md and ../../PROVENANCE.md.
# Dependencies and validator behavior are supplied by the public runner.
CASES = [('gpu tier = BANANA', 'GPU_SERIES.tsv', 'tier', 'BANANA', True), ('gpu tier = on_demand (real)', 'GPU_SERIES.tsv', 'tier', 'on_demand', False), ('gpu unit = USD_per_node_month', 'GPU_SERIES.tsv', 'unit', 'USD_per_node_month', True), ('gpu gpu_model = BANANA', 'GPU_SERIES.tsv', 'gpu_model', 'BANANA', True), ('gpu source_class = BANANA', 'GPU_SERIES.tsv', 'source_class', 'BANANA', True), ('gpu instrument = BANANA', 'GPU_SERIES.tsv', 'instrument', 'BANANA', True), ('gpu price_basis = BANANA', 'GPU_SERIES.tsv', 'price_basis', 'BANANA', True), ('gpu price_basis = term_normalized', 'GPU_SERIES.tsv', 'price_basis', 'term_normalized', False), ('gpu price_usd = -1   (declared > 0)', 'GPU_SERIES.tsv', 'price_usd', '-1', True), ('gpu price_usd = 0    (declared > 0)', 'GPU_SERIES.tsv', 'price_usd', '0', True), ('gpu price_usd = nan  (parses!)', 'GPU_SERIES.tsv', 'price_usd', 'nan', True), ('gpu price_usd = inf  (parses!)', 'GPU_SERIES.tsv', 'price_usd', 'inf', True), ('gpu price_usd = abc', 'GPU_SERIES.tsv', 'price_usd', 'abc', True), ('gpu price_usd = 2.53 (real)', 'GPU_SERIES.tsv', 'price_usd', '2.53', False), ('gpu n_observations = 0 (decl >= 1)', 'GPU_SERIES.tsv', 'n_observations', '0', True), ('gpu n_observations = 3.7 (non-int)', 'GPU_SERIES.tsv', 'n_observations', '3.7', True), ('gpu n_observations = 12 (real)', 'GPU_SERIES.tsv', 'n_observations', '12', False), ('VX score = 9   (declared 1|2|3|4|5)', 'VX.tsv', 'score', '9', True), ('VX score = 3   (real)', 'VX.tsv', 'score', '3', False), ('S4 band = BANANA', 'S4_SERIES.tsv', 'band', 'BANANA', True), ('S4 band = BANANA(paren)', 'S4_SERIES.tsv', 'band', 'BANANA(cum ticked)', True), ('S4 band = no-stress(...)  (real)', 'S4_SERIES.tsv', 'band', 'no-stress(cum 1->2)', False), ('S4 band = yellow-decel(...) (real)', 'S4_SERIES.tsv', 'band', 'yellow-decel(x)', False), ('S4 rev_ntd_mn = nan', 'S4_SERIES.tsv', 'rev_ntd_mn', 'nan', True), ('EDGAR tick = BANANA', 'EDGAR_SEEN.tsv', 'tick', 'BANANA', True), ('EDGAR tick = NVDA (real)', 'EDGAR_SEEN.tsv', 'tick', 'NVDA', False), ('EDGAR channel = S9', 'EDGAR_SEEN.tsv', 'channel', 'S9', True), ('EDGAR channel = S5/S1 (real)', 'EDGAR_SEEN.tsv', 'channel', 'S5/S1', False), ('EDGAR tier = 7  (declared 1|2|3)', 'EDGAR_SEEN.tsv', 'tier', '7', True), ('LAYER window_days = 44 (1|5|21|63)', 'LAYER_SERIES.tsv', 'window_days', '44', True), ('LAYER window_days = 63 (real)', 'LAYER_SERIES.tsv', 'window_days', '63', False)]

def run(script: Path) -> int:
    return subprocess.run([sys.executable, str(script)], capture_output=True, text=True).returncode

def main() -> int:
    print('validate_workbook.py — guard falsification (sandboxed: real ledgers are never written)\n')
    with tempfile.TemporaryDirectory() as td:
        base = Path(td) / 'base'
        base.mkdir()
        script = build_sandbox(base)
        rc0 = run(script)
        print(f'  {'BASELINE — untouched copy must be CLEAN':52} rc={rc0} {('✅' if rc0 == 0 else '❌ SANDBOX DIRTY — every result below is void')}')
        if rc0 != 0:
            return 1
        print()
        bad = 0
        for label, ledger, col, val, must_catch in CASES:
            case = Path(td) / 'case'
            if case.exists():
                shutil.rmtree(case)
            case.mkdir()
            s = build_sandbox(case)
            apply_case(case, ledger, col, val)
            rc = run(s)
            ok = (rc == 2) == must_catch
            bad += not ok
            print(f'  {label:52} rc={rc} {('CATCH' if must_catch else 'PASS '):5} {('✅' if ok else '❌ WRONG')}')
    n_neg = sum((1 for c in CASES if c[4]))
    print(f'\n  {len(CASES)} cases — {n_neg} defects injected, {len(CASES) - n_neg} real-form controls — WRONG: {bad}')
    return 1 if bad else 0
