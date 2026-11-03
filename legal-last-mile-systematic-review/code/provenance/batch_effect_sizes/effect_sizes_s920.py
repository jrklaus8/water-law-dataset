#!/usr/bin/env python3
import csv, tempfile, os

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
ES = f"{BASE}/05_analysis/effect_sizes/effect_sizes.csv"

with open(ES, newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)
    existing_ids = {row["study_id"] for row in rows}

assert "S920" not in existing_ids

row = {fn: "" for fn in fieldnames}
row.update({
    "study_id": "S920",
    "outcome_family": "water_access",
    "synthesis_family": "A",
    "exposure_definition": "Rural municipality implements a small-scale water supply system through a community-based water user association (WUA) -- a participatory institutional/legal management model -- versus",
    "comparator_definition": "Rural municipality implements a small-scale water supply system through non-participatory local government management (the referent/control project type).",
    "effect_measure": "Difference-in-differences estimator combined with kernel propensity-score matching, Brazilian census panel (2000, 2010) plus national water and sanitation survey",
    "effect_estimate": "Municipalities with WUA-managed projects realized piped-water access-rate increases of approximately 6 percentage points above the national average trend (statistically significant, robust to specification changes and matching-balance checks). Rural piped-water access rose from a 15-16% baseline (2000) to 33.4% in WUA-served areas versus 24.9% in local-government-served areas by 2010. Heterogeneity analysis: in local-government-project municipalities with independently higher accountability (local media presence, political competition, or pre-implementation citizen mobilization), access-rate gains matched WUA-area gains, indicating participatory accountability -- not project type per se -- is the underlying mechanism.",
    "lower_CI": "", "upper_CI": "", "standard_error": "",
    "sample_size": "national municipality-level panel, Brazil (2000-2010 census plus national water/sanitation survey)",
    "direction": "positive and significant (WUA/participatory management increases piped-water access rates)",
    "adjusted": "adjusted (kernel propensity-score matching on determinants of project-type choice, informed by semi-structured expert interviews; robustness checks confirm no structural treatment/control differences)",
    "evidence_status": "OBSERVED",
    "provenance_note": "extraction_database.csv S920; source Barde 2017, World Development. Difference-in-differences with kernel matching directly isolating a specific institutional/legal management-model mechanism (community-based water user association vs. non-participatory local government management) with piped-water access rate as the directly measured water-access outcome -- a genuine Family A (legal recognition/formal connection) estimate at national administrative-panel scale.",
    "included_in_pooled_estimate": "FALSE",
    "exclusion_from_pooling_reason": "ANALYSIS_PLAN.md S2 decision tree -- single study defining this exact exposure-comparator (Brazilian WUA vs. local-government rural water-project management model via DiD/kernel matching); no other Family A study yet shares this specific operationalization, so pooling is not yet possible or meaningful (too few independent studies in this family, per PROJECT_SPEC.md S8 guidance).",
})
rows.append(row)

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(ES))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, ES)

print(f"New total: {len(rows)}")
