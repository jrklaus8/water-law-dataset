"""2026-10-04: S348 (Andrews, Beynon & Baafi 2025, Local Government Studies 51(1):178-201) effect-size row. The row said exact coefficients, CIs and p-values were 'not recoverable' and that the source reports its models
narratively. The author's accepted manuscript (researcher's Drive) has a coefficient table (Table 2, hierarchical regression, N = 261 districts, three outcomes x five models, each model a different reference cluster). The row's
qualitative claims were checked against it and hold; the exact coefficients are now recorded. No confidence intervals or standard errors are reported (stars only: ^ p<.10, * p<.05, ** p<.01). Idempotent. Run from
legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
P = '05_analysis/effect_sizes/effect_sizes.csv'
raw = open(P, newline='').read(); crlf = '\r\n' in raw[:5000]
with open(P, newline='') as f:
    rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
n0 = len(rows); done = False
for r in rows:
    if r['study_id'] != 'S348':
        continue
    if 'Full-text check 2026-10-04' in r['provenance_note']:
        print('already applied'); continue
    assert 'not recoverable' in r['effect_estimate']
    r['effect_estimate'] = (
        "Table 2 (OLS hierarchical regression on fuzzy-cluster membership scores; each model uses a different cluster as the reference; N = 261 districts; no SE/CI reported, stars only). "
        "badly_managed districts versus big_wealthy_urban: sanitation -0.663**, safe drinking water -0.846**, electricity -1.054**. badly_managed versus rural_poor: sanitation +0.097, water +0.038 (both n.s.), electricity +0.401 (p<.10). "
        "badly_managed versus middling: sanitation +0.107 (n.s.), water -0.646**, electricity -0.707**; versus small: sanitation -0.130 (n.s.), water -0.645**, electricity -0.359 (n.s.). "
        "rural_poor versus big_wealthy_urban: sanitation -0.760**, water -0.884**, electricity -1.455**. big_wealthy_urban is significantly better than every other cluster for sanitation and electricity, but for water only against rural_poor and badly_managed "
        "(vs middling +0.200 and vs small +0.201, n.s.). Adjusted R2 0.145 (sanitation), 0.129 (water), 0.249 (electricity).")
    r['sample_size'] = '261 Ghanaian local government districts, 2021 secondary data'
    r['provenance_note'] += (" Full-text check 2026-10-04: coefficients taken from Table 2 of the author's accepted manuscript (enrich_s348_coefficients_2026-10-04.py); the original row's qualitative claims "
                             "('badly_managed' almost as weak as 'rural_poor', especially for drinking water; big_wealthy_urban significantly better for sanitation and electricity and for water in some comparisons) were confirmed. "
                             "Whether the published version differs from the accepted manuscript was not checked.")
    r['exclusion_from_pooling_reason'] = r['exclusion_from_pooling_reason'].replace(
        "No CI/p-value available to report even if a comparable study did exist, since the source itself reports these models narratively rather than in a coefficient table recoverable from this project's extraction.",
        "The source reports coefficients with significance stars only (no SE or CI), and the contrast depends on which cluster is the reference category.")
    assert 'significance stars' in r['exclusion_from_pooling_reason']
    done = True
assert len(rows) == n0
if done:
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(P), suffix='.tmp')
    with os.fdopen(fd, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n' if crlf else '\n'); w.writeheader(); w.writerows(rows)
    os.replace(tmp, P)
    print('S348 coefficients recorded')
