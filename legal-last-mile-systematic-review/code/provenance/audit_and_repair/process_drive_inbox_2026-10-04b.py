"""2026-10-04 (night): third Drive-inbox batch (88 files dropped in the 'Sep 26 2026' folder). What this dated script records for the first tier (the PDFs were read in the session;
nothing is copied into the repository):
  * FULLTEXT_VERIFICATION_2026-10-04.csv: S057, S084, S085, S149, S445, S483, S491 compared with the papers (all verified); S057's effect-size row also gets the sample the first
    pass could not locate (30 villages, 2,821 sales presentations).
  * AMSTAR 2 on the full text for the four reviews that were still 'Not ratable': S019 (Ilangovan 2026), S116 (Castleden 2017), S323 (Osisiogu 2024, a scoping review) and
    S329 (Sohns 2019, a narrative review with a systematic search). All four are Critically Low (critical items 2, 7, 9 and 13 flawed); item-level answers go to
    04_quality/appraisal_forms/S0xx_AMSTAR2.md and the extraction rows are upgraded from the abstract-level entry.
  * A19 re-screen verdicts for the four A19 records whose full text arrived (R0B0F3925F533, R977ECB01FA02, RC9378CBDB2EE, RFC362FE42028): written as proposals to
    02_screening/full_text/A19_RESCREEN_VERDICTS_2026-10-04.csv. No decision is changed (the criterion 2 scope reading is still the researcher's call, A16/A19).
Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
DATE = '2026-10-04'
ED = '03_extraction/extracted_data/extraction_database.csv'
ES = '05_analysis/effect_sizes/effect_sizes.csv'
VER = '05_analysis/effect_sizes/FULLTEXT_VERIFICATION_2026-10-04.csv'
A19V = '02_screening/full_text/A19_RESCREEN_VERDICTS_2026-10-04.csv'


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


# ---------------------------------------------------------------- effect-size verification
SRC = 'Drive inbox full text (2026-10-04 night)'
VERIFIED = {
    'S057': ('2', '2', '', 'verified', 'abstract and results: subsidy offer raised the sales closing rate among eligible households by 32 percentage points (the highlights say 31%); 38% eligible vs 6% ineligible in treatment areas (p = 0.00); control areas 8% vs 6% (p = 0.32); 30 villages (23 climate-vulnerable), 2,821 sales presentations'),
    'S084': ('6', '6', '', 'verified', 'Table 3 multivariate model (N = 593 households, 283 notified and 310 non-notified): non-notified -37.3% litres per capita per day (95% CI -46.4 to -26.5, p < 0.001); univariate -38.2%; mediators explain 38.7% of the association (23.4% fewer remains)'),
    'S085': ('4', '4', '', 'verified', 'Table 1 column 4 (eligible-lands sample, N = 5,251; full sample 6,652): T1 x T2 interaction 0.22 (SE 0.10, p = 0.04); the text gives the T1 effect of 19 percentage points (p = 0.001) when T2 is also assigned, 45% of the control mean'),
    'S149': ('6', '6', '', 'verified', 'abstract: 400 rural households in four Odisha districts; women\'s VWSC participation improved toilet functionality by 24.8%, cut water-collection time by 31.4 minutes and lowered illness incidence by 12.7%; GWII score 0.357'),
    'S445': ('12', '12', '', 'verified', 'web-article text (Portuguese, decimal commas): 56,544 rural public elementary schools in 2011 and 34,406 in 2023; North region vs Centre-West, water supply OR 2.58 (2011) and 6.40 (2023), sanitation OR 3.32 and 5.48, bathroom OR 5.17 (2023), all p < 0.001'),
    'S483': ('13', '13', '', 'verified', 'Table 4: 2,380 itineraries; high-income RR 5.78 (5.34-6.25), middle-income 3.80 (3.52-4.10), middle/low-income 1.65 (1.53-1.79), reference low-income, all p < 0.001'),
    'S491': ('7', '7', '', 'verified', 'Table 5: households that do not normally buy water OR 2.125 (95% CI 1.581-2.857, p < 0.001) for being unwilling to pay during the lockdown; 1,639 households'),
}


def m_ver(rows):
    n = 0
    for r in rows:
        if r['study_id'] in VERIFIED and r['verdict'] == 'not_checked':
            a, b, c, v, note = VERIFIED[r['study_id']]
            r['numbers_in_row'], r['numbers_found_in_text'], r['numbers_not_found'] = a, b, c
            r['source_text'] = SRC; r['verdict'] = v; r['note'] = note
            n += 1
    return n


OLD_S057_N = 'clustered RCT; exact n not located in extracted text (see extraction_database.csv S057 note)'
NEW_S057_N = 'clustered RCT; 30 villages in Kampong Chhnang province, Cambodia (23 climate-vulnerable; treatment and control halves), 2,821 sales presentations (full text read 2026-10-04)'


def m_es(rows):
    for r in rows:
        if r['study_id'] == 'S057' and r['sample_size'] == OLD_S057_N:
            r['sample_size'] = NEW_S057_N
            r['provenance_note'] += ' Full text read 2026-10-04: the abstract gives the effect as 32 percentage points and the highlights as 31%; both are reported here as in the text (process_drive_inbox_2026-10-04b.py).'
            return 'S057 sample enriched'
    return 'S057 already enriched'


# ---------------------------------------------------------------- AMSTAR 2
ITEMS = {1: 'PICO components in the research questions and inclusion criteria', 2: 'Review methods established prior to the review (protocol); deviations justified',
         3: 'Selection of study designs explained', 4: 'Comprehensive literature search strategy', 5: 'Study selection in duplicate', 6: 'Data extraction in duplicate',
         7: 'List of excluded studies with justification', 8: 'Included studies described in adequate detail', 9: 'Satisfactory technique for risk of bias in included studies',
         10: 'Funding sources of included studies reported', 11: 'Appropriate meta-analytic methods', 12: 'Impact of risk of bias on meta-analysis results',
         13: 'Risk of bias accounted for when interpreting results', 14: 'Heterogeneity explained and discussed', 15: 'Publication bias investigated (quantitative synthesis)',
         16: 'Conflicts of interest and funding of the review reported'}
CRIT = {2, 4, 7, 9, 11, 13, 15}
NA_ITEMS = {11, 12, 15}
RATING = 'Critically Low'
NAS = 'Not applicable to AMSTAR 2 domains; item-level appraisal in 04_quality/appraisal_forms/{sid}_AMSTAR2.md (full text, ' + DATE + ')'
NA_ANS = ('No', 'not applicable: no meta-analysis (narrative synthesis); not counted as a flaw')

AM = {}
AM['S019'] = dict(
    cit='Ilangovan K, Sankar JG, Srinivasan M (2026) Systematic review of rural drinking water interventions under Jal Jeevan Mission. Discover Environment 4:189',
    basis='critical items 2 (no protocol), 7 (no list of excluded studies), 9 (no risk-of-bias technique) and 13 (risk of bias not accounted for) are flawed; item 4 is borderline (search stopped at 20 Google Scholar results); items 11 and 15 do not apply (no meta-analysis)',
    pages='Discover Environment, 15 pages read; the PRISMA figure and the study table were not read as images',
    ans={
        1: ('Partial Yes', 'project convention: objectives name the population (rural households), the intervention (Jal Jeevan Mission tap connections) and the focus (equitable water access); no comparator'),
        2: ('No', 'CRITICAL FLAW: no protocol or registration is mentioned; PRISMA 2020 is cited only as a reporting guide'),
        3: ('No', 'articles, review papers and book chapters were accepted; the choice of designs is not explained'),
        4: ('Partial Yes', 'BORDERLINE: eight sources (Google Scholar, Scopus, ScienceDirect, Sage, Taylor & Francis, DOAJ, Elsevier, ResearchGate), four to five keyword strings, backward and forward citation search (8 papers); but only 62 records, English only (not justified) and a stopping rule that limits Google Scholar to the first 20 relevant articles'),
        5: ('Yes', 'titles and abstracts were screened independently by the authors, disagreements resolved by discussion'),
        6: ('No', 'coding in NVivo was reviewed by all authors, but independent duplicate extraction is not described'),
        7: ('No', 'CRITICAL FLAW: PRISMA counts only (70 records, 24 after de-duplication, 4 excluded at full text with grouped reasons); the excluded studies are not listed'),
        8: ('Partial Yes', 'distribution by year, journal, author, research approach, method, sampling and sample size is reported; per-study populations and outcomes are summarised only in the thematic text'),
        9: ('No', 'CRITICAL FLAW: the quality assessment was "assigned to the three authors" but no tool or criteria are given beyond inclusion of articles from reliable and reputed journals and books'),
        10: ('No', 'funding sources of the included studies are not reported'),
        11: NA_ANS, 12: NA_ANS,
        13: ('No', 'CRITICAL FLAW: with no risk-of-bias assessment, nothing is accounted for when interpreting the findings; the limitations (English only, secondary data, no field evidence) do not address study quality'),
        14: ('No', 'differences between included studies (regions, programme stages) are described but no heterogeneity discussion explains the findings'),
        15: ('No', 'not applicable: no quantitative synthesis; publication bias is not discussed'),
        16: ('Yes', 'funded by the Indian Council of Social Science Research (stated); no competing interests declared')},
    fields=dict(
        publication_type='journal article (systematic review, Discover Environment 4:189, open access)',
        population='rural households under India\'s Jal Jeevan Mission (JJM) functional household tap connection programme, as studied in 20 included articles (2002-May 2025)',
        sample_size='70 records identified (62 by database search, 8 by backward and forward citation search), 24 after de-duplication, 4 excluded at full text, 20 included; no meta-analysis',
        effect_measure='narrative thematic synthesis (NVivo 12); no pooled estimate',
        effect_estimate=('Reported findings (not appraised): easy tap access reduces the time and effort of women and indirectly empowers them; employment is generated in infrastructure building and maintenance; '
                         'universal access is linked to fewer waterborne diseases; regional disparities recur (drought-prone districts such as Raichur and Ballari in Karnataka and parts of Jharkhand still struggle); '
                         'implementation challenges are infrastructure quality, leakage, administrative inefficiency and delay; Gram Panchayat and community involvement in labour mobilisation and local contributions is associated with better maintenance. '
                         'Recommendations: post-installation monitoring, routine water-quality testing, dedicated operation-and-maintenance funding, and stronger decentralised governance.'),
        study_design='systematic review (PRISMA 2020 reporting; thematic synthesis of 20 articles; no protocol; no quality-appraisal tool; Google Scholar results capped at 20)',
        model_type='systematic review with narrative thematic synthesis (no meta-analysis)',
        section='Abstract; Methods 2-4.1; Findings 5; Discussion and Conclusion (full text)',
        exact_location='Methods 3.1-3.9 pp. 3-5 (search, screening, stopping rule, quality assessment paragraph); 4 and 4.1 pp. 5-6 (extraction and NVivo synthesis); Conclusion (themes and regional disparities)'),
    note=('Full-text appraisal 2026-10-04 from the open-access PDF in the researcher\'s Drive inbox (15 pages read). Replaces the abstract-level entry of 2026-09-12 and the 2-of-16-item pilot of 2026-09-16. '
          'No protocol, no excluded-study list, no quality-appraisal technique; the synthesis covers 20 articles on one national programme. Governance content: Gram Panchayat and community participation, administrative delay and decentralised implementation are narrative findings, not estimated effects.'))

AM['S116'] = dict(
    cit='Castleden HE, Hart C, Harper S, Martin D, Cunsolo A, Stefanelli R, Day L, Lauridsen K (2017). Implementing Indigenous and Western Knowledge Systems in Water Research and Management (Part 1): A Systematic Realist Review to Inform Water Policy and Governance in Canada. The International Indigenous Policy Journal 8(4)',
    basis='critical items 2 (no protocol; PRISMA-P is cited as a reference only), 7 (no list of excluded studies), 9 (relevance rating only, no risk-of-bias technique) and 13 (risk of bias not accounted for) are flawed; items 11 and 15 do not apply (no meta-analysis); the search (item 4) is rated Partial Yes',
    pages='International Indigenous Policy Journal 8(4):6, 26 pages read; figures not read as images',
    ans={
        1: ('Partial Yes', 'project convention: purpose, population (Indigenous peoples in Canada), concept (integrative Indigenous and Western knowledge in water research and management) and four reflective questions are stated; no comparator'),
        2: ('No', 'CRITICAL FLAW: criteria were co-determined with a National Advisory Committee, but no protocol or registration is described (the PRISMA-P reference is not a protocol)'),
        3: ('Yes', 'a combined systematic and realist design is justified, and empirical and non-empirical items are separated by a 0-3 relevance scale and four reflective questions'),
        4: ('Partial Yes', 'Scopus, Web of Science and Google Scholar with keyword strings in Table 1 (refined with a reference librarian), plus grey literature (Library and Archives Canada, two government sites, first 50 Google hits); replicate search Oct 2014-Aug 2015; English only; no reference-list searching reported'),
        5: ('Yes', 'two independent reviewers screened titles and abstracts; meetings held until all agreed; full-text review when unclear'),
        6: ('No', 'the 33-question Reporting Tool was completed by three team members, each on a share of the literature (First Nations, Inuit, Métis, multi-site); duplicate extraction is not described'),
        7: ('No', 'CRITICAL FLAW: counts are given (279 reviewed, 63 included, 64 peer-reviewed excluded) but the excluded studies are not listed'),
        8: ('Partial Yes', 'descriptive data by year, article type, authorship, funding and discipline, and the Reporting Tool fields are given; per-item characteristics are reported in aggregate, not item by item'),
        9: ('No', 'CRITICAL FLAW: relevance, not quality, was rated; no risk-of-bias technique is applied to the 63 items'),
        10: ('Yes', 'the funding agency of each item is a Reporting Tool field (question 12) and is summarised'),
        11: NA_ANS, 12: NA_ANS,
        13: ('No', 'CRITICAL FLAW: findings are interpreted without regard to the quality of the 63 items (academic and grey literature, including reports and theses)'),
        14: ('No', 'differences by Nation group and context are described, but heterogeneity is not discussed as an explanation of findings'),
        15: NA_ANS,
        16: ('No', 'funding by the Canadian Water Network is acknowledged; no conflict-of-interest statement was found in the text read')},
    fields=dict(
        publication_type='journal article (systematic realist review, International Indigenous Policy Journal 8(4):6)',
        population='Indigenous (First Nations, Inuit, Métis) peoples in Canada; 63 included items (40 peer-reviewed articles, 12 reports, 11 theses and dissertations) of 279 reviewed',
        sample_size='226 peer-reviewed records after the title and abstract search (Scopus, Web of Science, Google Scholar) -> 40 included; grey literature 13 theses/dissertations and 40 reports retrieved (2 reports inaccessible) -> 12 reports and 11 theses included; 279 reviewed, 63 included',
        effect_measure='realist narrative synthesis with a 33-question Reporting Tool; no pooled estimate',
        effect_estimate=('Reported findings (not appraised): an emerging trend of literature (71% published after 2009, surge in 2013); 24% of first authors identified as Indigenous and 61% of items described non-Indigenous researchers working in partnership with Indigenous communities; '
                         'much of the literature calls for the rejection of tokenism and for respectful nation-to-nation relationships in water research, management and policy; barriers include language and translation, the lack of Indigenous voices in water decision-making and the unequal weight given to Western science; '
                         'only one item reported written agreements ceding Aboriginal rights to resources, and other items state that the federal government does not actively support such agreements; recommendations include enforceable water laws co-created with First Nations and culturally sensitive operator certification.'),
        study_design='systematic review (realist review methodology; narrative synthesis of 63 items from academic and grey literature; no protocol; no quality appraisal)',
        model_type='systematic realist review (academic and grey literature synthesis)',
        section='Abstract; Methods (Data Collection, Data Analysis, Tables 1-3); Findings; Discussion; Limitations (full text)',
        exact_location='Methods pp. 3-6 (search, screening, 0-3 relevance scale, Reporting Tool); Findings p. 11 (279 reviewed, 63 included) and pp. 13-17 (context, purpose, mechanisms, outcomes); Limitations p. 22'),
    note=('Full-text appraisal 2026-10-04 from the PDF in the researcher\'s Drive inbox (26 pages read). Replaces the abstract-level entry of 2026-09-15 and the 3-of-16-item pilot of 2026-09-16. '
          'The review is about the integration of Indigenous and Western knowledge in water research and governance in Canada; access outcomes are context, so its contribution is mechanism evidence on governance (nation-to-nation relationships, consultation, co-created law), not an access estimate.'))

AM['S323'] = dict(
    cit='Osisiogu EU, Akinrotoye KP, Banini AE, Amemo RE (2024). A Systematic Scoping Review of Access to Safe Drinking Water in Sub-Saharan Africa: Mapping Literature on Determinants, Interventions, and Policy Implications over the Past Decade and the Path Forward. Ethiop J Health Sci 34(5):413-420',
    basis='critical items 2 (no protocol), 7 (no list of excluded studies), 9 (no risk-of-bias technique) and 13 (risk of bias not accounted for) are flawed; items 11 and 15 do not apply (no meta-analysis). Caveat: a scoping review (Arksey and O\'Malley, JBI) deliberately omits quality appraisal, which AMSTAR 2 was not designed to accommodate; the rating reflects AMSTAR 2 conventions, not a fault specific to the authors',
    pages='Ethiop J Health Sci 34(5) (PMC html version, 8 pages of text read; tables and the PRISMA figure not available in the copy)',
    ans={
        1: ('Partial Yes', 'population (people in sub-Saharan Africa), concept (access to safe drinking water) and context (determinants and interventions or policies) are stated in the JBI PCC format; no comparator'),
        2: ('No', 'CRITICAL FLAW: the review follows Arksey and O\'Malley and the JBI framework but no protocol or registration is mentioned'),
        3: ('Yes', 'peer-reviewed quantitative, qualitative and mixed-methods research, reviews and grey literature were all eligible; a scoping design justifies the breadth'),
        4: ('Partial Yes', 'PubMed, Embase, CINAHL, Web of Science, Scopus and Engineering Village; grey literature from WHO, UNICEF, USAID, World Bank and African government sites; PubMed strategy peer-reviewed against the PRESS checklist; English only, 2013 onward; no reference-list searching reported'),
        5: ('Yes', 'title/abstract and full-text screening by two independent reviewers, disagreements resolved by discussion'),
        6: ('Yes', 'a data extraction form was piloted; extraction by two independent reviewers with consensus'),
        7: ('No', 'CRITICAL FLAW: a PRISMA flow diagram gives exclusion counts and reasons; the excluded studies are not listed'),
        8: ('Partial Yes', 'study details, designs, locations and populations are summarised with descriptive statistics, but included studies are not described one by one in the text read'),
        9: ('No', 'CRITICAL FLAW: no quality appraisal (consistent with scoping-review practice, but AMSTAR 2 still counts it)'),
        10: ('No', 'funding sources of the included studies are not reported'),
        11: NA_ANS, 12: NA_ANS,
        13: ('No', 'CRITICAL FLAW: findings are counted and interpreted without any consideration of study quality'),
        14: ('No', 'variation across countries and designs is described, but heterogeneity is not discussed as a limit on the conclusions'),
        15: NA_ANS,
        16: ('Yes', 'funding: nil; competing interests declared (none)')},
    fields=dict(
        publication_type='journal article (systematic scoping review, Ethiopian Journal of Health Sciences 34(5):413-420)',
        population='people in sub-Saharan Africa; 137 included studies (peer-reviewed quantitative, qualitative and mixed-methods research, reviews and grey literature, 2013 onward)',
        sample_size='2,345 database records plus 37 grey-literature records identified; 137 studies included; no meta-analysis',
        effect_measure='narrative and thematic synthesis with study counts per determinant and intervention; no pooled estimate',
        effect_estimate=('Reported counts (not appraised), determinants of safe-water access: droughts or seasonal rainfall 38 studies; conflict 24; governance issues such as corruption 31; insufficient government prioritisation 44; '
                         'gender 17; wealth and education 29; poverty 43; water affordability 38; inadequate infrastructure 62; distance and time to source 49. Interventions and policies: infrastructure expansion 38 studies; community-based decentralised management 32; '
                         'water quality monitoring 24; governance reforms (corruption, budgets) 20; targeted subsidies and tariff models 18; watershed management 15; integrated WASH and water resources management 14; gender-transformative approaches 13; '
                         '23 studies noted that interventions often fail because comprehensive approaches are not adopted. Most studies described barriers rather than evaluating solutions.'),
        study_design='systematic scoping review (Arksey and O\'Malley and JBI frameworks; narrative synthesis of 137 studies; no protocol; no quality appraisal)',
        model_type='systematic scoping review with narrative synthesis (no meta-analysis)',
        section='Abstract; Methods; Results (determinants, interventions and policies); Discussion (full text)',
        exact_location='Methods (eligibility, information sources, screening, extraction, synthesis); Results paragraphs on determinants (environmental, political, social, economic, infrastructural) and on interventions and policies'),
    note=('Full-text appraisal 2026-10-04 from the PMC html copy in the researcher\'s Drive inbox (the PRISMA figure and tables were not in the copy). Replaces the abstract-level entry of 2026-09-15 and the empty pilot of 2026-09-16. '
          'Governance content: governance and corruption (31 studies), insufficient prioritisation by government (44), governance reforms and decentralised community-based management (20 and 32) are counted as determinants or interventions; counts are not effect sizes.'))

AM['S329'] = dict(
    cit='Sohns A, Ford JD, Riva M, Robinson B, Adamowski J (2019). Water Vulnerability in Arctic Households: A Literature-based Analysis. Arctic 72(3):300-316',
    basis='critical items 2 (no protocol), 7 (no list of excluded studies), 9 (no risk-of-bias technique) and 13 (risk of bias not accounted for) are flawed; items 11 and 15 do not apply (no meta-analysis). The paper calls itself a narrative review with a systematic search, so it is a hybrid case (see the 2026-09-28 eligibility note)',
    pages='Arctic 72(3):300-316, 17 pages read; the supplementary tables (S1 search terms, S2 code book) are not in the PDF',
    ans={
        1: ('Partial Yes', 'project convention: the aim (factors affecting household water vulnerability in the Arctic) and the population (households, Arctic region as defined by the AHDR 2015) are stated; no comparator'),
        2: ('No', 'CRITICAL FLAW: no protocol or registration is mentioned'),
        3: ('No', 'peer-reviewed articles, reviews, book chapters, proceedings papers and meeting abstracts were accepted without explaining the choice of designs'),
        4: ('Partial Yes', 'Scopus and Web of Science searched on 1 March 2018 with terms in Table S1; documents from 2000 on, English only (stated as a limitation); no grey literature, reference lists or expert consultation'),
        5: ('No', 'who screened the 722 abstracts and the full texts is not stated; duplicate selection is not shown'),
        6: ('No', 'a code book was piloted and coded in Atlas.ti; duplicate coding is not described'),
        7: ('No', 'CRITICAL FLAW: counts are given (831 records, 109 duplicates, 722 screened, 123 excluded on the abstract by criterion 5) but the excluded studies are not listed'),
        8: ('Partial Yes', 'documents are described by country (Canada 43%, Alaska 30%, Russia 10%), year, journal (66 journals) and framing; per-document details are only in the supplement'),
        9: ('No', 'CRITICAL FLAW: no risk-of-bias or quality technique is applied; documents were coded for factors, not appraised'),
        10: ('No', 'funding sources of the included documents are not reported'),
        11: NA_ANS, 12: NA_ANS,
        13: ('No', 'CRITICAL FLAW: findings (counts of documents that mention a factor) are interpreted without regard to the quality of the documents, which include meeting abstracts and a thesis'),
        14: ('No', 'the diversity of regions and document types is described, but heterogeneity is not discussed as a limit on the conclusions'),
        15: NA_ANS,
        16: ('No', 'funding from the Canadian Institutes of Health Research and ArcticNet is acknowledged; no conflict-of-interest statement was found in the text read')},
    fields=dict(
        publication_type='journal article (narrative review with a systematic search, Arctic 72(3):300-316)',
        population='households in the Arctic (AHDR 2015 definition); 112 documents (peer-reviewed articles, reviews, book chapters, proceedings papers, meeting abstracts), 2000-March 2018; Canada 48 (43%), Alaska 34 (30%), Russia 12 (10%), others fewer',
        sample_size='Web of Science 662 and Scopus 260 records; 831 combined, 109 duplicates, 722 screened; 123 excluded on the abstract (criterion 5); 112 documents analysed; no meta-analysis',
        effect_measure='deductive and inductive thematic coding (Atlas.ti) with counts of documents per factor; no pooled estimate',
        effect_estimate=('Reported findings (not appraised): seven themes in two categories, biophysical (climate change impacts on freshwater supplies and systems dominate, then extreme weather and seasonality) and anthropogenic '
                         '(infrastructure the primary issue affecting access, then economic, governance, socio-cultural and demographic factors). Governance and policy issues (limited local capacity, funding that does not match responsibilities, exclusion of Indigenous groups from engineered systems and legal frameworks) were highlighted in 25 papers (22%); '
                         '35 papers (31%) stated that lack of funding for water systems is a major concern; limited data were referenced by 39 documents (35%).'),
        study_design='narrative review with a systematic search (Scopus and Web of Science; 112 documents; thematic coding; no protocol; no quality appraisal)',
        model_type='narrative review with systematic search (no meta-analysis)',
        section='Abstract; Methods (search process and document selection, analysis); Results and Discussion; Conclusion (full text)',
        exact_location='Methods pp. 301-302 (search terms, inclusion criteria 1-6, exclusions, selection counts, coding); Results pp. 302-311 (description of studies, biophysical and anthropogenic factors); Conclusion p. 313'),
    note=('Full-text appraisal 2026-10-04 from the PDF in the researcher\'s Drive inbox (17 pages read; supplement not available). Replaces the abstract-level entry of 2026-09-15 and the metadata-only appraisal of 2026-09-28. '
          'Correction to the earlier entry: the review is pan-Arctic (Canada, Alaska, Russia, Nordic countries), not Canada alone. The review is a hybrid (narrative review with a systematic search) and is kept under AMSTAR 2 as in the 2026-09-28 eligibility note.'))


def m_ed(rows):
    done = []
    for r in rows:
        sid = r['study_id']
        if sid not in AM:
            continue
        a = AM[sid]
        if r['risk_of_bias_rating'].startswith(RATING + ' (appraised ' + DATE):
            continue
        assert r['risk_of_bias_rating'].startswith('Not ratable') and r['risk_of_bias_tool'].replace(' ', '').startswith('AMSTAR2'), sid
        for k, v in a['fields'].items():
            assert k in r, k
            r[k] = v
        if sid == 'S329':
            r['country'] = 'Arctic (Canada, Alaska, Russia, Nordic countries; pan-Arctic review)'
            r['sample_size'] = a['fields']['sample_size']
        r['risk_of_bias_rating'] = (f"{RATING} (appraised {DATE} against the official AMSTAR 2 checklist on the full text; item-level answers in 04_quality/appraisal_forms/{sid}_AMSTAR2.md; {a['basis']}). "
                                    "Supersedes the earlier 'Not ratable' entry; eligibility as a systematic review confirmed from the methods text.")
        for k in ('selection_bias', 'measurement_bias', 'confounding', 'attrition', 'reporting_bias'):
            r[k] = NAS.format(sid=sid)
        r['extraction_note'] = a['note'] + ' record_id ' + r['record_id'] + '.'
        r['researcher'] = 'Claude-AI-extraction-2026-10-04 (full-text appraisal)'; r['date_extracted'] = DATE
        done.append(sid)
        L = [f"# AMSTAR 2 appraisal (full text) — {sid}", "", f"**Citation:** {a['cit']}", "",
             f"**Date appraised:** {DATE} · **Appraiser:** Claude-AI-appraisal-{DATE} · **Basis:** the full-text copy in the researcher's Drive inbox (not committed): {a['pages']}. Supplementary files were **not read**. Supersedes the earlier abstract-level or partial pilot appraisal.", "",
             f"**Overall confidence: {RATING}** — {a['basis']}. Critical items: 2, 4, 7, 9, 11, 13, 15.", "",
             "| # | Critical? | Item | Answer | Basis (from the text read) |", "|---|---|---|---|---|"]
        for i, name in ITEMS.items():
            ans, why = a['ans'][i]
            L.append(f"| {i} | {'**Yes**' if i in CRIT else 'No'} | {name} | {ans}{' (n/a)' if i in NA_ITEMS else ''} | {why} |")
        L += ["", "Method note: where the text is silent the answer is No (AMSTAR 2's own convention). AMSTAR 2 rating rule: no critical flaw = High or Moderate; one critical flaw = Low; more than one = Critically Low. A 'Partial Yes' is not a flaw; items 11, 12 and 15 do not apply without a meta-analysis and are not counted.", ""]
        open(f'04_quality/appraisal_forms/{sid}_AMSTAR2.md', 'w', encoding='utf-8').write("\n".join(L) + "\n")
    return done


# ---------------------------------------------------------------- A19 re-screen verdicts
A19_FIELDS = ['record_id', 'authors_year', 'title', 'current_decision', 'full_text_read', 'water_service_access', 'institutional_factor', 'empirical', 'access_outcome',
              'ai_verdict_on_full_text', 'confidence', 'what_decides_it']
A19_ROWS = [
    dict(record_id='R0B0F3925F533', authors_year='Rahayu, Woltjer & Firman 2019 (Urban Studies 56(14):2917-2934)', title='Water governance in decentralising urban Indonesia',
         current_decision='exclude E01', full_text_read='yes, 18 pages (Groningen repository copy, publisher PDF)',
         water_service_access='partly: the city of Cirebon depends on piped water from springs in Kuningan District; the cooperation agreements and a crisis in which the district closed a gate valve are about continuity of that supply',
         institutional_factor='yes: decentralisation, a memorandum of understanding, conservation payments, informal and discretionary inter-local arrangements',
         empirical='yes: interviews and documents on three episodes of cooperation',
         access_outcome='no household access measure; the outcome is institutional capacity for regional water-resource coordination (one episode touches supply continuity)',
         ai_verdict_on_full_text='borderline: exclude stands under the narrow reading (no access outcome, E04 would fit better than E01); would be a candidate include under the broad reading of criterion 2 as an empirical governance study of urban water supply continuity',
         confidence='low', what_decides_it='the criterion 2 scope reading (decision 12 / A16); under the narrow reading change the code to E04'),
    dict(record_id='R977ECB01FA02', authors_year='Milgroom, Giller & Leeuwis 2014 (Human Ecology 42(2):199-215)', title='Three Interwoven Dimensions of Natural Resource Use: Quantity, Quality and Access in the Great Limpopo Transfrontier Conservation Area',
         current_decision='exclude E01', full_text_read='yes, 17 pages (author copy)',
         water_service_access='partly: water is one of four resources studied (with fields, grazing and forest); drinking and cooking water access is assessed by distance to the nearest sweet-water source, salinity and the rules of access, before and after resettlement',
         institutional_factor='yes: rules and norms of access (rights-based and structural-relational mechanisms) in a conservation-driven resettlement in southern Mozambique',
         empirical='yes: in-depth case study with GPS-recorded routes, measurements and key-informant interviews',
         access_outcome='yes for water as a component (distance, quality, access rules); the paper does not report separable water-only findings in a table',
         ai_verdict_on_full_text='borderline: exclude stands under the narrow reading because water is one resource among four and the framing is natural-resource access, not water service access (E01 fits); an include is defensible only if water-specific findings are extracted',
         confidence='low', what_decides_it='the researcher\'s rule on studies that cover several natural resources and the criterion 2 scope reading'),
    dict(record_id='RC9378CBDB2EE', authors_year='Šteflová, Koop, Fragkou & Mees 2022 (Int J Water Resources Development 38(5):742-765)', title='Desalinated drinking-water provision in water-stressed regions: challenges of consumer-perception and environmental impact lessons from Antofagasta, Chile',
         current_decision='exclude E01', full_text_read='yes, 24 pages (Utrecht repository copy)',
         water_service_access='drinking-water provision by desalination in a city where access indicators already score high; the paper is about provision method, consumer perception and environmental impact',
         institutional_factor='yes: governance capacity assessed with the City Blueprint Approach (indicators, stakeholder interviews); water-rights and regulation issues are discussed (the capacity of the law to ensure access is questioned by some stakeholders)',
         empirical='yes: indicator scoring and semi-structured stakeholder interviews',
         access_outcome='no: outcomes are governance barriers, perception of water quality and environmental impact; access is one rung of a proposed priority ladder',
         ai_verdict_on_full_text='exclude confirmed on the full text (E04 wrong outcome fits better than E01; the topic is drinking-water provision but not access or exclusion)',
         confidence='medium', what_decides_it='nothing beyond the code label; no change of decision recommended'),
    dict(record_id='RFC362FE42028', authors_year='Espluga, Ballester, Hernández-Mora & Subirats 2011 (REIS 134:3-26)', title='Public Participation and Institutional Inertia in Water Management in Spain',
         current_decision='exclude E01', full_text_read='yes, 24 pages (Spanish)',
         water_service_access='no: Water Framework Directive basin planning and participation processes; urban supply appears only as one category of user with a concession',
         institutional_factor='yes: river-basin authorities, user boards, public participation processes under the Directive and the Aarhus Convention',
         empirical='yes: document analysis and exploratory interviews',
         access_outcome='no: the outcomes are credibility and inclusiveness of participation processes',
         ai_verdict_on_full_text='exclude confirmed on the full text (E04 wrong outcome, or E01; water resource governance, not service access)',
         confidence='high', what_decides_it='nothing; no change of decision recommended'),
]


def write_a19():
    new = [{k: v for k, v in r.items()} for r in A19_ROWS]
    for r in new:
        assert set(r) == set(A19_FIELDS), set(r) ^ set(A19_FIELDS)
    with open(A19V, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=A19_FIELDS, lineterminator='\r\n'); w.writeheader(); w.writerows(new)
    return len(new)


print('verification rows updated:', rw(VER, m_ver))
print('effect sizes:', rw(ES, m_es))
print('AMSTAR 2 appraised:', rw(ED, m_ed) or 'nothing new')
print('A19 verdict rows written:', write_a19())
