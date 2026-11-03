import csv, tempfile, os

EM = '/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/descriptive/evidence_map.csv'

with open(EM) as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

new_rows = [
{
    'study_id': 'S536',
    'study_design_class': 'qualitative',
    'evidence_level': 'Transdisciplinary qualitative climate-risk-and-vulnerability case-study comparison (80+ interviews over 4 years in HaSinari; 8 interviews + observation in Prince Albert, 2018). CASP rating deferred pending the official instrument; provisional confidence: moderate -- long-term embedded fieldwork in HaSinari gives strong depth, but Prince Albert data collection was comparatively brief (2 days of fieldwork), and both case studies draw partly on prior/other researchers\' unpublished data.',
    'mechanism_family': 'MULTIPLE',
    'outcome_family': 'effective_access',
    'quantitative_synthesis_eligible': 'FALSE',
    'qualitative_synthesis_eligible': 'TRUE',
    'legal_context': 'common law (mixed, post-apartheid constitutional)',
    'institutional_context': 'Prince Albert\'s "leiwater" irrigation-furrow water allocation, managed by the Kweekvallei Irrigation Board, is restricted to residents holding allocation rights recorded in historical (Apartheid-era) title deeds, structurally excluding North-End residents; in HaSinari the formal municipal water department has ceased functioning in practice, and elected, fee-funded community Water Committees have taken over de facto water governance (residents wait ~2 weeks for intermittent taps).',
},
{
    'study_id': 'S537',
    'study_design_class': 'systematic_review_secondary',
    'evidence_level': 'PRISMA-ScR scoping review of 11 case studies (from 10,017 initial records) synthesizing sewer-connection behaviour-change interventions; quality-appraised via an adapted JBI checklist (6 high, 4 fair, 1 poor quality among included case studies). AMSTAR 2 rating of the review itself deferred pending the official instrument.',
    'mechanism_family': 'MULTIPLE',
    'outcome_family': 'effective_access',
    'quantitative_synthesis_eligible': 'FALSE',
    'qualitative_synthesis_eligible': 'TRUE',
    'legal_context': 'multiple (common law and civil law, 8 countries)',
    'institutional_context': 'Comparative synthesis across mandatory-connection legal provisions (e.g., Tamil Nadu\'s 100-meter connection mandate, Sao Paulo\'s 2002 municipal connection law, Salvador\'s Law 7307/1998), indirect financial subsidies (free connections), and penalty/legal-action provisions for non-connection; finds subsidy-plus-community-engagement packages outperform legal mandates or promotion alone.',
},
]

for nr in new_rows:
    row = {k: '' for k in fieldnames}
    row.update(nr)
    rows.append(row)

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EM))
with os.fdopen(fd, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp, EM)
print('done, total rows now', len(rows))
