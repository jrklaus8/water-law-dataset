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
assert "S1102" not in existing_ids

new_row = {
    "study_id": "S1102",
    "outcome_family": "water_access",
    "synthesis_family": "B",
    "exposure_definition": (
        "Household-level capital-cost contribution and meeting attendance "
        "(participatory/administrative engagement) in community-based rural "
        "drinking-water project governance, 45 villages, India."
    ),
    "comparator_definition": (
        "Households within the same villages that did not contribute to capital "
        "costs / did not attend project meetings, matched via propensity score on "
        "wealth, literacy, household and village size."
    ),
    "effect_measure": "Propensity-score-matched treatment-control mean difference (t-statistic)",
    "effect_estimate": (
        "Capital cost contribution -> water improvements index: treatment 0.364, "
        "control -0.676, difference 1.04 (t=4.26). Capital cost contribution -> "
        "household satisfaction: treatment 0.813, control 0.458, difference 0.355 "
        "(t=8.54). Meeting attendance -> water improvements index: treatment 0.497, "
        "control -0.252, difference 0.749 (t=3.46). Meeting attendance -> "
        "satisfaction: treatment 0.790, control 0.685, difference 0.105 (t=4.16). "
        "Water improvements index is a composite of change in distance to source, "
        "collection time, reliability, quality, pressure, adequacy, and perceived "
        "access."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "sample_size": "45 villages (Uttar Pradesh Hills, North Karnataka, South Karnataka), household-level data",
    "direction": "positive (participation and capital-cost contribution associated with improved water-access outcomes and satisfaction)",
    "adjusted": "TRUE",
    "evidence_status": "OBSERVED",
    "provenance_note": (
        "extraction_database.csv S1102; source Prokopy 2009, Journal of Development "
        "Studies, Table 4. Family B (administrative assistance/access): propensity-"
        "score-matched quasi-experimental estimates directly isolating a "
        "participatory/administrative institutional mechanism's (capital-cost "
        "contribution, meeting attendance) effect on a composite water-access "
        "outcome index, with no evidence of elite capture across income groups."
    ),
    "included_in_pooled_estimate": "FALSE",
    "exclusion_from_pooling_reason": (
        "ANALYSIS_PLAN.md S2 decision tree -- single study defining this exact "
        "exposure-outcome pairing (household participation/contribution and a "
        "composite water-improvements index in Indian rural water projects); no "
        "other Family B study yet shares this operationalization, so pooling is not "
        "yet possible or meaningful (too few independent studies in this family "
        "with this exposure)."
    ),
}

atomic_write(PATH, fieldnames, rows + [new_row])
print(f"effect_sizes.csv updated: 1 row added ({len(rows)} -> {len(rows) + 1}).")
