"""2026-10-04 (night), third Drive-inbox batch, second tier. Writes two files from the reading done in the session (the PDFs are not committed):
  * 02_screening/full_text/DECIDED_EXCLUDES_RECHECKED_2026-10-04.csv: the 15 already-decided full-text excludes whose papers were in the batch (R-named files), each compared with the paper;
    nothing in the screening database is changed (screening closed 2026-09-28; A15).
  * 00_admin/DRIVE_INBOX_BATCH3_LOG_2026-10-04.md: one row per file of the batch (88) saying what it was and what was done with it.
Idempotent; run from legal-last-mile-systematic-review/."""
import csv, re, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
HERE = Path(__file__).resolve().parent
RECHECK = Path('02_screening/full_text/DECIDED_EXCLUDES_RECHECKED_2026-10-04.csv')
LOG = Path('00_admin/DRIVE_INBOX_BATCH3_LOG_2026-10-04.md')
FIELDS = ['record_id', 'authors_year', 'title', 'code_now', 'what_the_paper_is', 'verdict', 'note']
R = lambda rid, ay, title, code, what, verdict, note='': dict(zip(FIELDS, [rid, ay, title, code, what, verdict, note]))
ROWS = [
    R('RB83291F58980', 'Weets & Katz 2024 (BMJ Global Health)', 'Global approaches to tackling antimicrobial resistance: a comprehensive analysis of water, sanitation and hygiene policies', 'E04',
      'analysis of WASH-related antimicrobial-resistance policy across 193 countries (policy mapping); the outcome is AMR policy coverage', 'stands', 'strong legal-mapping content, but no access outcome'),
    R('RC9C18FC0333A', 'Tseng et al. 2020 (BMJ Global Health)', 'Estimating the cost of interventions to improve water, sanitation and hygiene in Indian healthcare facilities', 'E06',
      'survey of 32 healthcare facilities to cost WASH upgrades nationally (ingredients-based costing)', 'stands', 'cost estimation; no legal or governance factor'),
    R('RB76A3B41BBBF', 'Sinharoy et al. 2022 (BMJ Open)', "Protocol for development and validation of instruments to measure women's empowerment in sanitation", 'E05',
      'a protocol for scale development and validation (ARISE scales); no results', 'stands', 'protocol only'),
    R('RFF1E12E56199', 'Nagheeby et al. 2026 (Third World Quarterly)', 'Escaping the Capitalist Black Hole: dethroning Mammon and liberating water', 'E05',
      'Research Note: a conceptual synthesis of five years of hub research in four countries, with no data presented in the note', 'stands', 'conceptual note'),
    R('RC3AD9364CFB5', 'Prieto 2016 (Chile)', 'Transando el agua, produciendo territorios e identidades indigenas', 'E07',
      'political-ecology study of water-rights transactions (Chilean Water Code 1981) and interviews with Atacameno urban leaders in Calama', 'borderline (code)', 'empirical and legal, but the water traded is for farming and mining rather than household supply; E07 stands under the narrow reading'),
    R('R6F38D218A764', 'Willetts et al. 2022 (EPB)', 'Co-developing evidence-informed adaptation actions for resilient citywide sanitation', 'E01',
      'co-production research with local governments of four Indonesian cities listing climate adaptation actions for sanitation systems (planning, institutions, financing, infrastructure)', 'stands (E04 fits better)', 'governance content, but the outcome is adaptation actions, not access'),
    R('R8FB559FE24DC', 'Kireitseva et al. 2025 (Ukraine)', 'Integral assessment of the effectiveness of water resource management in communities', 'E03',
      'SWOT and composite-index study of community water-resource management (nine indicators; index 0.382)', 'stands', 'sustainability index; access percentages are inputs only'),
    R('R788D093EA440', 'Felix-Lopez et al. 2023', "Exploring the impact of reclaimed water on Latin America's development", 'E07',
      'systematic review and meta-analysis of the economics of reclaimed water and wastewater regulation in Latin America', 'stands', 'wastewater reuse markets, not household access; note it is a systematic review by design'),
    R('R7B8C7CDFCC7A', 'Howard et al. 2020 (J Water Health)', "COVID-19: urgent actions, critical reflections and future relevance of 'WaSH'", 'E05',
      'narrative review of WaSH in disease emergence and COVID-19 prevention', 'stands', 'narrative review without a stated method'),
    R('R553D7F2BD960', 'Gomes et al. 2018 (Water)', 'Capacity building for water management in peri-urban communities, Bangladesh', 'E04',
      'role-playing simulation game workshop on drinking-water institutions in Khulna; outcome is participant learning', 'stands', ''),
    R('R47F7BDFF23F7', 'Jabari et al. 2020 (Water)', 'Assessment of the urban water security in a severe water stress area', 'E06',
      'SWARA risk index of water security for five Palestinian cities with water-service indicators (coverage, losses, continuity) and governance indicators (roles, information, stakeholder engagement)', 'borderline (code)', 'E06 (engineering) fits poorly: the index mixes service and governance indicators; no access outcome is measured, so E04 is the better label'),
    R('R6414B5FB0A19', 'Meng et al. 2026 (Journal of Environmental Engineering Technology, Chinese)', 'Spatiotemporal distribution and countermeasures of rural domestic sewage treatment facilities in tropical islands of Hainan', 'E06',
      'field survey of 741 rural sewage treatment facilities in 18 cities and counties (treatment rate 80.1%, 48.6% of facilities with operating problems, maintenance models)', 'stands', 'engineering and operations survey; governance appears only as the maintenance-operator model'),
    R('R47B995771A17', 'Inam 2025 (Turkey)', 'Determining the opinions of women living in the earthquake zone on the physical and psychosocial problems after the 2023 Kahramanmaras earthquake', 'E01',
      'qualitative interviews with 15 women; hygiene (toilet and bathroom) is one issue among many', 'stands', ''),
    R('R19A9F20BC53A', 'Marques 2008 (Portugal)', 'Measuring the total factor productivity of the Portuguese water and sewerage services', 'E01',
      'Malmquist total-factor-productivity study of utilities by ownership and rurality', 'stands', 'efficiency measurement; no access or legal factor'),
    R('R1C0CF917B85E', 'de Wit et al. 2024', 'Water, sanitation and hygiene (WASH): the evolution of a global health and development sector', 'E01',
      'document review and 19 expert interviews on seven decades of the global WASH sector', 'stands', 'sector history, not an access-barrier study'),
]


