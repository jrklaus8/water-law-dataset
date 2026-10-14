"""2026-10-14: the SWiM core verification table (after the A26 rulings: Family A 16, B 6, C 17 = 39 studies of the 58 rows of effect_sizes.csv; the 19 reasoned non-fits are not in the three syntheses; it had 44 rows before A26).
One row per study with the exposure against its comparator, the outcome, the estimate, the raw coefficient sign and the substantive direction for household access (both from SWIM_DIRECTION_CODING_2026-10-14.csv, which is also what the
three family documents and the sensitivity analysis carry; a test checks they agree), the risk-of-bias tool and rating now in extraction_database.csv, whether the inclusion decision is human-verified (a 'Human-' confirmation or a CK ruling),
and whether the AI checked the row against the full text (FULLTEXT_VERIFICATION_2026-10-04.csv). The ck_* columns come from SWIM_CK_CHECKS_2026-10-14.csv (the author's confirmations of 2026-10-14 for the 20 studies that passed the scope and outcome check; blank for the 10 flagged for A28 and for the 9 studies whose inclusion was confirmed earlier, whose direction coding nobody has checked yet).
READ-ONLY on every database. Writes 05_analysis/effect_sizes/SWIM_CORE_VERIFICATION_TABLE_2026-10-14.{csv,md}; a rebuild keeps the ck_* columns because they are merged from the checks file.
Run from legal-last-mile-systematic-review/."""
import csv, os, re, sys
sys.path.insert(0, 'code/analysis')
csv.field_size_limit(sys.maxsize)
import current_figures as cf
import sensitivity_analysis as sa

