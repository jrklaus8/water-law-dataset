"""2026-10-02: S319, S324, S325 and S344 re-extracted and AMSTAR 2-appraised from the full-text PDFs supplied by the researcher (PDFs not committed; text extractor
used, so Figures (PRISMA flow diagrams), image tables and supplementary tables were NOT read). Supersedes the abstract-only extractions and the 'Not ratable' entries.

Eligibility finding (applying the S326 test: does the paper state a search, a selection procedure and an appraisal method?):
  S324  Pu et al. 2022   registered (PROSPERO CRD42020199163), PRISMA, 3 databases + full string, duplicate screening/extraction, NICE-adapted appraisal -> systematic review
  S319  Yoanita et al.   'targeted systematic review', PRISMA 2020, Scopus only, PICO, 2 reviewers screened, CASP-adapted appraisal, 8 studies -> systematic review (narrow search)
  S325  Silva R. de S.M. self-described PRISMA review, 8 sources named, no string/dates, single author, no appraisal; 65 -> 10 duplicates -> 19 excluded -> 36 -> weak systematic review
  S344  Hendraputra 2026 self-described SLR, Google Scholar only, string + eligibility table + PRISMA, single author, no appraisal, 27 + 4 snowballed studies -> weak systematic review
All four therefore keep AMSTAR 2 (none is moved to NONE). Items answered only from the text read; where an item depends on an unread figure or supplement
the answer says so. Ratings follow the AMSTAR 2 algorithm on critical items 2, 4, 7, 9, 11, 13, 15 (11 and 15 not applicable: no meta-analysis).
NOT changed: include decisions, evidence_map flags (eligibility, families), effect_sizes.csv, mechanism/outcome flags. Removes the four from the abstract-only set (66 -> 62).
Run from legal-last-mile-systematic-review/. Asserts row counts; atomic rewrite; preserves line endings."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
ED = '03_extraction/extracted_data/extraction_database.csv'
EM = '05_analysis/descriptive/evidence_map.csv'
AB = '05_analysis/sensitivity/abstract_only_extractions_2026-09-28.csv'
DATE = '2026-10-02'
NA = 'Not applicable to AMSTAR 2 domains; item-level appraisal in 04_quality/appraisal_forms/{sid}_AMSTAR2.md (full text, ' + DATE + ')'

ITEMS = {1: 'PICO components in the research questions and inclusion criteria', 2: 'Review methods established prior to the review (protocol); deviations justified',
         3: 'Selection of study designs explained', 4: 'Comprehensive literature search strategy', 5: 'Study selection in duplicate', 6: 'Data extraction in duplicate',
         7: 'List of excluded studies with justification', 8: 'Included studies described in adequate detail', 9: 'Satisfactory technique for risk of bias in included studies',
         10: 'Funding sources of included studies reported', 11: 'Appropriate meta-analytic methods', 12: 'Impact of risk of bias on meta-analysis results',
         13: 'Risk of bias accounted for when interpreting results', 14: 'Heterogeneity explained and discussed', 15: 'Publication bias investigated (quantitative synthesis)',
         16: 'Conflicts of interest and funding of the review reported'}
CRIT = {2, 4, 7, 9, 11, 13, 15}

S = {}
S['S324'] = dict(
    ans={1: ('Partial Yes', 'school WASH in LMICs, three-part search; no formal PICO'), 2: ('Partial Yes', 'registered PROSPERO CRD42020199163; deviations not discussed in the text read'),
         3: ('No', 'designs defined (experimental, quasi-experimental, observational) but their inclusion is not explained'),
         4: ('Partial Yes', 'Web of Science, Scopus, PubMed, full string, English only, alerts May 2020-July 2021, author contact; no grey literature'),
         5: ('Yes', 'two researchers independently screened titles/abstracts and full texts; >95% agreement'), 6: ('Yes', 'two members independently extracted; a third compared'),
         7: ('No', 'text says reasons for exclusion are in Fig 1 (not read); no list of excluded studies in the text'), 8: ('Partial Yes', 'characteristic tables for observational and intervention studies'),
         9: ('Partial Yes', 'NICE-adapted checklists; selection, attrition, reporting, performance bias; two independent raters; confounding not named; S1-S6 Tables not read'),
         10: ('No', 'not reported in the text read'), 11: ('N/A', 'no meta-analysis (precluded by non-standardised outcomes)'),
         12: ('N/A', 'no meta-analysis'), 13: ('No', 'the text read does not use the appraisal results when interpreting findings; S1-S6 Tables not read'),
         14: ('Yes', 'differences in designs, indicators and time scales discussed; meta-analysis precluded'), 15: ('N/A', 'no quantitative synthesis'),
         16: ('Yes', 'funders (World Vision, USAID WASHPaLS, NSERC, a family gift) named, no role in the study; no competing interests')},
    rating='Critically Low (provisional)', basis='items 7 and 13 scored No because the text read does not show them; Figure 1 and S1-S6 Tables were not read -- if both are satisfied there the rating rises to Moderate, if only one, to Low',
    upd=dict(
        publication_type='systematic review (PRISMA, PROSPERO-registered)', country='multi-country (low- and middle-income countries; school settings)',
        population='school WASH service delivery (infrastructure maintenance and consumables) in LMIC schools',
        sample_size='19 included studies (from 3,841 unique records; Web of Science, Scopus, PubMed searched May 2020, alerts to July 2021; one study via author contact); nine observational, the rest experimental or quasi-experimental',
        effect_measure='narrative/qualitative-comparative synthesis of drivers of, and interventions for, sustainable school WASH; formal meta-analysis precluded by non-standardised outcomes',
        effect_estimate=("Observational studies mostly conclude that dysfunctional accountability and information-sharing mechanisms drive school WASH service failures; experimental/quasi-experimental studies mostly test added funds, infrastructure or supplies and find negligible impact across sustainability outcomes. "
                         "The authors conclude sustainable delivery depends on three simultaneously necessary components: resources, information and accountability."),
        study_design='systematic review (PRISMA, PROSPERO CRD42020199163; secondary synthesis of observational, quasi-experimental and experimental studies)',
        model_type='systematic review, narrative synthesis (no meta-analysis)', section='Methods; Results; Discussion (full text)',
        exact_location='Abstract; Methods (protocol registration, search strategy and selection, data extraction and quality checks, p2-3); Results (search results p3; Tables 1-3); Discussion (limitations: peer-reviewed English only)'),
    note='Re-extracted and AMSTAR 2-appraised 2026-10-02 from the full-text PDF supplied by the researcher (23 pp; PDF not committed). Figure 1 (PRISMA flow) and supplementary S1-S11 Tables not read.')
S['S319'] = dict(
    ans={1: ('Yes', 'PICO stated (rural water utilities / creative financing / conventional models / sustainability)'), 2: ('No', 'no protocol or registration stated'),
         3: ('Partial Yes', 'article publications chosen for peer-review standards'), 4: ('No', 'Scopus only (May 2024), English, 2009-2024; no other source or reference checking'),
         5: ('Yes', 'screening by two reviewers independently, discrepancies discussed'), 6: ('No', 'extraction described but not stated to be in duplicate'),
         7: ('No', '49 -> 41 -> 36 -> 8 stated; no list of excluded studies in the text (Fig 1 not read)'), 8: ('Partial Yes', 'tables of the 8 studies and financing mechanisms'),
         9: ('Partial Yes', 'five domains adapted from CASP (aims, methodology, intervention description, outcome reporting, data quality), consensus rating; not designed for confounding'),
         10: ('No', 'not reported'), 11: ('N/A', 'no meta-analysis'), 12: ('N/A', 'no meta-analysis'), 13: ('Yes', 'no studies excluded on risk of bias; judgments informed the weighting of findings; 5 moderate, 3 low reported'),
         14: ('No', 'context-dependence noted; heterogeneity not examined'), 15: ('N/A', 'no quantitative synthesis'),
         16: ('Yes', 'funding by the School of Environmental Science, University of Indonesia disclosed')},
    rating='Critically Low', basis='critical items 2 (no protocol), 4 (single database) and 7 (no list of excluded studies) are flawed',
    upd=dict(
        publication_type='targeted systematic review (PRISMA 2020), journal article', country='multi-country (developing countries; rural community-based piped water utilities)',
        population='community-based rural piped-water utilities in developing countries', regulatory_model='creative financing mechanisms for rural water utilities (prepaid tariffs, community financing, repayable loans, blended finance, cross-subsidy) vs conventional donor/subsidy models',
        sample_size='8 included studies (49 records identified in Scopus, 41 after exclusion of non-articles/non-English/inaccessible, 36 after date limits 2009-2024, 8 after criteria)',
        effect_measure='narrative synthesis mapped to PICO components; no pooled estimate',
        effect_estimate=("Creative financing mechanisms (prepaid tariff schemes, community financing, repayable loans, blended finance, cross-subsidisation) were associated with improved financial viability, service reliability and institutional resilience relative to donor- or subsidy-driven models, but effectiveness was context-dependent; "
                         "5 of 8 studies had moderate and 3 low risk of bias under adapted CASP criteria. The authors call the evidence base narrow and the findings indicative rather than comprehensive."),
        study_design='targeted systematic review (PRISMA 2020; Scopus only; PICO; secondary synthesis)', model_type='systematic review, narrative synthesis (no meta-analysis)',
        section='Methods; Results; Discussion (full text)', exact_location='Abstract; Methods (PRISMA flow stages, screening, risk-of-bias domains, p3-4); Results (8 studies, financing models); Discussion (limitations: single database)'),
    note='Re-extracted and AMSTAR 2-appraised 2026-10-02 from the full-text PDF supplied by the researcher (20 pp; PDF not committed). Figure 1 (selection process) not read.')
S['S325'] = dict(
    ans={1: ('No', 'objective and scope stated; no PICO'), 2: ('No', 'no protocol or registration'), 3: ('No', 'inclusion rule contradictory: "both empirical and non-empirical sources" yet sources "had to use quantitative approaches ... analytical"'),
         4: ('Partial Yes', 'eight sources named (Web of Science, MDPI, Scopus, Water Resources Abstracts, Environment Complete, Environment Index, Google Scholar, Google); only loose keywords, no search string or dates'),
         5: ('No', 'single researcher; no duplicate selection stated'), 6: ('No', 'not stated'), 7: ('No', '65 -> 10 duplicates -> 19 excluded -> 36 stated; no list of excluded studies'),
         8: ('Not assessable', 'Table 1 "Literature analyzed" is an image and was not read'), 9: ('No', 'no risk-of-bias or quality appraisal of included documents'),
         10: ('No', 'not reported'), 11: ('N/A', 'no meta-analysis'), 12: ('N/A', 'no meta-analysis'), 13: ('No', 'no appraisal to account for'), 14: ('No', 'not discussed'),
         15: ('N/A', 'no quantitative synthesis'), 16: ('No', 'no funding or competing-interest statement found in the text')},
    rating='Critically Low', basis='critical items 2, 7, 9 and 13 are flawed (and item 4 only partly met)',
    upd=dict(
        publication_type='self-described PRISMA systematic review, journal article (single author)', country='United States', legal_system='common law', urban_rural='rural',
        population='rural United States water supply (documents 1990-2019 on legal, institutional and governmental approaches to rural water access)',
        sample_size='36 documents included (65 identified, 10 duplicates removed, 19 excluded at eligibility); single researcher',
        effect_measure='narrative thematic synthesis; no pooled estimate',
        effect_estimate=("Rural US water supply infrastructure is described as below par and strained by urbanisation; about 70% of the reviewed documents addressed rural water rights, and the author concludes that government should reorganise existing structures, give municipalities flexibility, "
                         "develop community-management-oriented approaches and Rural Community Assistance Partnership-type regulatory support. Existing programmes are said to be effective but not to have addressed rising demand."),
        study_design='self-described PRISMA systematic review (single author; eight sources named; no search string, appraisal or excluded-study list)', model_type='systematic review, narrative thematic synthesis',
        section='Methodology; Results; Discussion; Conclusion (full text)', exact_location='Abstract; Methodology (PRISMA 4-stage flow, sources of data, inclusion criteria, p3-4); Results (65 -> 36 documents, p8); Discussion'),
    note='Re-extracted and AMSTAR 2-appraised 2026-10-02 from the full-text PDF supplied by the researcher (18 pp; PDF not committed). Table 1 (literature analysed) is an image and was not read. Methods reporting is weak and internally inconsistent (see form).')
S['S344'] = dict(
    ans={1: ('Partial Yes', 'three research questions and an eligibility table (Table 2); no PICO'), 2: ('No', 'no protocol or registration'), 3: ('Partial Yes', 'peer-reviewed articles/proceedings, English or Indonesian, 2010-2024, plus snowballed pre-2010 foundational studies, with criteria in Table 2'),
         4: ('No', 'Google Scholar only (acknowledged as less replicable) plus backward snowballing; string given'), 5: ('No', 'single author'), 6: ('No', 'single author; coding framework cross-checked against full texts'),
         7: ('No', '27 + 4 studies stated; no list of excluded studies (PRISMA Figure 2 not read)'), 8: ('Partial Yes', 'Table 3 characteristics of the 31 studies'),
         9: ('No', 'no risk-of-bias or quality appraisal'), 10: ('No', 'not reported'), 11: ('N/A', 'no meta-analysis'), 12: ('N/A', 'no meta-analysis'),
         13: ('No', 'no appraisal to account for'), 14: ('Partial Yes', 'themes traced across the pre- and post-2010 literature; no formal heterogeneity discussion'), 15: ('N/A', 'no quantitative synthesis'),
         16: ('Partial Yes', 'no specific funding declared; no competing-interest statement found')},
    rating='Critically Low', basis='critical items 2, 4, 7, 9 and 13 are flawed',
    upd=dict(
        publication_type='systematic literature review (conference proceedings, ICCB 2025; single author)', country='Indonesia', subnational_unit='Jakarta', urban_rural='urban',
        population='Jakarta clean-water provision and governance literature, 2004-2024 (27 contemporary studies 2010-2024 plus 4 foundational pre-2010 studies)',
        sample_size='31 studies (27 from a Google Scholar search, 4 added by backward snowballing)', effect_measure='thematic analysis (narrative synthesis); no pooled estimate',
        effect_estimate=("Four interconnected challenges are traced from the 1998 public-private partnership to the present: a dual environmental crisis (land subsidence, river pollution), infrastructural failure (high non-revenue water), a social crisis of water equity burdening the urban poor, and a governance crisis rooted in flawed contract design. "
                         "The author concludes the crisis is fundamentally one of governance rather than infrastructure or affordability, and that a sustainable public-utility business model requires rebuilt governance and public trust; evidence gaps include post-remunicipalisation evaluation and comparative studies of other sinking megacities."),
        study_design='systematic literature review (single author; Google Scholar search plus backward snowballing; thematic synthesis)', model_type='systematic literature review, thematic synthesis (no meta-analysis)',
        section='Method; Results; Discussion (full text)', exact_location='Abstract; Method (search strategy, eligibility Table 2, selection, extraction and synthesis, p4-6); Results (themes, p6-10); Limitations 3.2.4 (p11)'),
    note='Re-extracted and AMSTAR 2-appraised 2026-10-02 from the full-text PDF supplied by the researcher (13 pp; PDF not committed). The PRISMA flow diagram (Figure 2) was not read. Single-author review with a non-replicable single-engine search and no appraisal.')


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


def m_ed(rows):
    for r in rows:
        sid = r['study_id']
        if sid not in S:
            continue
        d = S[sid]
        assert r['extraction_note'].startswith('Extracted from published abstract/'), sid
        assert r['risk_of_bias_rating'].startswith('Not ratable') and r['risk_of_bias_tool'].startswith('AMSTAR 2'), sid
        for k, v in d['upd'].items():
            assert k in r, k
            r[k] = v
        r['risk_of_bias_rating'] = (f"{d['rating']} (appraised {DATE} against the official AMSTAR 2 checklist on the full text; item-level answers in 04_quality/appraisal_forms/{sid}_AMSTAR2.md; {d['basis']}). "
                                    "Supersedes the abstract-only 'Not ratable' entry; eligibility as a systematic review confirmed from the methods text (see the form).")
        for k in ('selection_bias', 'measurement_bias', 'confounding', 'attrition', 'reporting_bias'):
            r[k] = NA.format(sid=sid)
        r['extraction_note'] = d['note'] + ' ' + r['extraction_note'].split(' record_id ', 1)[1].join(['record_id ', '']) if False else d['note'] + ' record_id ' + r['record_id'] + '. | Study reinstated 2026-09-15 following E12 policy amendment (secondary/systematic reviews are valid systematic_review_secondary evidence per CODEBOOK.md).'
        r['researcher'] = 'Claude-AI-extraction-2026-10-02 (re-extraction)'; r['date_extracted'] = DATE
        r['page'] = r['page'] or 'see exact_location'
    return rows


def form(sid, d):
    L = [f"# AMSTAR 2 appraisal (full text) — {sid}", "",
         f"**Date appraised:** {DATE} · **Appraiser:** Claude-AI-appraisal-{DATE} · **Basis:** the full-text PDF supplied by the researcher (not committed). Figures (PRISMA flow diagrams), image tables and supplementary tables were **not read**; where an item depends on them the answer says so. "
         "Supersedes the abstract-only pilot form of 2026-09-16 (in git history). Appraised by the AI; not independently verified.", "",
         f"**Overall confidence: {d['rating']}** — {d['basis']}. Critical items: 2, 4, 7, 9, 11, 13, 15 (11 and 15 not applicable: no meta-analysis).", "",
         "| # | Critical? | Item | Answer | Basis (from the text read) |", "|---|---|---|---|---|"]
    for i, name in ITEMS.items():
        a, b = d['ans'][i]
        L.append(f"| {i} | {'**Yes**' if i in CRIT else 'No'} | {name} | {a} | {b} |")
    L += ["", "Method note: where the text is silent the answer is No (AMSTAR 2's own convention); this differs from the 2026-09-16 pilot, which scored silence in an abstract as 'Not assessable' because the full text was not available."]
    return "\n".join(L) + "\n"


rw(ED, m_ed, 1159, 1159)
rw(AB, lambda rows: [x for x in rows if x['study_id'] not in S], 66, 62)
for sid, d in S.items():
    open(f'04_quality/appraisal_forms/{sid}_AMSTAR2.md', 'w', encoding='utf-8').write(form(sid, d))
print('re-extracted and appraised', ', '.join(S), '; abstract-only set 66 -> 62')
