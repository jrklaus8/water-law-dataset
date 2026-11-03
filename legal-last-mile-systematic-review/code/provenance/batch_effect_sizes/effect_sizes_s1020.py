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
assert "S1020" not in existing

new_row = {
    "study_id": "S1020",
    "outcome_family": "water_access",
    "synthesis_family": "A",
    "exposure_definition": "Household residence in a treatment micro-watershed subject to a government watershed-development intervention (Rajiv Gandhi Mission for Watershed Development), rural Madhya Pradesh, India, evaluated via nearest-neighbor propensity score matching (n=470 matched households).",
    "comparator_definition": "Households in matched control (non-treatment) watersheds within the same study region, matched on observable household/land/income characteristics.",
    "effect_measure": "Propensity-score-matched average treatment effect on the treated (ATT), minutes/day change in domestic water collection time (dry season, March-July)",
    "effect_estimate": "Full matched sample: +17.37 min/day increase (SE 2.46). By social group: SC/ST +18.32 (SE 3.02), Other +16.19 (SE 4.04). By income quartile: bottom +12.83 (SE 4.50), 2nd +17.14 (SE 4.54), 3rd +8.57** (SE 5.09), top +31.03* (SE 5.28). By prior water-collection-time quartile: lowest +62.65* (SE 5.37), 2nd +35.36* (SE 4.40), 3rd +15.57 (SE 3.31), highest +31.13* (SE 3.16).",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "2.46 (full sample); see effect_estimate for subgroup SEs",
    "sample_size": "470 matched households",
    "direction": "negative (watershed-development intervention associated with increased, i.e. worsened, domestic water collection time on average)",
    "adjusted": "TRUE",
    "evidence_status": "OBSERVED",
    "provenance_note": "extraction_database.csv S1020; source Hope 2007, World Development, Table 8. Family A (legal recognition/institutional-management-model and access): a propensity-score-matched quasi-experimental estimate directly isolating a government institutional mechanism's (watershed-development programme) effect on a household water-access outcome (domestic water collection time), with heterogeneous effects by income and social group.",
    "included_in_pooled_estimate": "FALSE",
    "exclusion_from_pooling_reason": "ANALYSIS_PLAN.md S2 decision tree -- single study defining this exact exposure-comparator (government watershed-development programme vs. domestic water collection time, PSM design in one Indian microwatershed); no other Family A study yet shares this operationalization, so pooling is not yet possible or meaningful (too few independent studies in this family with this exposure).",
}

atomic_write(PATH, fieldnames, rows + [new_row])
print(f"effect_sizes.csv updated: 1 row added ({len(rows)} -> {len(rows) + 1}).")
