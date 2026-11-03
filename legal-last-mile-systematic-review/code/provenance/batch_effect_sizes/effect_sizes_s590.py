import csv, os, tempfile

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/effect_sizes/effect_sizes.csv"

def main():
    with open(DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    assert "S590" not in {r["study_id"] for r in rows}

    new_row = {
        "study_id": "S590",
        "outcome_family": "primary_connection",
        "synthesis_family": "C",
        "exposure_definition": "Degree to which a Prussian city's local franchise/voting-rights system concentrated political power among the wealthiest taxpayers (the tax-weighted 'Three Class System', in force in the Rhineland and Westphalia) versus a more equal, tax-based franchise (Hannover and Holstein), 1880-1887.",
        "comparator_definition": "Cities under the more equal-franchise systems of Hannover and Holstein, and within-province variation in the skewness of the local income/tax distribution (SKEW variable).",
        "effect_measure": "Logit regression coefficient and predicted-probability responsiveness, with counterfactual provincial coefficient-swap simulations",
        "effect_estimate": "SKEW (income/tax-payment skew) coefficient 0.457 in the Three-Class-System provinces (responsiveness 0.175); likelihood-ratio test rejects the null that franchise structure did not matter (test statistic -30.0, 3 df, significant at all conventional levels). Counterfactual: imposing Hannover's (equal-franchise) coefficients on Westphalian towns lowers their average predicted probability of building a waterworks by about one-third; imposing Holstein's coefficients reduces it to zero; conversely, imposing Rhineland's (Three-Class-System) coefficients on non-building towns in Hannover/Holstein substantially raises predicted probability.",
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "sample_size": "244 cities (50 building, 194 not building waterworks during 1880-1887)",
        "direction": "positive (greater concentration of local political power among wealthy taxpayers/property owners associated with a higher probability of a city investing in waterworks infrastructure)",
        "adjusted": "adjusted (instrumented cost per capita; controls for community ability to pay, cholera mortality, population density, and industrial/steel employment)",
        "evidence_status": "OBSERVED",
        "provenance_note": "extraction_database.csv S590; source Brown 1989, Urban Studies 26:2-12, Tables 3-4. One of the strongest quasi-experimental designs for a legal-institutional exposure in the corpus, exploiting genuine cross-province variation in 19th-century Prussian municipal franchise law.",
        "included_in_pooled_estimate": "FALSE",
        "exclusion_from_pooling_reason": "ANALYSIS_PLAN.md S2 -- single historical quasi-experimental study using a franchise-concentration exposure and a waterworks-construction-probability outcome; no other Family C study in the corpus shares this specific historical/legal operationalization (19th-century municipal voting-rights structure), so pooling is not yet possible or meaningful.",
    }

    extra = set(new_row.keys()) - set(fieldnames)
    assert not extra, f"unexpected fields: {extra}"
    missing = set(fieldnames) - set(new_row.keys())
    assert not missing, f"missing fields: {missing}"

    rows.append(new_row)

    fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(DB), suffix=".csv")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp_path, DB)

    print(f"done, effect_sizes rows now {len(rows)}")

if __name__ == "__main__":
    main()
