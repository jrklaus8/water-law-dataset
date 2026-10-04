#!/usr/bin/env python3
"""One-command integrity check for the whole repository.

Run from the project root (legal-last-mile-systematic-review/):
    python3 code/analysis/verify_repository.py

Exit status 0 = every check passed; 1 = at least one failed (each failure is printed). Three groups of checks:

  A. Schemas          — code/analysis/validate_schemas.py (headers of the 13 tracked CSVs).
  B. Cross-file logic — ID sets agree across databases; study<->record map is a bijection with the full-text includes;
                        exclusion log and full-text exclusions match one-to-one; retired study IDs are truly absent;
                        linked-report IDs exist; effect-size rows belong to extracted studies; every tool-applicable
                        study has a rating.
  C. Documents        — the current-status documents quote the figures computed by current_figures.py (positive checks
                        on curated phrases; dated/historical documents are deliberately not checked).
Also checks that 00_admin/current_figures.json is up to date with the databases.

No third-party dependencies. Read-only.
"""
import csv, json, os, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402

ROOT = cf.ROOT
fails, passes = [], 0
EXPECTED = []  # (file, phrase, label) for every hand-written phrase the verifier looks for; dumped when VERIFY_EMIT_EXPECTED is set (used by fix_documented_counts.py)


def check(cond, msg):
    global passes
    if cond:
        passes += 1
    else:
        fails.append(msg)


def _report_crash(exc_type, exc, tb):
    """If a later check or generated-file builder raises (typically because a database is inconsistent, e.g. a missing extraction row), still print the
    failures already collected: they usually name the cause, which a bare traceback would hide."""
    import traceback
    print(f"{passes} checks passed, {len(fails)} failed BEFORE THE VERIFIER CRASHED (it did not finish)")
    for f_ in fails:
        print('  FAIL:', f_)
    print('  CRASH:', ''.join(traceback.format_exception_only(exc_type, exc)).strip())
    traceback.print_exception(exc_type, exc, tb)
    sys.exit(1)


sys.excepthook = _report_crash


def text(rel):
    return (ROOT / rel).read_text(encoding='utf-8')


def has(rel, needle, label=None):
    EXPECTED.append((rel, needle, label))
    check(needle in text(rel), f"{rel}: expected to contain {needle!r}" + (f" ({label})" if label else ''))


# ---- A. schemas
r = subprocess.run([sys.executable, str(ROOT / 'code/analysis/validate_schemas.py')], capture_output=True, text=True, cwd=ROOT)
check(r.returncode == 0 and 'match their documented' in r.stdout, 'validate_schemas.py failed:\n' + (r.stdout + r.stderr)[-600:])

