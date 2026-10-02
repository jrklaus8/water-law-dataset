"""2026-09-29: S366 (Quattrochi et al. 2021, BMJ Global Health 6:e005030, record R3BFAF175DBF1) re-extracted from the full-text PDF supplied by
the researcher (11 pages; PDF not committed). Supersedes the abstract-only extraction of 2026-09-16 and the low-confidence RoB 2 rating of
2026-09-28. Text of the PDF was read through a text extractor: Figure 1 (trial profile) and the online supplemental tables were NOT read.

What changes (extraction_database.csv row S366 only; evidence_map.csv row S366 evidence_level; the appraisal form is rewritten separately):
  * populated fields that were blank because only the abstract was available (sample, effect measure/estimate/CIs, covariates, locators);
  * the five RoB 2 domain fields and the rating text, from signalling questions answered on the full text;
  * two mechanism/outcome flags now supported by the text: participation (village WASH committees, community mobilisation) and
    service_quantity (litres collected); household_level (household survey);
  * extraction_note no longer starts with the abstract-only prefix, so S366 leaves the abstract-only set (69 -> 68);
  * S366 is removed from 05_analysis/sensitivity/abstract_only_extractions_2026-09-28.csv (same precedent as S356 on 2026-09-28).
Not changed: effect_sizes.csv (no row added: S366 is a second report of the trial already represented by S294 in Family B; adding it is a
researcher decision), evidence_map eligibility flags, linked_reports (LR01 is annotated in CHANGELOG, not rewritten), mechanism_certainty (4).
Run from legal-last-mile-systematic-review/. Asserts row counts; atomic rewrite; preserves each file's line endings."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
ED = '03_extraction/extracted_data/extraction_database.csv'
EM = '05_analysis/descriptive/evidence_map.csv'
AB = '05_analysis/sensitivity/abstract_only_extractions_2026-09-28.csv'
SID = 'S366'


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
    'subnational_unit': 'rural DRC; four provinces (Kongo Central, Kasai, Kasai Central, South Kivu); 121 village clusters; 328 villages interviewed (abstract and design text say 332 villages; Figure 1 trial profile not read, difference unexplained in the text read)',
    'population': 'households (head woman interviewed) in rural villages eligible for the VEA programme: secure, accessible Health Areas with high diarrhoea/cholera/malnutrition incidence and interested Health Area staff',
    'sample_size': '121 clusters (50 intervention with 145 villages, 71 control with 183 villages); 1,312 households (732 control, 580 intervention) in 328 villages, 4 households per village; interviews 11 Oct-23 Dec 2019',
    'household_level': 'TRUE',
    'participation': 'TRUE',
    'service_quantity': 'TRUE',
    'effect_measure': 'intention-to-treat differences from linear models (percentage points for binary primary outcomes; minutes/litres for time and quantity; SD units for standardised summary indices), cluster-randomised controlled trial; SEs clustered by village cluster. Companion report of the same trial as S294 (2025, PLOS Medicine)',
    'effect_estimate': ('PRIMARY (Table 2): improved primary water source 83% intervention vs 43% control, adjusted effect +33 pp (95% CI 22 to 45); improved sanitation facility 46% vs 18%, +26 pp (95% CI 14 to 37); '
                        'time to collect water -3.0 min (95% CI -19.7 to 13.6), not significant; litres collected +2.3 L (95% CI -4.2 to 8.7), not significant. '
                        'SECONDARY (Table 3, SD units): water governance index +1.3 SD (1.1 to 1.5); water satisfaction +0.6 SD (0.4 to 0.9); handwashing practices +0.5 SD (0.3 to 0.7); sanitation practices +0.3 SD (0.1 to 0.4); '
                        'no significant difference in financial cost of water, school attendance, child health, water storage or water quality indices. '
                        'SUBGROUPS (Table 4): large province differences, e.g. time to collect water +43 min in Kasai (95% CI 13 to 72) but -61 min in Kasai Central (95% CI -95 to -26); no effect on primary outcomes in South Kivu.'),
    'lower_CI': '22 pp (improved water source); 14 pp (improved sanitation); -19.7 min (water time); -4.2 L (water quantity); 1.1 SD (governance index)',
    'upper_CI': '45 pp (improved water source); 37 pp (improved sanitation); 13.6 min (water time); 8.7 L (water quantity); 1.5 SD (governance index)',
    'extraction_sample_size': '1312 households; 121 clusters',
    'adjusted_or_unadjusted': 'adjusted (randomisation-strata dummies; intention-to-treat)',
    'covariates': 'randomisation strata dummies (province; number of villages per cluster); gender and age-in-months dummies for child-health outcomes only; no other covariates',
    'model_type': 'linear models (intention-to-treat) with randomisation-strata dummies, SEs clustered by village cluster; summary indices as standardised means relative to control ("greedy indexing")',
    'study_design': 'experimental (cluster-randomized controlled trial; 50 treatment / 71 control clusters of villages; stratified by province and number of villages per cluster; single post-intervention survey, median about 5 months after implementation; all outcomes self-reported)',
    'risk_of_bias_rating': ('Some concerns (re-appraised 2026-09-29 on the full text, RoB 2 cluster-trial variant; see 04_quality/appraisal_forms/S366_RoB2.md; supersedes the low-confidence abstract-only rating of 2026-09-28). '
                            'Domain 1 Low; Domain 2 Some concerns (fidelity and contamination not reported); Domain 3 Low (all 121 clusters analysed; Figure 1 unread); '
                            'Domain 4 Some concerns for the primary outcomes, High for the self-reported satisfaction/behaviour indices (participants aware of assignment); Domain 5 Some concerns (registered AEARCTR-0004648; one outcome split post hoc; registration date not visible). '
                            'Overall Some concerns for the primary outcomes.'),
    'selection_bias': 'Low (RoB 2 Domains 1a/1b -- Stata randomisation of all clusters at once, stratified; endline household sampling by interviewers blinded to assignment using a random rule; baseline characteristics balanced (Table 1); caveat: seven villages randomly dropped to meet operational targets, timing relative to allocation not stated -- appraised 2026-09-29)',
    'measurement_bias': 'Some concerns for primary outcomes / High for satisfaction and behaviour indices (RoB 2 Domain 4 -- all outcomes self-reported by the household head woman, who could not be blinded; interviewers blinded but one questionnaire module covered programme participation; authors argue against social-desirability bias from heterogeneity within indices -- appraised 2026-09-29)',
    'attrition': 'Low (RoB 2 Domain 3 -- 1,312 households interviewed in 328 villages across all 121 clusters, 732 control and 580 intervention; household non-response and Figure 1 trial profile not read -- appraised 2026-09-29)',
    'reporting_bias': 'Some concerns (RoB 2 Domain 5 -- registered AEARCTR-0004648 with 4 primary and 7 secondary outcomes and 5 subgroup analyses preregistered; "health behaviour and knowledge" split into three outcomes after seeing the data (disclosed); a "water quality index" is reported in the results without a method description; registration date and analysis plan not visible in the PDF -- appraised 2026-09-29)',
    'page': '1-11 (methods p3-5; results p6-8; discussion p8-10)',
    'table': 'Table 1 (baseline balance); Table 2 (primary outcomes); Table 3 (secondary outcome indices); Table 4 (province subgroups)',
    'figure': 'Figure 1 (trial profile) not read: image content not extracted from the PDF text',
    'section': 'Methods; Results; Discussion (full text)',
    'exact_location': 'Abstract; Methods (Randomisation p3; Outcomes p4-5; Sample size, Statistical analysis p5); Results (primary outcomes p6-7, Table 2 p7)',
    'researcher': 'Claude-AI-extraction-2026-09-29 (re-extraction; original Claude-AI-extraction-2026-09-16)',
    'date_extracted': '2026-09-29',
}
NOTE_NEW = ('Re-extracted 2026-09-29 from the full-text PDF supplied by the researcher (Quattrochi et al. 2021, BMJ Global Health 6:e005030; 11 pp; PDF not committed); supersedes the abstract-only extraction of 2026-09-16. '
            'Figure 1 (trial profile) and the online supplemental tables were not read. Same trial as S294 (LR01) but a different survey: this report covers 1,312 households (4 per village, Oct-Dec 2019) whereas S294 reports 3,283 households -- LR01 "same underlying data" holds for the trial and randomisation, not necessarily for the survey data. '
            'mechanism/outcome flags participation, service_quantity and household_level added on the full text. record_id R3BFAF175DBF1. | LINKED REPORT (audit 2026-09-28, LR01): related to S294 - yes underlying data; see 03_extraction/extracted_data/linked_reports_2026-09-28.csv.')
EVIDENCE_LEVEL = ('Single-study evidence: a cluster-randomised controlled trial (121 clusters, 1,312 households) read in full text 2026-09-29. Preregistered primary outcomes: improved water source +33 pp (95% CI 22 to 45) and improved sanitation +26 pp (14 to 37) '
                  'with no significant effect on time or quantity of water collected; all outcomes self-reported by unblinded respondents; the same trial is also reported in S294. Figure 1 and the supplement were not read.')


def m_ed(rows):
    r = [x for x in rows if x['study_id'] == SID][0]
    assert r['extraction_note'].startswith('Extracted from published abstract/introduction text only'), r['extraction_note'][:80]
    for k, v in UPD.items():
        assert k in r, k
        r[k] = v
    r['extraction_note'] = NOTE_NEW
    return rows


def m_em(rows):
    r = [x for x in rows if x['study_id'] == SID][0]
    r['evidence_level'] = EVIDENCE_LEVEL
    return rows


def m_ab(rows):
    return [x for x in rows if x['study_id'] != SID]


rw(ED, m_ed, 1159, 1159)
rw(EM, m_em, 1159, 1159)
rw(AB, m_ab, 69, 68)
print('S366 re-extracted from full text; abstract-only set 69 -> 68')
