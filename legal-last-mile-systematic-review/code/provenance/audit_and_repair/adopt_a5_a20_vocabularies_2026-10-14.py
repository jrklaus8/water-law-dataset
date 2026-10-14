"""2026-10-14: adopt the controlled vocabularies in evidence_map.csv (PI rulings on open items A5 and A20).

A20 (option a): the keyword mapping of the free-text `study_design_class` labels onto the 8-value enum (propose_design_vocabulary.py) is accepted for every study the rules could map; the studies labelled
`unmapped_needs_review` keep their free-text label.
A5: the single-label `mechanism_family_proposed` (nine families + `multiple`) and `outcome_family_proposed` (four families + `multiple`) from propose_family_vocabulary.py replace the free-text labels, with the
AI resolutions of the flagged rows in 05_analysis/descriptive/family_vocabulary_overrides_2026-10-14.csv; the studies still `unmapped_needs_review` are the genuine edge cases.
Before anything changes, the original strings are saved to 05_analysis/descriptive/evidence_map_original_labels_2026-10-14.csv (study_id, study_design_class_original, mechanism_family_original,
outcome_family_original); both generators read the originals from there, so their output stays reproducible. Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
from collections import Counter
csv.field_size_limit(sys.maxsize)
sys.path.insert(0, 'code/analysis')
import current_figures as cf  # noqa: E402

EM = '05_analysis/descriptive/evidence_map.csv'
raw = open(EM, newline='', encoding='utf-8').read(); eol = '\r\n' if '\r\n' in raw[:5000] else '\n'
with open(EM, newline='', encoding='utf-8') as f:
    rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
if not cf.ORIGINAL_LABELS.exists():
    with open(cf.ORIGINAL_LABELS, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, lineterminator='\n')
        w.writerow(['study_id', 'study_design_class_original', 'mechanism_family_original', 'outcome_family_original'])
        for r in rows:
            w.writerow([r['study_id'], r['study_design_class'], r['mechanism_family'], r['outcome_family']])
    print(f'saved the original labels of {len(rows)} studies to {cf.ORIGINAL_LABELS.name}')
import propose_design_vocabulary as dv  # noqa: E402
import propose_family_vocabulary as pv  # noqa: E402
design = {r['study_id']: r['proposed_class'] for r in dv.build()}
fam = {r['study_id']: r for r in pv.build()}
changed = Counter()
for r in rows:
    sid = r['study_id']
    if sid in design and design[sid] != 'unmapped_needs_review' and r['study_design_class'] != design[sid]:
        r['study_design_class'] = design[sid]; changed['design'] += 1
    m, o = fam[sid]['mechanism_family_proposed'], fam[sid]['outcome_family_proposed']
    if r['mechanism_family'] != m:
        r['mechanism_family'] = m; changed['mechanism'] += 1
    if r['outcome_family'] != o:
        r['outcome_family'] = o; changed['outcome'] += 1
if changed:
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EM), suffix='.tmp')
    with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator=eol); w.writeheader(); w.writerows(rows)
    os.replace(tmp, EM)
ENUM = dv.ENUM
print('fields changed:', dict(changed))
print('design class values:', dict(cf.ranked(Counter(r['study_design_class'] if r['study_design_class'] in ENUM else 'free text' for r in rows))))
print('mechanism values:', dict(cf.ranked(Counter(r['mechanism_family'] for r in rows))))
print('outcome values:', dict(cf.ranked(Counter(r['outcome_family'] for r in rows))))
assert all(r['mechanism_family'] in pv.CONTROLLED_MECH for r in rows) and all(r['outcome_family'] in pv.CONTROLLED_OUT for r in rows)
