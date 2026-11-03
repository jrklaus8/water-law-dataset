#!/usr/bin/env python3
"""Generate 06_outputs/EVIDENCE_ATLAS_INTERACTIVE.html: a self-contained interactive page (no network needed) that lets a reader explore everything the review has analysed so far
(flow and screening reliability, the 1,072-study evidence map, design and appraisal, the 31-study SWiM direction coding with its verification status, the sensitivity scenarios, and the gaps).

Every number is computed here from the project databases (current_figures.py, the evidence map, the extraction database, SWIM_CORE_VERIFICATION_TABLE, sensitivity_scenarios, the A16 re-read) and embedded as JSON; the page itself
only filters and re-counts that data. Nothing is pooled, no GRADE judgment is made, and the page says which figures are human-verified (13 of the 31 SWiM inclusion decisions, 459 of 2,277 full-text decisions) and which are AI-produced.
The template is code/analysis/evidence_atlas_template.html. Outputs: the standalone file in 06_outputs/ (wrapped in a document skeleton), an identical copy at docs/atlas/index.html in the repository root (for GitHub Pages) when that docs/ folder exists, and, with --fragment PATH, the bare fragment for publishing as an Artifact.

Run from legal-last-mile-systematic-review/:  python3 code/analysis/build_evidence_atlas.py [--fragment PATH]
"""
import argparse
import csv
import glob
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402
import build_manuscript_pieces as bmp  # noqa: E402

csv.field_size_limit(sys.maxsize)
ROOT = cf.ROOT
TEMPLATE = Path(__file__).resolve().parent / 'evidence_atlas_template.html'
OUT = ROOT / '06_outputs/EVIDENCE_ATLAS_INTERACTIVE.html'
PAGES = ROOT.parent / 'docs/atlas/index.html'   # the same page, served by GitHub Pages at <site>/atlas/ when the repository's docs/ folder is the Pages source
AS_OF = '2026-10-14'

MECH = [('institutional_fragmentation', 'Institutional fragmentation'), ('discretion_accommodation', 'Discretion and accommodation'), ('fees', 'Fees'), ('service_area', 'Service-area rules'),
        ('political_coordination', 'Political coordination'), ('enforcement', 'Enforcement'), ('participation', 'Participation'), ('eligibility', 'Eligibility'), ('burden', 'Administrative burden'),
        ('documentation', 'Documentation'), ('bureaucratic_assistance', 'Bureaucratic assistance'), ('administrative_review', 'Administrative review'), ('complaint', 'Complaint channels'),
        ('judicial_review', 'Judicial review'), ('disconnection', 'Disconnection'), ('reconnection', 'Reconnection'), ('tenure', 'Tenure'), ('property', 'Property rights'),
        ('planning', 'Planning'), ('zoning', 'Zoning'), ('procedural_steps', 'Procedural steps'), ('hardship_exception', 'Hardship exceptions')]
OUTC = [('water_access', 'Water access'), ('sanitation_access', 'Sanitation access'), ('service_coverage', 'Coverage'), ('service_reliability', 'Reliability'), ('service_quantity', 'Quantity'),
        ('service_quality', 'Quality'), ('affordability', 'Affordability'), ('service_continuity', 'Continuity'), ('formal_connection', 'Formal connection'), ('application_success', 'Application success'),
        ('refusal', 'Refusal'), ('delay_outcome', 'Delay')]
EXCL = {'E01': 'Wrong topic', 'E02': 'Wrong population', 'E03': 'Wrong exposure', 'E04': 'Wrong outcome', 'E05': 'No empirical evidence', 'E06': 'Engineering only', 'E07': 'Wrong service',
        'E08': 'Duplicate', 'E09': 'Insufficient information', 'E10': 'Inaccessible full text', 'E11': 'Wrong jurisdiction', 'E12': 'Wrong study design'}
T = lambda v: str(v).strip().upper() == 'TRUE'


