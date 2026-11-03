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
        "S622",
        "descriptive case study / NGO program evaluation",
        "moderate-high",
        "informal/illegal settlement legal status barring formal service extension",
        "household water/sanitation access, formal connection refusal, self-provision",
        "FALSE",
        "TRUE",
        "India: township authority land-zoning/illegal-settlement classification",
        "NOIDA Authority (state-appointed township authority); NGO-facilitated community self-provision (CURE)",
    )

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmppath, DB)

    print("Appended evidence_map row for S622. New total:", len(rows))


if __name__ == "__main__":
    main()
