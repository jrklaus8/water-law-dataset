import csv, os, tempfile

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/descriptive/evidence_map.csv"

def main():
    with open(DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    existing_ids = {r["study_id"] for r in rows}
    assert "S580" not in existing_ids and "S581" not in existing_ids

    new_rows = [
        {
            "study_id": "S580",
            "study_design_class": "qualitative",
            "evidence_level": "Qualitative case study of an intergroup negotiation process between indigenous highland communities and development professionals over water/natural-resource governance in the Chambo river subbasin, Ecuador. Documents indigenous communities' legal land titles, a judicial workshop process, and formation of a new interinstitutional legal consortium; provisional confidence: moderate -- concrete legal-institutional artefacts described in a process case narrative, but no quantified access outcome.",
            "mechanism_family": "indigenous_land_title_consortium_formation",
            "outcome_family": "water_access",
            "quantitative_synthesis_eligible": "FALSE",
            "qualitative_synthesis_eligible": "TRUE",
            "legal_context": "indigenous_land_titles_interinstitutional_consortium",
            "institutional_context": "Negotiations between indigenous communities and provincial development professionals/NGOs in the Chambo river subbasin proceeded through recognition of indigenous communities' legal land titles, a judicial workshop, and the creation of a formal Interinstitutional Consortium as a new legal governance structure spanning indigenous and state/professional institutions for subbasin water and natural-resource management.",
        },
        {
            "study_id": "S581",
            "study_design_class": "mixed-methods",
            "evidence_level": "Mixed-methods comparative study of water-supply-policy transitions across the 22 largest American Southwest metropolitan statistical areas. Documents institutional-logics conflicts (development, preservation, environmental, consumer) over supply-increase and demand-reduction water policy, and a quantitative decision-tree/random-forest model identifying political factors (Partisan Voting Index) as the dominant predictor of municipal water-conservation-policy adoption; provisional confidence: moderate-high -- systematic qualitative conflict coding plus quantitative modeling across a full population of 22 MSAs, though the outcome measured is a policy-adoption index rather than direct household access.",
            "mechanism_family": "municipal_water_policy_political_institutional_logics",
            "outcome_family": "service_reliability",
            "quantitative_synthesis_eligible": "FALSE",
            "qualitative_synthesis_eligible": "TRUE",
            "legal_context": "municipal_water_conservation_ordinances_water_rights_litigation",
            "institutional_context": "Municipal water-supply strategy in 22 American Southwest MSAs is shaped by conflict among development, rural-preservation, environmental, and urban-consumer institutional logics, manifest in water-rights litigation (e.g., Choctaw/Chickasaw Nations v. Oklahoma City Water Utilities Trust over Sardis Lake), tiered-pricing and conservation-mandate ordinances, and ratepayer opposition to infrastructure cost pass-through (e.g., San Antonio's Vista Ridge pipeline); a city's Partisan Voting Index was found to be the dominant predictor of the extent of demand-reduction/conservation-policy adoption.",
        },
    ]

    for row in new_rows:
        extra = set(row.keys()) - set(fieldnames)
        assert not extra, f"unexpected fields: {extra}"
        missing = set(fieldnames) - set(row.keys())
        assert not missing, f"missing fields: {missing}"

    rows.extend(new_rows)

    fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(DB), suffix=".csv")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp_path, DB)

    print(f"done, evidence_map rows now {len(rows)}")

if __name__ == "__main__":
    main()
