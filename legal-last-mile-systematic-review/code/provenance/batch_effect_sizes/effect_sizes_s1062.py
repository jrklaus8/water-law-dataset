#!/usr/bin/env python3
import csv, tempfile, os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/effect_sizes/effect_sizes.csv"

def atomic_write(path, fieldnames, rows):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path))
    with os.fdopen(fd, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp, path)

with open(PATH, newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing = {r["study_id"] for r in rows}
assert "S1062" not in existing

new_row = {
    "study_id": "S1062",
    "outcome_family": "service_coverage",
    "synthesis_family": "C",
    "exposure_definition": "Water-utility operation-and-maintenance (O&M) cost-recovery ratio (a financial/regulatory institutional-policy mechanism), and its square, across Sub-Saharan African water utilities.",
    "comparator_definition": "Utility-years within the same panel with lower cost-recovery ratios.",
    "effect_measure": "Panel regression coefficient (pooled OLS, fixed effects, random effects) on annual change in water-supply coverage (%)",
    "effect_estimate": "O&M cost-recovery ratio (cr): positive, significant coefficient on coverage change across all specifications. Squared term (cr^2): negative, significant coefficient of comparable magnitude -- curvilinear (inverted-U) relationship; coverage gains from cost recovery diminish and reverse beyond a threshold level. Exact numeric coefficient/SE values in source Table 4 were not cleanly extractable from PDF-to-text conversion (table structure garbled); direction and significance are drawn from the paper's own prose description of its regression results (Section 4).",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "not cleanly extractable from source PDF conversion",
    "sample_size": "225 observations, 22 Sub-Saharan African countries, 1995-2009",
    "direction": "positive up to a threshold, then negative (curvilinear/inverted-U)",
    "adjusted": "TRUE",
    "evidence_status": "OBSERVED",
    "provenance_note": "extraction_database.csv S1062; source Marson & Savin 2015, World Development, Section 4 (Regression Results) and Table 4. Family C (administrative/legal barriers and access inequality): panel-regression estimates directly isolating a financial/regulatory institutional mechanism's (utility cost-recovery policy) effect on a water-access outcome (coverage change), significant across pooled OLS, fixed-effects, and random-effects specifications.",
    "included_in_pooled_estimate": "FALSE",
    "exclusion_from_pooling_reason": "ANALYSIS_PLAN.md S2 decision tree -- single study defining this exact exposure-outcome pairing (utility cost-recovery ratio and water-coverage change across SSA utilities), with precise numeric coefficients not cleanly extractable from the source PDF; pooling is not yet possible or meaningful.",
}

atomic_write(PATH, fieldnames, rows + [new_row])
print(f"effect_sizes.csv updated: 1 row added ({len(rows)} -> {len(rows) + 1}).")