# ---- B. cross-file logic
F = cf.compute()
ft, el, ed, em, es, mp, links = (cf.read(k) for k in ('ft', 'el', 'ed', 'em', 'es', 'map', 'links'))
ed_ids, em_ids, es_ids = {r['study_id'] for r in ed}, {r['study_id'] for r in em}, {r['study_id'] for r in es}
check(len(ed) == len(ed_ids), 'extraction_database has duplicate study_ids')
_blank_core = [(r['study_id'], f) for r in ed for f in ('citation', 'record_id', 'study_design') if not r[f].strip()]
check(not _blank_core, f'extraction rows with a blank citation, record_id or study_design: {_blank_core[:5]}')
check(ed_ids == em_ids, f'extraction/evidence_map study_id sets differ: {sorted(ed_ids ^ em_ids)[:10]}')
check(es_ids <= ed_ids, f'effect_sizes has study_ids not extracted: {sorted(es_ids - ed_ids)}')
check(len(es) == len(es_ids), 'effect_sizes has more than one row for a study (CODEBOOK section 12: one prespecified effect per study)')
inc = {r['record_id'] for r in ft if r['final_decision'] == 'include'}
exc = {r['record_id'] for r in ft if r['final_decision'] == 'exclude'}
active = [r for r in mp if r['status'] == 'active']
check({r['study_id']: r['record_id'] for r in active} == {r['study_id']: r['record_id'] for r in ed}, 'extraction_database.record_id disagrees with study_record_map')
check({r['study_id'] for r in active} == ed_ids, 'study_record_map active rows do not match extraction study_ids')
check({r['record_id'] for r in active} == inc and len(active) == len(inc), 'study_record_map is not a bijection with the full-text includes')
retired = {r['study_id']: r for r in mp if r['status'] != 'active'}
check(all(s not in ed_ids for s in retired), f'retired study IDs still present in extraction: {[s for s in retired if s in ed_ids]}')
_nums = {int(r['study_id'][1:]) for r in mp}
_gaps = set(range(1, max(_nums) + 1)) - _nums
check(_gaps == {227, 399}, f'study_record_map gaps in the S-number sequence differ from the two documented ones (S227, S399, retired 2026-09-16 before the map existed): {sorted(_gaps)[:10]} (a retired row deleted?)')
check(all(r['record_id'] in {x['record_id'] for x in ft} for r in retired.values()), 'a retired study maps to an unknown record_id')
check(all(r['record_id'] in exc for r in retired.values()), 'a retired study\'s screening record is not an exclusion')
check({r['record_id'] for r in el} == exc and len(el) == len(exc), 'exclusion_log does not match full-text excludes one-to-one')
check(all(r['exclusion_reason'] for r in ft if r['final_decision'] == 'exclude'), 'a full-text exclude lacks an exclusion_reason code')
check(all(a in ed_ids and b in ed_ids for a, b in ((r['study_id_a'], r['study_id_b']) for r in links)), 'linked_reports refers to a study_id that is not extracted')
check(F['tool_unclassified'] == 0, f"{F['tool_unclassified']} studies have an unclassifiable risk_of_bias_tool")
check(F['tool_applicable_unrated'] == 0, f"{F['tool_applicable_unrated']} tool-applicable studies have no risk_of_bias_rating")
check(F['effect_size_rows_pooled'] == 0, 'an effect-size row is flagged pooled, contradicting the documented Phase 11 verdict (update ANALYSIS_PLAN/README if this is intended)')
check(F['full_text_undecided'] == F['unretrieved_not_retrievable'] + F['unretrieved_wrong_file'], 'undecided full-text rows are not all not_retrievable/wrong_file_retrieved')

# ---- freshness of the generated figures file
cur = json.loads((ROOT / '00_admin/current_figures.json').read_text(encoding='utf-8'))
check(cur == json.loads(json.dumps(F)), '00_admin/current_figures.json is stale: run `python3 code/analysis/current_figures.py --write`')

# ---- C. documents quote the computed figures
inc_n, exc_n, n = F['full_text_include'], F['full_text_exclude'], F['extraction_rows']
T = F['tools']
readme = 'README.md'
has(readme, f"**{inc_n:,} include / {exc_n:,} exclude**", 'full-text status row')
has(readme, f"{n:,} studies extracted", 'extraction row')
has(readme, f"All {F['tool_applicable']:,} studies to which a tool applies", 'risk-of-bias row')
for label, key in (('RoB 2', 'RoB 2'), ('ROBINS-I', 'ROBINS-I'), ('JBI Cross-Sectional', 'JBI Cross-Sectional'), ('MMAT', 'MMAT'),
                   ('CASP Qualitative', 'CASP Qualitative'), ('AMSTAR 2', 'AMSTAR 2'), ('Legal Institutional Evidence Appraisal Framework', 'Legal Framework')):
    has(readme, f"{T[key]} {label}", f'tool count {label}')
