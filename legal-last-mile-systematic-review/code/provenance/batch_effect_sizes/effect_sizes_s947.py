#!/usr/bin/env python3
import csv, tempfile, os

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
ES = f"{BASE}/05_analysis/effect_sizes/effect_sizes.csv"

with open(ES, newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)
    existing_ids = {row["study_id"] for row in rows}

assert "S947" not in existing_ids

rows.append({
    "study_id": "S947",
    "outcome_family": "water_access",
    "synthesis_family": "C",
    "exposure_definition": "Higher institutional/regulatory governance quality (World Bank Worldwide Governance Indicators 'regulation quality' index) at the national level, in the presence of natural-resource-rent dependence, across 44 African countries, 1995-2017.",
    "comparator_definition": "Countries/country-years with lower regulation-quality index scores, within the same 44-country dynamic panel.",
    "effect_measure": "two-step System Generalized Method of Moments (GMM) dynamic panel regression coefficient",
    "effect_estimate": "Regulation quality has a positive, statistically significant direct effect on access to drinking water for the total population (coefficient = 0.0121, p<0.01) and significantly reduces the urban-rural water-access gap (coefficient = -0.0511, p<0.01); broadly consistent significant effects are found for sanitation access. Separately, democratic institutional quality is shown to mitigate the negative resource-curse effect of natural-resource-rent dependence on water/sanitation access.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "0.00346 (regulation quality, water access total, Table 2 col. 2); 0.0147 (urban-rural gap, Table 2 col. 5)",
    "sample_size": "570-741 country-year observations, 43 African countries",
    "direction": "positive (higher institutional/regulatory quality associated with greater water/sanitation access and smaller urban-rural gap)",
    "adjusted": "TRUE",
    "evidence_status": "OBSERVED",
    "provenance_note": "extraction_database.csv S947; source Tadadjeu, Njangang, Ningaye & Nourou 2020, Resources Policy, Table 2. Family C (institutional/legal barriers and access inequality): a rigorous dynamic-panel GMM regression directly isolating the effect of institutional/regulatory governance quality on water/sanitation access and the urban-rural access gap, controlling for GDP, trade openness, FDI, and urbanization.",
    "included_in_pooled_estimate": "FALSE",
    "exclusion_from_pooling_reason": "ANALYSIS_PLAN.md S2 decision tree -- single study defining this exact exposure-comparator (national regulation-quality index vs. water/sanitation access across a 44-country African panel); no other Family C study yet shares this operationalization, so pooling is not yet possible or meaningful (too few independent studies in this family, per PROJECT_SPEC.md S8 Family C guidance).",
})

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(ES))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, ES)

print(f"New total: {len(rows)}")
