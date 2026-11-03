"""2026-10-14: the SWiM core verification table (after the A26, A28 and A29 rulings: Family A 13, B 3, C 15 = 31 studies of the 52 rows of effect_sizes.csv; the 21 reasoned non-fits are not in the three syntheses; it had 44 rows before A26, 39 before A29 and 37 before A28).
One row per study with the exposure against its comparator, the outcome, the estimate, the raw coefficient sign and the substantive direction for household access (both from SWIM_DIRECTION_CODING_2026-10-14.csv, which is also what the
three family documents and the sensitivity analysis carry; a test checks they agree), the risk-of-bias tool and rating now in extraction_database.csv, whether the inclusion decision is human-verified (a 'Human-' confirmation or a CK ruling),
and whether the AI checked the row against the full text (FULLTEXT_VERIFICATION_2026-10-04.csv). The ai_scope_check and a28_outcome columns come from SWIM_AI_SCOPE_CHECKS_2026-10-14.csv: 18 studies passed the AI's narrow-scope and outcome
check and are AI-checked only (not a human confirmation: relabelled under A31); the author ruled on the ten the AI flagged (A28, from the verbatim PDF passages: six excluded, four kept). The ck_* columns are the author's confirmation of the two direction
codings; they are empty for every study because the author has not confirmed any direction coding. READ-ONLY on every database. Writes 05_analysis/effect_sizes/SWIM_CORE_VERIFICATION_TABLE_2026-10-14.{csv,md}.
Run from legal-last-mile-systematic-review/."""
import csv, os, re, sys
sys.path.insert(0, 'code/analysis')
csv.field_size_limit(sys.maxsize)
import current_figures as cf
import sensitivity_analysis as sa

OUT = '05_analysis/effect_sizes/SWIM_CORE_VERIFICATION_TABLE_2026-10-14'
CKFILE = '05_analysis/effect_sizes/SWIM_AI_SCOPE_CHECKS_2026-10-14.csv'   # the AI's scope checks and the author's A28 outcomes (apply_a26_swim_core_checks_2026-10-14.py, apply_a31_relabel_ai_checked_2026-10-14.py, apply_a28_effect_row_rulings_2026-10-14.py); merged below
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
 'S1122': ('Non-zoned (informal) residence (Ouagadougou)', 'zoned periphery residents', 'time to first piped-water access', 'HR 0.14***'),
 'S085': ('Bureaucratic assistance (T1) with political coordination (T2)', 'control, no assistance', 'full formalisation of land/connection', '+19 pp (T1 with T2)'),
 'S366': ('Community-driven WASH (VEA programme) through village WASH committees (cluster RCT, DRC)', 'control clusters', 'improved primary drinking-water source', '83% vs 43%; ITT +33 pp (95% CI 22 to 45)'),
 'S1102': ('Capital-cost contribution and meeting attendance (India)', 'non-contributors', 'water improvements index', 'difference 1.04 (t=4.26)'),
 'S174': ('Municipal institutional capacity (Brazil)', 'lower-capacity municipalities', 'water and sanitation coverage', 'coef 6.02 (SE 1.02) financial factor'),
 'S470': ('Arsae-MG enforcement norm (Minas Gerais)', 'same municipalities in 2020', 'social-tariff implementation', '+19.2 pp (SE 0.82)'),
 'S471': ('Mayor-led local government (U.S. utilities)', 'manager/council forms', 'basic drinking-water cost', '-1.58 (SE 0.69); -1.03 n.s. with covariates'),
 'S526': ('Investor-owned utility under a state PUC', 'government-owned utilities', 'regressivity of unit pricing (UPR)', '-0.167, p<0.001'),
 'S539': ('Investor-owned utility', 'government/cooperative-owned', 'household bill; lowest-quintile affordability', '+$144 a year; +1.55 pp'),
 'S593': ('Si (urban) district status (South Korea)', 'gun (rural) districts', 'equity of unit price and cost recovery', 'unit price -0.917 (2021, p<0.01); mixed'),
 'S631': ('New district created by pemekaran (Indonesia)', 'original parent districts', 'household protected water and sanitation access', '~-1% (DiD)'),
 'S749': ('Private ownership of the corporation (Brazil)', 'public and mixed-capital corporations', 'water tariff level', '+0.3456 R$/m3'),
 'S879': ('Random contract enforcement: credible disconnection notices (Kenya)', 'enforcement-exempt compounds', 'payment compliance; water access', 'payment +30 pp (p<0.001); access null'),
 'S1032': ('Contact with the municipality or an NGO for redress (Ahmedabad)', 'no contact', 'household water complaints', 'OR 0.60* (municipal); 0.56* (NGO)'),
 'S1038': ('State PUC economic regulation of a municipal utility (U.S.; reported contrast)', 'local-only regulation', 'monopoly welfare loss, % of residential bill', '5.2% vs 9.6% (difference -4.6 pp)'),
 'S1062': ('O&M cost-recovery ratio (Sub-Saharan utilities)', 'lower cost-recovery ratios', 'coverage change', 'positive, then negative (inverted U)'),
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
assert len(fam_rows) == 31 and {s for _, s in fam_rows} == set(S) == set(coding), sorted({s for _, s in fam_rows} ^ set(S))
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
    return 'N (AI-checked only)' if ck_.get(r['study_id'], {}).get('ai_scope_check') == 'passed' else 'N'