has(readme, f"{F['quantitative_synthesis_eligible']} flagged quantitative-synthesis-eligible, {F['qualitative_synthesis_eligible']:,} qualitative", 'evidence classification row')
has(readme, f"E05 no\nempirical evidence {F['exclusion_by_code']['E05']}", 'E05 count')
has(readme, f"E08 duplicate {F['exclusion_by_code']['E08']}", 'E08 count')
has(readme, f"of {exc_n:,} total", 'exclusion total')
has(readme, f"{F['reviewer_2_confirmed_includes']} of {inc_n:,} current includes", 'reviewer_2 coverage')
# README's full exclusion-reason breakdown ("E01 wrong topic 496 · E02 wrong population 34 ...") must match the exclusion log
import re as _re
_flat = _re.sub(r'\s+', ' ', text(readme))
_m = _re.search(r'E01 wrong topic.*?E12 wrong study design \d+', _flat)
check(bool(_m), 'README: exclusion-reason breakdown not found')
if _m:
    _got = {c: int(v) for c, v in _re.findall(r'(E\d\d)[^0-9·]*?(\d+)(?= ·|\.|$|\s·)', _m.group(0))}
    for _code, _cnt in F['exclusion_by_code'].items():
        check(_got.get(_code) == _cnt, f"README exclusion breakdown: {_code} is {_got.get(_code)}, data says {_cnt}")
# The AI-assisted nature of the project must stay visible in the title and the disclosure must exist
check(text('README.md').lstrip().startswith('# The Legal Last Mile — An AI-Assisted Systematic Review'), 'README.md: H1 no longer carries "AI-Assisted"')
check('AI-Assisted' in text('CITATION.cff').split('\n')[3], 'CITATION.cff: title no longer carries "AI-Assisted"')
check('AI-Assisted' in text('PROTOCOL.md').split('## 2.')[0], 'PROTOCOL.md: working title no longer carries "AI-Assisted"')
check((ROOT / 'AI_USE_STATEMENT.md').exists(), 'AI_USE_STATEMENT.md is missing')
top_txt = (ROOT.parent / 'README.md').read_text(encoding='utf-8')
for needle in (f"**{inc_n:,} include / {exc_n:,} exclude**", f"{n:,} studies extracted", f"all {F['tool_applicable']:,} to which one applies",
               f"{F['quantitative_synthesis_eligible']} studies quantitative-synthesis-eligible, {F['qualitative_synthesis_eligible']:,} qualitative"):
    EXPECTED.append(('../README.md (repository root)', needle, None))
    check(needle in top_txt, f"../README.md (repository root): expected to contain {needle!r}")