def legal_bucket(v):
    v = v.strip().lower()
    if not v:
        return 'unspecified'
    has_c, has_v = 'common' in v, 'civil' in v
    if (has_c and has_v) or any(k in v for k in ('mixed', 'hybrid', 'pluralis', 'customary')):
        return 'mixed or customary'
    return 'common law' if has_c else 'civil law' if has_v else 'other'


def setting_bucket(v):
    v = v.strip().lower()
    if not v:
        return 'unspecified'
    if 'informal' in v:
        return 'urban informal'
    if v.startswith('urban'):
        return 'urban'
    if 'peri' in v:
        return 'peri-urban'
    if v.startswith('rural'):
        return 'rural'
    if any(k in v for k in ('mixed', 'both', 'national')):
        return 'mixed or national'
    return 'unspecified'


def country_of(c):
    multi_re = re.compile(r'[;/&,]| and |multi|global|various|several|worldwide|international', re.I)
    and_names = re.compile(r'trinidad and tobago|bosnia and herzegovina|antigua and barbuda|saint kitts and nevis|st\.? kitts and nevis|saint vincent and the grenadines|sao tome and principe|s[aã]o tom[eé] and pr[ií]ncipe|turks and caicos', re.I)
    c = c.strip()
    if not c:
        return ''
    return 'Several countries or region' if multi_re.search(and_names.sub('', c)) else c


def doi_of(d):
    return re.sub(r'^https?://(dx\.)?doi\.org/', '', d.strip(), flags=re.I)


def short(s, n):
    s = re.sub(r'\s+', ' ', s).strip()
    return s if len(s) <= n else s[:n - 1].rstrip() + '…'


def methods(F, ed):
    """Numbers and strings the Methodology tab states, computed from the search log, the raw exports and the screening databases."""
    raw = {}
    for p in sorted(glob.glob(str(ROOT / '01_search/raw_exports/*.csv'))):
        n = sum(1 for _ in csv.DictReader(open(p, encoding='utf-8', errors='replace', newline='')))
        b = os.path.basename(p)
        k = ('Scopus' if '_SCOPUS_' in b else 'Web of Science' if '_WOS_' in b else 'ProQuest (full-text and abstract query)' if 'SEARCH_039' in b else 'ProQuest Sociological Abstracts (thesaurus terms)' if 'SEARCH_040' in b
             else 'JSTOR' if '_JSTOR_' in b else 'HeinOnline' if 'HEINONLINE' in b else 'SSRN' if 'SSRN' in b else 'Exploratory web-search pilot')
        raw[k] = raw.get(k, 0) + n
    assert sum(raw.values()) == bmp.RAW, (sum(raw.values()), bmp.RAW)
    log = list(csv.DictReader(open(ROOT / '01_search/search_logs/search_log.csv', encoding='utf-8')))
    scopus = [r for r in log if r['database'] == 'Scopus']
    real = [r for r in log if r['database'] in ('Scopus', 'Web of Science', 'HeinOnline', 'ProQuest', 'ProQuest (Sociological Abstracts)', 'JSTOR')]
    first = next(r for r in log if r['search_id'] == 'SEARCH_018')['exact_search_string']
    ta = list(csv.DictReader(open(ROOT / '02_screening/title_abstract/screening_database.csv', encoding='utf-8')))
    tac = Counter(r['title_abstract_decision'] or 'blank' for r in ta)
    n_cols = len(ed[0])
    assert n_cols == 93, n_cols   # 92 codebook fields plus record_id
    return {'raw': raw, 'scopus_runs': len(scopus), 'search_first': min(r['date'] for r in real), 'search_last': max(r['date'] for r in real), 'scopus_string': first,
            'ta_ai': {'include': tac['include'], 'exclude': tac['exclude'], 'unsure': tac['unsure'], 'blank': tac['blank']}, 'fields': n_cols - 1,
            'models': 'Claude (Anthropic) for first-pass screening, extraction, appraisal and synthesis drafting; Codex (OpenAI) and Gemini (Google) as blind second reviewers on part of the full-text decisions'}


