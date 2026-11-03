import csv, os, tempfile

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/descriptive/evidence_map.csv"

def main():
    with open(DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    assert "S583" not in {r["study_id"] for r in rows}

    new_row = {
        "study_id": "S583",
        "study_design_class": "qualitative",
        "evidence_level": "Historical qualitative case-comparative study (primary archival sources: City Council/Waterworks Board/Water Company minutes, contemporary newspaper accounts, 1860-1890) of whether working-class suburbs of Norrkoping and Linkoping, Sweden received municipal piped-water connections, with secondary-source comparison to Stockholm and Malmo. Documents the planned-area/rural-district administrative boundary determining applicability of building, fire, and public-health codes, and discretionary municipal decisions on extension requests; provisional confidence: moderate-high -- primary archival council-minute and newspaper sources directly record the connection/refusal decisions and their stated rationale, though the analysis is a qualitative historical case-comparison rather than a controlled exposure-comparator design.",
        "mechanism_family": "administrative_boundary_discretionary_extension_decision",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "planned_area_boundary_building_health_fire_codes",
        "institutional_context": "Swedish national building, fire-protection, and public-health codes applied only within a city's formally designated 'planned area'; adjoining working-class suburbs fell under separate rural-district administration exempt from these codes. Water-pipe extension requests from suburbs were decided at the discretion of the Norrkoping Waterworks Board/City Council (which narrowly approved a fee-based 200-metre extension in 1886 after a contested debate citing epidemic fears and moral obligation) and the part-municipal Linkoping Water Company/City Council (which rejected Ladugardsbacke's request in 1881 and continued to deny it until 1921, even after the suburb's 1911 annexation), financed under a '10 percent rule' requiring projected fee revenue to exceed 10% of construction cost within 10 years.",
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
