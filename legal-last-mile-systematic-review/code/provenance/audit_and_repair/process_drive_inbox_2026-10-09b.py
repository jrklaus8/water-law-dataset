"""2026-10-09 (second round): twelve PDFs the researcher dropped in the Drive inbox after the browser-agent retrieval round (00_admin/PDF_RETRIEVAL_STATUS_2026-10-09.md). The PDFs were read in the
session; nothing is copied into the repository. What this dated script records:
  * A19 re-screen verdict for RF5C6D981DB3B (Rodriguez-Izquierdo et al. 2023, Chiapas): exclusion confirmed on the full text (a proposal row; no decision is changed, A15).
  * A22 verdict for S513 (McGranahan 2015): fails criterion 3 on the full text (a proposal row; A22 is researcher-gated).
  * S513's extraction row: the blank sample size and country are filled and the note records the full-text read (its design label, conceptual synthesis, is confirmed).
  * S393 (Curtis 2019): the published BMJ Global Health version was read and matches the preprint checked earlier; the item-level CASP rating is re-answered on it.
  * Nine more studies were re-extracted from their full texts by JSONs in reextract_2026-10-04/ (S271, S304, S310, S315, S352 abstract-only rows; S395, S415, S416, S417 rows that were extracted without a full text),
    applied by run_reextract_2026-10-04.py, which now honours a per-JSON "date".
  * 02_screening/full_text/PDF_RETRIEVAL_RECEIVED_2026-10-09.csv and 00_admin/DRIVE_INBOX_BATCH4_LOG_2026-10-09.md list what arrived and what was done with it.
Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _reextract_lib as L
csv.field_size_limit(sys.maxsize)

# ------------------------------------------------------------------ extraction rows
S513_MARK = 'Read in full 2026-10-09'
S393_OLD = 'the published BMJ Global Health version (e001892) has NOT been read and may differ.'
S393_NEW = ('the published BMJ Global Health version (e001892) was then read in full (Drive file e001892.full.pdf) and matches the preprint on the points checked (17 interviews, 11 face to face and 6 by Skype, '
            '60 to 80 minutes, May to July 2018; COREQ; framework analysis in NVivo; London School of Hygiene & Tropical Medicine ethics approval 15261; coverage from 39% to over 95%).')
S393_RATING = ("CASP Qualitative per-item (re-appraised 2026-10-09 on the published full text; supersedes the abstract-level rating of 2026-09-28): 1(aims)=Yes; 2(qual approach)=Yes; "
               "3(design)=Yes (interviews with a spread of national, state and district actors; a theory-of-change analysis); "
               "4(recruitment)=Yes (17 interviewees chosen to represent actor types at three levels, about four per type, interviewing until saturation; everyone approached agreed); "
               "5(data collection)=Yes (structured-format interviews of 60 to 80 minutes, 11 face to face and 6 by Skype, recorded and transcribed); "
               "6(researcher-participant)=Can't tell (the author discloses past work as an adviser to the ministry; the influence of that role is not discussed); "
               "7(ethics)=Yes (LSHTM approval 15261, written consent, anonymity, permission from the ministry); "
               "8(analysis rigor)=Can't tell (framework analysis steps in NVivo by a single analyst; no discussion of contradictory data); 9(findings)=Yes; 10(value)=Yes. "
               "Per CASP's own guidance no composite score is computed.")


def m_ed(rows):
    done = []
    for r in rows:
        if r['study_id'] == 'S513' and S513_MARK not in r['extraction_note']:
            assert r['extraction_note'].strip() == 'record_id RA0D30B3E8C1C.', r['extraction_note'][:80]
            r['country'] = 'global argument; illustrative cases in Pakistan (Karachi) and India (Pune and Mumbai)'
            r['sample_size'] = ('No primary data and no stated method: a conceptual and policy argument. Two community-driven sanitation initiatives (the Orangi Pilot Project in Karachi; the Alliance of Mahila Milan, SPARC '
                                'and the National Slum Dwellers Federation in Pune and Mumbai) are summarised from published documentation (Table 1); the author announces a companion article with the detailed analysis')
            r['extraction_note'] = (f'{S513_MARK} (World Development open-access journal PDF, 12 pages, Drive file main.pdf): confirms the design label (conceptual synthesis); the blank sample size and country are now filled. '
                                    'The paper states no data, sample or method, so the inclusion question under criterion 3 is raised in A22_VERDICTS_2026-10-04.csv (proposal only). record_id RA0D30B3E8C1C.')
            done.append('S513')
        if r['study_id'] == 'S393' and S393_OLD in r['extraction_note']:
            r['extraction_note'] = r['extraction_note'].replace(S393_OLD, S393_NEW)
            r['risk_of_bias_rating'] = S393_RATING
            done.append('S393')
    return rows, done


_done = []


def _fn(rows):
    rows, d = m_ed(rows)
    _done.extend(d)
    return rows


# ------------------------------------------------------------------ verdict rows
A19_NEW = dict(record_id='RF5C6D981DB3B', authors_year='Rodriguez-Izquierdo, Alvarado-Velazquez, Garcia-Meneses, Merino-Perez & Mazari-Hiriart 2023 (Regional Environmental Change 23:3)',
               title='Inequality, water accessibility, and health impacts in Chiapas, Mexico', current_decision='exclude E01',
               full_text_read='yes, 13 pages (Springer journal PDF, supplied 2026-10-09)',
               water_service_access='partly: the framing is unequal access to clean water and sanitation (SDG 6), but the data are water concessions by use, gastrointestinal disease and mortality records and land-cover change; household water or sanitation access is not measured (a CONEVAL figure that 56% of people in Chiapas lack basic water services is cited)',
               institutional_factor='partly: federal water concessions (REPDA, CONAGUA) are mapped by source and use (1,083 agricultural and 192 municipal or domestic public-use concessions; about 18 hm3 allocated for public use in Comitan against about 2 hm3 in the other two municipalities together) and governance (SDG 16) is discussed as a lever for action; no institution is analysed as a factor shaping access',
               empirical='yes: GIS land-cover change 2002-2017, the concession registry 1994-2019, municipal morbidity and mortality records 1998-2019 (non-parametric regression), the Palma ratio and the marginalisation index; no household data',
               access_outcome='no: the outcomes are land-cover change, gastrointestinal disease prevalence, cancer mortality and inequality indices',
               ai_verdict_on_full_text='exclude confirmed on the full text (E04 wrong outcome fits better than E01); borderline on criterion 2 only through the descriptive concession map',
               confidence='medium',
               what_decides_it='whether a descriptive map of water concessions by use counts as an institutional factor for access; the AI says no, because no access outcome is linked to it; no change of decision recommended')
A22_NEW = dict(record_id='RA0D30B3E8C1C', study_id='S513', authors_year='McGranahan 2015 (World Development 68:242-253)',
               title='Realizing the Right to Sanitation in Deprived Urban Communities: Meeting the Challenges of Collective Action, Coproduction, Affordability, and Housing Tenure',
               current_decision='include', full_text_read='yes, 12 pages (open-access journal PDF, supplied 2026-10-09)',
               empirical='no: a conceptual and policy argument built on the literature; two community-driven initiatives (the Orangi Pilot Project in Karachi; the Alliance of Mahila Milan, SPARC and the National Slum Dwellers Federation in Pune and Mumbai) are summarised in about a page and Table 1 from published documentation, with no data, sample or method, and a companion article with the detailed analysis is announced',
               ai_verdict_on_full_text='fails criterion 3 on the full text: exclusion proposed (E05 no empirical evidence); the service fits criterion 1 and the institutional topic (collective action, coproduction, affordability versus acceptability, tenure) fits criterion 2',
               confidence='high',
               what_decides_it='whether the project treats a policy argument illustrated by two documented cases as a systematic empirical synthesis; the AI reads criterion 3 as requiring data or a stated method, so the paper would move to a conceptual-evidence list; no decision is changed (A15; A22 is researcher-gated)')


def add_row(path, new, key):
    with open(path, encoding='utf-8', newline='') as f:
        raw = f.read()
    crlf = '\r\n' in raw[:5000]
    with open(path, encoding='utf-8', newline='') as f:
        rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
    if any(r[key] == new[key] for r in rows):
        return f'{os.path.basename(path)}: {new[key]} already present'
    assert set(new) == set(fields), set(new) ^ set(fields)
    rows.append(new)
    with open(path, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n' if crlf else '\n'); w.writeheader(); w.writerows(rows)
    return f'{os.path.basename(path)}: {new[key]} added'


# ------------------------------------------------------------------ what arrived
RECEIVED = [  # (id, tier in PDF_RETRIEVAL_TARGETS, Drive file name, what it is, pages, what was done)
    ('S513', 'A', 'main.pdf', 'World Development 68:242-253 (2015), open-access journal PDF', '12', 'A22 verdict: fails criterion 3 (conceptual; proposal only); extraction row filled in'),
    ('RF5C6D981DB3B', 'A', 's10113-022-01993-1.pdf', 'Regional Environmental Change 23:3 (2023), Springer journal PDF', '13', 'A19 verdict: exclusion confirmed (E04 fits better than E01; proposal only)'),
    ('S352', 'B', 'wamuchiru-2017-beyond-the-networked-city-situated-practices-of-citizenship-and-grassroots-agency-in-water.pdf', 'Environment & Urbanization 29(2):551-566 (2017), journal PDF', '16', 'abstract-only row re-extracted; CASP re-answered'),
    ('S271', 'B', 'joshi2011.pdf', 'Environment & Urbanization 23(1):91-111 (2011), journal PDF', '21', 'abstract-only row re-extracted; CASP re-answered'),
    ('S304', 'B', 'PDF_PersistantProblems2012.pdf', "Singapore J Trop Geogr 33(3):335-350 (2012), the author's final draft from the Edinburgh repository", '', 'abstract-only row re-extracted; CASP re-answered; the typeset article was not read'),
    ('S310', 'B', 'content (2).pdf', 'Int J Water Resources Development 29(4) (2013), scanned image PDF without a text layer', '17', 'abstract-only row re-extracted from page images; MMAT not re-answered (tool fit arguable, A11)'),
    ('S315', 'B', 'content (3).pdf', 'Natural Resources Forum 34(2):93-105 (2010), scanned image PDF without a text layer', '13', 'abstract-only row re-extracted from page images; CASP re-answered'),
    ('S416', 'C', '1573062X.2012.709254.pdf', 'Urban Water Journal 10(2):97-104 (2013), journal PDF', '8', 'extraction checked and fields filled; CASP re-answered (no methods section)'),
    ('S393', 'C', 'e001892.full.pdf', 'BMJ Global Health 4:e001892 (2019), published open-access version', '', 'matches the preprint checked earlier; CASP re-answered on the published text'),
    ('S395', 'C', 'bioconf_sage-grace2024_03002.pdf', 'BIO Web of Conferences 144:03002 (2024), conference paper', '12', 'extraction checked and fields filled; MMAT re-answered (5.5 = No; tables and text disagree)'),
    ('S417', 'C', 'pdf.pdf', 'Environ. Res.: Infrastruct. Sustain. 5:025006 (2025), open-access journal PDF', '', 'extraction checked and fields filled; CASP re-answered'),
    ('S415', 'C', '23251042.2026.2666400.pdf', 'Environmental Sociology (online 2 May 2026), journal PDF', '', 'extraction checked and fields filled; CASP re-answered'),
]
HDR = ['id', 'tier_in_PDF_RETRIEVAL_TARGETS', 'drive_file_name', 'what_it_is', 'pages', 'what_was_done']
LOG = '00_admin/DRIVE_INBOX_BATCH4_LOG_2026-10-09.md'
REC = '02_screening/full_text/PDF_RETRIEVAL_RECEIVED_2026-10-09.csv'


def write_received():
    with open(REC, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, lineterminator='\n'); w.writerow(HDR); w.writerows(RECEIVED)
    lines = ['# Drive inbox, fourth batch (2026-10-09): twelve PDFs after the browser-agent round', '',
             'The researcher dropped twelve PDFs in the Drive inbox folder (`Sep 26 2026`) after the retrieval brief (`PDF_RETRIEVAL_AGENT_BRIEF_2026-10-09.md`). The AI read each in the session. '
             'Two of them (`content (2).pdf`, `content (3).pdf`) are scanned images without a text layer; they were read page by page as images, so their table values are page-image readings, not machine extraction. '
             'No PDF is committed to the repository. Outputs: `process_drive_inbox_2026-10-09b.py` (this script), nine new JSONs in `reextract_2026-10-04/` and the rows listed below.', '',
             '| Study or record | Tier | Drive file | What it is | Pages | What was done |', '|---|---|---|---|---|---|']
    for r in RECEIVED:
        lines.append('| ' + ' | '.join(x.replace('|', '/') for x in r) + ' |')
    lines += ['', '## Two decisions the full texts raise (proposals only; screening is closed, A15)', '',
              '- **A19, RF5C6D981DB3B (Chiapas, E01):** exclusion confirmed on the full text; E04 (wrong outcome) is the better code. Three of the nine A19 records still have no full text: R155FFF508359, RA1F6E143593E and R803988411D3E.',
              '- **A22, S513 (McGranahan 2015):** a conceptual and policy argument with no stated data or method; fails criterion 3. Three A22 includes still need a full text: S264, S314, S340.', '',
              '## Things worth a human look', '',
              '- S310 (17-page scan) and S315 (13-page scan) were read from images: their numbers are an AI reading of table images.',
              '- S310 and S285 (same Nicaraguan national study, same research group) and S315 and S311 (Same District, Tanzania; same research group) probably share underlying data. They were not added to `linked_reports_2026-09-28.csv`; that is a researcher decision.',
              '- S395 (Jambon Village): the paper\'s own tables disagree (Table 6 against Table 7 dimension totals; tariff and water-quantity percentages differ between text and Conclusion), so its figures should be quoted with care.',
              '- S304 is the author\'s final draft, not the typeset article.', '']
    with open(LOG, 'w', encoding='utf-8', newline='') as f:
        f.write('\n'.join(lines))


print('extraction rows:', L._rw(L.ED, _fn), _done or 'nothing new')
print(add_row('02_screening/full_text/A19_RESCREEN_VERDICTS_2026-10-04.csv', A19_NEW, 'record_id'))
print(add_row('02_screening/full_text/A22_VERDICTS_2026-10-04.csv', A22_NEW, 'record_id'))
write_received()
print('wrote', REC, 'and', LOG)