OUT = '05_analysis/effect_sizes/SWIM_CORE_VERIFICATION_TABLE_2026-10-14'
CKFILE = '05_analysis/effect_sizes/SWIM_CK_CHECKS_2026-10-14.csv'   # the author's checks (apply_a26_swim_core_checks_2026-10-14.py); merged below, so a rebuild keeps them
# study: (exposure, comparator, outcome, estimate), written from effect_sizes.csv
S = {
 'S037': ('Place inside an irrigation district (DAC census places)', 'outside irrigation districts', 'poor drinking-water exposure score, % of places', '83% vs 79%, p=0.136'),
 'S057': ('Random offer of a targeted sanitation subsidy to eligible households', 'ineligible households / not offered', 'latrine purchase (sales closing)', '+32 pp; 38% vs 6%'),
 'S084': ('Non-notified slum status (Maharashtra Slum Areas Act)', 'notified slums', 'water per capita (log LPCD)', '-37.3% (95% CI -46.4 to -26.5), adjusted'),
 'S104': ('Home ownership', 'non-owners', 'piped-water interruption', 'OR 1.31, p<0.01 (more interruption)'),
 'S142': ('Unincorporated municipal status (U.S.)', 'incorporated block groups', 'centralised water/sewer access', 'significant reduction (neg. binomial IRR; CI in supplement)'),
 'S398': ('ZEIS zoning designation (Recife)', 'matched non-ZEIS tracts, DiD', 'sewage-network access', '+23 pp'),
 'S404': ('WRUA membership (Kenya Water Act)', 'non-members', 'water poverty', 'ATT -14% to -32%'),
 'S765': ('Legal land title (Peru PETT)', 'untitled households, DiD', 'improved water source', '+5.9 pp (SE 0.027), p<0.05'),
 'S780': ('Autonomous County legal status (Guizhou)', 'non-autonomous counties', 'drinking-water project beneficiaries', '-41,811 (SE 25,960), n.s.'),
 'S882': ('Own metered utility connection (Baguio)', 'no connection', 'consumption, cleanliness, ease, affordability', '+27.2% lpcd; +0.35 SD; ORs 2.16 and 2.76'),
 'S920': ('Water-user-association management of small systems', 'non-participatory municipal management', 'piped-water access rate', '~+6 pp over trend (DiD)'),
 'S930': ('Usos y costumbres municipality (Oaxaca)', 'party-governed municipalities', 'sewerage access', 'ATT 0.086, p<0.01'),
 'S1020': ('Watershed-development treatment villages', 'matched control watersheds', 'daily water-collection time', '+17.4 min/day (SE 2.46), i.e. worse'),
 'S1042': ('Community organisation and town-hall participation (Ukraine)', 'municipalities without', 'good water-supply situation', 'town hall +29 pp; peer pressure +14 pp'),
 'S1057': ('Design participation and satisfaction in demand-responsive programs', 'lower participation', 'log household collection-time saving', 'coef 1.63 (SE 0.95) to 2.92 (SE 0.95)'),
 'S1122': ('Non-zoned (informal) residence (Ouagadougou)', 'zoned periphery residents', 'time to first piped-water access', 'HR 0.14***'),
 'S085': ('Bureaucratic assistance (T1) with political coordination (T2)', 'control, no assistance', 'full formalisation of land/connection', '+19 pp (T1 with T2)'),
 'S294': ('Community-driven WASH with institutional strengthening (cluster RCT, DRC)', 'control villages', 'diarrhoea, child growth, WASH-institutions index', 'diarrhoea -0.01 (-0.05, 0.03); LAZ -0.01 (-0.15, 0.12)'),
 'S1102': ('Capital-cost contribution and meeting attendance (India)', 'non-contributors', 'water improvements index', 'difference 1.04 (t=4.26)'),
 'S1140': ('Network capital: number of partners (Nepal RWSSP)', 'fewer partners', 'funding success', 'log-odds 0.55*** (SE 0.10) per partner'),
 'S1144': ('Social-proximity trust in NGOs/CBOs (Kampala)', 'lower trust', 'access to NGO-supplied sanitation', 'coef 7.01 (SE 1.35); ME 1.01'),
 'S1163': ('External WASH-programme support to rural schools (14 LMICs)', 'no support', 'basic on-premises water service', 'OR 1.4 (1.1-1.7)'),
 'S174': ('Municipal institutional capacity (Brazil)', 'lower-capacity municipalities', 'water and sanitation coverage', 'coef 6.02 (SE 1.02) financial factor'),
 'S470': ('Arsae-MG enforcement norm (Minas Gerais)', 'same municipalities in 2020', 'social-tariff implementation', '+19.2 pp (SE 0.82)'),
 'S471': ('Mayor-led local government (U.S. utilities)', 'manager/council forms', 'basic drinking-water cost', '-1.58 (SE 0.69); -1.03 n.s. with covariates'),
 'S526': ('Investor-owned utility under a state PUC', 'government-owned utilities', 'regressivity of unit pricing (UPR)', '-0.167, p<0.001'),
 'S539': ('Investor-owned utility', 'government/cooperative-owned', 'household bill; lowest-quintile affordability', '+$144 a year; +1.55 pp'),
 'S593': ('Si (urban) district status (South Korea)', 'gun (rural) districts', 'equity of unit price and cost recovery', 'unit price -0.917 (2021, p<0.01); mixed'),
 'S631': ('New district created by pemekaran (Indonesia)', 'original parent districts', 'household protected water and sanitation access', '~-1% (DiD)'),
 'S749': ('Private ownership of the corporation (Brazil)', 'public and mixed-capital corporations', 'water tariff level', '+0.3456 R$/m3'),
 'S879': ('Random contract enforcement: credible disconnection notices (Kenya)', 'enforcement-exempt compounds', 'payment compliance; water access', 'payment +30 pp (p<0.001); access null'),
 'S947': ('Regulation quality, WGI (44 countries)', 'lower regulation-quality scores', 'access to drinking water', 'coef 0.0121 (SE 0.0035), p<0.01'),
 'S1032': ('Contact with the municipality or an NGO for redress (Ahmedabad)', 'no contact', 'household water complaints', 'OR 0.60* (municipal); 0.56* (NGO)'),
 'S1038': ('State PUC economic regulation of a municipal utility (U.S.; reported contrast)', 'local-only regulation', 'monopoly welfare loss, % of residential bill', '5.2% vs 9.6% (difference -4.6 pp)'),
 'S1062': ('O&M cost-recovery ratio (Sub-Saharan utilities)', 'lower cost-recovery ratios', 'coverage change', 'positive, then negative (inverted U)'),
 'S1136': ("Political capture: Gram Panchayat head's village or politician's road (India)", 'other roads', 'paved road, drain, cleanliness', 'paved 0.053***; drain 0.037**'),
 'S1146': ('Regional utilities-sector corruption (Afrobarometer)', 'regions with none', 'access to enough clean water', 'negative marginal effect (probit)'),
 'S1162': ('Municipality or town panchayat (India)', 'municipal corporations', 'water access, %', '-4.06 pp (SE 1.25), p<0.01'),
 'S1169': ('Price-regulated water provider (Texas colonias)', 'unregulated provider', 'colonia has water service', 'coef -1.19 (SE 0.42); ME -27 pp'),
}
ed = {r['study_id']: r for r in cf.read('ed')}
ft = {r['record_id']: r for r in cf.read('ft')}
es = {r['study_id']: r for r in cf.read('es')}
ver = {r['study_id']: r for r in csv.DictReader(open('05_analysis/effect_sizes/FULLTEXT_VERIFICATION_2026-10-04.csv', encoding='utf-8'))}
coding = {r['study_id']: r for r in csv.DictReader(open('05_analysis/effect_sizes/SWIM_DIRECTION_CODING_2026-10-14.csv', encoding='utf-8'))}
signs = {f: sa.parse_signs(f) for f in 'ABC'}
subst = {f: sa.parse_substantive(f) for f in 'ABC'}
fam_rows = [(f, s) for f in 'ABC' for s in sorted((x for x in es if es[x]['synthesis_family'] == f), key=lambda x: int(x[1:]))]
assert len(fam_rows) == 39 and {s for _, s in fam_rows} == set(S) == set(coding), sorted({s for _, s in fam_rows} ^ set(S))
SIGN_WORD = {'+': 'positive', '-': 'negative', 'null': 'null', 'mixed': 'mixed'}
for f, s in fam_rows:   # the family documents, the sensitivity analysis and this table must carry the same two codings
    assert signs[f][s] == SIGN_WORD[coding[s]['raw_coefficient_sign']] and subst[f][s] == coding[s]['substantive_direction'].lower(), (f, s)


