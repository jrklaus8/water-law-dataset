"""2026-09-29: S326 (Bagnoli, Bertomeu-Sanchez, Estache & Vagliasindi, 'Does the ownership of utilities matter for social outcomes? A survey of the
evidence for developing countries', Journal of Economic Policy Reform, online 22 Nov 2021; record RBEC1E4523ED3) re-extracted from the full-text PDF
supplied by the researcher (21 pp; PDF not committed; text extractor used, so images were not read).

Finding: the paper describes itself as a 'survey of the evidence' and states NO search strategy, databases, selection procedure, protocol, duplicate
screening, list of excluded studies or critical appraisal of the included studies. Its only stated selection rule is exclusionary (notes 2 and 5: qualitative
studies, case studies and narrative assessments without robust statistical tests are not covered), and it flags possible publication bias (note 4) without assessing it.
It is a narrative, non-systematic review of econometric, index-number and CGE studies on utility ownership -> same test that moved twelve other studies
(S079, S320, S321, S322, S429, S430, S436, S440, S466, S479, S480, S482) from AMSTAR 2 to NONE on 2026-09-28. Applied here: risk_of_bias_tool AMSTAR 2 -> NONE.

Deliberately NOT changed (researcher decisions): the include decision (criterion 3 asks for 'empirical evidence or a *systematic* empirical synthesis'; whether a
non-systematic survey of empirical studies qualifies is open for all 13 such studies), study_design_class in evidence_map (stays systematic_review_secondary, as for the twelve),
effect_sizes.csv (none), eligibility flags. Also corrects the citation (it read 'Util Policy'; the journal is Journal of Economic Policy Reform).
Extraction leaves the abstract-only set (68 -> 67). Run from legal-last-mile-systematic-review/. Asserts row counts; atomic rewrite; preserves line endings."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
ED = '03_extraction/extracted_data/extraction_database.csv'
EM = '05_analysis/descriptive/evidence_map.csv'
AB = '05_analysis/sensitivity/abstract_only_extractions_2026-09-28.csv'
SID = 'S326'


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


NA = 'Not assessable -- AMSTAR 2 does not apply; see risk_of_bias_tool and 04_quality/appraisal_forms/S326_AMSTAR2.md (superseded 2026-09-29)'
UPD = {
    'citation': 'Bagnoli L, Bertomeu-Sanchez S, Estache A, Vagliasindi M (2023). Does the ownership of utilities matter for social outcomes? A survey of the evidence for developing countries. Journal of Economic Policy Reform, doi:10.1080/17487870.2021.1997747 (published online 22 Nov 2021; the 2023 year is that of the screening record and was not verifiable from the PDF; the earlier citation said "Util Policy", corrected).',
    'publication_type': 'narrative evidence survey (journal article); no search or selection method stated',
    'country': 'multi-country (developing countries generally; global survey covering electricity and water/sanitation; examples include Malaysia, Mali, Northeast Brazil, Africa, Central America)',
    'population': 'not applicable to a narrative survey: an unstated selection of econometric, index-number and CGE studies on public vs private utility ownership (qualitative studies, case studies and narrative assessments without robust statistical tests excluded by notes 2 and 5)',
    'sample_size': 'not stated (no search, selection or count of studies reported)',
    'fees': 'TRUE',
    'enforcement': 'TRUE',
    'service_coverage': 'TRUE',
    'regulatory_model': 'utility ownership structure (public/private, PPP forms) and regulatory governance/mandate design (service obligations, tariff and subsidy design)',
    'effect_measure': 'narrative survey of econometric, index-number and computable-general-equilibrium evidence; no pooled, vote-counted or per-study effect reported',
    'effect_estimate': ('Concludes there is little evidence that ownership (public vs private) matters for social outcomes: Table 1 marks every access and affordability issue "Not significant" for ownership; regulatory governance, the clarity and enforcement of service obligations and market structure matter more; '
                        'SOEs and small alternative providers are more likely than large private operators to serve the poorest (cream skimming by private providers); the evidence is outdated, partial and "not precise enough yet".'),
    'model_type': 'narrative evidence survey (economics literature)',
    'study_design': 'narrative evidence survey (non-systematic): no search strategy, databases, selection procedure, protocol, duplicate screening or critical appraisal stated; secondary evidence (systematic_review_secondary class kept for consistency with S320 and the other eleven reclassified narrative reviews)',
    'risk_of_bias_tool': "NONE -- self-described 'survey of the evidence' (narrative); full text read 2026-09-29: no search strategy, databases, selection procedure, protocol or critical appraisal stated, so it is not a systematic review; AMSTAR 2 does not apply. RISK_OF_BIAS.md section 1 has no validated tool for a non-systematic review used as an evidence source (reclassified 2026-09-29 from AMSTAR 2; see CHANGELOG.md)",
    'risk_of_bias_rating': 'NOT APPLICABLE -- risk_of_bias_tool is NONE (2026-09-29, full text: confirmed not a systematic review, so not eligible for AMSTAR 2 or any other validated tool; see risk_of_bias_tool for the reason). The earlier "Not ratable" AMSTAR 2 entry rested on an abstract-only extraction and is superseded.',
    'selection_bias': NA, 'measurement_bias': NA, 'confounding': NA, 'attrition': NA, 'reporting_bias': NA,
    'page': '1-15 (text); notes p15-16',
    'table': 'Table 1 (summary of insights on ownership, access, affordability and distributional effects, p12-13)',
    'figure': 'none',
    'section': 'Full text (introduction, methodological preliminaries, evidence, policy implications, research agenda, notes)',
    'exact_location': 'Abstract; Introduction p2-3; Methodological preliminaries p3-5; Table 1 p12-13; Conclusions p13-15; Notes 2, 4, 5 p15-16',
    'researcher': 'Claude-AI-extraction-2026-09-29 (re-extraction; original Claude-AI-extraction-2026-09-15)',
    'date_extracted': '2026-09-29',
    'extraction_note': ('Re-extracted 2026-09-29 from the full-text PDF supplied by the researcher (21 pp; PDF not committed; images not read); supersedes the abstract-only extraction of 2026-09-15. '
                        'Full-text finding: no stated search, selection procedure, protocol or appraisal, so this is a narrative survey, not a systematic review -> tool AMSTAR 2 reclassified to NONE, as for S320 and eleven others. '
                        'Whether such a study meets inclusion criterion 3 (systematic empirical synthesis) is a researcher decision, not applied here. record_id RBEC1E4523ED3. '
                        '| Study reinstated 2026-09-15 following E12 policy amendment (secondary/systematic reviews are valid systematic_review_secondary evidence per CODEBOOK.md).'),
}
EVIDENCE_LEVEL = ('Secondary evidence: a narrative (non-systematic) survey of econometric evidence on utility ownership and social outcomes in developing countries, read in full text 2026-09-29. '
                  'No search, selection or appraisal method stated; not a systematic review and not certainty-graded. Its conclusion (ownership matters less than regulatory governance and market structure; evidence outdated and imprecise) is the authors\' own reading of studies not re-examined here.')


def m_ed(rows):
    r = [x for x in rows if x['study_id'] == SID][0]
    assert r['extraction_note'].startswith('Extracted from published abstract/repository metadata only'), r['extraction_note'][:80]
    assert r['risk_of_bias_tool'].startswith('AMSTAR 2')
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
rw(AB, lambda rows: [x for x in rows if x['study_id'] != SID], 68, 67)
print('S326 re-extracted from full text; tool AMSTAR 2 -> NONE; abstract-only set 68 -> 67')