ck_ = {r['study_id']: r for r in csv.DictReader(open(CKFILE, encoding='utf-8'))} if os.path.exists(CKFILE) else {}
assert all(ck_[s]['a28_outcome'] for s in set(ck_) - {s for _, s in fam_rows}), 'a checked study left the SWiM families without a recorded ruling'
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
                 'estimate_full': e['effect_estimate'], 'ai_scope_check_2026-10-14': ck_[s]['ai_scope_check'] if s in ck_ else '', 'a28_outcome': ck_[s]['a28_outcome'] if s in ck_ else '', 'ck_raw_sign_agrees (Y/N)': ck_[s]['ck_raw_sign_agrees (Y/N)'] if s in ck_ else '',
                 'ck_substantive_direction_agrees (Y/N)': ck_[s]['ck_substantive_direction_agrees (Y/N)'] if s in ck_ else '', 'ck_comment': (ck_[s]['check_note'] if s in ck_ and ck_[s]['ai_scope_check'] == 'flagged' else '')})
fields = list(rows[0])
with open(OUT + '.csv', 'w', newline='', encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=fields, lineterminator='\r\n'); w.writeheader(); w.writerows(rows)
L = ['# SWiM core verification table: the 31 family-assigned effect rows (A 13, B 3, C 15)', '',
     '*Generated by `code/provenance/audit_and_repair/build_swim_core_verification_table_2026-10-14.py`; read-only. It had 44 rows before the author\'s rulings of 2026-10-14: S358, S590 and S606 became reasoned non-fits under A26, S1121 and S1143 were excluded, S1140 and S1136 became reasoned non-fits under A29, and S1020, S1042, S1057, S1144, S1163 and S947 were excluded under A28 (S294\'s row moved to S366). '
     'Two direction columns, because the raw sign of a coefficient and its meaning for households are different things (`SWIM_DIRECTION_CODING_2026-10-14.csv`, the AI\'s coding): **Raw sign** is the sign of the reported estimate for the contrast it reports (ratio above 1 = +, below 1 = -; null = not significant); '
     '**Substantive** is Favourable / Unfavourable / Null / Mixed for household access, affordability or equity, derived from the raw sign, the polarity of the outcome (is a higher value better or worse?) and the pole of the exposure. '
     '† = the exposure is a non-recognised status and the contrast is restated to the recognised pole (S084, S142, S1122); ‡ = the fully adjusted estimate gives a different direction (S471: Null); '
     '**Inclusion** is the verification status of the inclusion decision only: **Y** = a Human- confirmation or a ruling under reviewer CK (for S920, S1102, S1146 and S366 the A28 rulings of 2026-10-14, made from the verbatim PDF passages); **AI** = checked only by the AI against the narrow reading of criteria 2 and 4 (no red flag), which is not a human confirmation (relabelled under A31; see `SWIM_31_SOURCE_VERIFICATION_DOSSIER.md` for the passages the author reviews); '
     '**N** = neither. **Direction** is the author\'s confirmation of both direction codings (the ck_* columns): the author has not confirmed any, so the column is empty throughout. '
     'The effect estimates were extracted and checked against the full texts by the AI; no estimate has been verified by a human. The CSV also carries the polarity, the exposure pole, the notes, the AI scope check and the A28 outcome.*', '',
     '| ID | Author (Year) | Fam | Exposure vs comparator | Outcome | Estimate | Raw sign | Substantive | RoB | Inclusion | Direction |', '|---|---|---|---|---|---|---|---|---|---|---|']
for x in rows:
    flags = ('†' if x['exposure_orientation'].startswith('restated') else '') + ('‡' if x['alternative_substantive_direction'] else '') + ('◊' if x['outcome_directness_check'].startswith('checked') else '')
    ckc = 'confirmed' if x['ck_raw_sign_agrees (Y/N)'] == 'Y' and x['ck_substantive_direction_agrees (Y/N)'] == 'Y' else ''
    inc = 'AI' if x['inclusion_decision_human_verified'].startswith('N (AI') else x['inclusion_decision_human_verified'][0]
    L.append(f"| {x['study_id']}{' ' + flags if flags else ''} | {x['author_year']} | {x['family']} | {x['exposure_short']} vs {x['comparator_short']} | {x['outcome_short']} | {x['estimate_short']} | {x['raw_coefficient_sign']} | {x['substantive_direction']} | {x['rob_tool']}: {x['rob_rating']} | {inc} | {ckc} |")
open(OUT + '.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
import collections
print('wrote', OUT + '.csv/.md; raw', collections.Counter(x['raw_coefficient_sign'] for x in rows), 'substantive', collections.Counter(x['substantive_direction'] for x in rows), 'human-verified:', collections.Counter(x['inclusion_decision_human_verified'] for x in rows))
