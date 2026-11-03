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
        "study_id": "S1136",
        "outcome_family": "sanitation_access",
        "synthesis_family": "C",
        "exposure_definition": (
            "Political capture of village sanitation infrastructure: "
            "residing in the Gram Panchayat head's village, or on a road "
            "where a politician resides, vs. other village roads; road "
            "inhabited predominantly by Scheduled Castes/Tribes vs. "
            "upper-caste road; 5,276 villages/wards, 10,408 roads, 4 South "
            "Indian states."
        ),
        "comparator_definition": "Roads/villages without these political-capture or caste characteristics, within the same block/village (fixed effects).",
        "effect_measure": "Linear probability model coefficients, village/block fixed effects",
        "effect_estimate": (
            "GP head's village: road paved 0.053***, has drain 0.037**, "
            "moderately clean 0.028*, no garbage 0.060***. Politician "
            "road: has drain 0.078***, paved 0.055***, moderately clean "
            "0.052*. SC/ST road (vs. upper-caste road): paved -0.051**, "
            "no garbage -0.032*. Oligarchic village structure and "
            "upper-caste land-ownership share show no significant "
            "infrastructure disadvantage/advantage across most outcomes."
        ),
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "clustered at colony level",
        "sample_size": "5,276 villages/wards; 10,408 roads (South India)",
        "direction": "positive (political proximity increases sanitation-infrastructure provision; SC/ST residence decreases it)",
        "adjusted": "TRUE",
        "evidence_status": "OBSERVED",
        "provenance_note": (
            "extraction_database.csv S1136; source Ban, Das Gupta & Rao "
            "2010, Journal of Development Studies, Tables 5-6. Family C "
            "(administrative/legal barriers/access inequality): linear-"
            "probability-model estimates with village- and block-level "
            "fixed effects directly isolating political capture of a "
            "constitutionally mandated local-government sanitation "
            "function as a mechanism producing differential sanitation-"
            "infrastructure access."
        ),
        "included_in_pooled_estimate": "FALSE",
        "exclusion_from_pooling_reason": (
            "ANALYSIS_PLAN.md S2 decision tree -- single study defining "
            "this exact exposure-outcome pairing (political capture of "
            "Gram Panchayat sanitation infrastructure and road-level "
            "sanitation outcomes in South India); no other Family C study "
            "yet shares this operationalization, so pooling is not yet "
            "possible or meaningful."
        ),
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"effect_sizes.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
