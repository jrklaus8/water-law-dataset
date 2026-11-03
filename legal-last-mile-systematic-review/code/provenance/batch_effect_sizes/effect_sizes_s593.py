import csv, os, tempfile

EF = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/effect_sizes/effect_sizes.csv"

def main():
    with open(EF, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    assert not any(r["study_id"] == "S593" for r in rows)

    new_row = {
        "study_id": "S593",
        "outcome_family": "primary_connection",
        "synthesis_family": "C",
        "exposure_definition": ("Administrative district legal/institutional classification (si, urban-type, "
            "coded 1) versus gun (rural-type, coded 0) among South Korean local governments, 2010/2016/2021, "
            "alongside municipal fiscal autonomy (degree of financial independence, i.e. own-source revenue "
            "share of general accounting revenue) and local tax burden per person (log)."),
        "comparator_definition": ("Gun (rural-type) administrative districts as the reference category for the "
            "si/gun coefficient; lower financial independence and lower local tax burden per person as the "
            "implicit comparison for the fiscal coefficients, within the same 152-local-government sample."),
        "effect_measure": "Tobit regression coefficient on a Coulter distributional-inequity coefficient (0-100, censored dependent variable)",
        "effect_estimate": ("Administrative district unit (si=1): significant NEGATIVE coefficient (improves "
            "equity) in 2021 on average unit price (-0.9174, p<0.01), cost-recovery rate (-0.9064, p<0.05), "
            "revenue-water ratio (-0.8489, p<0.05), water-supply rate (-0.8566, p<0.01), and number of "
            "employees (-1.1569, p<0.01); not significant for customer satisfaction. Degree of financial "
            "independence: significant POSITIVE coefficient (worsens equity) on all 6 variables at p<0.01 in "
            "all 3 years (e.g. average unit price 2021: 0.1353). Local tax burden per person (log): significant "
            "NEGATIVE coefficient (improves equity) on all 6 variables at p<0.01 in all 3 years (e.g. average "
            "unit price 2021: -1.9115). Coefficients were consistent in sign and significance pattern across "
            "2010, 2016, and 2021, and robust to an ordinary-multiple-regression sensitivity check."),
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "0.3006-0.6 depending on variable/year (see extraction_database.csv S593, Tables 9-14)",
        "sample_size": "152 local governments per year (2010, 2016, 2021); 18 Tobit models total (6 outcome variables x 3 years)",
        "direction": ("mixed: administrative si classification and local tax burden per person are associated "
            "with GREATER equity (lower inequity coefficient); municipal fiscal autonomy (financial "
            "independence) is associated with LESS equity (higher inequity coefficient)"),
        "adjusted": "adjusted (controls for mayoral re-election, private-consignment status, local-public-enterprise status)",
        "evidence_status": "OBSERVED",
        "provenance_note": ("extraction_database.csv S593; source Ko 2024, J. Korea Water Resources Assoc. "
            "57(6):393-407, Tables 9-14. A clean institutional/fiscal-governance exposure (administrative "
            "district classification, municipal fiscal autonomy) tested by Tobit regression against a "
            "directly measured, multi-year distributional-equity outcome across 152 local governments and "
            "6 water-service variables, with consistent, replicated significance across all 3 study years."),
        "included_in_pooled_estimate": "FALSE",
        "exclusion_from_pooling_reason": ("ANALYSIS_PLAN.md S2 -- single quantitative study using a South "
            "Korean administrative-district/fiscal-autonomy exposure and a Coulter inequity-coefficient "
            "outcome; no other Family C study in the corpus shares this specific institutional/fiscal "
            "operationalization (administrative district classification and municipal fiscal autonomy), so "
            "pooling is not yet possible or meaningful."),
    }
    rows.append(new_row)

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(EF) or ".")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmppath, EF)

    print("Appended effect_sizes row for S593")

if __name__ == "__main__":
    main()
