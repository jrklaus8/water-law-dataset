"""2026-10-14: the two-column direction coding of the family-assigned effect rows (44 when first built: Family A 18, B 6, C 20; 39 after the A26 rulings; 37 after the A29 ruling: A 16, B 5, C 16; 31 after the A28 rulings: A 13, B 3, C 15), under reviewer CK's instruction to stop conflating the raw sign of a coefficient with its
substantive direction for households (Campbell et al. 2020, SWiM item on the direction of effect; the earlier sign tables mixed the two, e.g. S358 and S404 were 'Positive' although both coefficients are negative).

Four coded fields per study, all by the AI from effect_sizes.csv (not human-verified; the ck_* columns of SWIM_CORE_VERIFICATION_TABLE_2026-10-14 are the worksheet for that):
  raw_coefficient_sign   '+' / '-' / 'null' / 'mixed': the sign of the reported estimate for the contrast the estimate reports (ratio above 1 is '+', below 1 is '-'; 'null' = reported as not significant;
                         'mixed' = components with different signs or a null and a non-null component);
  outcome_polarity       'higher = better' / 'higher = worse' for household access, affordability, equity or service (interruptions, water poverty, collection time, tariff, bill, groundwater decline: higher = worse);
  exposure_orientation   'as reported' (the exposure pole of the reported contrast), or 'restated to the recognised pole' where the paper's exposure is a binary non-recognised legal status (non-notified, unincorporated,
                         non-zoned) so that the recognised/formal pole is the exposure, as the Family A hypothesis ('recognition improves access') is stated;
  substantive_direction  DERIVED, never typed: Favourable / Unfavourable / Null / Mixed = sign(raw) x polarity x orientation, with null and mixed passed through.
Favourable therefore means: the exposure (oriented as above) is associated with better household access, affordability, equity or service on the paper's own outcome measure. It is not a judgment that the exposure is desirable.

Also recorded: whether the outcome is a household access measure (the check of 2026-10-14 found none in S358, S1121, S1140, S590 and S1136; the author's A26 rulings moved S358 and S590 to the reasoned non-fits and excluded S1121, S606 and S1143 left the families too, and the A29 ruling then moved S1140 and S1136 to the reasoned non-fits), an alternative substantive direction where the primary and fully
adjusted estimates differ (S471), and a short note. Writes 05_analysis/effect_sizes/SWIM_DIRECTION_CODING_2026-10-14.csv. READ-ONLY on every database. Run from legal-last-mile-systematic-review/."""
import csv, sys
sys.path.insert(0, 'code/analysis')
csv.field_size_limit(sys.maxsize)
import current_figures as cf

OUT = '05_analysis/effect_sizes/SWIM_DIRECTION_CODING_2026-10-14.csv'
HB, HW = 'higher = better', 'higher = worse'
AR, RS = 'as reported', 'restated to the recognised pole'
CHK = 'checked 2026-10-14: no household access measure; kept by the author (A26)'
NOT = 'not separately checked'

