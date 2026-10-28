"""Safe scaffolding, source inventory and limited text-placeholder checks (stdlib)."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from datetime import datetime, timezone

BASE = Path(__file__).resolve().parents[1]


def stamp():
    return datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')


def safe(root, relative):
    rel = Path(relative)
    if rel.is_absolute() or '..' in rel.parts:
        raise ValueError('Expected a project-relative path: ' + str(relative))
    target = root / rel
    for part in [target, *target.parents]:
        if part == root:
            break
        if part.is_symlink() or getattr(part, 'is_junction', lambda: False)():
            raise ValueError('Refusing redirected path: ' + str(part))
    if not target.resolve().is_relative_to(root):
        raise ValueError('Path escapes project: ' + str(target))
    return target


def write_new(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8', newline='\n') as handle:
        handle.write(value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def initialize(root):
    if root == BASE or root.is_relative_to(BASE):
        raise ValueError('Select a research project, not the skill installation.')
    layout = json.loads((BASE / 'assets/layout.json').read_text(encoding='utf-8'))
    files = {
        '00_project/START_HERE.md': (BASE / 'assets/START_HERE.md').read_text(encoding='utf-8'),
        '00_project/project.json': {'schema_version': 1, 'project_name': root.name, 'target_journal': None, 'article_type': None, 'study_summary': None, 'manuscript_language': 'English', 'canonical_manuscript': '05_drafts/merged_manuscript/manuscript.docx'},
        '00_project/status.json': {'schema_version': 1, 'stage': 'awaiting_journal_materials', 'gates': {'journal_profile': 'pending', 'evidence_and_blueprint': 'pending', 'submission': 'pending'}, 'readiness': {'draft_complete': False, 'scientific_review_complete': False, 'formatting_review_complete': False, 'author_approved_submission': False}}
    }
    # Preflight every managed path and ancestor before creating anything.
    for relative in [*layout['directories'], *files]:
        path = safe(root, relative)
        for parent in path.parents:
            if parent == root.parent:
                break
            if parent.exists() and not parent.is_dir():
                raise ValueError('Directory collision: ' + str(parent))
        if path.exists() and (path.is_dir() != (relative in layout['directories'])):
            raise ValueError('File/directory collision: ' + str(path))
    created, retained = [], []
    for relative in layout['directories']:
        safe(root, relative).mkdir(parents=True, exist_ok=True)
    for relative, value in files.items():
        path = safe(root, relative)
        if path.exists():
            retained.append(relative)
        else:
            write_new(path, value)
            created.append(relative)
    return {
        'created_files': created,
        'retained_files': retained,
        'root': str(root),
        'stage': 'awaiting_journal_materials',
        'input_map': {
            'target_journal_articles': '01_inputs/01_target_journal/reference_articles',
            'official_journal_guidance': '01_inputs/01_target_journal/author_guidelines',
            'journal_templates': '01_inputs/01_target_journal/journal_templates',
            'research_materials': '01_inputs/02_research_materials',
            'preference_papers_optional': '01_inputs/03_preference_papers'
        },
        'next_message': '期刊材料已放好'
    }


SCOPES = {
    'journal': ('01_inputs/01_target_journal', '02_corpus/target_journal/quality_control/inventories', 'JRN'),
    'research': ('01_inputs/02_research_materials', '03_evidence/inventories', 'SRC'),
    'preference': ('01_inputs/03_preference_papers', '02_corpus/preference_corpus/quality_control/inventories', 'PRE')
}


def inventory(root, scope):
    source_rel, output_rel, prefix = SCOPES[scope]
    source = safe(root, source_rel)
    output = safe(root, output_rel)
    if not source.is_dir():
        raise ValueError('Input directory missing: ' + str(source))
    previous = sorted(output.glob('inventory_*.json')) if output.exists() else []
    old = json.loads(safe(root, previous[-1].relative_to(root)).read_text(encoding='utf-8')) if previous else {'sources': [], 'last_id': 0}
    registry = {row['path']: row for row in old['sources']}
    last_id, rows, skipped, seen = old['last_id'], [], [], set()
    for folder, subdirs, filenames in os.walk(source, followlinks=False):
        for name in list(subdirs):
            path = Path(folder) / name
            try:
                safe(root, path.relative_to(root))
            except ValueError:
                subdirs.remove(name)
                skipped.append(path.relative_to(root).as_posix())
        for name in sorted(filenames):
            path = Path(folder) / name
            relative = path.relative_to(root).as_posix()
            try:
                safe(root, relative)
            except ValueError:
                skipped.append(relative)
                continue
            digest = hashlib.sha256()
            before = path.stat()
            with path.open('rb') as handle:
                for chunk in iter(lambda: handle.read(1024 * 1024), b''):
                    digest.update(chunk)
            after = path.stat()
            if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
                raise ValueError('Source changed during hashing; retry: ' + relative)
            prior = registry.get(relative)
            if not prior:
                last_id += 1
            change = 'added' if not prior else ('restored' if prior.get('status') == 'missing' else ('unchanged' if prior['sha256'] == digest.hexdigest() else 'changed'))
            rows.append({'source_id': prior['source_id'] if prior else f'{prefix}-{last_id:05d}', 'path': relative, 'size_bytes': after.st_size, 'sha256': digest.hexdigest(), 'status': 'present', 'change': change})
            seen.add(relative)
    for relative, prior in registry.items():
        if relative not in seen:
            rows.append({**prior, 'status': 'missing', 'change': 'removed' if prior['status'] == 'present' else 'still_missing'})
    snapshot = {'scope': scope, 'created_utc': stamp(), 'last_id': last_id, 'sources': sorted(rows, key=lambda row: row['path']), 'skipped_redirects': skipped, 'verification_scope': 'file identity only; no scientific review'}
    destination = safe(root, output_rel + '/inventory_' + snapshot['created_utc'] + '.json')
    write_new(destination, snapshot)
    return {'snapshot': str(destination), 'source_records': len(rows), 'skipped_redirects': skipped}


MARKERS = re.compile(r'\[PENDING:[^\]]+\]|\[(?:AUTHOR INPUT NEEDED|ECD PENDING|ECD DATA PENDING|ref)[^\]]*\]|\b(?:Table|Fig\.?|Figure)\s+[XY]\b|\bTODO\b', re.I)


def placeholders(root, relative):
    path = safe(root, relative)
    if path.suffix.lower() not in {'.md', '.txt', '.tex'}:
        raise ValueError('Only MD/TXT/TEX supported; extract and inspect other formats separately.')
    hits = []
    for number, line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(), 1):
        for match in MARKERS.finditer(line):
            hits.append({'line': number, 'marker': match.group()})
    return {'file': relative, 'hits': hits, 'scope': 'Limited marker scan only; not submission clearance.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ('init', 'inventory', 'placeholders'):
        child = sub.add_parser(name)
        child.add_argument('--root', required=True)
        if name == 'inventory':
            child.add_argument('--scope', choices=SCOPES, required=True)
        if name == 'placeholders':
            child.add_argument('--file', required=True, help='Project-relative MD/TXT/TEX path')
    args = parser.parse_args()
    root = Path(args.root).absolute()
    if root.is_symlink() or getattr(root, 'is_junction', lambda: False)():
        raise ValueError('Select the actual project directory, not a redirect.')
    root = root.resolve()
    if args.command == 'init':
        result = initialize(root)
    elif args.command == 'inventory':
        result = inventory(root, args.scope)
    else:
        result = placeholders(root, args.file)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result.get('hits') else 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as error:
        print(json.dumps({'error': str(error)}, ensure_ascii=False), file=sys.stderr)
        sys.exit(2)
