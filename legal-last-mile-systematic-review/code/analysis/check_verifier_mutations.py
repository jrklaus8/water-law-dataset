#!/usr/bin/env python3
"""Mutation check of the verifier: does `verify_repository.py` notice each kind of damage a careless edit could do?

A verifier that always says "passed" is worthless, and its checks were written one at a time, so nobody knew which realistic mistakes slip through. This script
copies the project to a scratch directory, applies ONE deliberate defect at a time to the copy (a dropped extraction row, an include flipped to exclude, a duplicated
DOI, a tampered headline figure, ...), runs the verifier there, and records whether it failed and which check said so; the copy is restored before the next defect.
The real project is never touched. Takes about 30 seconds per defect (the verifier regenerates every derived file in memory).
Output: a table on stdout, and with --write a dated map at 00_admin/VERIFIER_MUTATION_MAP_<date>.md. Exit code 1 if any defect goes UNCAUGHT.
Run from legal-last-mile-systematic-review/:  python3 code/analysis/check_verifier_mutations.py [--write] [--only NAME ...]
"""
from __future__ import annotations

import argparse
import csv
import datetime
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

csv.field_size_limit(sys.maxsize)
ROOT = Path(__file__).resolve().parents[2]
ED = '03_extraction/extracted_data/extraction_database.csv'
EM = '05_analysis/descriptive/evidence_map.csv'
MAP = '03_extraction/extracted_data/study_record_map.csv'
FT = '02_screening/full_text/full_text_screening_database.csv'
EL = '02_screening/exclusion_log/exclusion_log.csv'
ES = '05_analysis/effect_sizes/effect_sizes.csv'


def edit_csv(root: Path, rel: str, fn):
    """Read a CSV (keeping its line ending), let fn(rows, fields) change the row list in place, write it back."""
    p = root / rel
    raw = p.read_bytes().decode('utf-8')
    eol = '\r\n' if raw.split('\n', 1)[0].endswith('\r') else '\n'
    with open(p, encoding='utf-8', newline='') as f:
        rd = csv.DictReader(f)
        fields, rows = rd.fieldnames, list(rd)
    fn(rows, fields)
    with open(p, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator=eol)
        w.writeheader(); w.writerows(rows)


def edit_text(root: Path, rel: str, old: str, new: str):
    p = root / rel
    t = p.read_text(encoding='utf-8')
    assert old in t, f'{rel}: {old!r} not found'
    p.write_text(t.replace(old, new, 1), encoding='utf-8')


def _drop_last(rows, _):
    rows.pop()


def _map_wrong(rows, _):
    rows[0]['record_id'], rows[1]['record_id'] = rows[1]['record_id'], rows[0]['record_id']


def _flip_include(rows, _):
    next(r for r in rows if (r['final_decision'] or r['full_text_decision']) == 'include')['final_decision'] = 'exclude'


def _exclude_without_code(rows, _):
    next(r for r in rows if (r['final_decision'] or r['full_text_decision']) == 'exclude' and r['exclusion_reason'])['exclusion_reason'] = ''


def _dup_doi(rows, _):
    src = next(r for r in rows if r['doi'].strip())
    next(r for r in rows[1:] if not r['doi'].strip() and r is not src)['doi'] = src['doi']


def _bad_year(rows, _):
    rows[2]['publication_year'] = '302'


def _es_orphan(rows, _):
    rows[0]['study_id'] = 'S9999'


def _es_value(rows, _):
    r = next(x for x in rows if x.get('effect_estimate', '').strip())
    r['effect_estimate'] = '999'


def _blank_design(rows, _):
    rows[5]['study_design_class'] = 'not_a_design_class'


# (name, description, files the defect touches or creates, the defect)
def _bad_boolean(rows, _):
    rows[3]['household_level'] = 'maybe'


def _country(rows, _):
    rows[3]['country'] = 'Atlantis'


def _tool(rows, _):
    r = next(x for x in rows if x.get('risk_of_bias_tool', '').strip() == 'JBI Critical Appraisal Checklist')
    r['risk_of_bias_tool'] = 'RoB 2'


def _blank_citation(rows, _):
    rows[7]['citation'] = ''


def _include_with_reason(rows, _):
    next(r for r in rows if r['final_decision'] == 'include')['exclusion_reason'] = 'E01'


def _decision_disagree(rows, _):
    r = next(x for x in rows if x['final_decision'] == 'include')
    r['full_text_decision'] = 'exclude'