# study: (raw sign, outcome polarity, exposure orientation, outcome-directness check, alternative substantive direction, note)
D = {
 # Family A
 'S037': ('null', HW, AR, NOT, '', 'Irrigation-district places 83% vs 79% poor-drinking-water exposure, p=0.136: not significant.'),
 'S057': ('+', HB, AR, NOT, '', 'Offer of the targeted subsidy raised latrine purchase by 32 pp.'),
 'S084': ('-', HB, RS, NOT, '', 'Reported contrast is non-notified vs notified (-37.3% water per capita). Restated to notified vs non-notified the association is positive: Favourable for recognition.'),
 'S104': ('+', HW, AR, NOT, '', 'Home ownership: OR 1.31 for piped-water interruption (higher = worse). Raw sign +, substantive Unfavourable: the tenure-security hypothesis predicts fewer interruptions.'),
 'S142': ('-', HB, RS, NOT, '', 'Reported contrast is unincorporated vs incorporated (significantly reduced access). Restated to incorporated vs unincorporated the association is positive: Favourable for recognition.'),
 'S398': ('+', HB, AR, NOT, '', 'ZEIS zoning raised sewage-network access by 23 pp (DiD).'),
 'S404': ('-', HW, AR, NOT, '', 'WRUA membership: ATT -14% to -32% on a water-poverty index (higher = worse). Raw sign -, substantive Favourable.'),
 'S765': ('+', HB, AR, NOT, '', 'Legal title raised improved-water-source use by 5.9 pp (DiD).'),
 'S780': ('null', HB, AR, NOT, '', 'Autonomous-county status: -41,811 beneficiaries (SE 25,960), not significant.'),
 'S882': ('+', HB, AR, NOT, '', 'Own metered connection: +27.2% consumption, +0.35 SD cleanliness, ORs 2.16 (ease) and 2.76 (affordable expenses).'),
 'S920': ('+', HB, AR, NOT, '', 'Water-user-association management: piped-water access about 6 pp above trend (DiD with kernel matching).'),
 'S930': ('+', HB, AR, NOT, '', 'Usos y costumbres: ATT 0.086 on sewerage access (PSM-DiD).'),
 'S1122': ('-', HB, RS, NOT, '', 'Non-zoned periphery residents: HR 0.14 for first piped-water access (higher hazard = faster access). Restated to zoned vs non-zoned the association is positive: Favourable for recognition.'),
 # Family B
 'S085': ('+', HB, AR, NOT, '', 'Bureaucratic assistance with political coordination: +19 pp full formalisation.'),
 'S366': ('+', HB, AR, NOT, '', 'Improved primary drinking-water source: 83% against 43%, adjusted ITT difference +33 pp (95% CI 22 to 45), cluster RCT of the VEA programme. Replaced S294\'s row under the author\'s A28 ruling (the full text on file is the S366 report).'),
 'S1102': ('+', HB, AR, NOT, '', 'Capital-cost contribution: water-improvements index difference 1.04 (t = 4.26).'),
 # Family C
 'S174': ('+', HB, AR, NOT, '', 'Headline financial-capacity factor +6.02 on water coverage; the plan/policy (legal-compliance) factor is negative for water (-1.89, p = 0.033).'),
 'S470': ('+', HB, AR, NOT, '', 'Arsae-MG enforcement norm: +19.2 pp social-tariff implementation.'),
 'S471': ('-', HW, AR, NOT, 'Null', 'Primary estimate -1.58 (state fixed effects, organisation-only model, p < 0.05; a lower bill is better): raw sign -, Favourable. The fully adjusted estimate (-1.03) is not significant, so its adjusted direction is Null (sensitivity scenario S4c); the primary estimate is kept in the main count by the author (A26).'),
 'S526': ('-', HB, AR, NOT, '', 'Investor-owned utilities: -0.167 on the unit-price ratio (higher = more progressive pricing). Raw sign -, substantive Unfavourable (more regressive).'),
 'S539': ('+', HW, AR, NOT, '', 'Investor-owned utilities: +$144 a year in the household bill and +1.55 pp in the lowest-quintile income share (higher = worse). Raw sign +, substantive Unfavourable.'),
 'S593': ('mixed', HB, AR, NOT, '', 'Urban (si) status and tax burden go with lower inequity coefficients; fiscal independence goes with a higher one.'),
 'S631': ('-', HB, AR, NOT, '', 'New-district creation: about -1% protected water and sanitation access (DiD), -1.35 pp in the dynamic model.'),
 'S749': ('+', HW, AR, NOT, '', 'Private ownership: +0.3456 R$/m3 on the tariff level (higher = worse). Raw sign +, substantive Unfavourable.'),
 'S879': ('mixed', HB, AR, NOT, '', 'Credible disconnection notices: +30 pp payment compliance (a utility-side outcome), null on water access, connections, spending and collection time. Kept as Mixed by the author (A26); a sensitivity scenario (S4e) treats household water access alone as Null.'),
 'S1032': ('-', HW, AR, NOT, '', 'Contact with the municipality or an NGO: OR 0.60 and 0.56 for the odds of a water complaint (a complaint is a worse outcome). Raw sign -, substantive Favourable.'),
 'S1038': ('-', HW, AR, NOT, '', 'The reported contrast is state-regulated minus locally regulated welfare loss (-4.6 pp; higher = worse), so the exposure is state PUC regulation. effect_sizes.csv carried the opposite pole in its exposure_definition until the author\'s A26 ruling of 2026-10-14, which swapped exposure and comparator to match.'),
 'S1062': ('mixed', HB, AR, NOT, '', 'Inverted U: positive coefficient on cost recovery, negative on its square.'),
 'S1146': ('-', HB, AR, NOT, '', 'Regional utilities corruption: negative marginal effect on reporting enough clean water.'),
 'S1162': ('-', HB, AR, NOT, '', 'Municipality or town panchayat vs municipal corporation: -4.06 pp growth in household water coverage.'),
 'S1169': ('-', HB, AR, NOT, '', 'Price-regulated provider: coefficient -1.19, about 27 pp lower probability that a colonia had water service.'),
}
RECOMMEND = {}   # S1140 and S1136 carried a recommendation until the A29 ruling (2026-10-14) moved both to the reasoned non-fits
INDIRECT = tuple(sorted(RECOMMEND, key=lambda s: int(s[1:])))


def derive(raw, pol, ori):
    if raw == 'null':
        return 'Null'
    if raw == 'mixed':
        return 'Mixed'
    sign = (1 if raw == '+' else -1) * (1 if pol == HB else -1) * (1 if ori == AR else -1)
    return 'Favourable' if sign > 0 else 'Unfavourable'


def fam_rows():
    es = {r['study_id']: r for r in cf.read('es')}
    return [(f, s) for f in 'ABC' for s in sorted((x for x in es if es[x]['synthesis_family'] == f), key=lambda x: int(x[1:]))]


def build():
    fr = fam_rows()
    assert len(fr) == 31 and {s for _, s in fr} == set(D), sorted({s for _, s in fr} ^ set(D))
    out = []
    for f, s in fr:
        raw, pol, ori, chk, alt, note = D[s]
        assert raw in ('+', '-', 'null', 'mixed') and pol in (HB, HW) and ori in (AR, RS) and chk in (CHK, NOT)
        assert (chk == CHK) == (s in INDIRECT), s
        out.append({'study_id': s, 'family': f, 'raw_coefficient_sign': raw, 'outcome_polarity': pol, 'exposure_orientation': ori,
                    'substantive_direction': derive(raw, pol, ori), 'alternative_substantive_direction': alt, 'outcome_directness_check': chk,
                    'ai_recommendation_for_author': RECOMMEND.get(s, ''), 'coding_note': note})
    return out


if __name__ == '__main__':
    rows = build()
    with open(OUT, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), lineterminator='\r\n'); w.writeheader(); w.writerows(rows)
    from collections import Counter
    for f in 'ABC':
        sub = [r for r in rows if r['family'] == f]
        print(f, len(sub), 'raw:', dict(Counter(r['raw_coefficient_sign'] for r in sub)), 'substantive:', dict(Counter(r['substantive_direction'] for r in sub)))
    print('wrote', OUT)
