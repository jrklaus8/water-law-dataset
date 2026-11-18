"""2026-10-14: write the PI's A25 and A5 rulings (reviewer CK) as a filled adjudication sheet, 02_screening/full_text/A25_ADJUDICATION_FILLED_2026-10-14.csv, in the layout apply_a16_adjudications.py reads.
25 rows: the 21 records of E05_RECHECK_21_RECORDS_2026-10-14.csv (14 excluded E05, S429 and S466 excluded E03, 5 kept) and the four A5 edge-case studies excluded E03 (S1056, S1065, S1079, S1084; none has an effect-size row or a linked report).
Run from legal-last-mile-systematic-review/."""
import csv, sys
csv.field_size_limit(sys.maxsize)
ED = '03_extraction/extracted_data/extraction_database.csv'
OUT = '02_screening/full_text/A25_ADJUDICATION_FILLED_2026-10-14.csv'
E05 = 'A25 ruling 2026-10-14 (criterion 3, as S340, S513 and S1117; exclusion criteria 1 and 6): '
E03A = 'A5 edge-case ruling 2026-10-14: no legal or administrative rule is tested (criterion 2, narrow scope), the same ground as Group 5 of A24 and Mkondiwa et al. 2013; '
K = 'A25 ruling 2026-10-14: kept as an include. '
ROWS = [
 ('S320', 'exclude', 'E05', E05 + 'narrative review of water kiosks with no primary access data and no stated search or selection.'),
 ('S326', 'exclude', 'E05', E05 + 'narrative survey of the evidence on utility ownership with no stated search, selection, protocol or appraisal.'),
 ('S436', 'exclude', 'E05', E05 + 'documental synthesis through the Community Capitals Framework, no primary data and no stated selection.'),
 ('S440', 'exclude', 'E05', E05 + 'narrative review of US drinking-water disparities, no primary data and no stated search.'),
 ('S482', 'exclude', 'E05', E05 + 'conceptual review, no primary data and no search.'),
 ('S236', 'exclude', 'E05', E05 + 'conceptual and observational essay with no stated method for its field observations.'),
 ('S260', 'exclude', 'E05', E05 + 'narrative documentary review of Nigeria SDG 6 progress, no document count, selection or appraisal.'),
 ('S203', 'exclude', 'E05', E05 + 'doctrinal legal-historical analysis with a SWOT and no data (exclusion criterion 1).'),
 ('S243', 'exclude', 'E05', E05 + 'NGO description of two community projects with self-reported results and no stated method.'),
 ('S246', 'exclude', 'E05', E05 + 'design-stage description of a governance model, no outcomes and no method.'),
 ('S079', 'exclude', 'E05', E05 + 'focus article synthesising literature, with no empirical data and no systematic method, although its topic is squarely in scope.'),
 ('S430', 'exclude', 'E05', E05 + 'critical review of national SDG 6 progress without a systematic flow or study-level synthesis.'),
 ('S479', 'exclude', 'E05', E05 + 'comparison of statutes across seven primacy agencies without empirical household access data.'),
 ('S199', 'exclude', 'E05', E05 + 'pure doctrinal analysis of Spanish regional laws, no access evidence (exclusion criterion 1).'),
 ('S429', 'exclude', 'E03', 'A25 ruling 2026-10-14: fails the narrow criterion 2 scope, as Aluko 2022 (E03): menstrual hygiene in prisons, where the barrier is supply and facilities for an incarcerated population and policy is only background. Not moved to AMSTAR 2.'),
 ('S466', 'exclude', 'E03', 'A25 ruling 2026-10-14: fails the narrow criterion 2 scope, as S348 and S969 (E03): macro-governance and climate-adaptation framing of SDG 6 in Nigeria, with over-regulation and tariff structure in one sentence. Not moved to AMSTAR 2.'),
 ('S1056', 'exclude', 'E03', E03A + 'social capital and caste in access to basic goods (informal collective action).'),
 ('S1065', 'exclude', 'E03', E03A + 'regional inequality of opportunity (Human Opportunity Index) in access.'),
 ('S1079', 'exclude', 'E03', E03A + 'broad socioeconomic and structural determinants of improved-water access.'),
 ('S1084', 'exclude', 'E03', E03A + 'broad socioeconomic and geographic determinants of household drinking-water access.'),
 ('S267', 'include', '', K + 'Eight purposively selected municipal cases analysed from audit and other documents; appraised under the Legal Institutional Evidence Appraisal Framework (design class doctrinal, unchanged).'),
 ('S335', 'include', '', K + 'Targeted review of 40 documents plus institutional data for Piura, Peru; moved from CASP to the Legal Institutional Evidence Appraisal Framework (A25 tool move).'),
 ('S181', 'include', '', K + 'Bayesian-network analysis of 101 countries; keeps its JBI Cross-Sectional appraisal (the proposed move to NONE is declined).'),
 ('S281', 'include', '', K + 'Systems-thinking model with six-expert elicitation; keeps its Legal Institutional Evidence Appraisal Framework appraisal.'),
 ('S288', 'include', '', K + 'Baghdad household survey (n = 300); moved from MMAT to JBI Cross-Sectional, where its weak reporting is recorded in the rating (A25 tool move).'),
]
ed = {r['study_id']: r for r in csv.DictReader(open(ED, newline='', encoding='utf-8'))}
with open(OUT, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow(['record_id', 'study_id', 'citation', 'ai_decision', 'researcher_decision (include/exclude)', 'researcher_exclusion_code (E01-E12)', 'researcher_comment'])
    for sid, dec, code, com in ROWS:
        e = ed[sid]
        w.writerow([e['record_id'], sid, e['citation'], 'include', dec, code, com])
print('wrote', OUT, len(ROWS), 'rows')
