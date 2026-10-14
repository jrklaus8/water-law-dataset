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
        "S623",
        "mixed-methods cross-sectional survey",
        "moderate-high",
        "lack of legal land documentation / building permit barring formal utility connection",
        "household connection / service coverage / sanitation access",
        "FALSE",
        "TRUE",
        "Ghana: municipal land-title and building-permit requirements",
        "Ghana Water Company Limited (GWCL)",
    )
    add(
        "S624",
        "qualitative case study",
        "high",
        "central-government service-centralization directive contravening statutory local-authority mandate",
        "service coverage / quantity / reliability / affordability / health outcomes",
        "FALSE",
        "TRUE",
        "Zimbabwe: Public Health Act, Urban Councils Act, ZINWA Act",
        "ZINWA (central government) vs. urban local authorities",
    )
    add(
        "S625",
        "qualitative multi-site case study",
        "high",
        "land-title/construction-permit requirement and municipal debt-conditionality barring/withdrawing formal connection",
        "household connection / affordability / water quality",
        "FALSE",
        "TRUE",
        "Slovakia: Constitution, EU Drinking Water Directive, Government Decree 354/2006",
        "municipal water authorities and private water companies",
    )
    add(
        "S626",
        "qualitative in-depth interview study",
        "moderate-high",
        "regulatory ban on self-supply (wells/boreholes) and informal vending",
        "coping-strategy availability / household water access",
        "FALSE",
        "TRUE",
        "Nigeria: Federal Capital Development Authority and Abuja Environmental Protection Board regulations",
        "Federal Capital Territory Water Board",
    )

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmppath, DB)

    print("Appended evidence_map rows for S623-S626. New total:", len(rows))


if __name__ == "__main__":
    main()