def _bad_doi(rows, _):
    next(r for r in rows if r['doi'].strip())['doi'] = 'doi-not-valid'


def _bad_code(rows, _):
    next(r for r in rows if r['exclusion_reason'])['exclusion_reason'] = 'E99'


def _bad_status(rows, _):
    next(r for r in rows if r['full_text_status'] == 'retrieved')['full_text_status'] = 'maybe'


def _bad_pooled(rows, _):
    rows[0]['included_in_pooled_estimate'] = 'yes'


MUTATIONS = [
    ('drop_extraction_row', 'the last extraction row is deleted', [ED], lambda r: edit_csv(r, ED, _drop_last)),
    ('drop_evidence_map_row', 'the last evidence-map row is deleted', [EM], lambda r: edit_csv(r, EM, _drop_last)),
    ('map_wrong_record', 'two studies swap their screening record ids in the extraction database', [ED], lambda r: edit_csv(r, ED, _map_wrong)),
    ('flip_include_to_exclude', 'one full-text include is switched to exclude', [FT], lambda r: edit_csv(r, FT, _flip_include)),
    ('drop_exclusion_log_row', 'the last exclusion-log row is deleted', [EL], lambda r: edit_csv(r, EL, _drop_last)),
    ('exclude_without_code', 'a full-text exclude loses its exclusion code', [FT], lambda r: edit_csv(r, FT, _exclude_without_code)),
    ('es_study_not_extracted', 'an effect-size row points to a study that is not extracted', [ES], lambda r: edit_csv(r, ES, _es_orphan)),
    ('es_value_changed', 'an effect estimate is changed to 999 (derived tables become stale)', [ES], lambda r: edit_csv(r, ES, _es_value)),
    ('duplicate_doi', 'two extraction rows get the same DOI', [ED], lambda r: edit_csv(r, ED, _dup_doi)),
    ('bad_year', 'a publication year becomes 302', [ED], lambda r: edit_csv(r, ED, _bad_year)),
    ('invalid_design_class', 'an evidence-map design class outside the enumeration', [EM], lambda r: edit_csv(r, EM, _blank_design)),
    ('invalid_boolean_field', 'a yes/no extraction field is set to "maybe"', [ED], lambda r: edit_csv(r, ED, _bad_boolean)),
    ('drop_map_row', 'the last study_record_map row is deleted', [MAP], lambda r: edit_csv(r, MAP, _drop_last)),
    ('country_changed', 'a study\'s country is changed to a non-country', [ED], lambda r: edit_csv(r, ED, _country)),
    ('appraisal_tool_changed', 'a JBI study is relabelled RoB 2 without any appraisal', [ED], lambda r: edit_csv(r, ED, _tool)),
    ('blank_citation', 'a study loses its citation text', [ED], lambda r: edit_csv(r, ED, _blank_citation)),
    ('include_with_exclusion_code', 'a full-text include carries an exclusion code', [FT], lambda r: edit_csv(r, FT, _include_with_reason)),
    ('decision_fields_disagree', 'final_decision and full_text_decision disagree on a record', [FT], lambda r: edit_csv(r, FT, _decision_disagree)),
    ('malformed_doi', 'an extraction DOI is not a DOI', [ED], lambda r: edit_csv(r, ED, _bad_doi)),
    ('exclusion_code_out_of_range', 'an exclusion code E99', [FT], lambda r: edit_csv(r, FT, _bad_code)),
    ('undocumented_status', 'a full_text_status value the data dictionary does not list', [FT], lambda r: edit_csv(r, FT, _bad_status)),
    ('pooled_flag_invalid', 'included_in_pooled_estimate set to yes', [ES], lambda r: edit_csv(r, ES, _bad_pooled)),
    ('stale_generated_file', 'a generated audit file is edited by hand', ['05_analysis/descriptive/EXCLUSION_BASIS_AUDIT_2026-10-04.md'],
     lambda r: (r / '05_analysis/descriptive/EXCLUSION_BASIS_AUDIT_2026-10-04.md').open('a', encoding='utf-8').write('\nhand edit\n')),
    ('tamper_readme_figure', 'the README extraction figure is changed', ['README.md'], lambda r: _readme_any(r)),
    ('remove_ai_disclosure_title', 'the "AI-Assisted" marker is removed from the README title', ['README.md'], lambda r: edit_text(r, 'README.md', 'AI-Assisted Systematic Review', 'Systematic Review')),
    ('remove_ai_use_statement', 'AI_USE_STATEMENT.md is deleted', ['AI_USE_STATEMENT.md'], lambda r: (r / 'AI_USE_STATEMENT.md').unlink()),
    ('unlisted_test_file', 'a new test file that regenerate_all.sh does not run', ['code/tests/test_zz_unlisted.py'], lambda r: (r / 'code/tests/test_zz_unlisted.py').write_text('"""x"""\n', encoding='utf-8')),
]


