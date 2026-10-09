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
        "S630",
        "qualitative case study",
        "moderate-high",
        "mandatory self-supply regulation shifting water-provision responsibility to households",
        "household water access, quantity, reliability",
        "FALSE",
        "TRUE",
        "India: Mumbai mandatory rainwater-harvesting ordinance (2003/2007)",
        "Municipal Corporation of Greater Mumbai (MCGM/BMC)",
    )
    add(
        "S631",
        "quasi-experimental panel study (DiD/dynamic GMM)",
        "high",
        "administrative jurisdiction-splitting (local government proliferation)",
        "household water/sanitation access percentage",
        "TRUE",
        "TRUE",
        "Indonesia: post-2001 decentralization, pemekaran administrative-splitting process",
        "kabupaten/kota local district governments",
    )
    add(
        "S632",
        "mixed-methods case study",
        "moderate-high",
        "water-sector privatization contravening statutory state-responsibility mandate",
        "household connection / coverage / affordability / service quality",
        "FALSE",
        "TRUE",
        "Cameroon: Law 98/005 (1998 water law), Law 762/PJL/AN 2004 (decentralization)",
        "CamWater (parastatal); CDE (private operator); local councils",
    )

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmppath, DB)

    print("Appended evidence_map rows for S630-S632. New total:", len(rows))


if __name__ == "__main__":
    main()