has('06_outputs/prisma/prisma_flow.md', f"Studies included in systematic review (n = {inc_n:,}, FINAL)")
has('06_outputs/prisma/prisma_flow.md', f"E05 no empirical evidence (n = {F['exclusion_by_code']['E05']})")
has('06_outputs/prisma/prisma_flow.md', f"E08 duplicate (n = {F['exclusion_by_code']['E08']})")
has('06_outputs/prisma/prisma_flow.md', f"n = {exc_n:,} total")
has('PRISMA_WORKFLOW.md', f"{inc_n:,} include / {exc_n:,} exclude")
el_txt = '04_quality/risk_of_bias/2026-09-28_evidence_limitations.md'
has(el_txt, f"| {T['Legal Framework']} | {round(F['tool_share_pct']['Legal Framework'])}% |", 'tool table LF')
has(el_txt, f"| {T['MMAT']} | ", 'tool table MMAT')
has(el_txt, f"| {T['CASP Qualitative']} | ", 'tool table CASP')
has(el_txt, f"only {F['causal_capable_designs']} of {n:,} studies", 'causal-capable')
has(el_txt, f"{F['legal_framework_measurement_quality_populated']} of the\n{T['Legal Framework']} Legal Framework studies", 'LF measurement quality')
has(el_txt, f"{F['abstract_only_extractions']} of the {n:,}", 'abstract-only')
mcn = F['mechanism_certainty_numeric']
has(el_txt, f"only {mcn['3'] + mcn['4']} of {n:,} studies", 'mechanism_certainty 3-4')
has(el_txt, f"{mcn['1']} (", 'mechanism_certainty level 1')
has(el_txt, f"{mcn['2']} (", 'mechanism_certainty level 2')
has(el_txt, f"{F['mechanism_certainty_narrative_text']} of {n:,}", 'mechanism_certainty narrative')
has(el_txt, f"{F['robins_i_ratings'].get('Moderate', 0)} land at", 'ROBINS-I moderate')
has(el_txt, f"{F['robins_i_ratings'].get('Serious', 0)} at", 'ROBINS-I serious')
_fam = F['effect_size_by_family']
_sw = '06_outputs/supplementary/'
has(_sw + 'family_A_swim_synthesis_2026-09-28.md', f"the {_fam['A']} studies", 'Family A size')
has(_sw + 'family_B_swim_synthesis_2026-09-28.md', f"k = {_fam['B']}", 'Family B size')
has(_sw + 'family_C_swim_synthesis_2026-09-28.md', f"Vote count across all {_fam['C']} studies", 'Family C size')
lb = F['legal_system_buckets']
has(el_txt, f"common law only {lb['common law']} ", 'legal-system common')
has(el_txt, f"civil law only {lb['civil law']} ", 'legal-system civil')
has(el_txt, f"mixed / both / customary {lb['mixed / both / customary']} ", 'legal-system mixed')
has(el_txt, f"{F['country_single_name_studies']:,} name exactly one country", 'country single-name count')
has(el_txt, f"**{F['country_multi_or_regional_studies']} name several countries or a region", 'country multi count')
for cname, cnt in F['country_top10_single_name'][:4]:
    has(el_txt, f"{cname} {cnt} (", f'top country {cname}')
has('RISK_OF_BIAS.md', f"AMSTAR 2 {T['AMSTAR 2']}, Legal Framework {T['Legal Framework']}, NONE {T['NONE']} (sum {n:,})", 'dated-correction figures')

# ---- D. boolean fields, generated-file freshness, queue
BOOL_COLS = ['peer_reviewed', 'household_level', 'community_level', 'indigenous_population', 'eligibility', 'burden', 'discretion_accommodation', 'enforcement',
             'documentation', 'tenure', 'property', 'planning', 'zoning', 'building_permit', 'service_area', 'fees', 'procedural_steps', 'delay', 'discretion',
             'hardship_exception', 'administrative_review', 'complaint', 'judicial_review', 'disconnection', 'reconnection', 'sanction', 'participation',
             'institutional_fragmentation', 'political_coordination', 'bureaucratic_assistance', 'formal_connection', 'water_access', 'sanitation_access',
             'service_coverage', 'service_reliability', 'service_quantity', 'service_quality', 'affordability', 'service_continuity', 'application_success',
             'refusal', 'delay_outcome']
_bad = [(r['study_id'], k, r[k]) for r in ed for k in BOOL_COLS if r[k] not in ('TRUE', 'FALSE', '')]
check(not _bad, f'boolean fields hold non-TRUE/FALSE/blank values: {_bad[:5]}')
_KNOWN_MIGRANT = {'S129', 'S412', 'S416'}  # three annotated values ("TRUE (...)" or "included as ...") recorded in DECISIONS_AND_OPEN_ITEMS.md
_mig = {r['study_id'] for r in ed if r['migrant_population'] not in ('TRUE', 'FALSE', '')}
check(_mig == _KNOWN_MIGRANT, f'migrant_population annotated values differ from the three known ones: {sorted(_mig ^ _KNOWN_MIGRANT)}')

if not (ROOT / '05_analysis/descriptive/amstar2_overlap_check_2026-10-04.csv').exists():  # build_preliminary_report.py reads it; fail cleanly instead of crashing
    print('FAIL: 05_analysis/descriptive/amstar2_overlap_check_2026-10-04.csv is missing (needed by build_preliminary_report.py)')
    sys.exit(1)
