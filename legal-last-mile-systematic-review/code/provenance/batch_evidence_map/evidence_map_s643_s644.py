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
        "S643",
        "historical-institutional case study",
        "moderate-high",
        "connection-subsidy policy and land-tenure barriers in informal settlements",
        "household formal water connection, coverage",
        "FALSE",
        "TRUE",
        "Uganda: 2004 NWSC connection policy; land-tenure/property-rights barriers",
        "National Water and Sewerage Corporation (NWSC); Kampala Water pro-poor branch",
    )
    add(
        "S644",
        "quantitative household survey with contingent-valuation experiment",
        "moderate",
        "centralized vs. decentralized water-service governance",
        "household willingness-to-pay, service-provider preference",
        "FALSE",
        "TRUE",
        "Nicaragua: Law of Municipalities art. 7; 2005-2015 National Water Strategy decentralization policy",
        "ENACAL (centralized national utility); Municipality of Leon",
    )

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmppath, DB)

    print("Appended 2 evidence_map rows. New total:", len(rows))


if __name__ == "__main__":
    main()
