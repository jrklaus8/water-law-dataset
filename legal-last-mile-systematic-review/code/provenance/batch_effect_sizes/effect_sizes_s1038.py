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
assert "S1038" not in existing

new_row = {
    "study_id": "S1038",
    "outcome_family": "affordability",
    "synthesis_family": "C",
    "exposure_definition": "Residential customers of a municipally-owned water utility subject to local-only economic regulation (regulated by city council/water commission, not by a state public utility commission), United States, 1965 AWWA survey data.",
    "comparator_definition": "Residential customers of a municipally-owned water utility subject to state public utility commission economic regulation (in the five U.S. states that regulated municipal water rate structures at the state level).",
    "effect_measure": "Monopoly welfare loss as percent of residential customer's annual water bill (two-sample mean difference, t-test)",
    "effect_estimate": "Model 1 (unweighted average): locally-regulated 9.6% (SE 0.583, n=88) vs. state-regulated 5.2% (SE 0.818, n=27); difference -4.6 percentage points, t=-4.58 (p<0.01, one-tailed). Model 2 (weighted average): locally-regulated 10.39% (SE 0.786) vs. state-regulated 6.15% (SE 1.35); difference -4.24 percentage points, t=-2.71 (p<0.01, one-tailed).",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "0.583 (Model 1, locally-regulated); 0.818 (Model 1, state-regulated); 0.786 (Model 2, locally-regulated); 1.35 (Model 2, state-regulated)",
    "sample_size": "88 (locally-regulated); 27 (state-regulated)",
    "direction": "negative (state-level economic regulation associated with lower excess pricing / lower monopoly welfare loss, i.e., improved affordability, relative to local-only regulation)",
    "adjusted": "TRUE",
    "evidence_status": "OBSERVED",
    "provenance_note": "extraction_database.csv S1038; source Bruggink 1985, American Journal of Economics and Sociology, Table 2. Family C (institutional/legal barriers and access inequality): an econometrically-derived welfare-loss estimate directly isolates a regulatory/institutional mechanism's (state vs. local economic regulation of municipal water utilities) effect on a water-affordability outcome (excess residential pricing above long-run marginal cost).",
    "included_in_pooled_estimate": "FALSE",
    "exclusion_from_pooling_reason": "ANALYSIS_PLAN.md S2 decision tree -- single study defining this exact exposure-comparator (state vs. local economic regulation and monopoly welfare loss among U.S. municipal water utilities, 1965 cross-section); no other Family C study yet shares this operationalization, so pooling is not yet possible or meaningful (too few independent studies in this family with this exposure).",
}

atomic_write(PATH, fieldnames, rows + [new_row])
print(f"effect_sizes.csv updated: 1 row added ({len(rows)} -> {len(rows) + 1}).")
