# Historical source-derived excerpt; not a standalone data tool.
# See ../../PROVENANCE.md for extraction boundaries and source hashes.
# Source commit: 8eec88a841e6ade5096abaeb9a8aa21bc31db3e4
# Comments/docstrings removed; executable AST of selected definitions unchanged.
# Imports, clock, ledger path, and non-graded regime helper supplied by harness.

TICKERS = {'vix': '^VIX', 'vix9d': '^VIX9D', 'vix3m': '^VIX3M', 'vix6m': '^VIX6M', 'vvix': '^VVIX', 'skew': '^SKEW'}

def load_existing() -> tuple[list[str], dict[str, dict]]:
    if not DAILY_LOG.exists():
        raise FileNotFoundError(DAILY_LOG)
    with open(DAILY_LOG) as f:
        reader = csv.DictReader(f, delimiter='\t')
        rows = {r['date']: r for r in reader if r.get('date')}
        header = reader.fieldnames or []
    return (header, rows)

def write_merged(header: list[str], rows: dict[str, dict]):
    sorted_dates = sorted(rows.keys())
    with open(DAILY_LOG, 'w') as f:
        f.write('\t'.join(header) + '\n')
        for d in sorted_dates:
            row = rows[d]
            f.write('\t'.join((str(row.get(col, '') or '') for col in header)) + '\n')

def backfill_spot(days: int, rows: dict[str, dict], cboe_hist: dict[str, dict[str, float]] | None=None, cboe_failed: set[str] | None=None) -> int:
    import yfinance as yf
    import pandas as pd
    period = f'{max(days + 10, 30)}d'
    print(f'  Fetching yfinance history ({period}) for {list(TICKERS.values())}')
    hist = {}
    for key, sym in TICKERS.items():
        tk = yf.Ticker(sym)
        df = tk.history(period=period, auto_adjust=False)
        if df.empty:
            print(f'    ⚠ {sym}: empty history')
            continue
        s = df['Close']
        s.index = [d.date() if hasattr(d, 'date') else d for d in s.index]
        hist[key] = s
    if 'vix' not in hist:
        print('  ✗ cannot backfill: no VIX history')
        return 0
    df = pd.concat(hist, axis=1).dropna(how='all')
    companions = [c for c in ('vix3m', 'vvix', 'skew') if c in df.columns]
    if companions:
        df = df[df[companions].notna().any(axis=1)]
    failed = set(cboe_failed or ())
    scoped = cboe_hist is not None
    touched = 0
    provisional = 0
    withheld_failed = 0
    deferred_cboe = 0
    withheld_settle = 0
    withheld_occupied = 0
    for d, series in df.iterrows():
        d_str = d.isoformat()
        row = rows.get(d_str, {'date': d_str})
        changed = False
        row_is_settle = str(row.get('basis', '') or '').strip().upper() == 'SETTLE'
        for key in TICKERS:
            if key in hist and (not pd.isna(series.get(key))):
                if key in failed:
                    withheld_failed += 1
                    continue
                if cboe_hist is not None and cboe_hist.get(key, {}).get(d_str) is not None:
                    deferred_cboe += 1
                    continue
                if scoped and row_is_settle:
                    withheld_settle += 1
                    continue
                if scoped and str(row.get(key, '') or '').strip():
                    withheld_occupied += 1
                    continue
                val = round(float(series[key]), 4)
                if str(row.get(key, '')) != str(val):
                    row[key] = val
                    changed = True
                    provisional += 1
        vix = row.get('vix')
        vix3m = row.get('vix3m')
        vix9d = row.get('vix9d')
        if vix and vix3m:
            try:
                row['vix3m_vix_ratio'] = round(float(vix3m) / float(vix), 4)
                changed = True
            except (ValueError, ZeroDivisionError):
                pass
        if vix and vix9d:
            try:
                row['vix9d_vix_ratio'] = round(float(vix9d) / float(vix), 4)
                changed = True
            except (ValueError, ZeroDivisionError):
                pass
        if vix:
            try:
                row['regime'] = determine_regime(float(vix))
            except ValueError:
                pass
        if changed:
            rows[d_str] = row
            touched += 1
    if cboe_hist is not None or failed:
        print(f'  yfinance (provisional): {provisional} cell(s) written where CBOE publishes nothing, {deferred_cboe} deferred to CBOE, {withheld_failed} WITHHELD (CBOE series failed this run), {withheld_settle} WITHHELD (row already basis=SETTLE), {withheld_occupied} WITHHELD (cell already holds a value — no overwrite)')
    return touched
