"""2026-09-29: S277 (Beltran Aldaco, Pena Joya, Tellez Lopez & Canales Gomez 2026, 'Economia del agua y su asequibilidad para el derecho de acceso en Puerto Vallarta',
Dilemas contemporaneos 13(3), art. 79; record R77BFC4654E8A) re-extracted from the full-text PDF supplied by the researcher (24 pp, Spanish; PDF not committed;
text extractor used, figures/charts as images were not read -- values quoted come from the running text and tables).

Fills the fields left blank by the abstract-only extraction, re-answers the MMAT criteria on the full text, adds flags the text supports (eligibility,
hardship_exception, service_continuity), and removes S277 from the abstract-only set (67 -> 66).
Deliberately NOT changed: evidence_map quantitative_synthesis_eligible (TRUE). The full text reports only descriptive percentages and contingency tables with no effect
estimate or test statistic, which makes the flag look overstated, but the flag is a Phase 11 feasibility judgment (EVIDENCE_MAP_README: never derived) -- recorded in
DECISIONS_AND_OPEN_ITEMS.md for the researcher. effect_sizes.csv: no row. Run from legal-last-mile-systematic-review/. Asserts row counts; atomic rewrite; preserves line endings."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
ED = '03_extraction/extracted_data/extraction_database.csv'
EM = '05_analysis/descriptive/evidence_map.csv'
AB = '05_analysis/sensitivity/abstract_only_extractions_2026-09-28.csv'
SID = 'S277'


def rw(path, fn, before, after):
    raw = open(path, newline='').read(); crlf = '\r\n' in raw[:5000]
    with open(path, newline='') as f:
        rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
    assert len(rows) == before, (path, len(rows))
    rows = fn(rows)
    assert len(rows) == after, (path, len(rows))
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), suffix='.tmp')
    with os.fdopen(fd, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n' if crlf else '\n'); w.writeheader(); w.writerows(rows)
    os.replace(tmp, path)


UPD = {
    'subnational_unit': 'Puerto Vallarta, Jalisco (urban area; Lerma-Santiago-Pacifico hydrological-administrative region VIII; population 291,839 in 2020, tourism 51.5% of economic activity)',
    'population': 'users of the municipal utility SEAPAL-VALLARTA in Puerto Vallarta: domestic, residential-domestic, commercial and industrial users (D.C.I.) and hotel users; finite population of 88,686 users',
    'sample_size': 'two stratified random samples from a finite population of 88,686 SEAPAL-VALLARTA users: 364 D.C.I. users (survey points chosen randomly by QGIS across neighbourhoods) and 100 hotel users (from a utility-supplied list); 464 total',
    'eligibility': 'TRUE',
    'hardship_exception': 'TRUE',
    'service_continuity': 'TRUE',
    'effect_measure': 'descriptive percentages and contingency tables (SPSS) from two cross-sectional user surveys, combined with doctrinal/regulatory analysis of the Ley de Aguas Nacionales and the municipal tariff regulation; no effect estimate, test statistic or confidence interval reported',
    'effect_estimate': ('D.C.I. users: 60% find their tariff accessible, 38% (137 users) elevated, 2% no answer; hotel users: 63% accessible, 37% elevated. '
                        'Increasing-block ("costo creciente") billing predominates: 89.83% of D.C.I. and 69% of hotel users; the municipal regulation states a goal of reducing minimum consumption to 10 m3 but minimum blocks remain 15-20 m3. '
                        'Security of supply after paying: 66.20% of D.C.I. vs 91% of hotel users feel secure (33.80% and 9% do not). '
                        'Attitude to valuing water economically: 44.23% (D.C.I.) and 49% (hotels) agree, 20.87% and 23% disagree, mainly because tariffs could rise and hit the most vulnerable. '
                        'Domestic subsidy (up to 50% of consumption cost) requires Mexican citizenship, ownership or tenancy and residence, qualifying income, payments up to date and consumption of at most 60 m3 per bimester.'),
    'extraction_sample_size': '464 users (364 D.C.I.; 100 hotel)',
    'adjusted_or_unadjusted': 'unadjusted (descriptive)',
    'model_type': 'cross-sectional stratified-random-sample user surveys with descriptive statistics and contingency tables, plus doctrinal analysis of national water law and municipal tariff regulation',
    'study_design': 'cross-sectional mixed-methods: doctrinal/regulatory analysis of the Ley de Aguas Nacionales and the municipal tariff regulation plus two stratified random user surveys (self-described "qualitative approach")',
    'risk_of_bias_rating': ('MMAT (re-appraised 2026-09-29 on the full text; supersedes the abstract-only rating of 2026-09-28). S1=Yes, S2=Yes. Mixed-methods criteria: 5.1(rationale)=Can\'t tell (design described, no rationale for combining components stated); '
                            '5.2(integration)=Yes (survey results set against the regulatory tariff blocks and the 10 m3 goal); 5.3(meta-inference)=Can\'t tell; 5.4(divergence)=No (none discussed); '
                            '5.5(component quality)=No (quantitative component: no response rate, no confidence intervals or test statistics for the tables, questionnaire not described as validated, payments self-reported as approximate; legal analysis component is clear). '
                            'Per MMAT\'s own guide, no composite score is computed.'),
    'page': '1-20 (methods p6-7; results p8-19; conclusions p19-20)',
    'table': 'Tablas 1-4 (tariff schedule, highest reported payments, subsidy requirements)',
    'figure': 'Figures 1-7 (design, area, survey response distributions) are charts/images; values were taken from the running text only',
    'section': 'Full text (Spanish): Introduccion, Desarrollo (area de estudio, metodologia, resultados), Conclusiones',
    'exact_location': 'Abstract p1-2; Metodologia p6-7; Resultados p8-19 (asequibilidad, percepcion p17-19); Conclusiones p19-20',
    'researcher': 'Claude-AI-extraction-2026-09-29 (re-extraction; original Claude-AI-extraction-2026-09-15)',
    'date_extracted': '2026-09-29',
    'extraction_note': ('Re-extracted 2026-09-29 from the full-text PDF supplied by the researcher (24 pp, Spanish; PDF not committed; chart images not read); supersedes the abstract-only extraction of 2026-09-15. '
                        'Flags eligibility, hardship_exception and service_continuity added on the full text. The evidence_map flag quantitative_synthesis_eligible (TRUE) was NOT changed although the paper reports only descriptive percentages (no effect estimate) -- see DECISIONS_AND_OPEN_ITEMS.md. record_id R77BFC4654E8A.'),
}
EVIDENCE_LEVEL = ('Single-study evidence: a cross-sectional mixed-methods study read in full text 2026-09-29 (doctrinal analysis of national water law and the Puerto Vallarta tariff regulation plus two stratified random user surveys, n=364 and n=100). '
                  'Descriptive percentages only (no effect estimate, test statistic or confidence interval); user perceptions, not measured outcomes. Chart images not read.')


def m_ed(rows):
    r = [x for x in rows if x['study_id'] == SID][0]
    assert r['extraction_note'].startswith('Extracted from published abstract/repository metadata only'), r['extraction_note'][:80]
    for k, v in UPD.items():
        assert k in r, k
        r[k] = v
    return rows


def m_em(rows):
    r = [x for x in rows if x['study_id'] == SID][0]
    r['evidence_level'] = EVIDENCE_LEVEL
    return rows


rw(ED, m_ed, 1159, 1159)
rw(EM, m_em, 1159, 1159)
rw(AB, lambda rows: [x for x in rows if x['study_id'] != SID], 67, 66)
print('S277 re-extracted from full text; abstract-only set 67 -> 66')
