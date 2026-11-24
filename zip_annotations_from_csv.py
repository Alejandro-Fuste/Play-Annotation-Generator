#!/usr/bin/env python3
"""Package locally available annotation JSON files listed by Prefix,Number,FileName CSV."""
import argparse
import csv
import json
import sys
import zipfile
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--csv', required=True, type=Path, help='CSV with Prefix, Number, FileName columns')
    parser.add_argument('--repo-root', type=Path, default=Path.cwd(), help='Repository root (defaults to current directory)')
    parser.add_argument('--output', type=Path, default=Path('BootPass_annotations.zip'), help='Output ZIP path')
    parser.add_argument('--category', default='BootPass', help='Folder name used twice under outputs/batch')
    parser.add_argument('--strict', action='store_true', help='Do not write ZIP if any requested file is missing')
    parser.add_argument('--dry-run', action='store_true', help='Report what would be packaged without creating ZIP')
    args = parser.parse_args()

    root = args.repo_root.expanduser().resolve()
    csv_path = args.csv.expanduser().resolve()
    output = args.output.expanduser().resolve()
    if not root.is_dir():
        parser.error(f'Repository root does not exist: {root}')
    if not csv_path.is_file():
        parser.error(f'CSV does not exist: {csv_path}')
    if '/' in args.category or '\\' in args.category or args.category in {'.', '..'}:
        parser.error('Category must be a single directory name')

    found = []
    missing = []
    rejected = []
    seen = set()
    with csv_path.open('r', encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        required = {'Prefix', 'Number', 'FileName'}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            parser.error('CSV must contain Prefix, Number, FileName columns')
        for line, row in enumerate(reader, start=2):
            prefix = (row['Prefix'] or '').strip()
            number = (row['Number'] or '').strip()
            name = (row['FileName'] or '').strip()
            if not any([prefix, number, name]):
                continue
            if not prefix or not number.isdecimal() or not name or Path(name).name != name or name in {'.', '..'} or '/' in prefix or '\\' in prefix or '..' in prefix:
                rejected.append({'csv_line': line, 'reason': 'Invalid prefix, number or filename', 'row': row})
                continue
            relative = Path('outputs') / 'batch' / args.category / args.category / f'{prefix}{number}' / name
            key = relative.as_posix()
            if key in seen:
                rejected.append({'csv_line': line, 'reason': 'Duplicate path', 'path': key})
                continue
            seen.add(key)
            source = root / relative
            if not source.is_file():
                missing.append(key)
            elif not source.resolve().is_relative_to(root):
                rejected.append({'csv_line': line, 'reason': 'Source resolves outside repository', 'path': key})
            else:
                found.append((source, key))

    print(f'CSV entries: {len(found) + len(missing) + len(rejected)}')
    print(f'Found: {len(found)} | Missing: {len(missing)} | Invalid/duplicate: {len(rejected)}')
    if missing:
        print('\nMissing files:')
        for item in missing:
            print('  ' + item)
    if rejected:
        print('\nRejected rows:')
        for item in rejected:
            print('  ' + str(item))
    report = {'csv': str(csv_path), 'repo_root': str(root), 'found': len(found), 'missing': missing, 'rejected': rejected}
    report_path = output.with_suffix('.report.json')
    if not args.dry_run:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
        print(f'Wrote report: {report_path}')
    if args.dry_run:
        print('Dry run: no ZIP created.')
        return 1 if missing or rejected else 0
    if args.strict and (missing or rejected):
        print('Strict mode: ZIP not created because some entries are missing or invalid.')
        return 1
    if not found:
        print('No files found: ZIP not created.')
        return 1
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6, allowZip64=True) as archive:
        for source, archive_name in found:
            archive.write(source, arcname=archive_name)
    print(f'Created: {output} ({len(found)} annotation files)')
    return 1 if missing or rejected else 0


if __name__ == '__main__':
    sys.exit(main())
