"""2026-10-14, open item A29 (PI ruling, reviewer CK): S1140 (Shrestha 2013, Family B) and S1136 (Ban, Das Gupta & Rao 2010, Family C) move to the reasoned non-fits.

The ruling (the author's own words, 2026-10-14): keeping studies without a household water or sanitation access outcome inside the primary SWiM families weakens the discipline of eligibility criterion 4, so both
move to the reasoned non-fits in effect_sizes.csv, matching S358, S590, S606 and S331. Reasoned non-fits go from 19 to 21 and the families from 39 to 37 studies (A 16, B 5, C 16). The sensitivity scenario that
dropped the two (S4b) is retired, because the primary count now excludes them.

What this script changes, and only this:
1. effect_sizes.csv: `synthesis_family` becomes blank for both, `exclusion_from_pooling_reason` gives the reason (the S331 form), and `provenance_note` records the ruling. The effect estimates themselves are not touched.
2. full_text_screening_database.csv: a dated note is appended to the two studies' rows. Their inclusion decisions are unchanged (both stay included studies, with their extraction, appraisal and evidence-map rows).
   The earlier A26 note on these two rows (the author kept them in their families) is superseded as to the families; no reviewer or decision field is touched, and this ruling is not added to HUMAN_RULING_MARKS
   (the rows already carry the A26 mark, so the count of human-verified decisions does not change).
Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
ES = '05_analysis/effect_sizes/effect_sizes.csv'
FT = '02_screening/full_text/full_text_screening_database.csv'
MARK = 'A29 ruling 2026-10-14 by CK'
NONFIT = {
    'S1140': ('B', 'R102EBEF65059',
              'the outcome is whether a village community in Nepal secured Rural Water Supply and Sanitation Program (RWSSP) infrastructure funding (the log odds of funding success rise by 0.55 with each organisational partner), '
              'a community-level application outcome, not household connection, access or service quality, so it does not match Family A, B or C. '
              'It is a single study with this exposure (self-organised network capital) and this outcome, so pooling is not possible.'),
    'S1136': ('C', 'R111EFC29F4F6',
              'the outcome is the state of village roads (paved road, drain, cleanliness and garbage across 10,408 roads in South India), road-level public sanitation infrastructure, not household connection, access or service quality, '
              'so it does not match Family A, B or C. It is a single study with this exposure (political capture of a mandated local-government function) and this outcome, so pooling is not possible.'),
}


def read(p):
    raw = open(p, newline='', encoding='utf-8').read()
    with open(p, newline='', encoding='utf-8') as f:
        rd = csv.DictReader(f)
        return rd.fieldnames, list(rd), '\r\n' if '\r\n' in raw[:20000] else '\n'


def write(p, fields, rows, eol):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(p) or '.', suffix='.tmp')
    with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator=eol)
        w.writeheader(); w.writerows(rows)
    os.replace(tmp, p)


fields, rows, eol = read(ES)
by = {r['study_id']: r for r in rows}
changed = []
for s, (fam, rec, why) in NONFIT.items():
    r = by[s]
    if MARK in r['provenance_note']:
        continue
    assert r['synthesis_family'] == fam, (s, r['synthesis_family'])
    r['synthesis_family'] = ''
    r['exclusion_from_pooling_reason'] = f'ANALYSIS_PLAN.md section 2 decision tree and PROJECT_SPEC.md section 8: reasoned non-fit, no family assigned ({MARK}, formerly Family {fam}): {why}'
    r['provenance_note'] = (r['provenance_note'].rstrip() + f' {MARK}: moved from Family {fam} to the reasoned non-fits; ' + why.split(', so it does not')[0] + '.').strip()
    changed.append(s)
write(ES, fields, rows, eol)
ff, ft, fe = read(FT)
fb = {r['record_id']: r for r in ft}
for s, (fam, rec, why) in NONFIT.items():
    r = fb[rec]
    assert r['final_decision'] == 'include', s
    if MARK in r['notes']:
        continue
    r['notes'] = (r['notes'].rstrip() + f' | {MARK}: the effect row moved from Family {fam} to the reasoned non-fits because the outcome is not a household water or sanitation access outcome (criterion 4); '
                  f'the inclusion decision is unchanged and the two-column direction coding no longer applies.').strip(' |')
    changed.append(f'{s} note')
write(FT, ff, ft, fe)
from collections import Counter
print('changed:', changed if changed else 'nothing (already applied)')
print(Counter(r['synthesis_family'] or 'non-fit' for r in rows), len(rows))
