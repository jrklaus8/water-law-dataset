"""2026-10-14: write the PI's A20-residue rulings (reviewer CK) as a filled adjudication sheet, 02_screening/full_text/A20_RESIDUE_ADJUDICATION_FILLED_2026-10-14.csv, in the layout apply_a16_adjudications.py reads.
Four studies are excluded E05 (S707, S976, S1077, S1098: policy or legal reviews and essays with no primary access data and no systematic method; none has an effect-size row, a linked report or a place in the
second-extractor sample) and six are confirmed as includes (S791, S799, S949, S1092, S937, S1071; their design classes are set by design_class_overrides_2026-10-14.csv). Run from legal-last-mile-systematic-review/."""
import csv, sys
csv.field_size_limit(sys.maxsize)
ED = '03_extraction/extracted_data/extraction_database.csv'
OUT = '02_screening/full_text/A20_RESIDUE_ADJUDICATION_FILLED_2026-10-14.csv'
E05 = 'A20 residue ruling 2026-10-14 (criterion 3, as the A25 E05 rulings and S340, S513, S1117): '
K = 'A20 residue ruling 2026-10-14: kept as an include. '
ROWS = [
 ('S707', 'exclude', 'E05', E05 + 'national policy review (urban sanitation in India), no primary access data and no systematic method.'),
 ('S976', 'exclude', 'E05', E05 + 'policy and legal review of domestic rainwater harvesting, no primary sample and no systematic method.'),
 ('S1077', 'exclude', 'E05', E05 + 'critical policy-analysis essay, no primary data and no systematic method.'),
 ('S1098', 'exclude', 'E05', E05 + 'policy-reform analysis of municipal water pricing, no data.'),
 ('S791', 'include', '', K + 'Cross-national analysis of GLAAS survey rounds; design class observational.'),
 ('S799', 'include', '', K + 'Policy-document analysis with descriptive water-quality sampling; design class mixed_methods.'),
 ('S949', 'include', '', K + 'Delphi expert consensus with legal-reform analysis; design class qualitative.'),
 ('S1092', 'include', '', K + 'Policy analysis with a survey of 260 urban centres; design class observational.'),
 ('S937', 'include', '', K + 'Ex-ante regulatory impact assessment (MCDA); design class other.'),
 ('S1071', 'include', '', K + 'Game-theoretic model with empirical evidence; design class other.'),
]
ed = {r['study_id']: r for r in csv.DictReader(open(ED, newline='', encoding='utf-8'))}
with open(OUT, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow(['record_id', 'study_id', 'citation', 'ai_decision', 'researcher_decision (include/exclude)', 'researcher_exclusion_code (E01-E12)', 'researcher_comment'])
    for sid, dec, code, com in ROWS:
        e = ed[sid]
        w.writerow([e['record_id'], sid, e['citation'], 'include', dec, code, com])
print('wrote', OUT, len(ROWS), 'rows')
