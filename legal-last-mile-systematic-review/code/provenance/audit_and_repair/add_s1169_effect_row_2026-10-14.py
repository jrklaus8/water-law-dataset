"""2026-10-14: effect_sizes.csv row for S1169 (Olmstead 2004, Land Economics 80(1):136-150, Thirsty colonias), which the PI's A15 ruling of 2026-10-14 added as an include (record RBEDB6556B711).
The row records the paper's main access-relevant estimate: Model B, price regulation of the water provider, probit coefficient -1.1858 (SE 0.4163, p = 0.004; marginal effect -0.2718) on the probability that a colonia
had obtained water service by 1996, N = 781 colonias in four Texas border counties, adjusted. The exposure is an administrative/legal barrier (price regulation of the provider's rates, no universal-service mandate), so it goes in
Family C (06_outputs/supplementary/family_C_swim_synthesis_2026-09-28.md, k 19 to 20). Not pooled: a single study with this exposure-comparator and a coverage, not a price, outcome. A FULLTEXT_VERIFICATION row records the numbers checked
against the pages read. Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
EP = '05_analysis/effect_sizes/effect_sizes.csv'
VP = '05_analysis/effect_sizes/FULLTEXT_VERIFICATION_2026-10-04.csv'
SID = 'S1169'


def read(p):
    raw = open(p, newline='', encoding='utf-8').read()
    crlf = '\r\n' in raw[:5000]
    with open(p, newline='', encoding='utf-8') as f:
        rd = csv.DictReader(f)
        return rd.fieldnames, list(rd), crlf


def write(p, fields, rows, crlf):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(p), suffix='.tmp')
    with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n' if crlf else '\n')
        w.writeheader()
        w.writerows(rows)
    os.replace(tmp, p)


fields, rows, crlf = read(EP)
if any(r['study_id'] == SID for r in rows):
    print('effect row already present')
else:
    new = {k: '' for k in fields}
    new.update(
        study_id=SID, outcome_family='service_coverage', synthesis_family='C',
        exposure_definition=("The colonia's water provider is subject to price (rate) regulation (municipal systems under their own rate-setting, county systems and districts under the state environmental commission), as opposed to providers whose rates are not regulated "
                             "(non-profit water supply corporations and for-profit suppliers); Texas law does not mandate universal service."),
        comparator_definition='Colonias served, or most likely to be served, by an unregulated provider (mainly non-profit water supply corporations); other provider characteristics held constant (rural-development funding access, income, population, urban status, county enforcement of the model subdivision rules).',
        effect_measure='probit regression coefficient and marginal effect on the probability of having obtained water service (Model B)',
        effect_estimate=("Price-regulated provider: coefficient -1.1858 (SE 0.4163, p = 0.004), marginal effect -0.2718, about 27 percentage points lower probability that a colonia had water service by 1996. Access to Rural Development funding 0.2162 (p = 0.401); "
                         "county cited for lax enforcement of the model subdivision rules -7.5722 (p = 0.004), marginal effect -0.6943; median per capita income +0.1410 (p = 0.001). Model A (provider type against private for-profit): municipal -1.9433 (p = 0.051), district or county -1.1105 (p = 0.035), "
                         "non-profit corporation -0.3795 (p = 0.535), wells or unknown -2.3819 (p = 0.007). The author reads this as rate regulation, intended to make service affordable, possibly reducing coverage among the poor."),
        standard_error='0.4163', sample_size='781 colonias in four Texas border counties (Cameron, El Paso, Hidalgo, Webb); 267,384 residents in 1996',
        direction='negative (a price-regulated provider is associated with a lower probability that the colonia had obtained water service)',
        adjusted='TRUE (income, population, urban status, rural-development funding, colonia share of county population, county enforcement of the model subdivision rules)', evidence_status='OBSERVED',
        provenance_note=("extraction_database.csv S1169; source Olmstead 2004, Land Economics 80(1):136-150, Model B (price regulation) with Table 3 summary statistics. New include by the PI's A15 ruling of 2026-10-14 (a recorded exception to the 2026-09-28 closure). "
                         "The marginal effect is the paper's own (computed at the variable means); no confidence interval is reported, only standard errors, and the standard errors are clustered by infrastructure-project group, which the author notes may still be downward-biased. The outcome is whether service had been obtained, an upper bound on safe access. "
                         "Model B (pricing flexibility) was recorded rather than Model A (provider type) because it isolates the legal mechanism, in line with CODEBOOK section 12's one-prespecified-effect-per-study default."),
        included_in_pooled_estimate='FALSE',
        exclusion_from_pooling_reason=("ANALYSIS_PLAN.md section 2 decision tree: a single study with this exposure-comparator (price regulation of the provider versus unregulated providers) and a coverage outcome; it is a regulatory-structure exposure on the same theme as S1038 (state regulation) "
                                       "but with a service-coverage, not a price, outcome, so no comparable estimand exists and pooling is not possible or meaningful (PROJECT_SPEC.md section 8)."))
    rows.append(new)
    write(EP, fields, rows, crlf)
    print('effect row added for', SID, '(', len(rows), 'rows )')

vf, vrows, vcrlf = read(VP)
if any(r['study_id'] == SID for r in vrows):
    print('verification row already present')
else:
    v = {k: '' for k in vf}
    v.update(study_id=SID, synthesis_family='C', numbers_in_row='7', numbers_found_in_text='7', numbers_not_found='', source_text='Drive inbox full text (2026-10-14; page images read)', verdict='verified',
             note="Model B in the full text: price regulation -1.1858 (SE 0.4163, p = 0.004), marginal effect -0.2718; N = 781 colonias; income 0.1410 (p = 0.001); county enforcement -7.5722 (p = 0.004); Table 3 means (water service 0.86, price-regulated supplier 0.20, urban 0.34)")
    vrows.append(v)
    write(VP, vf, vrows, vcrlf)
    print('verification row added')
