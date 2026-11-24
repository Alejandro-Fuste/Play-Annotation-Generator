#!/usr/bin/env python3
"""Export CSV-selected annotations into train/ and test/ ZIP folders."""
import argparse
import csv
import json
import re
import sys
import tempfile
import zipfile
from collections import Counter
from pathlib import Path


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--csv', required=True, type=Path)
    p.add_argument('--repo-root', type=Path, default=Path.cwd())
    p.add_argument('--output', type=Path, default=Path('BootPass_annotations.zip'))
    p.add_argument('--category', help='Override source category; default: infer from Prefix')
    p.add_argument('--dry-run', action='store_true')
    p.add_argument('--strict', action='store_true')
    p.add_argument('--overwrite', action='store_true')
    a = p.parse_args()
    root = a.repo_root.expanduser().resolve()
    output = a.output.expanduser().resolve()
    report_path = output.with_suffix('.report.json')
    csv_path = a.csv.expanduser().resolve()
    if not root.is_dir() or not csv_path.is_file():
        p.error('Repository root or CSV does not exist')
    if output.suffix.lower() != '.zip':
        p.error('Output must end in .zip')
    required = ['Prefix', 'Number', 'Original File Name', 'New File Name', 'Destination Folder']
    found, missing, rejected = [], [], []
    sources, destinations = set(), set()
    requested = Counter()
    def component(s):
        return bool(re.fullmatch(r'[A-Za-z0-9_-]+', s))
    def filename(s):
        return bool(re.fullmatch(r'[A-Za-z0-9_.-]+\.json', s, re.IGNORECASE))
    with csv_path.open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        if not set(required).issubset(reader.fieldnames or []):
            p.error('CSV must contain: ' + ', '.join(required))
        for line, row in enumerate(reader, 2):
            prefix, number, original, new, split = [(row.get(k) or '').strip() for k in required]
            if not any((prefix, number, original, new, split)):
                continue
            split = split.lower()
            requested[split] += 1
            category = a.category or prefix.rstrip('_')
            if not (component(prefix) and component(category) and re.fullmatch(r'[0-9]+', number) and filename(original) and filename(new) and split in {'train', 'test'}):
                rejected.append({'line': line, 'reason': 'Invalid path, filename, number or split', 'row': row})
                continue
            relative = Path('outputs') / 'batch' / category / category / (prefix + number) / original
            source = root / relative
            target = f'{split}/{new}'
            entry = {'source': relative.as_posix(), 'destination': target, 'line': line}
            sk, dk = str(source.resolve()).casefold(), target.casefold()
            if sk in sources or dk in destinations:
                rejected.append({**entry, 'reason': 'Duplicate source or destination'})
                continue
            sources.add(sk)
            destinations.add(dk)
            if not source.resolve().is_relative_to(root):
                rejected.append({**entry, 'reason': 'Source outside repository'})
            elif not source.is_file() or source.stat().st_size == 0:
                missing.append(entry)
            else:
                found.append(entry)
    counts = Counter(e['destination'].split('/')[0] for e in found)
    print(f'CSV entries: {sum(requested.values())}')
    print(f'Found: {len(found)} | Missing/empty: {len(missing)} | Rejected: {len(rejected)}')
    for split in ('train', 'test'):
        print(f'{split}: {counts[split]}/{requested[split]} files found')
    for entry in missing + rejected:
        print(entry)
    for entry in found[:5]:
        print(f"{entry['source']} -> {entry['destination']}")
    failed = bool(missing or rejected)
    if a.dry_run:
        print('Dry run: no files written.')
        return int(failed or not found)
    if not a.overwrite and (output.exists() or report_path.exists()):
        p.error('Output or report already exists; choose a new --output or use --overwrite')
    output.parent.mkdir(parents=True, exist_ok=True)
    report = {'csv': str(csv_path), 'repo_root': str(root), 'requested': dict(requested), 'found': len(found), 'found_by_split': dict(counts), 'missing': missing, 'rejected': rejected, 'mappings': found, 'zip_created': False}
    if (a.strict and failed) or not found:
        print('ZIP not created: preflight failed.')
    else:
        tmp = None
        try:
            with tempfile.NamedTemporaryFile(dir=output.parent, suffix='.zip.tmp', delete=False) as f:
                tmp = Path(f.name)
            with zipfile.ZipFile(tmp, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6, allowZip64=True) as z:
                for split in ('train', 'test'):
                    z.writestr(split + '/', b'')
                for i, entry in enumerate(found, 1):
                    z.write(root / entry['source'], arcname=entry['destination'])
                    if i % 25 == 0 or i == len(found):
                        print(f'Archived {i}/{len(found)} files')
            with zipfile.ZipFile(tmp) as z:
                if z.testzip() is not None:
                    raise OSError('ZIP integrity check failed')
            tmp.replace(output)
            report['zip_created'] = True
            print(f'Created: {output}')
        finally:
            if tmp is not None:
                tmp.unlink(missing_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(f'Report: {report_path}')
    return int(failed or not found)


if __name__ == '__main__':
    sys.exit(main())
