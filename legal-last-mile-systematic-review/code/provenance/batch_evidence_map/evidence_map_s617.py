#!/usr/bin/env python3
import csv, os, tempfile

EM = "05_analysis/descriptive/evidence_map.csv"


def main():
    with open(EM, newline="", encoding="utf-8") as f:
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
        "S617",
        "cross_sectional_survey",
        "Cross-sectional questionnaire survey (100 households, 10 slums, 3 zones) of water supply for the urban poor in Rajshahi, Bangladesh; provisional confidence: moderate -- concrete household-level access/quantity/reliability data by slum, corroborated by documented corruption instances, but a descriptive composite performance index rather than a regression-based exposure-outcome link.",
        "unrecognized_settlement_status_illegal_connection_household_access",
        "service_quantity",
        "FALSE",
        "TRUE",
        "bangladesh_unrecognized_slum_legal_connection_eligibility_corruption",
        "Slum residents in Rajshahi lack the legal right to apply for formal water connections due to unrecognized settlement status, resulting in widespread informal/illegal pipeline connections tolerated but only occasionally monitored (4 of 10 slums monitored vs 6 never monitored), with documented institutional corruption (BDT 2000-3000 bribes for connection/tubewell placement); household water quantity (61% receive 10-20 L/person/day) and reliability (79% receive water only 4-8 hours/day) vary systematically by slum location and institutional-dimension performance.",
    )

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(EM))
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmppath, EM)

    print("Appended", 1, "evidence_map rows: ['S617']")


if __name__ == "__main__":
    main()
