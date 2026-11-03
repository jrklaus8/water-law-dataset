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
assert "S1032" not in existing

new_row = {
    "study_id": "S1032",
    "outcome_family": "water_access",
    "synthesis_family": "C",
    "exposure_definition": "Household contact with the Ahmedabad Municipal Corporation (amc_com) or with an NGO (ngo_com) to seek redress for infrastructure/service problems within the Ahmedabad Slum Networking Project (SNP), a municipal-NGO-community co-production partnership, India.",
    "comparator_definition": "SNP participant households that did not contact the municipal corporation or an NGO for redress, within the same logistic regression sample (n=277).",
    "effect_measure": "Logistic regression odds ratio (respondent complains about water quality/quantity)",
    "effect_estimate": "Municipal corporation contact (amc_com): OR = 0.60* (SE 0.14). NGO contact (ngo_com): OR = 0.56* (SE 0.13). Area wealth (areawealth): OR = 0.07** (SE 0.06). Distance from central municipal offices (distance): OR = 1.44* (SE 0.21).",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "0.14 (amc_com); 0.13 (ngo_com); 0.06 (areawealth); 0.21 (distance)",
    "sample_size": "277 (water-complaint model)",
    "direction": "negative (institutional redress-seeking contact associated with reduced odds of water complaints)",
    "adjusted": "TRUE",
    "evidence_status": "OBSERVED",
    "provenance_note": "extraction_database.csv S1032; source Russ & Takahashi 2013, Urban Studies, Table 6. Family C (institutional/legal barriers and access inequality): a logistic-regression estimate directly isolating institutional/administrative redress-seeking mechanisms' (municipal-corporation contact, NGO contact) effect on a water-service-complaint outcome within a specific slum-upgrading infrastructure programme.",
    "included_in_pooled_estimate": "FALSE",
    "exclusion_from_pooling_reason": "ANALYSIS_PLAN.md S2 decision tree -- single study defining this exact exposure-comparator (institutional redress-seeking contact vs. water-complaint odds within one Indian slum-networking programme); no other Family C study yet shares this operationalization, so pooling is not yet possible or meaningful (too few independent studies in this family with this exposure).",
}

atomic_write(PATH, fieldnames, rows + [new_row])
print(f"effect_sizes.csv updated: 1 row added ({len(rows)} -> {len(rows) + 1}).")