import build_manuscript_pieces as bmp, build_preliminary_report as bpr, propose_family_vocabulary as pv, sensitivity_analysis as sa  # noqa: E402
def fresh(path, generated, script):
    check(path.read_text(encoding='utf-8') == generated, f'{path.relative_to(ROOT)} is stale: run `python3 code/analysis/{script}`')
import build_report_html as brh  # noqa: E402
fresh(bmp.OUT, bmp.build(), 'build_manuscript_pieces.py')
fresh(bpr.OUT, bpr.build(), 'build_preliminary_report.py')
fresh(brh.OUT, brh.build(), 'build_report_html.py')
import build_manuscript_draft as bmd  # noqa: E402
fresh(bmd.OUT, bmd.build(), 'build_manuscript_draft.py')
import build_supporting_texts as bst  # noqa: E402
fresh(bst.OUT, bst.build(), 'build_supporting_texts.py')
fresh(pv.OUT_MD, pv.render(pv.build()), 'propose_family_vocabulary.py')
fresh(sa.OUT_MD, sa.render(*sa.scenarios()), 'sensitivity_analysis.py')
for needle in ('34,594', '27,481', '26,222', '1,259', '3,665'):
    check(needle in text('README.md'), f'README.md no longer contains {needle}, which build_manuscript_pieces.py hard-codes')
_q = csv.DictReader(open(ROOT / '02_screening/full_text/full_text_reviewer_2_priority_queue_2026-09-28.csv', encoding='utf-8', newline=''))
_tier1 = sum(1 for r in _q if r['priority_tier'] == '1')
check(_tier1 == F['decided_blank_reviewer_1'], f"reviewer_2 priority queue tier 1 has {_tier1} rows but {F['decided_blank_reviewer_1']} decided rows have no reviewer_1: rebuild the queue")
for f_ in ('00_admin/disclosures/FUNDING_AND_COMPETING_INTERESTS_TEMPLATE.md', '06_outputs/slides/Water_Access_Evidence_Diagnostic_slides_2026-09-29.pdf', '06_outputs/slides/README.md',
           '05_analysis/descriptive/amstar2_overlap_check_2026-10-04.csv', '05_analysis/descriptive/AMSTAR2_OVERLAP_CHECK_2026-10-04.md',
           '00_admin/RESEARCHER_DECISION_BRIEF_2026-10-04.md', *[f'06_outputs/figures/{x}.svg' for x in ('fig1_design_mix', 'fig2_publication_years', 'fig3_countries', 'fig4_direction_by_family', 'fig5_appraisal_tools')]):  # the report builder reads the overlap CSV
    check((ROOT / f_).exists(), f'{f_} is missing')

# ---- E. database sanity checks (added 2026-09-29) and freshness of the audit outputs
import re  # noqa: E402
import audit_data_quality as adq, build_second_extractor_sample as bse, build_fulltext_request_list as bfr, audit_sparse_records as asr, build_reclassification_proposal as brp, build_a16_adjudication_sheet as baa, audit_exclusion_basis as aeb, propose_design_vocabulary as pdv, audit_effect_size_families as aef, audit_includes_criterion3 as aic  # noqa: E402
_doi_bad = [(r['study_id'], r['doi']) for r in ed if r['doi'].strip() and not re.match(r'^10\.\d{4,9}/\S+$', r['doi'].strip())]
check(not _doi_bad, f'malformed DOI in extraction_database: {_doi_bad[:5]}')
_dois = [r['doi'].strip().lower() for r in ed if r['doi'].strip()]
check(len(_dois) == len(set(_dois)), 'the same DOI appears on two extraction rows (a double-counted paper?)')
_KNOWN_YEAR = {'S020', 'S071', 'S1057', 'S1085', 'S1148', 'S284', 'S285', 'S306', 'S425', 'S429', 'S449', 'S462', 'S465', 'S467', 'S492', 'S571', 'S589', 'S608', 'S614', 'S773', 'S794',
               'S796', 'S797', 'S931', 'S942', 'S948', 'S959', 'S972', 'S975'}  # publication_year differs from the screening record's year; listed in DATA_QUALITY_AUDIT_2026-09-29.md section 4
