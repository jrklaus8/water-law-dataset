"""2026-10-14: the two-column direction coding of the 44 family-assigned effect rows (Family A 18, B 6, C 20), under reviewer CK's instruction to stop conflating the raw sign of a coefficient with its
substantive direction for households (Campbell et al. 2020, SWiM item on the direction of effect; the earlier sign tables mixed the two, e.g. S358 and S404 were 'Positive' although both coefficients are negative).

Four coded fields per study, all by the AI from effect_sizes.csv (not human-verified; the ck_* columns of SWIM_CORE_VERIFICATION_TABLE_2026-10-14 are the worksheet for that):
  raw_coefficient_sign   '+' / '-' / 'null' / 'mixed': the sign of the reported estimate for the contrast the estimate reports (ratio above 1 is '+', below 1 is '-'; 'null' = reported as not significant;
                         'mixed' = components with different signs or a null and a non-null component);
  outcome_polarity       'higher = better' / 'higher = worse' for household access, affordability, equity or service (interruptions, water poverty, collection time, tariff, bill, groundwater decline: higher = worse);
  exposure_orientation   'as reported' (the exposure pole of the reported contrast), or 'restated to the recognised pole' where the paper's exposure is a binary non-recognised legal status (non-notified, unincorporated,
                         non-zoned) so that the recognised/formal pole is the exposure, as the Family A hypothesis ('recognition improves access') is stated;
  substantive_direction  DERIVED, never typed: Favourable / Unfavourable / Null / Mixed = sign(raw) x polarity x orientation, with null and mixed passed through.
Favourable therefore means: the exposure (oriented as above) is associated with better household access, affordability, equity or service on the paper's own outcome measure. It is not a judgment that the exposure is desirable.

Also recorded: whether the outcome is a household access measure (the five-study check requested 2026-10-14: S358, S1121, S1140, S590, S1136 report none), an alternative substantive direction where the primary and fully
adjusted estimates differ (S471), and a short note. Writes 05_analysis/effect_sizes/SWIM_DIRECTION_CODING_2026-10-14.csv. READ-ONLY on every database. Run from legal-last-mile-systematic-review/."""
import csv, sys
sys.path.insert(0, 'code/analysis')
csv.field_size_limit(sys.maxsize)
import current_figures as cf

OUT = '05_analysis/effect_sizes/SWIM_DIRECTION_CODING_2026-10-14.csv'
HB, HW = 'higher = better', 'higher = worse'
AR, RS = 'as reported', 'restated to the recognised pole'
CHK = 'checked 2026-10-14: no household access measure'
NOT = 'not separately checked'