def author(r):
    cit = r['citation']
    head = re.split(r'\s\(\d{4}|\.\s', cit)[0]
    names = [t.strip() for t in head.split(',') if t.strip()]
    def sur(t):
        w = t.split()
        # drop trailing initials (all-caps tokens)
        while len(w) > 1 and re.fullmatch(r"[A-ZÀ-Þ\.\-]{1,4}", w[-1]):
            w.pop()
        return ' '.join(w)
    if any('et al' in t for t in names) or len(names) >= 3:
        return f"{sur(names[0])} et al."
    if len(names) == 2:
        return f"{sur(names[0])} & {sur(names[1])}"
    return sur(names[0])


def rating(r):
    t = r['risk_of_bias_rating']
    if t.startswith('MMAT screening'):
        return 'no composite score (per-criterion answers)'
    m = re.match(r'^([A-Za-z][A-Za-z \-/]*?)(?: \(|:|;|\.|,|$)', t)
    return (m.group(1) if m else t[:30]).strip()


def ck(r):
    f = ft[r['record_id']]
    if f['reviewer_2'].startswith('Human-'):
        return 'Y (confirmed S001-S200)'
    if f['reviewer_2'] == 'CK' or any(m in f['notes'] for m in cf.HUMAN_RULING_MARKS):
        return 'Y (CK ruling)'
    return 'N'


ck_ = {r['study_id']: r for r in csv.DictReader(open(CKFILE, encoding='utf-8'))} if os.path.exists(CKFILE) else {}
assert set(ck_) <= {s for _, s in fam_rows}, 'a CK check names a study that is no longer in a SWiM family'
rows = []
for fam, s in fam_rows:
    r, e = ed[s], es[s]
    ex, cm, out, est = S[s]
    v = ver.get(s, {})
    c = coding[s]
    rows.append({'study_id': s, 'author_year': f"{author(r)} ({r['publication_year']})", 'family': fam, 'exposure_short': ex, 'comparator_short': cm, 'outcome_short': out, 'outcome_family': e['outcome_family'], 'estimate_short': est,
                 'raw_coefficient_sign': c['raw_coefficient_sign'], 'substantive_direction': c['substantive_direction'], 'outcome_polarity': c['outcome_polarity'], 'exposure_orientation': c['exposure_orientation'],
                 'alternative_substantive_direction': c['alternative_substantive_direction'], 'outcome_directness_check': c['outcome_directness_check'], 'ai_recommendation_for_author': c['ai_recommendation_for_author'], 'coding_note': c['coding_note'],
                 'rob_tool': cf.tool_of(r['risk_of_bias_tool']), 'rob_rating': rating(r), 'inclusion_decision_human_verified': ck(r),
                 'effect_row_checked_vs_full_text_by_AI': v.get('verdict', ''), 'raw_direction_text': e['direction'], 'exposure_full': e['exposure_definition'], 'comparator_full': e['comparator_definition'],
                 'estimate_full': e['effect_estimate'], 'scope_outcome_check_2026-10-14': ck_[s]['scope_outcome_check'] if s in ck_ else '', 'ck_raw_sign_agrees (Y/N)': ck_[s]['ck_raw_sign_agrees (Y/N)'] if s in ck_ else '',
                 'ck_substantive_direction_agrees (Y/N)': ck_[s]['ck_substantive_direction_agrees (Y/N)'] if s in ck_ else '', 'ck_comment': (ck_[s]['check_note'] if s in ck_ and ck_[s]['scope_outcome_check'] == 'flagged' else '')})