_new_year = [y for y in adq.year_audit() if y[0] not in _KNOWN_YEAR]
check(not _new_year, f'publication_year disagrees with the screening record for a study not in the known list: {_new_year[:5]}')
check(all(r['publication_year'].strip() == '' or (r['publication_year'].strip().isdigit() and 1900 <= int(r['publication_year']) <= 2027) for r in ed), 'publication_year outside 1900-2027 or not a number')
_class = {r['study_id']: r['study_design_class'] for r in em}
_ALLOWED = {'RoB 2': {'experimental'}, 'ROBINS-I': {'quasi_experimental'}, 'AMSTAR 2': {'systematic_review_secondary'}, 'JBI Cross-Sectional': {'observational'},
            'CASP Qualitative': {'qualitative'}, 'MMAT': {'mixed_methods'}}
_mismatch = [(r['study_id'], cf.tool_of(r['risk_of_bias_tool']), _class[r['study_id']]) for r in ed
             if cf.tool_of(r['risk_of_bias_tool']) in _ALLOWED and _class[r['study_id']] not in _ALLOWED[cf.tool_of(r['risk_of_bias_tool'])]]
check(not _mismatch, f'risk-of-bias tool does not fit the design class: {_mismatch[:5]}')
_none_class = [(r['study_id'], _class[r['study_id']]) for r in ed if cf.tool_of(r['risk_of_bias_tool']) == 'NONE' and _class[r['study_id']] not in ('systematic_review_secondary', 'doctrinal', 'jurimetric', 'qualitative', 'observational', 'mixed_methods') and _class[r['study_id']] in ('experimental', 'quasi_experimental')]
check(not _none_class, f'a randomised/quasi-experimental study has tool NONE: {_none_class[:5]}')
_STARTS = {'RoB 2': ('Some concerns', 'Low', 'High'), 'ROBINS-I': ('Low', 'Moderate', 'Serious', 'Critical', 'No information'),
           'AMSTAR 2': ('High', 'Moderate', 'Low', 'Critically Low', 'Not ratable'), 'JBI Cross-Sectional': ('High concern', 'Some concern', 'Low concern', 'JBI Cross')}
_badrate = [(r['study_id'], cf.tool_of(r['risk_of_bias_tool']), r['risk_of_bias_rating'][:30]) for r in ed
            if cf.tool_of(r['risk_of_bias_tool']) in _STARTS and not r['risk_of_bias_rating'].startswith(_STARTS[cf.tool_of(r['risk_of_bias_tool'])])]
check(not _badrate, f'rating text does not use its tool\'s vocabulary: {_badrate[:5]}')
_none_rate = [r['study_id'] for r in ed if cf.tool_of(r['risk_of_bias_tool']) == 'NONE' and r['risk_of_bias_rating'].strip() and not r['risk_of_bias_rating'].startswith('NOT APPLICABLE')]
check(not _none_rate, f'a tool-NONE study carries a real rating: {_none_rate[:5]}')
check(all(r['mechanism_certainty'] in ('0', '1', '2', '3', '4') or len(r['mechanism_certainty']) >= 10 for r in ed), 'mechanism_certainty is neither 0-4 nor a narrative')
check(all(re.match(r'^\d{4}-\d\d-\d\d', r['date_extracted']) and r['researcher'].strip() for r in ed), 'date_extracted not ISO or researcher blank')
_abs_ids = {r['study_id'] for r in ed if r['extraction_note'].startswith(cf.ABSTRACT_ONLY_PREFIXES)}
_abs_file = {r['study_id'] for r in csv.DictReader(open(ROOT / '05_analysis/sensitivity/abstract_only_extractions_2026-09-28.csv', encoding='utf-8', newline=''))}
check(_abs_ids == _abs_file, f'abstract_only_extractions csv differs from the extraction notes: {sorted(_abs_ids ^ _abs_file)[:8]}')