def texts(F, ed, em):
    """The full lists a reader needs to reproduce the study: every included text with its full citation and DOI, every full text excluded with its code, and every candidate never assessed."""
    ft = cf.read('ft')
    fam = {r['study_id']: r['synthesis_family'] for r in cf.read('es') if r['synthesis_family'] in ('A', 'B', 'C')}
    inc = [[r['study_id'], r['publication_year'], re.sub(r'\s+', ' ', r['citation']).strip(), doi_of(r['doi']), r['record_id'], fam.get(r['study_id'], '')] for r in ed]
    inc.sort(key=lambda x: int(x[0][1:]))
    exc = [[r['record_id'], r['year'], re.sub(r'\s+', ' ', r['authors']).strip(), re.sub(r'\s+', ' ', r['title']).strip(), doi_of(r['doi']), r['exclusion_reason'], short(r['exclusion_reason_detail'], 150)]
           for r in ft if r['final_decision'] == 'exclude']
    una = [[r['record_id'], r['year'], re.sub(r'\s+', ' ', r['authors']).strip(), re.sub(r'\s+', ' ', r['title']).strip(), doi_of(r['doi']), 'wf' if r['full_text_status'] == 'wrong_file_retrieved' else 'nr']
           for r in ft if not r['final_decision']]
    assert (len(inc), len(exc), len(una)) == (F['full_text_include'], F['full_text_exclude'], F['full_text_undecided'])
    return {'inc': inc, 'exc': sorted(exc, key=lambda x: (x[5], x[3].lower())), 'una': sorted(una, key=lambda x: x[3].lower())}


