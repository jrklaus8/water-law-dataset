#!/usr/bin/env python3
import csv, tempfile, os

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
ES = f"{BASE}/05_analysis/effect_sizes/effect_sizes.csv"

with open(ES, newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)
    existing_ids = {row["study_id"] for row in rows}

assert "S969" not in existing_ids, "S969 already exists"

row = {fn: "" for fn in fieldnames}
row.update({
    "study_id": "S969",
    "outcome_family": "water_access",
    "synthesis_family": "A",
    "exposure_definition": "Longer duration of the colonial era (years under effective European colonial control, YRSCOL) in a given African country, 2008 cross-section, 43 countries.",
    "comparator_definition": "Countries/cities with a shorter duration of colonial-era governance, within the same 43-country cross-national sample.",
    "effect_measure": "Ordinary Least Squares (OLS) multiple regression coefficient",
    "effect_estimate": "Colonial duration (YRSCOL) has a positive, statistically significant effect on the composite urban water-and-sanitation access index (b=0.322, t=4.500, p<0.000); colonizer identity (British=1) is positively but not significantly associated (b=2.420, t=0.649). Model: ACCESS = 41.956 + 0.322*YRSCOL + 2.420*COLONIZER. A supporting bivariate chi-square test finds 87.5% of long-colonial-duration countries have 'high' urban water access versus 48.1% of short-duration countries (Chi-square=6.659, p=0.010, Phi=0.394); a parallel significant relationship holds for sanitation access.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "0.071 (YRSCOL coefficient, Table 3)",
    "sample_size": "43 African countries (2008 cross-sectional data)",
    "direction": "positive (longer colonial-era governance duration associated with greater contemporary urban water/sanitation access)",
    "adjusted": "TRUE",
    "evidence_status": "OBSERVED",
    "provenance_note": "extraction_database.csv S969; source Njoh & Akiwumi 2011, Cities, Table 3. Family A (legal recognition/institutional-management-model and access): a cross-national OLS regression directly isolating the effect of a historical-institutional/legal-administrative variable (colonial governance duration, as a proxy for accumulated institutional and infrastructural investment) on a quantified water/sanitation access index, Adj. R2=0.34, F=11.545 p<0.000.",
    "included_in_pooled_estimate": "FALSE",
    "exclusion_from_pooling_reason": "ANALYSIS_PLAN.md S2 decision tree -- single study defining this exact exposure-comparator (colonial-era governance duration vs. urban water/sanitation access index across a 43-country African cross-section); no other Family A study yet shares this operationalization, so pooling is not yet possible or meaningful (too few independent studies in this family with this exposure).",
})
rows.append(row)

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(ES))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for r_ in rows:
        w.writerow(r_)
os.replace(tmp, ES)

print(f"New total: {len(rows)}")