def _csv_rows(path):
    return list(csv.DictReader(open(path, encoding='utf-8', newline='')))


def _as_str(rows):
    return [{k: str(v) for k, v in r.items()} for r in rows]


fresh(asr.OUT_MD, asr.render(asr.audit()), 'audit_sparse_records.py')
_brp_rows, _brp_md = brp.build()
_baa_rows, _baa_md = baa.build()
# hand-written A16 figures in the status documents must match the computed projection (they went stale once when 9 more reviewer-2 rows were merged)
_a16_total, _a16_narrow, _a16_literal = baa.implied_total()
_a16_n3, _a16_k3, _a16_imp, _a16_lo, _a16_hi = baa.includes_side()
_a16_pool = F['full_text_include'] - F['reviewer_2_confirmed_includes']
_ws = lambda rel: ' '.join(text(rel).split())
for _rel, _phrases in {
        'README.md': (f'roughly {_a16_total} further includes', f'about {_a16_narrow} even under a narrow reading', f'{_a16_k3} of {_a16_n3} sampled'),
        '00_admin/DECISIONS_AND_OPEN_ITEMS.md': (f'roughly {_a16_total} further includes', f'about {_a16_narrow} even under a narrow reading', f'{_a16_k3} of {_a16_n3} sampled unconfirmed includes',
                                                 f'roughly {_a16_imp} of {_a16_pool:,} (range {_a16_lo}-{_a16_hi})'.replace(f'{_a16_pool:,}', str(_a16_pool))),
        '00_admin/RESEARCHER_DECISION_BRIEF_2026-10-04.md': (f'roughly {_a16_total} further includes', f'about {_a16_narrow} even under a narrow reading', f'{_a16_k3} of {_a16_n3} sampled includes',
                                                              f'roughly {_a16_imp} of the {_a16_pool} unconfirmed includes (range {_a16_lo}–{_a16_hi})'),
        '00_admin/SESSION_HANDOFF_2026-10-04.md': (f'about {_a16_total} implied further includes', f'about {_a16_narrow} under a narrow reading', f'{_a16_k3} of {_a16_n3} sampled unconfirmed includes',
                                                   f'about {_a16_imp} of {_a16_pool}, range {_a16_lo}-{_a16_hi}')}.items():
    _t = _ws(_rel)
    for _ph in _phrases:
        EXPECTED.append((_rel, _ph, 'A16 figure'))
        check(_ph in _t, f'{_rel}: A16 figure out of date, expected the phrase {_ph!r} (computed by build_a16_adjudication_sheet.py)')
