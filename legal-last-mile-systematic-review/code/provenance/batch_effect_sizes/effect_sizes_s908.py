#!/usr/bin/env python3
import csv, tempfile, os

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
ES = f"{BASE}/05_analysis/effect_sizes/effect_sizes.csv"

with open(ES, newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)
    existing_ids = {row["study_id"] for row in rows}

assert "S908" not in existing_ids

row = {fn: "" for fn in fieldnames}
row.update({
    "study_id": "S908",
    "outcome_family": "water_access",
    "synthesis_family": "B",
    "exposure_definition": "Public service district (PSD) uses multiple raw-water sources, a source-diversification practice explicitly encouraged by West Virginia's Source Water Protection Act (Senate Bill 373, 2014).",
    "comparator_definition": "PSDs relying on only one raw-water source (surface water, purchased water, or groundwater alone).",
    "effect_measure": "OLS regression of residential water charges per 4,500 gallons, cross-sectional analysis of 110 West Virginia public service districts",
    "effect_estimate": "PSDs using multiple raw-water sources have residential water charges approximately 29% higher than single-source PSDs (statistically significant). No statistically significant difference found between PSDs using NRCS flood-control impoundments versus conventional single sources. Combined water+sewer service and greater network length are separately associated with lower and higher charges respectively.",
    "lower_CI": "", "upper_CI": "", "standard_error": "",
    "sample_size": "110 public service districts, West Virginia",
    "direction": "positive and significant (higher water charges for multi-source PSDs)",
    "adjusted": "adjusted (long-term debt, network length, combined water/sewer service provision as controls)",
    "evidence_status": "OBSERVED",
    "provenance_note": "extraction_database.csv S908 (Essay 3 of 3); source Alzahrani 2019, PhD Dissertation, West Virginia University, Essay 3 abstract and results. OLS regression directly isolating a specific state statutory mechanism (West Virginia's Source Water Protection Act, Senate Bill 373, 2014, encouraging multi-source water supply) with residential water charges (a directly measured water-affordability/access outcome) as the dependent variable across 110 public service districts.",
    "included_in_pooled_estimate": "FALSE",
    "exclusion_from_pooling_reason": "ANALYSIS_PLAN.md S2 decision tree -- single study defining this exact exposure-comparator (West Virginia Source Water Protection Act/multi-source PSD status regressed on residential water charges); no other Family B study yet shares this specific operationalization, so pooling is not yet possible or meaningful (too few independent studies in this family, per PROJECT_SPEC.md S8 guidance).",
})
rows.append(row)

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(ES))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, ES)

print(f"New total: {len(rows)}")
