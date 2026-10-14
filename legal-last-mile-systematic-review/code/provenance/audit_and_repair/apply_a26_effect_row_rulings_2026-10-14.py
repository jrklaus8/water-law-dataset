"""2026-10-14, open item A26 (PI rulings, reviewer CK): the effect_sizes.csv side of the rulings. Run BEFORE resolve_a16_pending_reversals.py, which refuses to retire a study that still has an effect row.

1. S358 (Williams et al. 2025; Family A), S590 (Brown 1989; Family C) and S606 (Zhou & Liang 2021; Family C) move to the reasoned non-fits: `synthesis_family` becomes blank, the pooling reason says why (the S331 form), and the
   provenance note records the ruling. Their outcomes are groundwater decline and contamination at service-area level, a city's decision to build waterworks, and back-end treatment capacity per capita; none is household access.
2. S1121 (Hanak 2008; Family A) and S1143 (Jones et al. 1978; Family C) leave the review (E04 and E07, applied with apply_a16_adjudications.py and resolve_a16_pending_reversals.py from the A26 sheet): their effect rows and their
   FULLTEXT_VERIFICATION rows are archived to 11_archive/effect_sizes_removed_2026-10-13.csv and 11_archive/fulltext_verification_removed_2026-10-13.csv (the rows of S312, S435, S348 and S969 stay there).
3. S1038 (Bruggink 1985): `exposure_definition` and `comparator_definition` are swapped so that the exposure is state PUC regulation and the comparator local-only regulation, which is the contrast the reported estimate
   (state-regulated minus locally regulated welfare loss, -4.6 percentage points) and the `direction` text already use. The pole mismatch flag is removed from the coding file by build_swim_direction_coding_2026-10-14.py.
Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
ES = '05_analysis/effect_sizes/effect_sizes.csv'
VF = '05_analysis/effect_sizes/FULLTEXT_VERIFICATION_2026-10-04.csv'
ARCH_ES = '11_archive/effect_sizes_removed_2026-10-13.csv'
ARCH_VF = '11_archive/fulltext_verification_removed_2026-10-13.csv'
MARK = 'A26 ruling 2026-10-14 by CK'
NONFIT = {
    'S358': ('A', 'the outcome is groundwater decline and contamination risk at the level of 1,881 groundwater-supplied service areas (aquifer availability), not household connection, access or service quality, so it does not match Family A, B or C. '
                  'It is a single study with this exposure (Tribal oversight against state primacy) and this outcome, so pooling is not possible.'),
    'S590': ('C', 'the outcome is whether a 19th-century Prussian city decided to build waterworks (municipal capital investment; SKEW coefficient 0.457), not household connection, access or service quality, so it does not match Family A, B or C. '
                  'It is a single study with this exposure (the franchise structure) and this outcome, so pooling is not possible.'),
    'S606': ('C', 'the outcome is wastewater (and solid-waste) treatment capacity per capita, back-end plant capacity rather than household connection or access, so it does not match Family A, B or C. '
                  'It is a single study with this exposure (the share of hukou-unregistered residents) and this outcome, so pooling is not possible.'),
}
REMOVE = ('S1121', 'S1143')
S1038_EXPOSURE = ('Residential customers of a municipally-owned water utility subject to state public utility commission (PUC) economic regulation (in the five U.S. states that regulated municipal water rate structures at the state level), '
                  'United States, 1965 AWWA survey data.')
S1038_COMPARATOR = 'Residential customers of a municipally-owned water utility subject to local-only economic regulation (regulated by city council or water commission, not by a state public utility commission).'


def read(p):
    raw = open(p, newline='', encoding='utf-8').read()
    with open(p, newline='', encoding='utf-8') as f:
        rd = csv.DictReader(f)
        return rd.fieldnames, list(rd), '\r\n' if '\r\n' in raw[:5000] else '\n'


def write(p, fields, rows, eol):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(p) or '.', suffix='.tmp')
    with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator=eol)
        w.writeheader(); w.writerows(rows)
    os.replace(tmp, p)


fields, rows, eol = read(ES)
by = {r['study_id']: r for r in rows}
changed = []
for s, (fam, why) in NONFIT.items():
    r = by[s]
    if MARK in r['provenance_note']:
        continue
    assert r['synthesis_family'] == fam, (s, r['synthesis_family'])
    r['synthesis_family'] = ''
    r['exclusion_from_pooling_reason'] = f'ANALYSIS_PLAN.md section 2 decision tree and PROJECT_SPEC.md section 8: reasoned non-fit, no family assigned ({MARK}, formerly Family {fam}): {why}'
    r['provenance_note'] = (r['provenance_note'].rstrip() + f' {MARK}: moved from Family {fam} to the reasoned non-fits; ' + why.split(', so it does not')[0] + '.').strip()
    changed.append(s)
r = by['S1038']
if MARK not in r['provenance_note']:
    assert r['exposure_definition'].startswith('Residential customers of a municipally-owned water utility subject to local-only')
    r['exposure_definition'], r['comparator_definition'] = S1038_EXPOSURE, S1038_COMPARATOR
    r['provenance_note'] = (r['provenance_note'].rstrip() + f' {MARK}: exposure and comparator swapped (state PUC regulation is now the exposure) so that the definitions match the reported contrast, state-regulated minus locally regulated welfare loss (-4.6 percentage points), and the direction text.').strip()
    changed.append('S1038')
os.makedirs('11_archive', exist_ok=True)
for src, arch in ((ES, ARCH_ES), (VF, ARCH_VF)):
    f2, rs, e2 = (fields, rows, eol) if src == ES else read(src)
    out = [x for x in rs if x['study_id'] in REMOVE]
    if not out:
        continue
    assert {x['study_id'] for x in out} == set(REMOVE), (src, [x['study_id'] for x in out])
    keep = [x for x in rs if x['study_id'] not in REMOVE]
    af, ar, ae = read(arch)
    assert af == f2, (arch, af, f2)
    write(arch, af, [x for x in ar if x['study_id'] not in REMOVE] + out, ae)
    if src == ES:
        rows = keep
    else:
        write(src, f2, keep, e2)
    changed.append(f'{src}: removed {REMOVE}')
write(ES, fields, rows, eol)
print('changed:', changed if changed else 'nothing (already applied)')
from collections import Counter
print(Counter(r['synthesis_family'] or 'non-fit' for r in rows), len(rows))
