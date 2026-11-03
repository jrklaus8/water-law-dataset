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

existing_ids = {r["study_id"] for r in rows}

new_rows = [
    {
        "study_id": "S1162",
        "outcome_family": "water_access",
        "synthesis_family": "C",
        "exposure_definition": "Local-government administrative category (municipality, or town panchayat and other categories) versus municipal corporation, for urban local governments in India.",
        "comparator_definition": "Urban local governments classified as a municipal corporation (the reference category, generally larger cities with greater revenue-raising and administrative capacity).",
        "effect_measure": "Multilevel linear regression coefficient (percentage-point difference in household water-coverage growth, 2001-2011)",
        "effect_estimate": "Municipality vs. municipal corporation: -4.062 percentage points (SE 1.254, p<0.01). Town panchayat and other vs. municipal corporation: -4.034 percentage points (SE 1.540, p<0.01). Small city vs. metropolitan (large) city, in the alternate city-size-category model specification: -5.122 percentage points (SE 2.011, p<0.05); small town vs. metropolitan city: -5.432 percentage points (SE 2.209, p<0.05).",
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "1.254 (municipality); 1.540 (town panchayat); 2.011 (small city); 2.209 (small town)",
        "sample_size": "3,547 cities/towns nested within 21 states, India, 2001-2011",
        "direction": "negative (lower local-government administrative capacity/category is associated with significantly lower growth in household water-supply coverage)",
        "adjusted": "TRUE",
        "evidence_status": "OBSERVED",
        "provenance_note": "extraction_database.csv S1162; source Subramanyam 2020, Water Policy 22(3):468-482, Table 4. Family C (administrative/legal barriers and access inequality): multilevel-regression estimates directly isolating local-government administrative-category effects on differential household water-coverage growth across Indian cities.",
        "included_in_pooled_estimate": "FALSE",
        "exclusion_from_pooling_reason": "ANALYSIS_PLAN.md S2 decision tree -- single study defining this exact exposure-outcome pairing (Indian local-government administrative category and household water-coverage growth); no other Family C study yet shares this operationalization, so pooling is not yet possible or meaningful.",
    },
    {
        "study_id": "S1163",
        "outcome_family": "water_access",
        "synthesis_family": "B",
        "exposure_definition": "Rural school has externally-funded, supported, or implemented WaSH (water, sanitation, and hygiene) programs in the last year, across 14 low- and middle-income countries.",
        "comparator_definition": "Rural schools without externally-funded/supported/implemented WaSH programs in the last year, holding school enrollment size, pre-primary status, water accessibility to youngest children, water-source sharing with the community, PTA presence, number of water points, and country constant.",
        "effect_measure": "Odds ratio (multilevel mixed-effects logistic regression)",
        "effect_estimate": "1.4",
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "sample_size": "2,677 schools, 13 countries",
        "direction": "positive (external WaSH-program funding/support is associated with significantly higher odds of the school having at least a basic, continuously-available on-premises water service)",
        "adjusted": "TRUE",
        "evidence_status": "OBSERVED",
        "provenance_note": "extraction_database.csv S1163; source Cronk, Guo, Fleming & Bartram 2021, Science of the Total Environment 761:144226, Table 3 (p=0.021). Family B (administrative assistance/access): multilevel logistic-regression estimate directly isolating an external institutional-assistance mechanism's (WaSH program funding/support) effect on school-level water-service access.",
        "included_in_pooled_estimate": "FALSE",
        "exclusion_from_pooling_reason": "ANALYSIS_PLAN.md S2 decision tree -- single study defining this exact exposure-outcome pairing (external WaSH-program funding and rural-school water-service access, 14 LMICs); no other Family B study yet shares this operationalization, so pooling is not yet possible or meaningful.",
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"effect_sizes.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
