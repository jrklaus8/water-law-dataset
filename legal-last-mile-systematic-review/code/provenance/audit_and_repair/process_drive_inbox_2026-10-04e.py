"""2026-10-04 (late): fifth Drive-inbox batch (17 full texts, 'Sep 26 2026' folder). What this dated script records (PDFs were read in the session; nothing is copied into the repository):
  * AMSTAR 2 on the full text for five reviews that were still 'Not ratable': S350 (Abdulhadi 2024), S427 (Cooper 2021), S475 (Murebwayire 2025), S521 (Fono 2025) and S537 (Alam 2025).
    S350, S427, S475 and S521 are Critically Low (more than one critical flaw); S537 is Low (one critical flaw, item 7). Item-level answers go to 04_quality/appraisal_forms/S0xx_AMSTAR2.md
    and the extraction rows are upgraded from the abstract-level entry.
  * 02_screening/full_text/A22_VERDICTS_2026-10-04.csv: a proposal for S297 (conceptual paper with an illustrative case; borderline on criterion 3). No decision is changed (A15, A22).
The re-extractions of S285 and of the stale-status rows (S297, S389, S394, S396, S402, S403) are JSONs in reextract_2026-10-04/ applied by run_reextract_2026-10-04.py.
Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
DATE = '2026-10-04'
ED = '03_extraction/extracted_data/extraction_database.csv'
A22V = '02_screening/full_text/A22_VERDICTS_2026-10-04.csv'


def rw(path, fn):
    raw = open(path, newline='', encoding='utf-8').read(); crlf = '\r\n' in raw[:5000]
    with open(path, newline='', encoding='utf-8') as f:
        rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
    n = len(rows); out = fn(rows); assert len(rows) == n
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), suffix='.tmp')
    with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n' if crlf else '\n'); w.writeheader(); w.writerows(rows)
    os.replace(tmp, path)
    return out


ITEMS = {1: 'PICO components in the research questions and inclusion criteria', 2: 'Review methods established prior to the review (protocol); deviations justified',
         3: 'Selection of study designs explained', 4: 'Comprehensive literature search strategy', 5: 'Study selection in duplicate', 6: 'Data extraction in duplicate',
         7: 'List of excluded studies with justification', 8: 'Included studies described in adequate detail', 9: 'Satisfactory technique for risk of bias in included studies',
         10: 'Funding sources of included studies reported', 11: 'Appropriate meta-analytic methods', 12: 'Impact of risk of bias on meta-analysis results',
         13: 'Risk of bias accounted for when interpreting results', 14: 'Heterogeneity explained and discussed', 15: 'Publication bias investigated (quantitative synthesis)',
         16: 'Conflicts of interest and funding of the review reported'}
CRIT = {2, 4, 7, 9, 11, 13, 15}
NA_ITEMS = {11, 12, 15}
NAS = 'Not applicable to AMSTAR 2 domains; item-level appraisal in 04_quality/appraisal_forms/{sid}_AMSTAR2.md (full text, ' + DATE + ')'
NA_ANS = ('No', 'not applicable: no meta-analysis (narrative synthesis); not counted as a flaw')
NOT_FOUND = 'not located in the text read'

AM = {}
AM['S350'] = dict(
    rating='Critically Low',
    cit='Abdulhadi R, Bailey A, Van Noorloos F, et al. (2024). Access inequalities to WASH and housing in slums in low- and middle-income countries: A scoping review. Global Public Health',
    basis='critical items 7 (no list of excluded studies), 9 (no risk-of-bias assessment) and 13 (nothing accounted for) are flawed; item 2 is Partial Yes (a written JBI protocol exists but was not registered); items 11 and 15 do not apply (no meta-analysis)',
    pages='Global Public Health, full text read (about 20 pages); the appendices (protocol, search string, extraction table) were not read',
    ans={
        1: ('Yes', 'a PICOC framework defines slum dwellers, the phenomenon (access to WASH and housing), the context and the outcome'),
        2: ('Partial Yes', 'a written protocol (Appendix 1, JBI scoping methodology) exists but was deliberately not registered; it covers the question, criteria and search but no risk-of-bias plan'),
        3: ('Yes', 'qualitative and secondary qualitative designs were chosen and strictly quantitative studies were excluded, with the reasons given (lived experience; survey data mask slum residents)'),
        4: ('Partial Yes', 'PubMed, Scopus and Web of Science searched in November 2022 with a synonym list and search string (appendices); 2000-2022, English only, grey literature excluded and the reasons given; no reference-list searching reported'),
        5: ('No', 'two reviewers screened 102 records independently by title and abstract, but the full texts of the remaining 57 were assessed by one reviewer'),
        6: ('No', 'the 33 articles were extracted by one author into an Excel table'),
        7: ('No', 'CRITICAL FLAW: counts only (45 excluded on title and abstract, 24 at full text); the excluded studies are not listed'),
        8: ('Partial Yes', 'the extraction table (appendix, not read) captures author, year, geography, focus, population, barriers and recommendations; the text describes the 33 studies in summary'),
        9: ('No', 'CRITICAL FLAW: no risk-of-bias or quality assessment of the included studies is reported (scoping method)'),
        10: ('No', 'funding sources of the included studies are not reported'),
        11: NA_ANS, 12: NA_ANS,
        13: ('No', 'CRITICAL FLAW: with no appraisal, study quality is not considered when interpreting the themes'),
        14: ('No', 'differences between settings are discussed as themes of barriers, not as heterogeneity of findings'),
        15: ('No', 'not applicable: no quantitative synthesis; publication bias is not discussed'),
        16: ('No', 'a funding or conflict statement was ' + NOT_FOUND)},
    fields=dict(
        study_design='scoping review (JBI methodology, PRISMA-ScR style; unregistered written protocol; PubMed, Scopus and Web of Science, Nov 2022; thematic synthesis; no risk-of-bias assessment)',
        sample_size='102 records after de-duplication screened by title and abstract (45 excluded), 57 full texts assessed (24 excluded), 33 published articles included (2000-2022; qualitative and secondary qualitative studies in low- and middle-income countries)',
        model_type='scoping review with thematic narrative synthesis (no meta-analysis)'),
    note='Full-text appraisal 2026-10-04 from the PDF in the researcher\'s Drive inbox (appendices not read). Replaces the abstract-level entry and the 2026-09-28 "Not ratable" appraisal. Scoping method, so no quality appraisal; the protocol was written but unregistered. The review is kept under AMSTAR 2 as a systematic search with narrative synthesis.')
AM['S427'] = dict(
    rating='Critically Low',
    cit='Cooper B, Behnke NL, Cronk R, et al. (2021). Environmental health conditions in the transitional stage of forcible displacement: A systematic scoping review. Science of the Total Environment',
    basis='critical items 2 (no protocol or registration located), 7 (no list of excluded studies), 9 (no risk-of-bias technique; the AACODS checklist is used only for the four grey-literature records) and 13 (nothing accounted for) are flawed; items 11 and 15 do not apply (no meta-analysis)',
    pages='Science of the Total Environment, full text read (about 20 pages, line-numbered manuscript); the supplement with the full search terms was not read',
    ans={
        1: ('Yes', 'research questions on environmental health conditions in the transitional phase of forcible displacement, with population, setting and outcome defined in Tables 1 and 3'),
        2: ('No', 'CRITICAL FLAW: no protocol or registration is mentioned (PRISMA and the scoping framework are cited as guidance; the search strategy is taken from an earlier review by the same group)'),
        3: ('Yes', 'peer-reviewed and grey literature of any design that reports data on the transitional phase; the exclusion criteria are in Table 3 and follow two earlier scoping reviews'),
        4: ('Yes', 'PubMed, Web of Science, Scopus and EBSCOhost Global Health (searched 12 October 2017) plus grey sources (DisasterLit, IRC, UNICEF WASH, UNHCR, RAND, CDC, World Bank Water; 6 January 2018); search terms in Table 2 and the supplement; 10,324 peer-reviewed and 100 grey records'),
        5: ('Yes', 'five reviewers screened in Covidence; a study approved by two reviewers went to full-text review, and a third reviewer resolved disagreements; the same method was used at full text'),
        6: ('No', 'the data in Table 4 were extracted from the included papers, but duplicate extraction is not described'),
        7: ('No', 'CRITICAL FLAW: counts only (6,949 screened, 1,125 full texts assessed, 88 included); the excluded studies are not listed'),
        8: ('Yes', 'Table 4 lists the data extracted per paper (setting, population, health outcomes, risk factors, recommendations) and the results report counts by theme and setting'),
        9: ('No', 'CRITICAL FLAW: no risk-of-bias technique for the 84 peer-reviewed studies; the AACODS credibility checklist was applied to the four grey-literature records only'),
        10: ('No', 'funding sources of the included studies are not reported'),
        11: NA_ANS, 12: NA_ANS,
        13: ('No', 'CRITICAL FLAW: no appraisal, so quality is not considered when interpreting results; the limitations paragraph concerns missed terms and databases'),
        14: ('No', 'descriptive counts by theme, country and setting without a heterogeneity discussion'),
        15: ('No', 'not applicable: no quantitative synthesis; publication bias is not discussed'),
        16: ('No', 'a funding or conflict statement was ' + NOT_FOUND)},
    fields=dict(
        study_design='systematic scoping review (PRISMA and scoping framework; four databases plus grey literature, 2017-2018 searches; Covidence dual screening; thematic summary; no protocol located; no quality appraisal for peer-reviewed studies)',
        sample_size='10,324 peer-reviewed and 100 grey literature records identified; 6,949 after de-duplication screened by title and abstract; 1,125 full texts assessed; 88 transitional-phase studies included (4 grey literature records; earliest published 1946)',
        model_type='systematic scoping review with descriptive and thematic synthesis (no meta-analysis)'),
    note='Full-text appraisal 2026-10-04 from the PDF in the researcher\'s Drive inbox (supplement not read). Replaces the abstract-level entry and the 2026-09-28 "Not ratable" appraisal. Scoping review with systematic search and dual screening but no protocol, excluded-study list or quality appraisal.')
AM['S475'] = dict(
    rating='Critically Low',
    cit='Murebwayire ML, Nilsson E, Nhapi I, et al. (2025). A Systematic Review of Households\' Fecal Sludge Management Situation to Identify Gaps and Priority Actions in Kigali, Rwanda. Sustainability 17(17):7588',
    basis='critical items 2 (no protocol or registration located) and 7 (no list of excluded studies) are flawed; item 13 is also answered No because the quality ratings are reported but not used to weigh the findings in the text read; items 11 and 15 do not apply (no meta-analysis)',
    pages='Sustainability 17:7588, full text read (34 pages); the appendices (list of included publications, evaluation results) and the supplementary materials were not read',
    ans={
        1: ('Partial Yes', 'project convention: the question concerns household faecal sludge management in Kigali (population, topic and outcomes); no comparator'),
        2: ('No', 'CRITICAL FLAW: PRISMA 2020 is cited as a reporting guide; no protocol or registration is mentioned'),
        3: ('No', 'publications of any type from 2013 to 2024 were included (scientific and governmental sources); the choice of designs is not explained'),
        4: ('Partial Yes', 'Google, Google Scholar, ResearchGate, PubMed and ScienceDirect with keyword strings; 2013-2024; no explicit reference-list searching and no statement of search dates or full strategies'),
        5: ('Partial Yes', '270 publications were screened by two reviewers against the criteria; independence and the handling of disagreements are not described'),
        6: ('No', 'duplicate extraction is not described'),
        7: ('No', 'CRITICAL FLAW: PRISMA counts only (270 screened, 73 retained); excluded publications and those whose full text was not reached are not listed'),
        8: ('Partial Yes', 'all 73 included publications are listed in an appendix (not read); the text summarises them by theme'),
        9: ('Partial Yes', 'the adapted Newcastle-Ottawa Scale and JBI tools were used for 40 publications (17 high, 19 good, 1 satisfactory, 3 poor quality); the 33 government publications were not appraised with a risk-of-bias tool and were checked for authenticity only'),
        10: ('No', 'funding sources of the included publications are not reported'),
        11: NA_ANS, 12: NA_ANS,
        13: ('No', 'CRITICAL FLAW (conservative): the three poor-quality publications were kept because their findings aligned with high-quality studies, but the discussion does not weigh the findings by quality; the limitations section concerns the citywide focus and scarcity of literature'),
        14: ('No', 'themes are described; no heterogeneity discussion'),
        15: ('No', 'not applicable: no quantitative synthesis; publication bias is not discussed'),
        16: ('No', 'a funding or conflict statement was ' + NOT_FOUND)},
    fields=dict(
        study_design='systematic review (PRISMA 2020 screening; five search sources; adapted Newcastle-Ottawa Scale and JBI tools for 40 publications; thematic, descriptive and narrative synthesis; no protocol located)',
        sample_size='270 publications screened by two reviewers, 73 retained (2013-2024; scientific and governmental sources on sanitation in Kigali, Rwanda); 40 appraised with NOS or JBI tools, 33 government publications checked for authenticity only',
        model_type='systematic review with thematic narrative synthesis (no meta-analysis)'),
    note='Full-text appraisal 2026-10-04 from the PDF in the researcher\'s Drive inbox (appendices not read). Replaces the abstract-level entry and the 2026-09-28 "Not ratable" appraisal. A city-level review that mixes research articles and government documents; quality tools were applied to 40 of 73 publications.')
AM['S521'] = dict(
    rating='Critically Low',
    cit='Fono MA, Chapman F, Christie V, Parter C, Knight J, Sherriff S, Rambaldini UB, Moggridge B, Gwynne K (2025). Aboriginal and Torres Strait Islander Perspectives in Drinking Water Policy: A Realist Review. Australian Journal of Social Issues 60:602-620',
    basis='critical items 2 (no protocol or registration located) and 7 (no list of excluded studies) are flawed; item 9 is Partial Yes (JBI qualitative checklist plus a cultural assessment, rated independently by all authors) and item 13 is answered No because no use of the ratings in the interpretation was found; items 11 and 15 do not apply (no meta-analysis)',
    pages='Australian Journal of Social Issues 60:602-620, full text read (19 pages); Appendices A and B were not read',
    ans={
        1: ('Yes', 'realist review questions: how Aboriginal and Torres Strait Islander peoples are engaged in drinking water policy at macro, meso and micro levels, and which contextual factors and mechanisms influence it; population, concept and context are defined'),
        2: ('No', 'CRITICAL FLAW: no protocol or registration is mentioned; the programme theory was developed with the research team through yarning'),
        3: ('Yes', 'a realist review is justified for a complex policy question, and peer-reviewed studies and grey literature are both eligible with stated exclusion criteria'),
        4: ('Partial Yes', 'electronic databases with MeSH terms and keywords plus grey literature (government and organisation sources), English only unless translations were available; no reference-list searching or search dates were located; the limitations section says the search may have missed relevant studies'),
        5: ('Yes', 'screening by two authors with a third resolving discrepancies; authors 1 to 3 reviewed the full texts'),
        6: ('No', 'author 1 extracted the key data; duplicate extraction is not described'),
        7: ('No', 'CRITICAL FLAW: a PRISMA diagram with counts only; the excluded studies are not listed'),
        8: ('Partial Yes', 'the five peer-reviewed studies and 33 grey literature sources are described in Table 1 with their context'),
        9: ('Partial Yes', 'the planned CREATE tool did not fit; the five peer-reviewed studies were assessed with a cultural assessment and the JBI Critical Appraisal Checklist for Qualitative Research, rated independently by all authors and agreed by consensus (Appendix A); the 33 grey literature sources were not appraised with a risk-of-bias tool'),
        10: ('No', 'funding sources of the included studies are not reported'),
        11: NA_ANS, 12: NA_ANS,
        13: ('No', 'CRITICAL FLAW (conservative): no use of the quality ratings in the interpretation was located; the limitations concern the search'),
        14: ('Partial Yes', 'context-mechanism-outcome configurations are used to explain why engagement differs across settings (a realist synthesis); not framed as statistical heterogeneity'),
        15: ('No', 'not applicable: no quantitative synthesis; publication bias is not discussed'),
        16: ('Yes', 'funded by Macquarie University and the University of New South Wales (stated); the research team\'s positions are declared in a reflexivity statement')},
    fields=dict(
        study_design='realist review (programme theory developed through yarning; electronic databases and grey literature; two-author screening; JBI qualitative checklist and cultural assessment of the peer-reviewed studies; no protocol located)',
        sample_size='5 peer-reviewed studies and 33 grey literature sources included (Australia; Aboriginal and Torres Strait Islander engagement in drinking water policy), plus four local examples',
        model_type='realist review with context-mechanism-outcome synthesis (no meta-analysis)'),
    note='Full-text appraisal 2026-10-04 from the PDF in the researcher\'s Drive inbox (appendices not read). Replaces the abstract-level entry and the 2026-09-28 "Not ratable" appraisal. Realist review with a thin peer-reviewed base (five studies) and a larger grey literature base.')
AM['S537'] = dict(
    rating='Low',
    cit='Alam M-U, Rahat MA, Nawaz S, et al. (2025). Behaviour change interventions to promote household connectivity to sewer and their effectiveness: a scoping review. Global Health Action',
    basis='one critical flaw, item 7 (no list of excluded studies); item 2 is Partial Yes (a written protocol with questions, criteria and sources, not registered), item 4 is Partial Yes and item 9 is Partial Yes (an adapted JBI case-report checklist); items 11 and 15 do not apply (no meta-analysis)',
    pages='Global Health Action (2025), full text read (about 15 pages); Supplementary Tables S1 and S2 were not read',
    ans={
        1: ('Yes', 'households, sewer connection, behaviour change interventions, promotion and effectiveness are defined as the review elements; the outcome is the uptake of sewer connections'),
        2: ('Partial Yes', 'a written protocol specified the questions, inclusion and exclusion criteria, data sources and search engines (Supplementary Table S1); registration is not mentioned and no risk-of-bias plan is described'),
        3: ('Yes', 'case reports and programme reports of interventions were included and the eligibility criteria are justified (Supplementary Tables S1-S2)'),
        4: ('Partial Yes', 'PubMed, Cochrane, Scopus and ProQuest (via Hinari) searched independently by two reviewers (1980 to December 2022), plus grey literature (Google, Google Scholar, World Bank, WSUP, Practical Action, WaterAid; first 300 results); English only; no reference-list searching reported'),
        5: ('Yes', 'three authors screened titles and abstracts collaboratively in Rayyan and disagreements were resolved among two reviewers with a third approving'),
        6: ('No', 'a data extraction form was created, but duplicate extraction is not described'),
        7: ('No', 'CRITICAL FLAW: the flow diagram gives counts only; the excluded studies are not listed'),
        8: ('Partial Yes', 'the eleven included cases are described by programme, country and intervention in the results tables'),
        9: ('Partial Yes', 'an adapted JBI Critical Appraisal Checklist for Case Reports with eight criteria scored 1, 0.5 or 0 (high at 6 or more, moderate at 4-5, low below 4); the adaptation is not a validated instrument'),
        10: ('No', 'funding sources of the included cases are not reported'),
        11: NA_ANS, 12: NA_ANS,
        13: ('Yes', 'the limitations paragraph states that the evidence rests on eleven cases with no randomised trial and that this limits the quality of the evidence'),
        14: ('Partial Yes', 'differences between programmes (free connection, subsidies, community engagement) are discussed as explanations of different uptake'),
        15: ('No', 'not applicable: no quantitative synthesis; publication bias is not discussed'),
        16: ('Yes', 'no potential conflict of interest was reported by the authors (stated); the funding statement was ' + NOT_FOUND)},
    fields=dict(
        study_design='scoping review (PRISMA-ScR; written protocol, unregistered; four databases plus grey literature; adapted JBI case-report checklist; narrative synthesis; eleven cases)',
        sample_size='eleven cases of behaviour change interventions to increase sewer connection included (searches 1980 to December 2022; peer-reviewed and grey literature; no randomised trial)',
        model_type='scoping review with narrative synthesis (no meta-analysis)'),
    note='Full-text appraisal 2026-10-04 from the PDF in the researcher\'s Drive inbox (supplementary tables not read). Replaces the earlier "Not ratable" entry. The only AMSTAR 2 critical flaw found is the missing list of excluded studies, which gives a Low rating.')


def m_ed(rows):
    done = []
    for r in rows:
        sid = r['study_id']
        if sid not in AM:
            continue
        a = AM[sid]
        if r['risk_of_bias_rating'].startswith(a['rating'] + ' (appraised ' + DATE):
            continue
        assert r['risk_of_bias_rating'].startswith('Not ratable') and r['risk_of_bias_tool'].replace(' ', '').startswith('AMSTAR2'), sid
        for k, v in a['fields'].items():
            assert k in r, k
            r[k] = v
        r['risk_of_bias_rating'] = (f"{a['rating']} (appraised {DATE} against the official AMSTAR 2 checklist on the full text; item-level answers in 04_quality/appraisal_forms/{sid}_AMSTAR2.md; {a['basis']}). "
                                    "Supersedes the earlier 'Not ratable' entry; eligibility as a systematic review confirmed from the methods text.")
        for k in ('selection_bias', 'measurement_bias', 'confounding', 'attrition', 'reporting_bias'):
            r[k] = NAS.format(sid=sid)
        r['extraction_note'] = a['note'] + ' record_id ' + r['record_id'] + '.'
        r['researcher'] = 'Claude-AI-extraction-2026-10-04 (full-text appraisal)'; r['date_extracted'] = DATE
        done.append(sid)
        L = [f"# AMSTAR 2 appraisal (full text) — {sid}", "", f"**Citation:** {a['cit']}", "",
             f"**Date appraised:** {DATE} · **Appraiser:** Claude-AI-appraisal-{DATE} · **Basis:** the full-text copy in the researcher's Drive inbox (not committed): {a['pages']}. Supplementary files and appendices were **not read**. Supersedes the earlier abstract-level or partial pilot appraisal.", "",
             f"**Overall confidence: {a['rating']}** — {a['basis']}. Critical items: 2, 4, 7, 9, 11, 13, 15.", "",
             "| # | Critical? | Item | Answer | Basis (from the text read) |", "|---|---|---|---|---|"]
        for i, name in ITEMS.items():
            ans, why = a['ans'][i]
            L.append(f"| {i} | {'**Yes**' if i in CRIT else 'No'} | {name} | {ans}{' (n/a)' if i in NA_ITEMS else ''} | {why} |")
        L += ["", "Method note: where the text is silent the answer is No (AMSTAR 2's own convention). AMSTAR 2 rating rule: no critical flaw = High or Moderate; one critical flaw = Low; more than one = Critically Low. A 'Partial Yes' is not a flaw; items 11, 12 and 15 do not apply without a meta-analysis. Items 13 and 16 marked conservative or 'not located' rest on the extracted text, which can omit front and back matter."]
        open(f'04_quality/appraisal_forms/{sid}_AMSTAR2.md', 'w', encoding='utf-8').write("\n".join(L) + "\n")
    return done


A22_FIELDS = ['record_id', 'study_id', 'authors_year', 'title', 'current_decision', 'full_text_read', 'empirical', 'ai_verdict_on_full_text', 'confidence', 'what_decides_it']
A22_ROWS = [dict(
    record_id='R6739F4D885E3', study_id='S297', authors_year='Jones 2015 (International Journal of the Commons 9(1):65-86)',
    title='Bridging political economy analysis and critical institutionalism: an approach to help analyse institutional change for rural water services',
    current_decision='include', full_text_read='yes, 22 pages (journal PDF)',
    empirical='partly: one illustrative case of the NGO WaterAid and its partners in Mali, drawing on collaborative research in 2010 and 2011 with a few dated interviews quoted; the paper says it focuses on the conceptual approach and that the key data are in other publications (Jones 2013a, 2013b)',
    ai_verdict_on_full_text='borderline on criterion 3: the contribution is a framework; the Mali case illustrates it and the empirical base (number of interviews, methods) is not reported here. The institutional topic fits criterion 2 (financing institutions for rural water services)',
    confidence='low', what_decides_it='whether the project accepts a conceptual paper with an illustrative case as an empirical design; the other Jones papers (the data sources) could be screened instead of or with this one')]


def write_a22():
    with open(A22V, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=A22_FIELDS, lineterminator='\r\n'); w.writeheader(); w.writerows(A22_ROWS)
    return len(A22_ROWS)


print('AMSTAR 2 appraised:', rw(ED, m_ed) or 'nothing new')
print('A22 verdict rows written:', write_a22())