CBOE_HISTORY_URL = 'https://cdn.cboe.com/api/global/us_indices/daily_prices/{sym}_History.csv'
CBOE_SERIES = {'vix': 'VIX', 'vix9d': 'VIX9D', 'vix3m': 'VIX3M', 'vix6m': 'VIX6M', 'vvix': 'VVIX', 'skew': 'SKEW'}
CBOE_TOL = 0.005

def fetch_cboe_history(sym: str) -> tuple[dict[str, float], bool]:
    try:
        r = requests.get(CBOE_HISTORY_URL.format(sym=sym), timeout=30, headers={'User-Agent': 'Mozilla/5.0'})
    except requests.RequestException as e:
        print(f'    ⚠ CBOE {sym}: request FAILED ({type(e).__name__}) — NOT used this run')
        return ({}, False)
    if r.status_code != 200:
        print(f'    ⚠ CBOE {sym}: HTTP {r.status_code} — NOT used this run')
        return ({}, False)
    reader = csv.DictReader(io.StringIO(r.text))
    fields = [f.strip() for f in reader.fieldnames or [] if f]
    if 'DATE' not in fields and 'Date' not in fields:
        print(f'    ⚠ CBOE {sym}: HTTP 200 but body is NOT a daily-prices CSV (no DATE column; header={fields[:4]}) — parse FAILURE, NOT used this run')
        return ({}, False)
    if 'CLOSE' not in fields and sym not in fields:
        print(f'    ⚠ CBOE {sym}: HTTP 200 but no CLOSE/{sym} value column (header={fields[:6]}) — parse FAILURE, NOT used this run')
        return ({}, False)
    out: dict[str, float] = {}
    for row in reader:
        d = row.get('DATE') or row.get('Date')
        if not d:
            continue
        raw = row.get('CLOSE') or row.get(sym)
        try:
            if '/' in d:
                dd = datetime.strptime(d, '%m/%d/%Y').date().isoformat()
            else:
                dd = datetime.strptime(d, '%Y-%m-%d').date().isoformat()
            out[dd] = round(float(raw), 4)
        except (ValueError, KeyError, TypeError):
            continue
    return (out, True)

def fetch_all_cboe() -> tuple[dict[str, dict[str, float]], set[str]]:
    print(f'  Fetching CBOE daily-prices CSVs (publisher of record) for {list(CBOE_SERIES.values())}')
    hist: dict[str, dict[str, float]] = {}
    failed: set[str] = set()
    for col, sym in CBOE_SERIES.items():
        data, ok = fetch_cboe_history(sym)
        hist[col] = data
        if not ok:
            failed.add(col)
    return (hist, failed)

