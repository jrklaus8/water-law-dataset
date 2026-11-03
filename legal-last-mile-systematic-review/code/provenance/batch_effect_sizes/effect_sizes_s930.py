#!/usr/bin/env python3
import csv, tempfile, os

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
ES = f"{BASE}/05_analysis/effect_sizes/effect_sizes.csv"

with open(ES, newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)
    existing_ids = {row["study_id"] for row in rows}

assert "S930" not in existing_ids

rows.append({
    "study_id": "S930",
    "outcome_family": "sanitation_access",
    "synthesis_family": "A",
    "exposure_definition": "Municipality governed by usos y costumbres -- traditional indigenous customary-law participatory governance given full legal standing by Oaxaca's 1995 constitutional reform -- vs. municipality governed by political-party representative democracy, both retaining the same formal municipal institutions and fiscal relationships with the state/federal government.",
    "comparator_definition": "Party-governed municipalities in Oaxaca, Mexico (n=146 control, over common support after kernel-density propensity-score matching on municipal characteristics and long-term settlement patterns).",
    "effect_measure": "kernel-density propensity-score matching, average treatment effect on the treated (ATT), bootstrapped SE (B=1000)",
    "effect_estimate": "Sewerage access ATT = 0.086 (level, 1995-2005, p<0.01), and 9.05 percentage-point ATT in rate of change (1995-2005, p<0.01); smaller but still positive effect for 2000-10. Piped-water-access ATT was small and not statistically significant across all periods examined (e.g. 1990-2010 level ATT = 0.027, p=0.595).",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "0.034 (sewerage ATT, level, 1995-2005)",
    "sample_size": "418 treated / 146 control municipalities over common support",
    "direction": "positive (usos y costumbres associated with greater sewerage-access gains)",
    "adjusted": "TRUE",
    "evidence_status": "OBSERVED",
    "provenance_note": "extraction_database.csv S930; source Diaz-Cayeros, Magaloni & Ruiz-Euler 2014, World Development, Table 4. The water-specific ATT itself was not statistically significant; this effect_sizes entry is based on the sewerage/sanitation-access outcome, which was significant and directly isolates the 1995 legal-reform mechanism (usos y costumbres legal recognition) via matching.",
    "included_in_pooled_estimate": "FALSE",
    "exclusion_from_pooling_reason": "ANALYSIS_PLAN.md S2 decision tree -- single study defining this exact exposure-comparator (indigenous customary-governance legal recognition vs. party governance, Oaxaca Mexico); no other Family A study yet shares this operationalization, so pooling is not yet possible or meaningful (too few independent studies in this family, per PROJECT_SPEC.md S8 Family A guidance).",
})

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(ES))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, ES)

print(f"New total: {len(rows)}")
