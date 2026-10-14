import csv, os, tempfile

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/effect_sizes/effect_sizes.csv"

def main():
    with open(DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    assert "S589" not in {r["study_id"] for r in rows}

    new_row = {
        "study_id": "S589",
        "outcome_family": "economic_access",
        "synthesis_family": "A",
        "exposure_definition": "Formal household connection to the municipal piped water network in Machala, Ecuador (a city with 90% water coverage).",
        "comparator_definition": "Unconnected households (the poorest, uncovered segment of the population) served instead by private water tankers.",
        "effect_measure": "descriptive group comparison (unadjusted; monthly consumption volume and water expenditure as a percentage of household income)",
        "effect_estimate": "Connected households consumed ~15 m3/month at ~US$1.20/month (0.4% of monthly family income); unconnected households consumed only ~4-5 m3/month at ~US$29.00/month (9.0% of monthly family income) -- roughly 22-24x higher effective per-unit water cost and ~3x lower consumption for unconnected households.",
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "sample_size": "not reported in source (illustrative city-level comparison)",
        "direction": "negative (lack of a formal water connection associated with lower consumption and a dramatically higher cost share of income)",
        "adjusted": "unadjusted",
        "evidence_status": "OBSERVED",
        "provenance_note": "extraction_database.csv S589; source World Bank/IDB 2004, Report No. 28911-EC, Box 3.2 (underlying household data originally from Yepes, Gomez and Carvajal 2002; Sotomayor 2004). Illustrative case comparison, not a formal regression estimate; no sample size, CI, or significance test reported in the source.",
        "included_in_pooled_estimate": "FALSE",
        "exclusion_from_pooling_reason": "ANALYSIS_PLAN.md S2 -- single illustrative case comparison (not a study-level regression/RCT estimate, no CI/sample size reported); conceptually shares Family A's exposure-comparator (formal connection vs. no connection) with S084 and others, but its descriptive city-case nature and lack of any statistical uncertainty measure makes it non-comparable/non-poolable with the other Family A studies at this time.",
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
