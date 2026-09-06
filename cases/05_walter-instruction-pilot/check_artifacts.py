#!/usr/bin/env python3
"""Check archived evidence integrity, not model performance. No model calls/writes."""
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def require(value, message):
    if not value:
        raise ValueError(message)


def main():
    manifest = json.loads((ROOT / 'evidence/manifest.json').read_text())
    for name, entry in manifest['sources'].items():
        data = (ROOT / name).read_bytes()
        require(hashlib.sha256(data).hexdigest() == entry['public_sha256'], f'Changed artifact: {name}')
    old = (ROOT / 'evidence/instruction_original.txt').read_bytes()
    new = (ROOT / 'evidence/instruction_revised.txt').read_bytes()
    require((len(old), len(new)) == (1724, 1537), 'Unexpected instruction-file sizes')
    for arm, count in [('control', 5), ('revised', 6)]:
        record = (ROOT / f'evidence/record_{arm}.md').read_text()
        require(record.count('### TOOL CALL: Bash') == count, f'Tool-call count differs: {arm}')
        require(len(manifest['session_metadata'][arm]['tool_calls']) == count, 'Metadata count differs')
        require('/home/' not in record and 'github_pat_' not in record, 'Private path/token marker')
    fixture = ROOT / 'fixture'
    signal = (fixture / 'BOARD/SIG-W-20260812-003-example-signal.md').read_text()
    require(re.search(r'^status: PARTIALLY-SUPERSEDED$', signal, re.M), 'Fixture A changed')
    registry = (fixture / 'AGENTS/REGINALD/registry/THRESHOLDS.tsv').read_text()
    require('CREED is NOT in this chain and no second-bar note exists' in registry, 'Fixture B changed')
    require(not (fixture / 'AGENTS/WALTER/registry/intake_pending.json').exists(), 'Fixture C must remain absent')
    times = manifest['chronology']
    core = datetime.fromisoformat(times['269fa140f'].split()[1])
    addendum = datetime.fromisoformat(times['4c5482939'].split()[1])
    for arm, metadata in manifest['session_metadata'].items():
        start = datetime.fromisoformat(metadata['first_record_utc'])
        end = datetime.fromisoformat(metadata['last_record_utc'])
        require(core < start < addendum < end, f'Chronology differs: {arm}')
    print(f'PASS: {len(manifest["sources"])} archived artifacts match their public hashes.')
    print('Instruction files: 1724 -> 1537 UTF-8 bytes; difference 187 (not tokens or total prompt cost).')
    print('Tool records: 5 original / 6 revised calls; core rubric before runs, addendum during runs.')
    print('No model runs or automated behavior grading performed.')
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f'FAIL: {error}', file=sys.stderr)
        raise SystemExit(1)