def write_recheck():
    with open(RECHECK, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator='\r\n'); w.writeheader(); w.writerows(ROWS)


# --------------------------------------------------------------------------- batch log
CAT = {}
def put(keys, cat, did):
    for k in keys.split():
        CAT[k] = (cat, did)
put('S057 S084 S085 S149 S445 S483 S491', 'effect-size row', 'numbers compared with the paper; all verified (FULLTEXT_VERIFICATION_2026-10-04.csv; S057 sample added)')
put('R0B0F3925F533 R977ECB01FA02 RC9378CBDB2EE RFC362FE42028', 'A19 re-screen', 'screened against INCLUSION_EXCLUSION.md; verdict in A19_RESCREEN_VERDICTS_2026-10-04.csv; no decision changed')
put('S019 S116 S323 S329', 'AMSTAR 2', 'appraised on the full text, all Critically Low; 04_quality/appraisal_forms/<id>_AMSTAR2.md; extraction row upgraded')
put('S268 S311 S363 S374 S362 S361 S355 S359 S360 S354 S357 S306 S308 S303 S250 S292 S291 S273 S286 S214 S322 S321 S320 S103 S161 S210 S156 S164 S364', 'sparse or abstract-only row', 're-extracted from the full text (reextract_2026-10-04/<id>.json); eligibility or fit flags added where the paper raised them')
put('S115 S111 S118 S117 S100 S112 S107 S109 S358 S079', 'moderate-sparse row', 'read against the existing row: the extraction already carries page-level full-text detail; no change')
put('S120 S121 S169', 'second-extractor sample / moderate-sparse row', 'checked; extraction kept as is (the abstract-level location is the only signal); file moved so the human second extractor can use the original')
put('S114', 'moderate-sparse row', 'the converted text layer is scrambled (words out of order), so no re-extraction was possible; a clean copy is needed')
put('R3BFAF175DBF1 R812E3C486FA8 RD03D0D823CB8 RF6F82FE94F8C RDE592D874BF6 RE0CF385853FE RD874B0BA92F5 RC869B89B74B1 RDBEE0C32E0CA R928138B31379 R835B5C80B84D RBFF9D3F5FAD2 R798F6D592650 R7AC977C0F191 R6667931A0DBB R581406026ADC', 'included study (file named by record id)',
    'the row already rests on the full text (table-level locations) except S364, which was re-extracted; no other change')
for r in ROWS:
    CAT[r['record_id']] = ('decided exclude', f"compared with the paper: {r['verdict']} (DECIDED_EXCLUDES_RECHECKED_2026-10-04.csv)")


def write_log():
    rows = [l.rstrip('\n').split('\t') for l in open(HERE / 'drive_inbox_batch3_files_2026-10-04.tsv', encoding='utf-8')]
    L = ['# Drive inbox, third batch (88 files dropped 2026-10-04): what was done with each', '',
         'The researcher dropped 88 full texts in the Drive inbox folder (`Sep 26 2026`). Each was read by the AI in the session and moved to `Processed` once its work was recorded. No PDF is committed to the repository. '
         'Outputs: `process_drive_inbox_2026-10-04b.py` (effect-size verification, AMSTAR 2, A19 verdicts), `reextract_2026-10-04/*.json` (full-text re-extractions), `process_drive_inbox_2026-10-04c.py` (this log and the recheck of decided excludes).', '',
         '| File key | Category | What was done | Drive file name |', '|---|---|---|---|']
    miss = []
    for fid, name in rows:
        k = re.match(r'^([SR][0-9A-F]{3,12})_', name).group(1)
        if k not in CAT:
            miss.append(k); continue
        L.append(f'| {k} | {CAT[k][0]} | {CAT[k][1]} | {name[:90]} |')
    assert not miss, miss
    LOG.write_text('\n'.join(L) + '\n', encoding='utf-8')
    return len(rows)


write_recheck()
print('recheck rows:', len(ROWS), '| log rows:', write_log())
