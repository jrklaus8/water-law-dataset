import csv, os, tempfile

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/descriptive/evidence_map.csv"

def main():
    with open(DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    assert "S582" not in {r["study_id"] for r in rows}

    new_row = {
        "study_id": "S582",
        "study_design_class": "qualitative",
        "evidence_level": "Qualitative comparative case study (48 interviews plus field observations, 2018-2020) of hybrid public/private, formal/informal maintenance-and-repair labor relations in water supply across Nima (informal settlement) and Dodowa (peri-urban), Accra, Ghana. Documents GWCL's PURC/WRC-regulated maintenance mandate, the legality/illegality distinction for private and illegal connections and informal self-repair, household maintenance obligations, and the decentralized CWSA/WSMT community-management framework; provisional confidence: moderate-high -- triangulated interview/observation data across two contrasting neighborhoods with named legal-institutional actors, though descriptive/qualitative rather than a controlled exposure-comparator design.",
        "mechanism_family": "hybrid_public_private_maintenance_repair_legality",
        "outcome_family": "service_reliability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "gwcl_purc_wrc_regulatory_framework_cwsa_wsmt",
        "institutional_context": "GWCL is Ghana's state water provider for urban areas (Accra), regulated by PURC and WRC, while CWSA and community-level WSMTs govern decentralized peri-urban/rural water systems; households are formally responsible for maintaining private connections (usually outsourced to private plumbers), private plumbers routinely and often illegally repair public-network leaks and maintain illegal connections in informal settlements, and GWCL employees moonlight as private plumbers in peri-urban areas -- a hybrid public/private, formal/informal labor configuration that both sustains and contests the utility's regulatory authority over water-service maintenance and reliability.",
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
