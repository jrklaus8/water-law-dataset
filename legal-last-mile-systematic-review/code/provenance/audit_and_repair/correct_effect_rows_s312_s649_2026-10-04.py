"""2026-10-04: two effect-size rows corrected after the researcher's full texts were read (Drive).
S312 (Warner, Zhang & Gonzalez Rivas 2020, Utilities Policy 67:101118): the row was written from the abstract and mislabelled the models. In the paper the logit AND the Cox proportional-hazards models are STATE-level
(N = 50; Table 2); the CITY-level model (N = 2,818 cities, 14 states without a statewide moratorium) is a multilevel logit with a county effect (Table 3). State PUC regulation is a state-level variable only. The row's
claim that PUC authority predicts adoption 'at both state and city level' and its 'Democratic-leaning' label were not in the paper (it measures unified Republican control and the 2016 Trump vote share). Exact odds/hazard
ratios are now recorded; the row stays outside every synthesis (outcome is policy adoption, not household access) and is not pooled.
S649 (Gonzalez Rivas 2012): the estimate text attributed the -0.003 coefficient to 'federal transfers per capita'; in Table 4 it is the INDIGENOUS-share coefficient in the transfers model (outcome: per-capita transfers).
Transfers per capita enter only the combined coverage model (0.5713, Table 5). Estimate text and exposure wording corrected; numbers unchanged. Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
P = '05_analysis/effect_sizes/effect_sizes.csv'
raw = open(P, newline='').read(); crlf = '\r\n' in raw[:5000]
with open(P, newline='') as f:
    rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
n0 = len(rows); changed = []
for r in rows:
    if r['study_id'] == 'S312' and 'Full-text correction 2026-10-04' not in r['provenance_note']:
        assert r['effect_measure'].startswith('logit regression (state-level); Cox')
        r['effect_measure'] = ('Logit regression (odds ratios; state-level moratorium) and Cox proportional-hazards regression (hazard ratios; state-level time to moratorium); multilevel logit regression with a county effect '
                               '(odds ratios; city-level moratorium)')
        r['effect_estimate'] = ('State level (N = 50): state PUC economic regulation of private utilities OR 134.3 (SE 318.6), p = 0.039 -- extremely imprecise; Cox HR 9.55 (SE 10.16), p = 0.034. Unified Republican control OR 0.012 (SE 0.019), p = 0.007; '
                                'Cox HR 0.205 (SE 0.090), p = 0.000 as printed. City level (2,818 cities in 14 states without a statewide moratorium; 135 with one): county share voting Trump 2016 OR 0.966 (SE 0.011), p = 0.003; '
                                'percent minority OR 1.021 (SE 0.008), p = 0.005; Gini index OR 1.084 (SE 0.023), p < 0.001; PUC regulation is not a city-level variable.')
        r['direction'] = ('positive for state PUC economic regulation (state level only); negative for unified Republican control (state) and Trump vote share (city); outcome is adoption of a disconnection moratorium, a policy outcome')
        r['sample_size'] = '50 states; 2,818 cities (2,684 without a moratorium, 135 with one, in 14 states without a statewide moratorium)'
        r['provenance_note'] = r['provenance_note'].replace('No exact numeric coefficient/OR/CI located in the extracted abstract text.',
                               'Exact odds and hazard ratios are now taken from Tables 2-3 of the full text.') + (
            ' Full-text correction 2026-10-04: the original row (from the abstract) said the Cox model was city-level and that PUC authority and a Democratic-leaning orientation predicted adoption at both levels; in the paper both the logit and Cox models are state-level, '
            'the city model is a multilevel logit, PUC regulation is state-level only, and partisanship is measured as unified Republican control (state) and Trump vote share (city). No confidence intervals are reported (SEs only).')
        r['exclusion_from_pooling_reason'] = r['exclusion_from_pooling_reason'].replace(
            'no numeric effect size available in extracted text to pool even in principle, per PROJECT_SPEC.md S14 never-fabricate rule.',
            'exact odds ratios are available but the PUC odds ratio is extremely imprecise and the outcome is policy adoption, so nothing is pooled.')
        changed.append('S312')
    if r['study_id'] == 'S649' and 'Full-text correction 2026-10-04' not in r['provenance_note']:
        old = 'federal transfers per capita: -0.003 (transfers-received OLS model, p=0.005) and 0.5713 (piped-water-coverage GLM model including transfers, p=0.019)'
        assert old in r['effect_estimate']
        r['effect_estimate'] = r['effect_estimate'].replace(old,
            'indigenous population share on per-capita federal transfers received: -0.003 (transfers OLS model, Table 4, p=0.005); federal transfers per capita on piped-water coverage: 0.5713 (GLM model including transfers, Table 5, p=0.019; indigenous share -0.0305, p=0.017, in that model)')
        r['provenance_note'] += (' Full-text correction 2026-10-04: the -0.003 coefficient is the indigenous-share effect in the transfers model (Table 4), not an effect of transfers; wording corrected, numbers unchanged.')
        changed.append('S649')
for r in rows:
    if r['study_id'] == 'S312' and r['adjusted'] == '':
        r['adjusted'] = ('adjusted (state models: private-ownership level, unemployment, poverty, urbanisation, minority share, COVID-19 case rate, unified Republican control; city multilevel logit: income, unemployment, '
                         'minority share, Gini, health insurance, county COVID-19 rate, Trump vote share, community health, county effect)')
        changed.append('S312 adjusted')
assert len(rows) == n0
if changed:
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(P), suffix='.tmp')
    with os.fdopen(fd, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n' if crlf else '\n'); w.writeheader(); w.writerows(rows)
    os.replace(tmp, P)
print('corrected:', changed or 'already applied')
