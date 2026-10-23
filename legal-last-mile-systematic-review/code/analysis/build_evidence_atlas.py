#!/usr/bin/env python3
"""Generate 06_outputs/EVIDENCE_ATLAS_INTERACTIVE.html: a self-contained interactive page (no network needed) that lets a reader explore everything the review has analysed so far
(flow and screening reliability, the 1,072-study evidence map, design and appraisal, the 31-study SWiM direction coding with its verification status, the sensitivity scenarios, and the gaps).

Every number is computed here from the project databases (current_figures.py, the evidence map, the extraction database, SWIM_CORE_VERIFICATION_TABLE, sensitivity_scenarios, the A16 re-read) and embedded as JSON; the page itself
only filters and re-counts that data. Nothing is pooled, no GRADE judgment is made, and the page says which figures are human-verified (13 of the 31 SWiM inclusion decisions, 459 of 2,277 full-text decisions) and which are AI-produced.
The template is code/analysis/evidence_atlas_template.html. Two outputs: the standalone file in 06_outputs/ (wrapped in a document skeleton) and, with --fragment PATH, the bare fragment for publishing as an Artifact.

Run from legal-last-mile-systematic-review/:  python3 code/analysis/build_evidence_atlas.py [--fragment PATH]
"""
import argparse
import csv
import json
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


def short(s, n):
    s = re.sub(r'\s+', ' ', s).strip()
    return s if len(s) <= n else s[:n - 1].rstrip() + '…'


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
    if a.fragment:
        Path(a.fragment).write_text(frag, encoding='utf-8')
    print(f'wrote {OUT.relative_to(ROOT)} ({len(page) / 1024:.0f} KB; {len(D["studies"])} studies, {len(D["swim"])} SWiM studies, {len(D["scen"])} scenarios)')


if __name__ == '__main__':
    main()
