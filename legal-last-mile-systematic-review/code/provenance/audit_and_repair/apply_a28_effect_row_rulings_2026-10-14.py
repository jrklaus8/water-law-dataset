"""2026-10-14, open item A28 (PI rulings, reviewer CK, from the verbatim PDF passages): the effect_sizes.csv side of the rulings. Run BEFORE resolve_a16_pending_reversals.py, which refuses to retire a study that still has an effect row.

1. S1020, S1042, S1057, S1144, S1163 and S947 leave the review (E03, E04, E03, E03, E03, E03; applied with apply_a16_adjudications.py and resolve_a16_pending_reversals.py from A28_ADJUDICATION_FILLED_2026-10-14.csv):
   their effect rows and FULLTEXT_VERIFICATION rows are archived to 11_archive/effect_sizes_removed_2026-10-13.csv and 11_archive/fulltext_verification_removed_2026-10-13.csv (which already hold the rows of S312, S435, S348, S969, S1121 and S1143).
2. S294 / S366 (Quattrochi et al., the DRC Healthy Villages and Schools cluster RCT): the full-text PDF on file is the 2021 BMJ Global Health report catalogued as S366, so the Family B effect row moves to S366 and is anchored to that report's
   verified improved-water-source estimate (Table 2, p. 7: intervention 0.83 vs control 0.43, adjusted ITT +0.33, 95% CI 0.22 to 0.45; 1,312 households, 121 clusters). S294 (the 2025 companion report) stays as the linked report of S366 with no
   effect row, because its diarrhoea, child-growth and institutions-index numbers could not be checked against a full text; its old effect row and verification row are archived with that explanation. S366 becomes quantitative-synthesis eligible and S294 does not.
3. S920 (Barde 2017): the provenance and extraction notes record its specific mechanism, regulatory_model_ownership (municipal concession transfer of water-supply responsibility to the user association by a formal concession contract) alongside participatory management.
   S1102 and S1146: provenance notes record the ruling (and, for S1102, that the project rule is written at village level while the analysed contributions are the households').
Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
ES = '05_analysis/effect_sizes/effect_sizes.csv'
VF = '05_analysis/effect_sizes/FULLTEXT_VERIFICATION_2026-10-04.csv'
ARCH_ES = '11_archive/effect_sizes_removed_2026-10-13.csv'
ARCH_VF = '11_archive/fulltext_verification_removed_2026-10-13.csv'
ED = '03_extraction/extracted_data/extraction_database.csv'
EM = '05_analysis/descriptive/evidence_map.csv'
LK = '03_extraction/extracted_data/linked_reports_2026-09-28.csv'
MARK = 'A28 ruling 2026-10-14 by CK'
REMOVE = ('S1020', 'S1042', 'S1057', 'S1144', 'S1163', 'S947')

S366_ROW = {
    'study_id': 'S366', 'outcome_family': 'water_access', 'synthesis_family': 'B',
    'exposure_definition': ("Random assignment to the DRC government's national Healthy Villages and Schools (VEA) programme, a community-driven WASH programme delivered through elected village WASH committees (new or improved water infrastructure, "
                            "sanitation and hygiene promotion, community financing), cluster-randomized across 121 clusters (50 intervention, 71 control) and 332 villages in four provinces of rural DRC in 2019."),
    'comparator_definition': 'Control clusters (71 clusters; no VEA intervention during the trial).',
    'effect_measure': ('Intention-to-treat adjusted difference in the proportion of households whose primary drinking-water source is improved (cluster-randomized controlled trial; the model includes controls for the randomisation blocks, province and number of villages per cluster; '
                       'Table 2, PDF p. 7).'),
    'effect_estimate': '0.33 (adjusted ITT difference in the proportion with an improved primary water source; 83% intervention vs 43% control)',
    'lower_CI': '0.22', 'upper_CI': '0.45', 'standard_error': '',
    'sample_size': '1,312 households (732 control, 580 intervention) in 328 villages in 121 clusters',
    'direction': 'positive (the programme raised the share of households using an improved primary drinking-water source by 33 percentage points, 95% CI 22 to 45)',
    'adjusted': 'adjusted (intention-to-treat; randomisation-block controls; cluster-randomized)',
    'evidence_status': 'OBSERVED',
    'provenance_note': (f'{MARK}: replaces the S294 effect row. The full-text PDF on file is the 2021 BMJ Global Health report of the VEA cluster RCT (Quattrochi et al., BMJ Glob Health 2021;6:e005030), which is the report catalogued as S366; '
                        'the estimate is its prespecified primary access outcome (Table 2, PDF p. 7; abstract, PDF p. 1: "increased access to improved water sources by 33 percentage points (pp) (95% CI 22 to 45)"). '
                        'The 2025 companion report (S294, linked report LR01) keeps its extraction row but no effect row: its diarrhoea, child-growth and institutions-index numbers were not checked against a full text. '
                        'The same trial also reports improved sanitation (+26 pp, 95% CI 14 to 37), time to collect water (-3.0 min, n.s.) and litres collected (+2.3 L, n.s.); those are not the Family B access estimate and are not entered here.'),
    'included_in_pooled_estimate': 'FALSE',
    'exclusion_from_pooling_reason': ('ANALYSIS_PLAN.md S2 -- single cluster-RCT; no other Family B study measures an improved-water-source outcome for a comparable exposure (S085 measures individual land formalisation, S1102 a participation-based water improvements index), '
                                      'so the studies are not poolable without manufacturing comparability across different outcome constructs. Vote counted only (SWiM).'),
}
S294_ARCH_NOTE = (f' | ARCHIVED 2026-10-14 ({MARK}): the full-text PDF on file under this ID is the 2021 report catalogued as S366, so these numbers (diarrhoea, child growth, institutions index) could not be checked against a full text; '
                  'the Family B effect row now sits on S366 (improved water source, +33 pp, 95% CI 22 to 45).')
S920_NOTE = (f' {MARK}: inclusion confirmed from the verbatim PDF passages (pp. 2-4, 8). Its specific mechanism is regulatory_model_ownership: the municipality transfers responsibility for water supply to the user association through a formal concession contract, '
             'alongside participatory management (the +6 pp rural piped-water access on premises is the matched difference-in-differences contrast between the two management models).')
S1102_NOTE = (f' {MARK}: inclusion confirmed from the verbatim PDF passages (pp. 6, 10; n = 1,523 households in 45 villages). The project rule that each village contribute capital costs (cash, labour or materials) is written at village level; '
              'the analysed exposures are the households\' own contribution and meeting attendance.')
S1146_NOTE = f' {MARK}: inclusion confirmed from the verbatim PDF passages (pp. 1, 10; N = 44,778, Afrobarometer Round 7): the exposure is the regional incidence of utility-sector corruption and extortion, which reduces household access to clean water.'
EXTRACTION_NOTES = {
    'S920': f' | {MARK}: its specific mechanism is regulatory_model_ownership (municipal concession transfer of water-supply responsibility to the user association through a formal concession contract) alongside participatory management; inclusion confirmed from the verbatim PDF passages (pp. 2-4, 8).',
    'S294': f' | {MARK}: kept as the linked report of S366. The full text on file is the S366 report, so this record\'s effect numbers (diarrhoea, child growth, institutions index) are not used in the synthesis and have not been checked against its own full text.',
    'S366': f' | {MARK}: the Family B effect row is anchored to this report\'s verified improved-water-source estimate (Table 2, PDF p. 7: +33 pp, 95% CI 22 to 45; 1,312 households, 121 clusters); the PDF filed under S294 is this report.',
}
S366_FV = {'study_id': 'S366', 'synthesis_family': 'B', 'numbers_in_row': '7', 'numbers_found_in_text': '7', 'numbers_not_found': '',
           'source_text': 'Drive full text (PDF filed under S294; it is the S366 report, BMJ Global Health 2021), pp. 1, 6-7', 'verdict': 'verified',
           'note': 'Table 2 (PDF p. 7): improved water source 0.43 control (N 732) vs 0.83 intervention (N 580), ITT 0.33 (0.22 to 0.45); text p. 6: 83% vs 43%, adjusted effect 33 percentage points (95% CI 22 to 45); 1312 households in 328 villages in 121 clusters; '
                    f'{MARK}.'}


def read(p):
    raw = open(p, newline='', encoding='utf-8').read()
    with open(p, newline='', encoding='utf-8') as f:
        rd = csv.DictReader(f)
        return rd.fieldnames, list(rd), '\r\n' if '\r\n' in raw[:30000] else '\n'


def write(p, fields, rows, eol):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(p) or '.', suffix='.tmp')
    with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator=eol)
        w.writeheader(); w.writerows(rows)
    os.replace(tmp, p)


changed = []
ef, er, ee = read(ES)
vf, vr, ve = read(VF)
byE = {r['study_id']: r for r in er}
if 'S366' not in byE:
    assert 'S294' in byE and byE['S294']['synthesis_family'] == 'B'
    ai, af_, ae = read(ARCH_ES)
    bi, bf_, be = read(ARCH_VF)
    assert ai == ef and bi == vf, 'archive headers differ from the live files'
    gone_e = [r for r in er if r['study_id'] in REMOVE + ('S294',)]
    gone_v = [r for r in vr if r['study_id'] in REMOVE + ('S294',)]
    assert {r['study_id'] for r in gone_e} == set(REMOVE) | {'S294'} and {r['study_id'] for r in gone_v} == set(REMOVE) | {'S294'}, 'a removed study lacks an effect or verification row'
    for r in gone_e:
        if r['study_id'] == 'S294':
            r['provenance_note'] = r['provenance_note'].rstrip() + S294_ARCH_NOTE
    for r in gone_v:
        if r['study_id'] == 'S294':
            r['note'] = r['note'].rstrip() + S294_ARCH_NOTE
    write(ARCH_ES, ai, [x for x in af_ if x['study_id'] not in {g['study_id'] for g in gone_e}] + gone_e, ae)
    write(ARCH_VF, bi, [x for x in bf_ if x['study_id'] not in {g['study_id'] for g in gone_v}] + gone_v, be)
    out_e, out_v = [], []
    for r in er:
        if r['study_id'] == 'S294':
            out_e.append({k: S366_ROW.get(k, '') for k in ef})
        elif r['study_id'] not in REMOVE:
            out_e.append(r)
    for r in vr:
        if r['study_id'] == 'S294':
            out_v.append({k: S366_FV.get(k, '') for k in vf})
        elif r['study_id'] not in REMOVE:
            out_v.append(r)
    er, vr = out_e, out_v
    write(VF, vf, vr, ve)
    changed.append(f'archived {len(REMOVE)} excluded studies and the S294 rows; S366 now holds the Family B effect row')
byE = {r['study_id']: r for r in er}
for s, note in (('S920', S920_NOTE), ('S1102', S1102_NOTE), ('S1146', S1146_NOTE)):
    if MARK not in byE[s]['provenance_note']:
        byE[s]['provenance_note'] = byE[s]['provenance_note'].rstrip() + note
        changed.append(f'{s} provenance note')
write(ES, ef, er, ee)

xf, xr, xe = read(ED)
bx = {r['study_id']: r for r in xr}
for s, note in EXTRACTION_NOTES.items():
    if MARK not in bx[s]['extraction_note']:
        bx[s]['extraction_note'] = bx[s]['extraction_note'].rstrip() + note
        changed.append(f'{s} extraction note')
write(ED, xf, xr, xe)

mf, mr, me = read(EM)
bm = {r['study_id']: r for r in mr}
if bm['S366']['quantitative_synthesis_eligible'] != 'TRUE':
    bm['S366']['quantitative_synthesis_eligible'] = 'TRUE'
    bm['S294']['quantitative_synthesis_eligible'] = 'FALSE'
    write(EM, mf, mr, me)
    changed.append('evidence map: S366 quantitative-synthesis eligible, S294 not')

lf, lr, le = read(LK)
l1 = next(r for r in lr if r['link_id'] == 'LR01')
if MARK not in l1['status']:
    l1['in_effect_sizes'] = 'second only'
    l1['status'] = l1['status'].rstrip() + f' | {MARK}: the Family B effect row moved from S294 to S366 (the report whose full text is on file); S294 stays the linked report with no effect row'
    write(LK, lf, lr, le)
    changed.append('LR01 in_effect_sizes = second only')
# the status file: the ten studies the AI flagged now carry the author's ruling
CK = '05_analysis/effect_sizes/SWIM_AI_SCOPE_CHECKS_2026-10-14.csv'
OUTCOME = {'S920': 'include (CK)', 'S1102': 'include (CK)', 'S1146': 'include (CK)', 'S294': 'include (CK); linked report of S366, which carries the Family B effect row',
           'S1020': 'exclude E03 (CK)', 'S1042': 'exclude E04 (CK)', 'S1057': 'exclude E03 (CK)', 'S1144': 'exclude E03 (CK)', 'S1163': 'exclude E03 (CK)', 'S947': 'exclude E03 (CK)'}
cf_, cr, ce = read(CK)
done = 0
for r in cr:
    if r['study_id'] in OUTCOME and not r['a28_outcome']:
        r['a28_outcome'] = OUTCOME[r['study_id']]
        r['ck_comment'] = f'{MARK} (inclusion only; the author has not yet confirmed the two-column direction coding)'
        done += 1
if done:
    write(CK, cf_, cr, ce)
    print(f'checks file: {done} A28 outcomes recorded')
from collections import Counter
print('changed:', changed if changed else 'nothing (already applied)')
print(Counter(r['synthesis_family'] or 'non-fit' for r in er), len(er))
