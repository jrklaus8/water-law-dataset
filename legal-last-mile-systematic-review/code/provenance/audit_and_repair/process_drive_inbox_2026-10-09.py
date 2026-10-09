"""2026-10-09: results of the browser-agent retrieval round (see 00_admin/PDF_RETRIEVAL_AGENT_BRIEF_2026-10-09.md). What this dated script records (PDFs were read in the session; nothing is copied into the repository):
  * AMSTAR 2 on the full text for S027 (Fanaian 2025, WIREs Water), the last of the 23 reviews to be appraised: Critically Low (critical items 7, 9 and 13 flawed).
  * S393 (Curtis, BMJ Global Health 2019): the copy supplied is the medRxiv PREPRINT ("DRAFT: under review"); the existing extraction was compared with it and matches; the blank sample size is filled
    and the note says the published version has not been read.
  * RAB6AA06D8E9D: settled without a full text. The retrieval agent found that the Europe PMC record (PMC12848418) is an abstract with no body and that no separate full article exists, so the E09 exclusion
    (conference abstract) stands. Written as a proposal row in A19_RESCREEN_VERDICTS_2026-10-04.csv. No decision is changed (A15).
Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, importlib.util, os, sys, io, contextlib
csv.field_size_limit(sys.maxsize)
spec = importlib.util.spec_from_file_location('inbox_e', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'process_drive_inbox_2026-10-04e.py'))
E = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):  # the 2026-10-04 script is idempotent; its own output is not wanted here
    spec.loader.exec_module(E)
E.DATE = '2026-10-09'
NA = E.NA_ANS
E.AM['S027'] = dict(
    rating='Critically Low',
    cit='Fanaian S, Manero A, Nguyen N-M, Grafton RQ (2025). Beyond a Decade of Water Justice: Review, Directions, and Pathways to Achieve "Water for All". Wiley Interdisciplinary Reviews: Water 12:e70043',
    basis='critical items 7 (no list of excluded studies in the text read), 9 (no risk-of-bias technique) and 13 (nothing accounted for) are flawed; item 2 is Partial Yes (a protocol was published in a university repository, with a late addition of 2023 papers disclosed) and item 4 is Partial Yes; items 11 and 15 do not apply (no meta-analysis)',
    pages='Wiley Interdisciplinary Reviews: Water 12:e70043, full text read (19 pages); the Supporting Information annex and the published protocol (ANU repository, Fanaian 2024) were not read',
    ans={
        1: ('Partial Yes', 'project convention: four research questions on the meaning, growth, location and responses of water justice, with the scope set by the concept "water justice" rather than a PICO; no comparator'),
        2: ('Partial Yes', 'a written protocol was published in the ANU library repository (Fanaian 2024) with the selection criteria and coding decisions; it is not described as registered, and 46 papers from 2023 were added after the protocol by a targeted follow-up screening in March 2024, which is disclosed'),
        3: ('No', 'English-language peer-reviewed articles, chapters and reviews were accepted; the choice of study designs is not explained'),
        4: ('Partial Yes', 'six sources (Scopus, Web of Science, Science Direct, Springer, JSTOR and Google Scholar), January 2012 to December 2023, English only, terms limited to "water justice" OR "water equity" (related concepts excluded on purpose); no grey literature and no reference-list searching reported; the limits are acknowledged'),
        5: ('Yes', 'three co-authors screened the 1,935 titles and abstracts and discrepancies were resolved among the three with expert input; independent duplicate screening is implied, not stated'),
        6: ('Partial Yes', 'two researchers "collaborated on the full-text review and literature coding"; a 20-article pilot refined the deductive framework; independent duplicate extraction is not described'),
        7: ('No', 'CRITICAL FLAW: counts only (364 duplicates removed, 1,935 screened, 496 plus 46 retained, 72 excluded during coding with grouped reasons, 470 included; 35 were unavailable despite library access); the excluded studies are not listed in the text read'),
        8: ('Partial Yes', 'the coding database covers definitions of justice, research question, solutions, conclusions, theoretical grounding, scale, region, water system and Indigenous engagement; the 470 studies are summarised by theme and over time, not described one by one in the text'),
        9: ('No', 'CRITICAL FLAW: no risk-of-bias or quality assessment of the included studies is reported'),
        10: ('No', 'funding sources of the included studies are not reported'),
        11: NA, 12: NA,
        13: ('No', 'CRITICAL FLAW: with no appraisal, study quality is not considered when interpreting the themes; the limitations paragraph concerns language and scope'),
        14: ('Partial Yes', 'the change of emphasis over time (distributive and procedural justice, then decolonial, socio-ecological and pluralistic approaches) and the differences by region are described and discussed; not statistical heterogeneity'),
        15: ('No', 'not applicable: no quantitative synthesis; publication bias is not discussed'),
        16: ('Yes', 'the authors declare no conflicts of interest and acknowledge the support of the International Water Management Institute; the funding statement as such was not separately located')},
    fields=dict(
        study_design='systematic review (PRISMA 2020; six databases, 2012 to 2023; protocol published in a repository; deductive qualitative coding of 470 studies; no risk-of-bias appraisal)',
        sample_size='1,935 titles and abstracts screened after 364 duplicates removed; 496 articles (2012 to 2022) plus 46 from a 2023 follow-up search = 542 full texts; 72 excluded during coding; 470 peer-reviewed publications included (English only)',
        model_type='systematic review with deductive qualitative coding and narrative thematic synthesis (no meta-analysis)'),
    note='Full-text appraisal 2026-10-09 from the open-access PDF the retrieval agent placed in the researcher\'s Drive inbox (19 pages; annex and published protocol not read). Replaces the abstract-level entry and the 2026-09-16 partial pilot. Confirmed as a systematic review (the article is typed "Systematic review"); the last of the 23 AMSTAR 2 reviews to be rated.')


def m_s393(rows):
    for r in rows:
        if r['study_id'] == 'S393':
            if 'Checked 2026-10-09 against the full text of the medRxiv PREPRINT' in r['extraction_note']:
                return 'S393 already updated'
            r['sample_size'] = ('17 interviews (60 to 80 minutes, May to July 2018) with actors in the Swachh Bharat Mission (Gramin) at national (4), state (4) and district (6) level, in the capital and four states with varied toilet coverage; '
                                'six career civil servants, five assigned to the programme, four from partner organisations outside government and two academics (categories overlap); 15 Indian nationals, 7 women; 11 face to face and 6 by Skype')
            r['extraction_note'] = ('Checked 2026-10-09 against the full text of the medRxiv PREPRINT (24 pages, marked "DRAFT: under review"; doi 10.1101/19004689), supplied by the retrieval agent: the extraction matches (17 interviews, theory of change, '
                                    'coverage from 39% to over 95%, 100 flagship districts, 500 young professionals); the published BMJ Global Health version (e001892) has NOT been read and may differ. The earlier status "no full text read" was stale. ' + r['extraction_note'])
            return 'S393 updated'
    raise AssertionError('S393 missing')


A19_NEW = dict(record_id='RAB6AA06D8E9D', authors_year='Carranza, Verdura & Gargallo 2025 (European Journal of Public Health, abstract 286; DOI 10.1093/eurpub/ckaf180.144)',
               title='Socioeconomic impacts derived from the effects of climate change on water quality in Catalonia (Spain) with a special emphasis on vulnerable groups',
               current_decision='exclude E09', full_text_read='no full text exists: the retrieval agent opened the Europe PMC record (PMC12848418), which is article-type "abstract" with no body sections',
               water_service_access='not assessable', institutional_factor='not assessable', empirical='the abstract reports 8 semi-structured interviews with quadruple-helix stakeholders (QUEEN project)',
               access_outcome='not assessable', ai_verdict_on_full_text='exclude confirmed: only a conference abstract exists and no separate full article was found (E09 stands)', confidence='high',
               what_decides_it='nothing; if the authors later publish a full article it can be screened then')


def write_a19():
    path = E.ED.rsplit('/', 3)[0]  # unused; keep explicit path below
    p = '02_screening/full_text/A19_RESCREEN_VERDICTS_2026-10-04.csv'
    with open(p, encoding='utf-8', newline='') as f:
        rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
    if any(r['record_id'] == A19_NEW['record_id'] for r in rows):
        return 'A19 verdict already present'
    assert set(A19_NEW) == set(fields), set(A19_NEW) ^ set(fields)
    rows.append(A19_NEW)
    with open(p, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n'); w.writeheader(); w.writerows(rows)
    return 'A19 verdict added'


for _k in [k for k in E.AM if k != 'S027']:  # the five earlier appraisals are already in the data; only S027 is new here
    del E.AM[_k]
print('AMSTAR 2 appraised:', E.rw(E.ED, E.m_ed) or 'nothing new')
print(E.rw(E.ED, m_s393))
print(write_a19())