# study: (raw sign, outcome polarity, exposure orientation, outcome-directness check, alternative substantive direction, note)
D = {
 # Family A
 'S037': ('null', HW, AR, NOT, '', 'Irrigation-district places 83% vs 79% poor-drinking-water exposure, p=0.136: not significant.'),
 'S057': ('+', HB, AR, NOT, '', 'Offer of the targeted subsidy raised latrine purchase by 32 pp.'),
 'S084': ('-', HB, RS, NOT, '', 'Reported contrast is non-notified vs notified (-37.3% water per capita). Restated to notified vs non-notified the association is positive: Favourable for recognition.'),
 'S104': ('+', HW, AR, NOT, '', 'Home ownership: OR 1.31 for piped-water interruption (higher = worse). Raw sign +, substantive Unfavourable: the tenure-security hypothesis predicts fewer interruptions.'),
 'S142': ('-', HB, RS, NOT, '', 'Reported contrast is unincorporated vs incorporated (significantly reduced access). Restated to incorporated vs unincorporated the association is positive: Favourable for recognition.'),
 'S358': ('-', HW, AR, CHK, '', 'Tribal oversight: OR 0.62 for groundwater decline (higher = worse). Raw sign -, substantive Favourable. Outcome is groundwater decline and contamination of service areas, not a household access measure; the effect_sizes provenance note already calls it a looser fit.'),
 'S398': ('+', HB, AR, NOT, '', 'ZEIS zoning raised sewage-network access by 23 pp (DiD).'),
 'S404': ('-', HW, AR, NOT, '', 'WRUA membership: ATT -14% to -32% on a water-poverty index (higher = worse). Raw sign -, substantive Favourable.'),
 'S765': ('+', HB, AR, NOT, '', 'Legal title raised improved-water-source use by 5.9 pp (DiD).'),
 'S780': ('null', HB, AR, NOT, '', 'Autonomous-county status: -41,811 beneficiaries (SE 25,960), not significant.'),
 'S882': ('+', HB, AR, NOT, '', 'Own metered connection: +27.2% consumption, +0.35 SD cleanliness, ORs 2.16 (ease) and 2.76 (affordable expenses).'),
 'S920': ('+', HB, AR, NOT, '', 'Water-user-association management: piped-water access about 6 pp above trend (DiD with kernel matching).'),
 'S930': ('+', HB, AR, NOT, '', 'Usos y costumbres: ATT 0.086 on sewerage access (PSM-DiD).'),
 'S1020': ('+', HW, AR, NOT, '', 'Watershed development: +17.4 min/day collection time (higher = worse). Raw sign +, substantive Unfavourable.'),
 'S1042': ('+', HB, AR, NOT, '', 'Town-hall participation +29 pp, established CBO about +25 pp, probability of a good water-supply situation.'),
 'S1057': ('+', HB, AR, NOT, '', 'Community design satisfaction raised log collection-time saving (coefficients 1.63 to 2.92); a larger saving is better.'),
 'S1121': ('-', HB, AR, CHK, '', 'Water-adequacy screening: coefficient -0.31 to -0.53 on new residential permitting (higher = more new housing and connections). Raw sign -, substantive Unfavourable for permitting. The outcome is housing growth, not household access; connection fees are a regressor, not an outcome.'),
 'S1122': ('-', HB, RS, NOT, '', 'Non-zoned periphery residents: HR 0.14 for first piped-water access (higher hazard = faster access). Restated to zoned vs non-zoned the association is positive: Favourable for recognition.'),
 # Family B
 'S085': ('+', HB, AR, NOT, '', 'Bureaucratic assistance with political coordination: +19 pp full formalisation.'),
 'S294': ('mixed', HB, AR, NOT, '', 'Null on diarrhoea (-0.01; CI -0.05 to 0.03) and child growth; positive on the community WASH-institutions index (+0.40; CI 0.16 to 0.65).'),
 'S1102': ('+', HB, AR, NOT, '', 'Capital-cost contribution: water-improvements index difference 1.04 (t = 4.26).'),
 'S1140': ('+', HB, AR, CHK, '', 'Number of partners: log-odds 0.55 for funding success. Outcome is success in securing programme funding (an application outcome), not household access; time saved per household enters only as a control.'),
 'S1144': ('+', HB, AR, NOT, '', 'Trust in NGOs: coefficient 7.01 on access to NGO-supplied sanitation.'),
 'S1163': ('+', HB, AR, NOT, '', 'External WASH support: OR 1.4 for basic on-premises school water.'),
 # Family C
 'S174': ('+', HB, AR, NOT, '', 'Headline financial-capacity factor +6.02 on water coverage; the plan/policy (legal-compliance) factor is negative for water (-1.89, p = 0.033).'),
 'S470': ('+', HB, AR, NOT, '', 'Arsae-MG enforcement norm: +19.2 pp social-tariff implementation.'),
 'S471': ('-', HW, AR, NOT, 'Null', 'Primary estimate -1.58 (state fixed effects, organisation-only model, p < 0.05; a lower bill is better): raw sign -, Favourable. The fully adjusted estimate (-1.03) is not significant, so its adjusted direction is Null (sensitivity scenario S7).'),
 'S526': ('-', HB, AR, NOT, '', 'Investor-owned utilities: -0.167 on the unit-price ratio (higher = more progressive pricing). Raw sign -, substantive Unfavourable (more regressive).'),
 'S539': ('+', HW, AR, NOT, '', 'Investor-owned utilities: +$144 a year in the household bill and +1.55 pp in the lowest-quintile income share (higher = worse). Raw sign +, substantive Unfavourable.'),
 'S590': ('+', HB, AR, CHK, '', 'Concentrated franchise: SKEW coefficient 0.457 on the probability that a Prussian city builds waterworks. Outcome is a city investment decision, not household access (sewer coverage appears only as background).'),
 'S593': ('mixed', HB, AR, NOT, '', 'Urban (si) status and tax burden go with lower inequity coefficients; fiscal independence goes with a higher one.'),
 'S606': ('-', HB, AR, NOT, '', 'One-point rise in the unregistered-resident share: -0.00164 wastewater treatment capacity per capita. The outcome is infrastructure capacity (not in the five-study check).'),
 'S631': ('-', HB, AR, NOT, '', 'New-district creation: about -1% protected water and sanitation access (DiD), -1.35 pp in the dynamic model.'),
 'S749': ('+', HW, AR, NOT, '', 'Private ownership: +0.3456 R$/m3 on the tariff level (higher = worse). Raw sign +, substantive Unfavourable.'),
 'S879': ('mixed', HB, AR, NOT, '', 'Credible disconnection notices: +30 pp payment compliance (a utility-side outcome), null on water access, connections, spending and collection time. A strict household-access reading would be Null.'),
 'S947': ('+', HB, AR, NOT, '', 'Regulation quality: coefficient 0.0121 on access to drinking water.'),
 'S1032': ('-', HW, AR, NOT, '', 'Contact with the municipality or an NGO: OR 0.60 and 0.56 for the odds of a water complaint (a complaint is a worse outcome). Raw sign -, substantive Favourable.'),
 'S1038': ('-', HW, AR, NOT, '', 'The reported contrast is state-regulated minus locally regulated welfare loss (-4.6 pp; higher = worse), so it is coded on state PUC regulation as the exposure. The exposure_definition in effect_sizes.csv names local-only regulation as the exposure; flagged for the author to confirm which pole the row should carry.'),
 'S1062': ('mixed', HB, AR, NOT, '', 'Inverted U: positive coefficient on cost recovery, negative on its square.'),
 'S1136': ('+', HB, AR, CHK, '', 'Political proximity (GP head village +0.053 paved, +0.037 drain; politician road +0.078 drain): a favouritism finding; SC/ST roads are less likely to be paved (-0.051). Outcome is road-level public sanitation infrastructure, not household access; the household survey is used only to rank problems.'),
 'S1143': ('mixed', HB, AR, NOT, '', 'Weight rule alone favours better-off tracts; the supplementary centre-city rule reverses it for inner tracts. The service is garbage collection (not in the five-study check).'),
 'S1146': ('-', HB, AR, NOT, '', 'Regional utilities corruption: negative marginal effect on reporting enough clean water.'),
 'S1162': ('-', HB, AR, NOT, '', 'Municipality or town panchayat vs municipal corporation: -4.06 pp growth in household water coverage.'),
 'S1169': ('-', HB, AR, NOT, '', 'Price-regulated provider: coefficient -1.19, about 27 pp lower probability that a colonia had water service.'),
}
RECOMMEND = {
 'S358': 'reasoned non-fit candidate (groundwater availability and contamination of service areas; no household access outcome)',
 'S1121': 'reasoned non-fit candidate (new-housing permits; the same outcome problem as S312, S397 and S435, excluded under E04)',
 'S590': 'reasoned non-fit candidate (a 19th-century city decision to build waterworks; no household access outcome)',
 'S1140': 'keep: funding success is an application outcome the protocol lists (application_success); add to a sensitivity row',
 'S1136': 'keep as a distributional finding (public sanitation infrastructure by caste and political connection); add to a sensitivity row',
}
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
    assert len(fr) == 44 and {s for _, s in fr} == set(D), sorted({s for _, s in fr} ^ set(D))
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
