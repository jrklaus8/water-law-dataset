#!/usr/bin/env python3
"""Data manifest: every data file of the review (CSV and JSON) with its size, shape, SHA-256 and where it came from.

Writes 10_reproducibility/DATA_MANIFEST.csv. It lets anyone confirm that the files they hold are the files this review analysed (a changed byte changes the hash), and shows at a glance which files are raw
exports, which are decisions, which are generated and by what. Hashes are taken after normalising CRLF to LF, so a checkout with Windows line endings gives the same hash.
`verify_repository.py` fails if the manifest differs from what this script writes, so it cannot go stale: after any change to a data file run this script (regenerate_all.sh does).

Run from legal-last-mile-systematic-review/:  python3 code/analysis/build_data_manifest.py
"""
import csv
import hashlib
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / '10_reproducibility/DATA_MANIFEST.csv'
COLUMNS = ['path', 'role', 'produced_by', 'bytes_lf_normalised', 'rows', 'columns', 'sha256_lf_normalised']
GLOBS = ['01_search/raw_exports/*', '01_search/deduplicated/*.csv', '02_screening/**/*.csv', '03_extraction/**/*.csv', '05_analysis/**/*.csv', '00_admin/*.csv', '00_admin/*.json',
         '11_archive/*.csv', '_reviewer2_codex/*.csv', '_reviewer2_codex/results*/*.json', 'code/analysis/weakness_register_source.csv']
SKIP = {'10_reproducibility/DATA_MANIFEST.csv'}

GENERATED = {
    '00_admin/STUDY_AUDIT_TRAIL.csv': 'code/analysis/build_study_audit_trail.py', '00_admin/AI_USE_LEDGER.csv': 'code/analysis/build_ai_use_ledger.py',
    '00_admin/WEAKNESS_REGISTER.csv': 'code/analysis/build_weakness_register.py', '00_admin/current_figures.json': 'code/analysis/current_figures.py',
    '05_analysis/sensitivity/sensitivity_scenarios_2026-09-28.csv': 'code/analysis/sensitivity_analysis.py',
}
HAND = {'00_admin/DEVIATIONS_REGISTER.csv': 'hand-maintained register', '00_admin/ERRORS_FOUND_REGISTER.csv': 'hand-maintained register', 'code/analysis/weakness_register_source.csv': 'hand-maintained register source'}


def role_and_origin(rel):
    if rel in HAND:
        return HAND[rel], 'AI-drafted from the repository\'s records; maintained by hand'
    if rel in GENERATED:
        return 'generated data', GENERATED[rel]
    if rel.startswith('01_search/raw_exports/'):
        return 'raw search export (never edited)', 'researcher, from the database'
    if rel.startswith('01_search/deduplicated/'):
        return 'de-duplicated records or merge log', 'code/search/deduplicate.py and dated audit scripts'
    if rel == '02_screening/title_abstract/screening_database.csv':
        return 'title/abstract screening database', 'AI first pass and human second pass; see code/provenance/'
    if rel.startswith('02_screening/title_abstract/'):
        return 'title/abstract screening companion file', 'AI or human; see 02_screening/README.md'
    if rel == '02_screening/full_text/full_text_screening_database.csv':
        return 'full-text screening database (source of truth)', 'AI first reviewer; human, PI and second-model reviewers; see code/provenance/'
    if rel.startswith('02_screening/full_text/') and Path(rel).name[0] == 'A' and Path(rel).name[1].isdigit():
        return 'adjudication sheet (researcher rulings or the blank sheet prepared for them)', 'AI-prepared; rulings entered under reviewer CK'
    if rel.startswith('02_screening/full_text/'):
        return 'full-text working file', 'AI scripts and the researcher; see 02_screening/full_text/FULL_TEXT_README.md'
    if rel.startswith('02_screening/exclusion_log/'):
        return 'exclusion log', 'AI, with researcher rulings'
    if rel.startswith('03_extraction/extracted_data/extraction_database.csv'):
        return 'extraction database (92 fields)', 'AI; no second extractor'
    if rel.startswith('03_extraction/'):
        return 'extraction companion file', 'AI scripts; second-extractor sheets are blank or blind'
    if rel.startswith('05_analysis/effect_sizes/'):
        return 'effect sizes, synthesis verification or direction coding', 'AI, with researcher rulings'
    if rel.startswith('05_analysis/'):
        return 'evidence map, audit or sensitivity file', 'AI scripts; see 05_analysis/README.md'
    if rel.startswith('11_archive/'):
        return 'archived data removed from the live databases', 'dated ruling; see 11_archive/README.md'
    if rel.startswith('_reviewer2_codex/results'):
        return 'raw output of an independent AI model run', 'Codex or Gemini; see _reviewer2_codex/AI_USE_AND_TOOLS_DISCLOSURE.md'
    if rel.startswith('_reviewer2_codex/'):
        return 'second-model reviewer table', 'AI scripts in _reviewer2_codex/'
    return 'data file', 'see the folder README'


def files():
    seen = {}
    for g in GLOBS:
        for p in ROOT.glob(g):
            if p.is_file() and '__pycache__' not in p.parts:
                rel = p.relative_to(ROOT).as_posix()
                if rel not in SKIP:
                    seen[rel] = p
    return [seen[k] for k in sorted(seen)]


def digest(p):
    data = p.read_bytes().replace(b'\r\n', b'\n')
    return len(data), hashlib.sha256(data).hexdigest()


def shape(p):
    if p.suffix != '.csv':
        return '', ''
    with open(p, newline='', encoding='utf-8') as f:
        rd = csv.reader(f)
        header = next(rd, [])
        n = sum(1 for _ in rd)
    return str(n), str(len(header))


def render():
    import io
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator='\n')
    w.writerow(COLUMNS)
    for p in files():
        rel = p.relative_to(ROOT).as_posix()
        role, by = role_and_origin(rel)
        rows, cols = shape(p)
        size, sha = digest(p)
        w.writerow([rel, role, by, size, rows, cols, sha])
    return buf.getvalue()


def main():
    text = render()
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(text, encoding='utf-8', newline='')
    print(f'wrote {OUT.relative_to(ROOT)} ({text.count(chr(10)) - 1} files)')


if __name__ == '__main__':
    main()
