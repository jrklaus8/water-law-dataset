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
assert "S1057" not in existing

new_row = {
    "study_id": "S1057",
    "outcome_family": "water_access",
    "synthesis_family": "A",
    "exposure_definition": "Household-level participation in community-based water-service design and local decision-making, and resulting community design satisfaction, in government demand-responsive rural water programs (Sri Lanka; Karnataka and Maharashtra, India).",
    "comparator_definition": "Households/communities within the same programs with lower levels of design participation, local decision-making, and community design satisfaction.",
    "effect_measure": "OLS coefficient on log household water-collection time-saving (Huber-adjusted standard errors); multivariate probit marginal effects on community design satisfaction",
    "effect_estimate": "Community design satisfaction -> log household water-collection time-saving: Sri Lanka 1.63 (SE 0.95, p<.10); Karnataka 2.92 (SE 0.95, p<.01); Maharashtra 1.06 (SE 0.38, p<.01). Design participation and local decision-making both significantly increase community design satisfaction across all three sites (p<.01 to p<.05).",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "0.95 (Sri Lanka); 0.95 (Karnataka); 0.38 (Maharashtra)",
    "sample_size": "288 households/18 communities (Sri Lanka); 188 households/12 communities (Karnataka); 249 households/20 communities (Maharashtra)",
    "direction": "positive (higher design participation and community design satisfaction associated with greater household water-collection time-savings)",
    "adjusted": "TRUE",
    "evidence_status": "OBSERVED",
    "provenance_note": "extraction_database.csv S1057; source Isham & Kahkonen 2001, World Bank working paper, Tables 3-4. Family A (legal recognition/institutional-management-model and access): OLS/probit/IV estimates directly isolating an institutional/participatory mechanism's (community design participation) effect on a water-access-relevant outcome (household water-collection time-savings) across three independent sites.",
    "included_in_pooled_estimate": "FALSE",
    "exclusion_from_pooling_reason": "ANALYSIS_PLAN.md S2 decision tree -- three site-specific coefficients from a single study, not independent studies; heterogeneous outcome scaling (log time-saving) not directly comparable to other Family A studies' effect measures, so pooling is not yet possible or meaningful.",
}

atomic_write(PATH, fieldnames, rows + [new_row])
print(f"effect_sizes.csv updated: 1 row added ({len(rows)} -> {len(rows) + 1}).")