fields = list(rows[0])
with open(OUT + '.csv', 'w', newline='', encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=fields, lineterminator='\r\n'); w.writeheader(); w.writerows(rows)
L = ['# SWiM core verification table: the 39 family-assigned effect rows (A 16, B 6, C 17)', '',
     '*Generated by `code/provenance/audit_and_repair/build_swim_core_verification_table_2026-10-14.py`; read-only. Before the author\'s A26 rulings of 2026-10-14 it had 44 rows: S358 and S590 and S606 became reasoned non-fits, S1121 and S1143 were excluded. '
     'Two direction columns, because the raw sign of a coefficient and its meaning for households are different things (`SWIM_DIRECTION_CODING_2026-10-14.csv`, the AI\'s coding): **Raw sign** is the sign of the reported estimate for the contrast it reports (ratio above 1 = +, below 1 = -; null = not significant); '
     '**Substantive** is Favourable / Unfavourable / Null / Mixed for household access, affordability or equity, derived from the raw sign, the polarity of the outcome (is a higher value better or worse?) and the pole of the exposure. '
     '† = the exposure is a non-recognised status and the contrast is restated to the recognised pole (S084, S142, S1122); ‡ = the fully adjusted estimate gives a different direction (S471: Null); '
     '◊ = the outcome is not a household access measure (S1136 and S1140, kept by the author). **Human-verified** is the inclusion decision only (a Human- confirmation or a CK ruling). **CK check** is the author\'s confirmation of 2026-10-14 of the inclusion and of both direction codings '
     '(`SWIM_CK_CHECKS_2026-10-14.csv`): confirmed for the studies that passed the AI\'s narrow-scope and outcome check, **flagged** for the ten that did not (open item A28, not confirmed), blank for the nine whose inclusion was confirmed earlier and whose direction coding has not been checked. '
     'The effect estimates were extracted and checked against the full texts by the AI; no estimate has been verified by a human. The CSV also carries the polarity, the exposure pole, the notes and the ck_* columns.*', '',
     '| ID | Author (Year) | Fam | Exposure vs comparator | Outcome | Estimate | Raw sign | Substantive | RoB | Human-verified | CK check |', '|---|---|---|---|---|---|---|---|---|---|---|']
for x in rows:
    flags = ('†' if x['exposure_orientation'].startswith('restated') else '') + ('‡' if x['alternative_substantive_direction'] else '') + ('◊' if x['outcome_directness_check'].startswith('checked') else '')
    ckc = 'confirmed' if x['ck_raw_sign_agrees (Y/N)'] == 'Y' and x['ck_substantive_direction_agrees (Y/N)'] == 'Y' else 'flagged' if x['scope_outcome_check_2026-10-14'] == 'flagged' else ''
    L.append(f"| {x['study_id']}{' ' + flags if flags else ''} | {x['author_year']} | {x['family']} | {x['exposure_short']} vs {x['comparator_short']} | {x['outcome_short']} | {x['estimate_short']} | {x['raw_coefficient_sign']} | {x['substantive_direction']} | {x['rob_tool']}: {x['rob_rating']} | {x['inclusion_decision_human_verified'][0]} | {ckc} |")
open(OUT + '.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
import collections
print('wrote', OUT + '.csv/.md; raw', collections.Counter(x['raw_coefficient_sign'] for x in rows), 'substantive', collections.Counter(x['substantive_direction'] for x in rows), 'human-verified:', collections.Counter(x['inclusion_decision_human_verified'] for x in rows))
