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
        "S620",
        "cross-sectional survey (logistic regression)",
        "moderate",
        "institutional/municipal vs. private water-supply arrangement (payment-amount proxy), location-based differential institutional coverage",
        "household drinking-water access (piped supply, sufficiency, daily availability, quality)",
        "FALSE",
        "TRUE",
        "India: 73rd/74th Constitutional amendments (urban/rural local bodies)",
        "municipal/institutional water supply vs. private suppliers vs. individual tube wells",
    )
    add(
        "S621",
        "mixed-methods comparative case study",
        "moderate",
        "public-private-community institutional partnership model for water treatment service delivery (panchayat resolutions, tripartite agreements, village development councils)",
        "service coverage / quantity / affordability / inclusiveness",
        "FALSE",
        "TRUE",
        "India: panchayati raj institutional framework",
        "gram panchayat, private/NGO foundations (Byrraju, Naandi, Sai Oral Health), government RWSSD",
    )

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmppath, DB)

    print("Appended evidence_map rows for S620, S621. New total:", len(rows))


if __name__ == "__main__":
    main()
