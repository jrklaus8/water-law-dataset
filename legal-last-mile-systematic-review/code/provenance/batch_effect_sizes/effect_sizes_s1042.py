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
assert "S1042" not in existing

new_row = {
    "study_id": "S1042",
    "outcome_family": "water_access",
    "synthesis_family": "A",
    "exposure_definition": "Rural municipality (Dnipropetrowskyy or Ternopilskyy region, Ukraine) with an established community-based organization (CBO) and/or higher levels of non-electoral resident participation (town hall meeting attendance, peer pressure).",
    "comparator_definition": "Rural municipality within the same survey sample without an established CBO and/or with lower levels of non-electoral participation.",
    "effect_measure": "Marginal effect on probability of good water-supply system quality (SUR and ordered Probit with instrumental variables)",
    "effect_estimate": "Town hall meeting participation (unit increase): +29 percentage points probability of good water-supply situation. Peer pressure: +14 percentage points. Established CBO (dummy): approximately +25 percentage points probability of good water-supply system.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "sample_size": "7.2% of municipalities randomly sampled across two Ukrainian regions (Dnipropetrowskyy, Ternopilskyy)",
    "direction": "positive (participation and CBO establishment associated with improved water-supply-system quality)",
    "adjusted": "TRUE",
    "evidence_status": "OBSERVED",
    "provenance_note": "extraction_database.csv S1042; source Kvartiuk 2016, Voluntas, Tables 3-4. Family A (legal recognition/institutional-management-model and access): regression-based estimates (SUR, ordered Probit with IVs) directly isolating institutional/participatory mechanisms' (CBO establishment, non-electoral participation) effect on a water-supply-quality access outcome.",
    "included_in_pooled_estimate": "FALSE",
    "exclusion_from_pooling_reason": "ANALYSIS_PLAN.md S2 decision tree -- single study defining this exact exposure-comparator (CBO establishment/non-electoral participation and water-supply-system quality in rural Ukrainian municipalities); no other Family A study yet shares this operationalization, so pooling is not yet possible or meaningful (too few independent studies in this family with this exposure).",
}

atomic_write(PATH, fieldnames, rows + [new_row])
print(f"effect_sizes.csv updated: 1 row added ({len(rows)} -> {len(rows) + 1}).")