def weaknesses():
    """The weakness register as written to 00_admin/WEAKNESS_REGISTER.csv (read from the file, not imported: that generator imports this module)."""
    with open(ROOT / '00_admin/WEAKNESS_REGISTER.csv', newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    def first(t, n=190):
        s = re.split(r'(?<=[a-z0-9\)])\.\s', t, maxsplit=1)[0].rstrip('.')
        return s if len(s) <= n else s[:n - 1].rstrip() + '…'
    order = {'high': 0, 'medium': 1, 'low': 2}
    return [{'id': r['id'], 'stage': r['stage'], 'sev': r['severity_ai_judgment'], 'text': first(r['weakness']), 'test': first(r['how_to_test_or_break_it'], 170), 'status': r['status']}
            for r in sorted(rows, key=lambda r: (order[r['severity_ai_judgment']], r['id']))]


def gather():
    F = cf.compute()
    ed, em = cf.read('ed'), {r['study_id']: r for r in cf.read('em')}
    ft = {r['record_id']: r for r in cf.read('ft')}
    studies = []
    for r in ed:
        s = r['study_id']
        e = em[s]
        yr = int(r['publication_year']) if r['publication_year'].strip().isdigit() else 0
        mb = sum(1 << i for i, (k, _) in enumerate(MECH) if T(r.get(k, '')))
        ob = sum(1 << i for i, (k, _) in enumerate(OUTC) if T(r.get(k, '')))
        cert = r['mechanism_certainty'].strip()
        studies.append({'id': s, 'y': yr, 'c': country_of(r['country']), 'd': e['study_design_class'], 'm': e['mechanism_family'], 'o': e['outcome_family'], 't': cf.tool_of(r['risk_of_bias_tool']),
                        'q': int(e['quantitative_synthesis_eligible'] == 'TRUE'), 'l': legal_bucket(r['legal_system']), 'u': setting_bucket(r['urban_rural']), 'k': int(cert) if cert.isdigit() else -1,
                        'mb': mb, 'ob': ob, 'cite': short(r['citation'], 130)})
    # ---- SWiM core
    tab = list(csv.DictReader(open(ROOT / '05_analysis/effect_sizes/SWIM_CORE_VERIFICATION_TABLE_2026-10-14.csv', encoding='utf-8')))
    es = {r['study_id']: r for r in cf.read('es')}
    edb = {r['study_id']: r for r in ed}
    swim = []
    for r in tab:
        s = r['study_id']
        inc = r['inclusion_decision_human_verified']
        f = ft[edb[s]['record_id']]
        a28 = 'A28 ruling' in f['notes']
        status = 'ai' if inc.startswith('N') else 'human'
        detail = ('Ruled in by the author under A28, from the verbatim PDF passages' if a28 else 'Confirmed by the author in the S001-S200 pass' if 'S001' in inc else 'Decided by the author in an earlier ruling' if status == 'human'
                  else "AI-checked only: the AI's scope and outcome check found no red flag; not a human confirmation")
        swim.append({'id': s, 'fam': r['family'], 'ay': r['author_year'], 'ex': r['exposure_short'], 'cm': r['comparator_short'], 'out': r['outcome_short'], 'est': r['estimate_short'],
                     'raw': r['raw_coefficient_sign'], 'sub': r['substantive_direction'], 'pol': r['outcome_polarity'], 'ori': r['exposure_orientation'], 'alt': r['alternative_substantive_direction'],
                     'note': r['coding_note'], 'tool': r['rob_tool'], 'rob': r['rob_rating'], 'status': status, 'detail': detail, 'country': edb[s]['country'], 'year': edb[s]['publication_year'],
                     'cite': short(edb[s]['citation'], 230), 'n': short(es[s]['sample_size'], 140), 'design': em[s]['study_design_class'],
                     'checked': r['effect_row_checked_vs_full_text_by_AI']})
    swim.sort(key=lambda x: (x['fam'], int(x['id'][1:])))
    # ---- scenarios
    scen = []
    for r in csv.DictReader(open(ROOT / '05_analysis/sensitivity/sensitivity_scenarios_2026-09-28.csv', encoding='utf-8')):
        scen.append({'name': r['scenario'], 'dropped': [x for x in r['dropped_studies_in_families'].split(';') if x], 'recoded': [x for x in r['recoded_as_null'].split(';') if x],
                     'A': [int(r[k]) for k in ('A_k', 'A_favourable', 'A_unfavourable', 'A_subst_null', 'A_subst_mixed')],
                     'B': [int(r[k]) for k in ('B_k', 'B_favourable', 'B_unfavourable', 'B_subst_null', 'B_subst_mixed')],
                     'C': [int(r[k]) for k in ('C_k', 'C_favourable', 'C_unfavourable', 'C_subst_null', 'C_subst_mixed')],
                     'Craw': [int(r[k]) for k in ('C_positive', 'C_negative', 'C_null', 'C_mixed')],
                     'tests': {'A majority favourable': r['A_test_majority_concordant'], 'B none unfavourable or null': r['B_test_none_negative_or_null'],
                               'C no dominant raw sign': r['C_test_no_dominant_sign'], 'C no dominant substantive direction': r['C_test_no_dominant_direction']}})
    a16 = bmp._a16_outcome()
    n_dec = F['full_text_decided']
    hv_inc = F['reviewer_2_confirmed_includes'] + F['human_adjudicated_includes']
    hv = {'confirmed_includes': F['reviewer_2_confirmed_includes'], 'adj_includes': F['human_adjudicated_includes'], 'adj_excludes': F['human_adjudicated_excludes'],
          'ai_includes': F['full_text_include'] - hv_inc, 'ai_excludes': F['full_text_exclude'] - F['human_adjudicated_excludes'], 'total': F['human_verified_rows'], 'decided': n_dec}
    assert sum(hv[k] for k in ('confirmed_includes', 'adj_includes', 'adj_excludes', 'ai_includes', 'ai_excludes')) == n_dec
    flow = [{'k': 'identified', 'label': 'Records identified', 'n': bmp.RAW, 'note': f'Searches closed {bmp.SEARCH_CLOSED}; SSRN and Westlaw/Lexis were never searched'},
            {'k': 'unique', 'label': 'After de-duplication', 'n': bmp.UNIQUE, 'note': f"{bmp.RAW - bmp.UNIQUE:,} duplicates merged"},
            {'k': 'ta_in', 'label': 'Title and abstract: included', 'n': F['title_abstract_include'], 'note': f"{bmp.TA_SCREENED:,} had an abstract and were screened by the AI; a human second pass covered the {bmp.TA_HUMAN_PASS:,} include-or-unsure records, not the AI's excludes"},
            {'k': 'ft', 'label': 'Full text assessed', 'n': n_dec, 'note': f"{F['full_text_undecided']:,} candidates never assessed ({F['unretrieved_not_retrievable']:,} not retrievable, {F['unretrieved_wrong_file']} wrong file); retrieval closed by decision"},
            {'k': 'inc', 'label': 'Included studies', 'n': F['full_text_include'], 'note': f"{F['full_text_exclude']:,} excluded on full text"},
            {'k': 'es', 'label': 'With an extractable effect-size row', 'n': F['effect_size_rows'], 'note': f"{F['effect_size_by_family']['(none: reasoned non-fit)']} are reasoned non-fits outside the three families; none is pooled"},
            {'k': 'swim', 'label': 'In the three SWiM families', 'n': F['swim_core_studies'], 'note': 'Vote counting of direction only'},
            {'k': 'hv', 'label': 'SWiM studies with a human-verified inclusion', 'n': F['swim_core_inclusion_human_verified'], 'note': f"{F['swim_core_ai_checked_not_human']} are AI-checked only; the author has confirmed the direction coding of {F['swim_core_direction_ck_confirmed']}"}]
    D = {'asof': AS_OF, 'release': '0.2.0-interim', 'flow': flow,
         'excl': [{'code': k, 'label': EXCL[k], 'n': v} for k, v in F['exclusion_by_code'].items()],
         'a16': {k: a16[k] for k in ('reread_excludes', 'sample', 'reversed_in_sample', 'rate', 'rate_lo', 'rate_hi', 'pool', 'scaled', 'scaled_lo', 'scaled_hi', 'moved_to_exclusion')},
         'hv': hv, 'second_model': {'rows': F['reviewer_2_second_model_rows'], 'conflicts': F['reviewer_2_second_model_conflicts']},
         'mech': [{'key': k, 'label': l} for k, l in MECH], 'outc': [{'key': k, 'label': l} for k, l in OUTC], 'excl_labels': EXCL,
         'tools': F['tools'], 'robins': F['robins_i_ratings'], 'rob2': F['rob2_ratings'], 'jbi_high': F['jbi_high_concern'], 'abstract_only': F['abstract_only_extractions'],
         'qeligible': F['quantitative_synthesis_eligible'], 'effect_rows': F['effect_size_rows'], 'families': F['effect_size_by_family'], 'borderline': F['borderline_includes'],
         'studies': studies, 'swim': swim, 'scen': scen,
         'methods': methods(F, ed), 'texts': texts(F, ed, em), 'weak': weaknesses(),
         'unassessed': F['full_text_undecided'], 'distinct_studies': F['distinct_studies_definite_links'], 'direction_confirmed': F['swim_core_direction_ck_confirmed']}
    return D


def render(D):
    t = TEMPLATE.read_text(encoding='utf-8')
    assert '/*__DATA__*/' in t
    return t.replace('/*__DATA__*/', 'const D = ' + json.dumps(D, ensure_ascii=False, separators=(',', ':')) + ';')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--fragment', help='also write the bare fragment (for publishing as an Artifact) to this path')
    a = ap.parse_args()
    D = gather()
    frag = render(D)
    page = '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n</head>\n<body>\n' + frag + '\n</body>\n</html>\n'
    OUT.write_text(page, encoding='utf-8')
    if PAGES.parent.parent.is_dir():
        PAGES.parent.mkdir(exist_ok=True)
        PAGES.write_text(page, encoding='utf-8')
    if a.fragment:
        Path(a.fragment).write_text(frag, encoding='utf-8')
    print(f'wrote {OUT.relative_to(ROOT)} ({len(page) / 1024:.0f} KB; {len(D["studies"])} studies, {len(D["swim"])} SWiM studies, {len(D["scen"])} scenarios)')


if __name__ == '__main__':
    main()
