#!/usr/bin/env python3
"""Apply the researcher's A16 adjudications from a filled copy of 02_screening/full_text/A16_ADJUDICATION_SHEET_2026-10-04.csv.

DRY RUN BY DEFAULT: prints what would change and writes nothing. Pass --apply to write.

What it does, per row whose `researcher_decision (include/exclude)` is filled:
- The researcher CONFIRMS the AI's decision (same include/exclude): the record's notes get a dated adjudication note; if the researcher gives a
  different exclusion code for a confirmed exclude, `exclusion_reason` in the full-text database and `exclusion_code` in the exclusion log are both
  changed (the detail text is prefixed with the adjudication). `final_decision` and every count stay as they are.
- The researcher REVERSES the AI's decision (exclude -> include, or include -> exclude): the decision fields are NOT touched, because an include must
  map one-to-one to an extraction row and a study_record_map entry (verify_repository.py). The record's notes get a dated "pending" note and the row
  is added to 02_screening/full_text/A16_PENDING_REVERSALS.csv. A later dated script turns each pending reversal into a real inclusion (new study ID,
  extraction, appraisal, map entry, exclusion-log row removed) or exclusion (retired study ID, exclusion-log row added), as resolve_s356_exclude_2026-09-28.py
  did for S356; only then do the counts change.
Blank rows are skipped. Invalid values (decision not include/exclude, exclusion code missing or not E01-E12 for an exclude) stop the run before anything
is written. Re-running is safe: rows already carrying this script's note are skipped.

Usage (from legal-last-mile-systematic-review/):
  python3 code/screening/apply_a16_adjudications.py FILLED.csv --reviewer "Initials"            # dry run
  python3 code/screening/apply_a16_adjudications.py FILLED.csv --reviewer "Initials" --apply    # write
Then: bash code/analysis/regenerate_all.sh  (the verifier must pass), and add a dated CHANGELOG entry.
"""
from __future__ import annotations

import argparse
import csv
import datetime
import os
import sys
import tempfile
from pathlib import Path

csv.field_size_limit(sys.maxsize)
CODES = {f'E{i:02d}' for i in range(1, 13)}
MARK = 'A16 adjudication'
DEC_COL, CODE_COL, COMMENT_COL = 'researcher_decision (include/exclude)', 'researcher_exclusion_code (E01-E12)', 'researcher_comment'


def _read(path: Path):
    raw = path.read_bytes().decode('utf-8')
    with open(path, encoding='utf-8', newline='') as f:
        rd = csv.DictReader(f)
        return rd.fieldnames, list(rd), ('\r\n' if raw.split('\n', 1)[0].endswith('\r') else '\n')


def _write(path: Path, fields, rows, eol):
    fd, tmp = tempfile.mkstemp(dir=path.parent, suffix='.tmp')
    with os.fdopen(fd, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator=eol); w.writeheader(); w.writerows(rows)
    os.replace(tmp, path)


def norm_code(raw: str) -> str:
    """'e3', 'E3', 'E03 - wrong design' and ' e03 ' all mean E03; anything else is returned upper-cased so plan() can reject it."""
    import re
    m = re.match(r'\s*E\s*0*(\d{1,2})\b', raw or '', re.I)
    return f'E{int(m.group(1)):02d}' if m else (raw or '').strip().upper()


def read_sheet(path: Path):
    """Read the researcher's filled sheet tolerantly: a spreadsheet program may save it with a UTF-8 BOM or in Windows-1252, with ';' as the
    delimiter (European locales), with stray spaces in headers or record ids, or with blank trailing rows. Raises ValueError if the required columns are missing."""
    raw = path.read_bytes()
    try:
        text = raw.decode('utf-8-sig')
    except UnicodeDecodeError:
        text = raw.decode('cp1252')
    first = text.split('\n', 1)[0]
    delim = ';' if first.count(';') > first.count(',') else ','
    rd = csv.DictReader(text.splitlines(), delimiter=delim)
    rd.fieldnames = [(h or '').strip() for h in (rd.fieldnames or [])]
    missing = [c for c in ('record_id', DEC_COL, CODE_COL) if c not in rd.fieldnames]
    if missing:
        raise ValueError(f'the sheet lacks the column(s) {missing}; keep the original header row of the A16 sheet')
    rows = []
    for r in rd:
        r = {k: (v or '').strip() if isinstance(v, str) or v is None else v for k, v in r.items() if k is not None}
        if r.get('record_id'):
            r['record_id'] = r['record_id'].upper()
            rows.append(r)
    return rows