def _readme_any(root: Path):
    """Fallback tamper: change the first '<n> studies extracted' figure in the README."""
    import re
    p = root / 'README.md'
    t = p.read_text(encoding='utf-8')
    m = re.search(r'(\d{1,3}(?:,\d{3})*) studies extracted', t)
    assert m, 'no figure to tamper with'
    p.write_text(t[:m.start(1)] + '9,999' + t[m.end(1):], encoding='utf-8')


def run_verifier(project: Path):
    r = subprocess.run([sys.executable, str(project / 'code/analysis/verify_repository.py')], cwd=project, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip().splitlines()
    fails = [x.strip()[6:] for x in out if x.strip().startswith('FAIL:')]
    crashed = any('CRASH' in x or 'Traceback' in x for x in out)
    return r.returncode, fails, crashed, out[-6:]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--write', action='store_true', help='write 00_admin/VERIFIER_MUTATION_MAP_<date>.md')
    ap.add_argument('--only', nargs='*', help='run only these defect names')
    a = ap.parse_args(argv)
    todo = [m for m in MUTATIONS if not a.only or m[0] in a.only]
    unknown = set(a.only or []) - {m[0] for m in MUTATIONS}
    if unknown:
        print('unknown defect name(s):', sorted(unknown)); return 2
    results = []
    with tempfile.TemporaryDirectory() as d:
        proj = Path(d) / ROOT.name
        shutil.copytree(ROOT, proj, ignore=shutil.ignore_patterns('.git', '__pycache__', 'retrieval_results'))
        shutil.copy2(ROOT.parent / 'README.md', Path(d) / 'README.md')  # the verifier also checks the repository-root README
        rc, fails, _, tail = run_verifier(proj)
        print(f'baseline on the copy: rc={rc}, {len(fails)} failure(s)')
        if rc != 0:
            print('the verifier must pass on the untouched copy first:'); [print('  ', x) for x in (fails[:5] or tail)]
            return 2
        for name, desc, files, fn in todo:
            saved = {f: (proj / f).read_bytes() if (proj / f).exists() else None for f in files}  # restore exactly what the defect touches
            try:
                fn(proj)
                rc, fails, crashed, _ = run_verifier(proj)
                status = 'CAUGHT' if rc != 0 else 'UNCAUGHT'
                results.append((name, desc, status, len(fails), fails[0] if fails else '', crashed))
                print(f'{name:28} {status:9} {len(fails):3d} failing  {(fails[0] if fails else "")[:110]}')
            finally:
                for f, b in saved.items():
                    if b is None:
                        (proj / f).unlink(missing_ok=True)
                    else:
                        (proj / f).write_bytes(b)
    missed = [r for r in results if r[2] == 'UNCAUGHT']
    if a.write:
        p = ROOT / f'00_admin/VERIFIER_MUTATION_MAP_{datetime.date.today().isoformat()}.md'
        lines = [f'# Verifier mutation map ({datetime.date.today().isoformat()})', '',
                 'Produced by `python3 code/analysis/check_verifier_mutations.py --write`: one deliberate defect at a time is applied to a scratch copy of the project and `verify_repository.py` is run on it. "Failing" is the number of failed checks; "first message" is the check that said so. An UNCAUGHT row is a mistake the verifier would let through.', '',
                 '| Defect | What was done | Result | Failing | First message |', '|---|---|---|---|---|']
        for name, desc, status, n, first, crashed in results:
            lines.append(f'| `{name}` | {desc} | {status}{" (crash)" if crashed else ""} | {n} | {first[:140].replace("|", "/")} |')
        lines += ['', f'{len(results) - len(missed)} of {len(results)} defects caught.', '']
        p.write_text('\n'.join(lines), encoding='utf-8')
        print('wrote', p.relative_to(ROOT))
    print(f'{len(results) - len(missed)} of {len(results)} defects caught')
    return 1 if missed else 0


if __name__ == '__main__':
    sys.exit(main())
