#!/usr/bin/env python3
import csv, os, tempfile

DB = "05_analysis/descriptive/evidence_map.csv"


def main():
    with open(DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    existing_ids = {r["study_id"] for r in rows}

    def add(sid, design_class, evidence_level, mech_family, outcome_family, quant, qual, legal_ctx, inst_ctx):
        assert sid not in existing_ids, f"{sid} already exists"
        rows.append({
            "study_id": sid,
            "study_design_class": design_class,
            "evidence_level": evidence_level,
            "mechanism_family": mech_family,
            "outcome_family": outcome_family,
            "quantitative_synthesis_eligible": quant,
            "qualitative_synthesis_eligible": qual,
            "legal_context": legal_ctx,
            "institutional_context": inst_ctx,
        })

    add(
        "S627",
        "qualitative field study",
        "moderate-high",
        "weak/non-existent regulatory enforcement of WASH standards in public spaces",
        "facility water-supply/toilet-provision coverage and service quality",
        "FALSE",
        "TRUE",
        "Nigeria: fragmented multi-agency WASH regulatory regime, 1999 Constitution right-to-water",
        "Akwa Ibom Water Company; local council; State Ministry of Environment (regulation/enforcement)",
    )
    add(
        "S628",
        "mixed-methods case study",
        "high",
        "government slum-notification/recognition status and inter-agency jurisdictional disputes",
        "service interruption / coverage / affordability / health outcomes",
        "FALSE",
        "TRUE",
        "India: Indian government slum-notification classification system",
        "Hyderabad Metropolitan Water Supply and Sewerage Board; Greater Hyderabad Municipal Corporation; Secunderabad Cantonment Board",
    )
    add(
        "S629",
        "qualitative ethnographic study",
        "moderate",
        "village-government O&M funding constraints, state infrastructure-program failure, school-district water-rationing rule",
        "household water consumption / access / quality",
        "FALSE",
        "TRUE",
        "United States: State of Alaska Village Safe Water program",
        "Newtok village government; Newtok school district; State of Alaska",
    )

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmppath, DB)

    print("Appended evidence_map rows for S627-S629. New total:", len(rows))


if __name__ == "__main__":
    main()
