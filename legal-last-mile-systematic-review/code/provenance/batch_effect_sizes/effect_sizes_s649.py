import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/effect_sizes/effect_sizes.csv"

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing_ids = {r["study_id"] for r in rows}
assert "S649" not in existing_ids

rows.append({
    "study_id": "S649",
    "outcome_family": "formal_connection",
    "synthesis_family": "",
    "exposure_definition": "Per-capita federal intergovernmental transfers (Aportaciones Federales, 2000-2005) received by a Mexican municipality, operating under the constitutionally assigned (Article 115) municipal responsibility for water-service provision -- with indigenous population share as the key predictor of lower transfer receipt.",
    "comparator_definition": "Cross-municipal variation across 2,342-2,372 Mexican municipalities, comparing municipalities by indigenous population share and by level of per-capita federal transfers received, controlling for population density, income, migration, and prior (2000) coverage.",
    "effect_measure": "Generalized linear model (logit-link) and OLS regression coefficients",
    "effect_estimate": "Indigenous population share: -0.0310 (piped-water-coverage GLM model, p=0.014); federal transfers per capita: -0.003 (transfers-received OLS model, p=0.005) and 0.5713 (piped-water-coverage GLM model including transfers, p=0.019)",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "0.0126 (indigenous coefficient, coverage model); 0.001 (indigenous coefficient, transfers model); 0.2437 (transfers coefficient, coverage model)",
    "sample_size": "2,372 municipalities (coverage model); 2,342 municipalities (transfers and combined models)",
    "direction": "negative (higher indigenous population share associated with LOWER per-capita federal transfers and, independently, lower piped-water coverage; transfers positively associated with piped-water coverage)",
    "adjusted": "adjusted (population density, per-capita income, migration share, prior 2000 piped-water coverage, spatial lag, state fixed effects; transfers model additionally adjusts for vote share for incumbent president)",
    "evidence_status": "OBSERVED",
    "provenance_note": "extraction_database.csv S649; source Gonzalez Rivas 2012, Development in Practice 22(1):31-43, Tables 3-5. A clean institutional/fiscal-transfer exposure (federal intergovernmental transfers under Mexico's constitutionally assigned municipal water-governance system) tested by a national three-model regression design (coverage model, transfers-mechanism model, combined model) against a directly measured piped-water-coverage outcome across 2,342-2,372 municipalities, with statistically significant coefficients confirming the proposed fiscal-transfer mechanism.",
    "included_in_pooled_estimate": "FALSE",
    "exclusion_from_pooling_reason": "ANALYSIS_PLAN.md S2 -- single quantitative study using a Mexico-specific municipal fiscal-transfer exposure and a piped-water-coverage outcome; the fiscal-grant/transfer-allocation exposure does not cleanly map onto the Family A/B/C legal-recognition, administrative-assistance, or administrative-barrier definitions, so no synthesis_family is assigned and no other study in the corpus shares this specific institutional/fiscal operationalization, so pooling is not yet possible or meaningful.",
})

fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)
print(f"New total: {len(rows)}")
