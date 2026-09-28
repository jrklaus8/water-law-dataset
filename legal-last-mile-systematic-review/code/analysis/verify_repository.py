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
import csv, json, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402

ROOT = cf.ROOT
fails, passes = [], 0


def check(cond, msg):
    global passes
    if cond:
        passes += 1
    else:
        fails.append(msg)


def text(rel):
    return (ROOT / rel).read_text(encoding='utf-8')


def has(rel, needle, label=None):
    check(needle in text(rel), f"{rel}: expected to contain {needle!r}" + (f" ({label})" if label else ''))


# ---- A. schemas
r = subprocess.run([sys.executable, str(ROOT / 'code/analysis/validate_schemas.py')], capture_output=True, text=True, cwd=ROOT)
check(r.returncode == 0 and 'match their documented' in r.stdout, 'validate_schemas.py failed:\n' + (r.stdout + r.stderr)[-600:])

# ---- B. cross-file logic
F = cf.compute()
ft, el, ed, em, es, mp, links = (cf.read(k) for k in ('ft', 'el', 'ed', 'em', 'es', 'map', 'links'))
ed_ids, em_ids, es_ids = {r['study_id'] for r in ed}, {r['study_id'] for r in em}, {r['study_id'] for r in es}
check(len(ed) == len(ed_ids), 'extraction_database has duplicate study_ids')
check(ed_ids == em_ids, f'extraction/evidence_map study_id sets differ: {sorted(ed_ids ^ em_ids)[:10]}')
check(es_ids <= ed_ids, f'effect_sizes has study_ids not extracted: {sorted(es_ids - ed_ids)}')
check(len(es) == len(es_ids), 'effect_sizes has more than one row for a study (CODEBOOK section 12: one prespecified effect per study)')
inc = {r['record_id'] for r in ft if r['final_decision'] == 'include'}
exc = {r['record_id'] for r in ft if r['final_decision'] == 'exclude'}
active = [r for r in mp if r['status'] == 'active']
check({r['study_id'] for r in active} == ed_ids, 'study_record_map active rows do not match extraction study_ids')
check({r['record_id'] for r in active} == inc and len(active) == len(inc), 'study_record_map is not a bijection with the full-text includes')
retired = {r['study_id']: r for r in mp if r['status'] != 'active'}
check(all(s not in ed_ids for s in retired), f'retired study IDs still present in extraction: {[s for s in retired if s in ed_ids]}')
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
has(readme, f"100 of {inc_n:,} current includes", 'reviewer_2 coverage')
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
has(el_txt, f"1,029 name exactly one country".replace('1,029', f"{F['country_single_name_studies']:,}"), 'country single-name count')
has(el_txt, f"**{F['country_multi_or_regional_studies']} name several countries or a region", 'country multi count')
for cname, cnt in F['country_top10_single_name'][:4]:
    has(el_txt, f"{cname} {cnt} (", f'top country {cname}')
has('RISK_OF_BIAS.md', f"Legal Framework {T['Legal Framework']}, NONE 12 (sum {n:,})", 'dated audit annotation figures')

print(f"{passes} checks passed, {len(fails)} failed")
for f_ in fails:
    print('  FAIL:', f_)
sys.exit(1 if fails else 0)
