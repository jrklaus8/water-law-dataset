#!/usr/bin/env python3
"""Score a filled second-extractor sheet: agreement of the AI extraction with an independent human, by field and overall.

Usage: python3 code/analysis/score_second_extractor_sheet.py path/to/filled_sheet.csv
Counts rows whose `agrees (Y/N/cannot_tell)` is Y or N (cannot_tell and blank are excluded and reported; yes/no and "can't tell" spellings are accepted; any other verdict, and a filled value with a blank verdict, is flagged as a warning and not scored; exit code 2 if a verdict is invalid). Reports disagreement rate with a Wilson 95% interval.
With ~60 studies the interval for any one field is wide (about +/-10 points); read the overall figure, not single fields.
"""
import csv, math, sys
from collections import Counter, defaultdict


def wilson(k, n, z=1.96):
    if n == 0:
        return (float('nan'),) * 2
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (c - h) / d, (c + h) / d


VERDICT = 'agrees (Y/N/cannot_tell)'
VALID = {'Y', 'N', 'CANNOT_TELL', ''}
SYNONYMS = {'YES': 'Y', 'NO': 'N', 'CANNOTTELL': 'CANNOT_TELL', "CAN'T_TELL": 'CANNOT_TELL', 'CANT_TELL': 'CANNOT_TELL', 'UNCLEAR': 'CANNOT_TELL'}  # what a person types into the column


def verdict_of(r):
    """Normalise a verdict cell: case, spaces, and the obvious spellings (yes/no/can't tell). Anything else is returned as typed and flagged by score()."""
    v = (r[VERDICT] or '').strip().upper().replace(' ', '_')
    return SYNONYMS.get(v, v)


def score(rows):
    """Return a dict of the scoring results (see main for how they are printed). Pure function of the sheet rows, so it can be tested."""
    tot, bad, skipped = Counter(), Counter(), Counter()
    st_tot, st_bad = Counter(), Counter()
    per_study = defaultdict(int)
    invalid, filled_unjudged = [], []
    for i, r in enumerate(rows, start=2):  # row 1 is the header
        v = verdict_of(r)
        r = {**r, 'study_id': (r['study_id'] or '').strip()}
        if v not in VALID:
            invalid.append((i, r['study_id'], r['field'], r[VERDICT]))
        if v not in ('Y', 'N'):
            skipped[r['field']] += 1
            if v == '' and (r.get('second_extractor_value') or '').strip():
                filled_unjudged.append((i, r['study_id'], r['field']))
            continue
        tot[r['field']] += 1; st_tot[r.get('stratum', '')] += 1
        if v == 'N':
            bad[r['field']] += 1; st_bad[r.get('stratum', '')] += 1
            per_study[r['study_id']] += 1
    return dict(tot=tot, bad=bad, skipped=skipped, st_tot=st_tot, st_bad=st_bad, per_study=per_study, invalid=invalid, filled_unjudged=filled_unjudged,
                n_studies=len({r['study_id'] for r in rows}))


def read_rows(path):
    """Read a filled sheet tolerantly (UTF-8 with or without BOM, else Windows-1252; ',' or ';' delimiter; padded headers), as a spreadsheet program may save it."""
    raw = __import__('pathlib').Path(path).read_bytes()
    try:
        text = raw.decode('utf-8-sig')
    except UnicodeDecodeError:
        text = raw.decode('cp1252')
    first = text.split('\n', 1)[0]
    rd = csv.DictReader(text.splitlines(), delimiter=';' if first.count(';') > first.count(',') else ',')
    rd.fieldnames = [(h or '').strip() for h in (rd.fieldnames or [])]
    missing = [c for c in ('study_id', 'field', VERDICT) if c not in rd.fieldnames]
    if missing:
        raise SystemExit(f'the sheet lacks the column(s) {missing}; keep the original header row')
    return [{k: (v or '') for k, v in r.items() if k is not None} for r in rd if (r.get('study_id') or '').strip()]


def coverage_note():
    """One line on what the sample can and cannot speak for: it is drawn from S001-S200 only, which skews recent (checked against the whole corpus)."""
    try:
        sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
        import current_figures as cf
        ed = cf.read('ed')
        yr = lambda rows: [int(r['publication_year']) for r in rows if r['publication_year'].strip().isdigit()]
        a, b = yr([r for r in ed if int(r['study_id'][1:]) <= 200]), yr(ed)
        return (f"NOTE: the sample was drawn from S001-S200 only ({100 * sum(y >= 2020 for y in a) / len(a):.0f}% published 2020 or later, against "
                f"{100 * sum(y >= 2020 for y in b) / len(b):.0f}% of all {len(ed):,} extracted studies). The disagreement rate describes the AI's extraction of those 200 studies; "
                "applying it to the later batches (S201-S1164) is an assumption, not a measurement.")
    except Exception:  # pragma: no cover - the note is advisory; never block scoring
        return ''


def main(path):
    rows = read_rows(path)
    R = score(rows)
    tot, bad = R['tot'], R['bad']
    if R['invalid']:
        print(f"WARNING: {len(R['invalid'])} rows have a verdict that is not Y, N or cannot_tell and were NOT scored (sheet row, study, field, value):")
        for x in R['invalid'][:20]:
            print('   ', x)
    if R['filled_unjudged']:
        print(f"WARNING: {len(R['filled_unjudged'])} rows have a second-extractor value but a blank verdict and were NOT scored (e.g. sheet row {R['filled_unjudged'][0][0]}, {R['filled_unjudged'][0][1]} {R['filled_unjudged'][0][2]}).")
    print(f"{'field':22} {'n':>4} {'disagree':>8} {'rate':>6}   95% CI")
    for f in list(tot):
        lo, hi = wilson(bad[f], tot[f])
        print(f"{f:22} {tot[f]:4d} {bad[f]:8d} {100 * bad[f] / tot[f]:5.1f}%   {100 * lo:.0f}-{100 * hi:.0f}%")
    n, k = sum(tot.values()), sum(bad.values())
    if n:
        lo, hi = wilson(k, n)
        print(f"{'ALL FIELDS':22} {n:4d} {k:8d} {100 * k / n:5.1f}%   {100 * lo:.0f}-{100 * hi:.0f}%  (fields are not independent within a study)")
    if len(R['st_tot']) > 1:
        print('\nby stratum (the sample was stratified by appraisal tool or extraction type; small cells are noisy):')
        for st in sorted(R['st_tot']):
            print(f"  {st:28} {R['st_tot'][st]:4d} {R['st_bad'][st]:8d} {100 * R['st_bad'][st] / R['st_tot'][st]:5.1f}%")
    print(f"studies with at least one disagreement: {len(R['per_study'])} of {R['n_studies']}; rows skipped (blank or cannot_tell): {sum(R['skipped'].values())}")
    note = coverage_note()
    if note:
        print('\n' + note)
    return 2 if R['invalid'] else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