fresh(baa.OUT_MD, _baa_md, 'build_a16_adjudication_sheet.py')
_aeb_rows, _aeb_md = aeb.build()
fresh(aeb.OUT_MD, _aeb_md, 'audit_exclusion_basis.py')
_pdv_rows = pdv.build()
fresh(pdv.OUT_MD, pdv.render(_pdv_rows), 'propose_design_vocabulary.py')
_aef_rows = aef.build()
fresh(aef.OUT_MD, aef.render(_aef_rows), 'audit_effect_size_families.py')
_aic_rows = aic.build()
fresh(aic.OUT_MD, aic.render(_aic_rows), 'audit_includes_criterion3.py')
fresh(brp.OUT_MD, _brp_md, 'build_reclassification_proposal.py')
fresh(adq.OUT_MD, adq.render(adq.flag_audit(), *adq.es_scan()[:1], len(es), adq.es_scan()[1], adq.amstar_sweep(), adq.year_audit(), adq.certainty_audit()), 'audit_data_quality.py')
for _path, _rows, _script in ((adq.OUT_CSV, adq.flag_audit(), 'audit_data_quality.py'), (adq.OUT_AM, adq.amstar_sweep(), 'audit_data_quality.py'),
                             (bse.OUT, bse.draw(), 'build_second_extractor_sample.py'), (bfr.OUT, bfr.rows(), 'build_fulltext_request_list.py'),
                             (asr.OUT_CSV, asr.audit(), 'audit_sparse_records.py'), (brp.OUT_CSV, _brp_rows, 'build_reclassification_proposal.py'), (baa.OUT_CSV, _baa_rows, 'build_a16_adjudication_sheet.py'), (aeb.OUT_CSV, _aeb_rows, 'audit_exclusion_basis.py'), (pdv.OUT_CSV, _pdv_rows, 'propose_design_vocabulary.py'), (aef.OUT_CSV, _aef_rows, 'audit_effect_size_families.py'), (aic.OUT_CSV, _aic_rows, 'audit_includes_criterion3.py')):
    check(_csv_rows(_path) == _as_str(_rows), f'{_path.relative_to(ROOT)} is stale: run `python3 code/analysis/{_script}`')

# every maintained script (everything outside code/provenance, which holds one-shot historical records that are deliberately not edited) has a module docstring
import ast as _ast
_nodoc = [str(q.relative_to(ROOT)) for q in sorted(list((ROOT / 'code').glob('**/*.py')) + list((ROOT / '08_code').glob('**/*.py'))) if 'provenance' not in q.parts and not _ast.get_docstring(_ast.parse(q.read_text(encoding='utf-8')))]
check(not _nodoc, f'scripts without a module docstring: {_nodoc[:5]}')

# the drop-down workbooks the researcher fills in must hold exactly the CSV rows (code/analysis/sheet_xlsx.py)
import sheet_xlsx as _sx  # noqa: E402
for _p in _sx.SPECS:
    check(_sx.in_sync(_p), f'{_sx.xlsx_path(_p).relative_to(ROOT)} is out of date: run `python3 code/analysis/sheet_xlsx.py`')

# every unit-test file in code/tests must be run by regenerate_all.sh (a new test file that is not listed there would never run)
_ra = text('code/analysis/regenerate_all.sh')
_unlisted = [q.stem for q in sorted((ROOT / 'code/tests').glob('test_*.py')) if q.stem not in _ra]
check(not _unlisted, f'unit-test files not run by code/analysis/regenerate_all.sh: {_unlisted}')

# provenance files the verifier and generated texts depend on must be tracked by git (a `*.json` ignore rule once kept the 2026-10-04 re-extraction records out of the repository)
try:
    import subprocess as _sp
    _tracked = {p.replace('\\', '/') for p in _sp.run(['git', 'ls-files', 'code/provenance/audit_and_repair/reextract_2026-10-04'], cwd=ROOT, capture_output=True, text=True, check=True).stdout.split()}
    _local = {str(q.relative_to(ROOT)).replace('\\', '/') for q in (ROOT / 'code/provenance/audit_and_repair/reextract_2026-10-04').glob('S*.json')}
    check(_local <= _tracked, f're-extraction JSONs not tracked by git (check .gitignore): {sorted(_local - _tracked)[:5]}')
except (OSError, _sp.CalledProcessError):
    pass  # not a git checkout (e.g. an exported archive): nothing to compare

if os.environ.get('VERIFY_EMIT_EXPECTED'):
    Path(os.environ['VERIFY_EMIT_EXPECTED']).write_text(json.dumps(EXPECTED), encoding='utf-8')
print(f"{passes} checks passed, {len(fails)} failed")
for f_ in fails:
    print('  FAIL:', f_)
sys.exit(1 if fails else 0)