def backfill_spot_cboe(rows: dict[str, dict], today: str | None=None, hist: dict[str, dict[str, float]] | None=None, failed: set[str] | None=None) -> dict[str, int]:
    if today is None:
        today = date.today().isoformat()
    if hist is None:
        hist, fetch_failed = fetch_all_cboe()
        failed = fetch_failed if failed is None else set(failed) | fetch_failed
    failed = set(failed or ())
    if failed:
        print(f'  🔴 CBOE INCOMPLETE — {len(failed)} of {len(CBOE_SERIES)} series unavailable: {sorted(failed)}')
        print('     Those columns are NOT written by anything this run; previously verified values are PRESERVED.')
    filled = corrected = agreed = settle_stamped = 0
    settle_withheld_provisional = 0
    corrections: list[str] = []
    for d_str, row in rows.items():
        for col in CBOE_SERIES:
            if col in failed:
                continue
            ref = hist[col].get(d_str)
            if ref is None:
                continue
            raw = str(row.get(col, '') or '').strip()
            if not raw:
                row[col] = ref
                filled += 1
                continue
            try:
                cur = float(raw)
            except ValueError:
                row[col] = ref
                corrected += 1
                corrections.append(f'     {d_str}  {col:6s} unparseable {raw!r} -> {ref}')
                continue
            if abs(cur - ref) <= CBOE_TOL:
                agreed += 1
            else:
                row[col] = ref
                corrected += 1
                corrections.append(f'     {d_str}  {col:6s} {cur:>9.2f} -> {ref:>9.2f}  ({cur - ref:+.2f})')
        vix = str(row.get('vix', '') or '').strip()
        for num, out in (('vix3m', 'vix3m_vix_ratio'), ('vix9d', 'vix9d_vix_ratio')):
            n = str(row.get(num, '') or '').strip()
            if vix and n:
                try:
                    row[out] = round(float(n) / float(vix), 4)
                except (ValueError, ZeroDivisionError):
                    pass
        if vix:
            try:
                row['regime'] = determine_regime(float(vix))
            except ValueError:
                pass
        if not failed and d_str < today and (hist['vix'].get(d_str) is not None):
            unconfirmed = [c for c in CBOE_SERIES if hist.get(c, {}).get(d_str) is None and str(row.get(c, '') or '').strip()]
            if unconfirmed:
                settle_withheld_provisional += 1
                continue
            if str(row.get('basis', '') or '').strip() != 'SETTLE':
                row['basis'] = 'SETTLE'
                settle_stamped += 1
    print(f'  CBOE: {agreed} cell(s) agreed, {filled} blank(s) filled, {corrected} CORRECTED, {settle_stamped} row(s) stamped SETTLE, {settle_withheld_provisional} row(s) NOT stamped (hold an unconfirmed cell)')
    if corrections:
        print(f'  🔴 {len(corrections)} VALUE CORRECTION(S) — ledger was wrong, CBOE wins:')
        for line in corrections:
            print(line)
    return {'filled': filled, 'corrected': len(corrections), 'agreed': agreed, 'settle_stamped': settle_stamped, 'settle_withheld_provisional': settle_withheld_provisional}

def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--spot-days', type=int, default=90)
    p.add_argument('--m1m2-days', type=int, default=30)
    p.add_argument('--spot-only', action='store_true')
    p.add_argument('--m1m2-only', action='store_true')
    p.add_argument('--allow-m1m2', action='store_true', help='Override the m1m2 hard gate (convention unresolved — see docstring/MAINTENANCE #4)')
    args = p.parse_args(argv)
    header, rows = load_existing()
    print(f'Loaded {len(rows)} existing rows from {DAILY_LOG.name}')
    cboe_failed: set[str] = set()
    if not args.m1m2_only:
        print('\n[1a] Fetching CBOE (publisher of record) BEFORE any write...')
        cboe_hist, cboe_failed = fetch_all_cboe()
        print(f'\n[1b] yfinance provisional pass ({args.spot_days} days)...')
        touched = backfill_spot(args.spot_days, rows, cboe_hist=cboe_hist, cboe_failed=cboe_failed)
        print(f'  touched {touched} rows')
        print('\n[1c] Writing spot columns from CBOE (authoritative)...')
        backfill_spot_cboe(rows, hist=cboe_hist, failed=cboe_failed)
    if not args.spot_only:
        print(f'\n[2/2] Backfilling M1:M2 steepness ({args.m1m2_days} trading days)...')
        touched = backfill_m1m2(args.m1m2_days, rows, allow=args.allow_m1m2)
        print(f'  touched {touched} rows')
    write_merged(header, rows)
    print(f'\n✓ wrote {len(rows)} rows to {DAILY_LOG}')
    if cboe_failed:
        print(f'\n🔴 BACKFILL INCOMPLETE — CBOE unavailable for {len(cboe_failed)} of {len(CBOE_SERIES)} series: {sorted(cboe_failed)}')
        print('   Those columns were NOT refreshed and NOT overwritten; no basis=SETTLE was stamped this run. Re-run when CBOE is reachable.')
        return 2
    return 0
