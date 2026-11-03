#!/usr/bin/env python3
import csv, tempfile, os

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
EFF = f"{BASE}/05_analysis/effect_sizes/effect_sizes.csv"

with open(EFF, newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)
    existing_ids = {row["study_id"] for row in rows}

assert "S882" not in existing_ids

rows.append({
    "study_id": "S882",
    "outcome_family": "water_access",
    "synthesis_family": "A",
    "exposure_definition": "Household formal connection status to the municipal water utility (Baguio Water District, BWD): own household metered connection, requiring an upfront PHP 10,000-14,000 (US$234-327) connection fee plus installation cost.",
    "comparator_definition": "Households with no BWD connection (referent category); a shared/other BWD connection category also modeled.",
    "effect_measure": "Multiple regression (linear log-transformed and logistic models), randomly sampled household survey, N=396",
    "effect_estimate": "Own household BWD connection vs. none: +27.2% increase in reported liters-per-capita-per-day consumption; +0.35 SD in perceived-cleanliness PCA score; 2.16x odds of reporting extreme ease of water access; 2.76x odds of reporting affordable water expenses (all coefficients statistically significant at conventional thresholds per reported asterisks). Shared/other BWD connection vs. none: -20.8% decrease in consumption but 2.71x odds of affordability.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "sample_size": "396 households, Pinget, Baguio City, Philippines",
    "direction": "positive and significant across all four water-security outcomes for own household connection",
    "adjusted": "adjusted (household size as control variable; financial, physical, and social resource covariates)",
    "evidence_status": "OBSERVED",
    "provenance_note": "extraction_database.csv S882; source Mason 2014, Journal of the Society for Social Work and Research, multiple regression results described in text (consumption, cleanliness, ease, affordability models). Household survey regression directly isolating a documented institutional/fee-based formal-connection mechanism (Family A: legal recognition/formal connection) with four directly measured water-access outcomes, all showing statistically significant positive effects for having one's own utility connection.",
    "included_in_pooled_estimate": "FALSE",
    "exclusion_from_pooling_reason": "ANALYSIS_PLAN.md S2 decision tree -- while this is a genuine Family A (formal connection/legal recognition) exposure-outcome pairing, its specific operationalization (household survey regression of BWD metered-connection status on water consumption/cleanliness/ease/affordability in a single Philippine community) does not share an exposure-comparator-outcome combination with other Family A studies already in this table closely enough for meaningful pooling at this stage (too few independent studies with this exact operationalization, per PROJECT_SPEC.md S8 guidance).",
})

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EFF))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EFF)

print(f"New total: {len(rows)}")