def plan(sheet_rows, ft_by_id):
    """Validate the filled sheet and return (actions, errors). Each action: (kind, record_id, sheet_row)."""
    actions, errors, seen = [], [], set()
    for r in sheet_rows:
        dec = (r.get(DEC_COL) or '').strip().lower()
        if not dec:
            continue
        rid = r['record_id']
        if rid in seen:
            errors.append(f'{rid}: appears with a decision on more than one row of the sheet'); continue
        seen.add(rid)
        code = norm_code(r.get(CODE_COL))
        if dec not in ('include', 'exclude'):
            errors.append(f'{rid}: decision must be include or exclude, got {dec!r}'); continue
        if dec == 'exclude' and code not in CODES:
            errors.append(f'{rid}: an exclude needs an exclusion code E01-E12, got {code!r}'); continue
        if rid not in ft_by_id:
            errors.append(f'{rid}: not in the full-text screening database'); continue
        ft = ft_by_id[rid]
        if MARK in ft['notes']:
            actions.append(('already', rid, r)); continue
        ai = ft['final_decision'] or ft['full_text_decision']
        if dec == ai:
            actions.append(('confirm_recode' if dec == 'exclude' and code != ft['exclusion_reason'] else 'confirm', rid, r))
        else:
            actions.append(('reverse', rid, r))
    return actions, errors


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('filled_sheet', type=Path)
    ap.add_argument('--reviewer', required=True, help='who adjudicated (initials or name); recorded in the notes')
    ap.add_argument('--apply', action='store_true', help='write the changes (default: dry run)')
    ap.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2], help='project root (for testing on a copy)')
    a = ap.parse_args(argv)
    root = a.root
    FT = root / '02_screening/full_text/full_text_screening_database.csv'
    EL = root / '02_screening/exclusion_log/exclusion_log.csv'
    PEND = root / '02_screening/full_text/A16_PENDING_REVERSALS.csv'
    today = datetime.date.today().isoformat()

    try:
        sheet = read_sheet(a.filled_sheet)
    except ValueError as e:
        print(f'Nothing written: {e}'); return 2
    ft_fields, ft, ft_eol = _read(FT)
    el_fields, el, el_eol = _read(EL)
    ft_by_id = {r['record_id']: r for r in ft}
    el_by_id = {r['record_id']: r for r in el}
    actions, errors = plan(sheet, ft_by_id)
    if errors:
        print('Nothing written; fix these rows first:'); [print('  ' + e) for e in errors]
        return 2
    n_ft, n_el = len(ft), len(el)
    pending = []
    for kind, rid, r in actions:
        row = ft_by_id[rid]
        dec = r[DEC_COL].strip().lower(); code = norm_code(r.get(CODE_COL)); comment = (r.get(COMMENT_COL) or '').strip()
        if kind == 'already':
            print(f'skip     {rid}: already adjudicated'); continue
        note = f'{MARK} {today} by {a.reviewer}: '
        if kind == 'confirm':
            note += f'confirms {dec}' + (f' ({code})' if code else '') + (f'; {comment}' if comment else '')
            print(f'confirm  {rid}: {dec}' + (f' {code}' if code else ''))
        elif kind == 'confirm_recode':
            old = row['exclusion_reason']
            note += f'confirms exclude, code {old} -> {code}' + (f'; {comment}' if comment else '')
            print(f'recode   {rid}: exclude {old} -> {code}')
            row['exclusion_reason'] = code
            row['exclusion_reason_detail'] = f'[{MARK} {today}: code changed {old} -> {code}] ' + row['exclusion_reason_detail']
            if rid in el_by_id:
                el_by_id[rid]['exclusion_code'] = code
                el_by_id[rid]['exclusion_reason_detail'] = row['exclusion_reason_detail']
        else:
            ai = row['final_decision'] or row['full_text_decision']
            note += f'REVERSES the AI {ai} -> {dec}' + (f' ({code})' if code else '') + ' -- pending: decision fields unchanged until a dated script processes A16_PENDING_REVERSALS.csv' + (f'; {comment}' if comment else '')
            print(f'REVERSE  {rid}: {ai} -> {dec}' + (f' {code}' if code else '') + '  (queued, decision fields unchanged)')
            pending.append({'record_id': rid, 'title': row['title'], 'ai_decision': ai, 'researcher_decision': dec, 'researcher_exclusion_code': code,
                            'researcher_comment': comment, 'adjudicated_by': a.reviewer, 'date': today,
                            'next_step': 'new inclusion: assign study ID, extract, appraise, add study_record_map row, remove exclusion-log row' if dec == 'include'
                            else 'new exclusion: retire study ID in study_record_map, remove extraction/evidence-map rows, add exclusion-log row'})
        row['notes'] = (row['notes'] + ' | ' if row['notes'] else '') + note
    counts = {k: sum(1 for x in actions if x[0] == k) for k in ('confirm', 'confirm_recode', 'reverse', 'already')}
    print(f"\n{counts['confirm']} confirmed, {counts['confirm_recode']} confirmed with a new code, {counts['reverse']} reversals queued, {counts['already']} already done.")
    if not a.apply:
        print('DRY RUN: nothing written. Re-run with --apply to write.')
        return 0
    assert len(ft) == n_ft and len(el) == n_el
    _write(FT, ft_fields, ft, ft_eol)
    _write(EL, el_fields, el, el_eol)
    if pending:
        fields = list(pending[0].keys())
        old = _read(PEND)[1] if PEND.exists() else []
        _write(PEND, fields, old + pending, '\n')
    print('Written. Now run: bash code/analysis/regenerate_all.sh, and add a dated CHANGELOG entry.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
