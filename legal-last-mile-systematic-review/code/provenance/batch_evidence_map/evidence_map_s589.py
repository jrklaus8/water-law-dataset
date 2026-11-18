import csv, os, tempfile

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/descriptive/evidence_map.csv"

def main():
    with open(DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    assert "S589" not in {r["study_id"] for r in rows}

    new_row = {
        "study_id": "S589",
        "study_design_class": "observational",
        "evidence_level": "National fiscal-management/public-expenditure review (World Bank/IDB, 2004) presenting an original World-Bank-staff quantile-based subsidy-incidence estimate for Ecuador's water sector (Table 3.4) and an illustrative household-level case comparison (Box 3.2, Machala) of connected vs. unconnected household water costs; provisional confidence: moderate -- water/sanitation is a minor sub-topic within a much larger multi-sector fiscal report, and the household case data is itself drawn from a secondary source, but the quintile subsidy-incidence estimate is original to this report and both findings converge on the same regressive-access pattern.",
        "mechanism_family": "decentralized_governance_regressive_subsidy_incidence",
        "outcome_family": "economic_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "decentralized_municipal_water_governance_incomplete_regulatory_framework",
        "institutional_context": "Water and sanitation service provision in Ecuador is fully decentralized to municipal governments, with no integrated national system for managing water resources and an incomplete regulatory/institutional framework (contrasted with the more developed electricity-sector framework). Central Government transfers to municipalities for water investment (via MIDUVI) fell from US$52 million in 2001 to US$5 million in 2002, with 70% of remaining sector resources concentrated in Quito and Guayaquil. Water subsidies are regressively distributed (7.9% to the poorest income quintile vs. 41.3% to the richest), and in Machala, households with a formal connection pay roughly 22 times less per unit of water than unconnected households dependent on tanker supply.",
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

    print(f"done, evidence_map rows now {len(rows)}")

if __name__ == "__main__":
    main()
