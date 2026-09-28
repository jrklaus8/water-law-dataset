#!/usr/bin/env python3
import csv, tempfile, os

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
EFF = f"{BASE}/05_analysis/effect_sizes/effect_sizes.csv"

with open(EFF, newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)
    existing_ids = {row["study_id"] for row in rows}

assert "S869" not in existing_ids

rows.append({
    "study_id": "S869",
    "outcome_family": "service_coverage",
    "synthesis_family": "",
    "exposure_definition": "Municipality engaged in a formal intermunicipal cooperation consortium (program contract) for water/sewage service delivery, pursuant to Brazil's 1988 Constitution decentralisation framework and 2007/2020 federal sanitation legal framework -- coded as a binary cooperation variable.",
    "comparator_definition": "Municipalities providing water/sewage services as stand-alone (non-cooperating) local government units.",
    "effect_measure": "Bootstrapped multivariate general linear model regression coefficient (F-Wald test, robust standard errors, stratified bootstrap sampling by State), municipality-year panel",
    "effect_estimate": "Cooperation coefficient on water-service coverage (log): not statistically significant, p=.494 (F-statistic .468) in the bootstrapping regression (Table 3), and p=.240 (B=.064) in the parameter-estimation model (Table 4). Cooperation coefficient on sewage-service coverage (log): statistically significant, p=.026 (F-statistic 4.938) in the bootstrapping regression, and p=.007 (B=.466) in the parameter-estimation model. Cooperating municipalities had lower mean overall service coverage (M=41.58) than non-cooperating municipalities (M=59.45).",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "sample_size": "1157-1159 municipality-year panel observations (2013-2020), Brazil",
    "direction": "null for water coverage (not significant); positive and significant for sewage coverage",
    "adjusted": "adjusted (asset specificity: water/sewage investment; contract management complexity; population, area, density; year/financial-crisis fixed effects)",
    "evidence_status": "OBSERVED",
    "provenance_note": "extraction_database.csv S869; source Silvestre, Marques, Dollery & Correia 2022, Utilities Policy, Tables 3-4. Panel regression isolating a specific documented legal/institutional mechanism (formal intermunicipal consortium cooperation contracts under Brazil's sanitation legal framework) with water- and sewage-service coverage as directly-measured water/sanitation-access outcomes -- distinguished from the S837 Houston precedent (excluded there because the outcome was capital investment/debt, not a water-access measure).",
    "included_in_pooled_estimate": "FALSE",
    "exclusion_from_pooling_reason": "ANALYSIS_PLAN.md S2 decision tree -- single study defining this exact exposure-comparator (Brazilian intermunicipal sanitation-consortium cooperation via panel GLM); no other study yet shares this specific operationalization of institutional cooperation arrangements, so pooling is not yet possible or meaningful (too few independent studies in this family, per PROJECT_SPEC.md S8 guidance). Consistent with the S749/S795 precedent, synthesis_family is left blank as this institutional-cooperation-arrangement exposure does not cleanly map to Family A/B/C.",
})

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EFF))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EFF)

print(f"New total: {len(rows)}")
