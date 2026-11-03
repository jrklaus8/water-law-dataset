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
        "S616",
        "qualitative",
        "Qualitative case study (35 resident interviews/FGDs across 5 residential areas, plus municipal/utility official interviews) of a proposed prepaid water meter policy in Karoi, Zimbabwe; provisional confidence: moderate -- real revenue-collection data corroborates the billing-system context, but the PWM policy had not yet been implemented, so the analysis captures pre-implementation stakeholder perceptions rather than an observed exposure-outcome relationship.",
        "constitutional_right_to_water_prepaid_meter_disconnection_risk",
        "affordability",
        "FALSE",
        "TRUE",
        "zimbabwe_constitutional_right_to_water_prepaid_meter_policy_debate",
        "Karoi Town Council and ZINWA's proposed prepaid water meter (PWM) policy, which would automatically disconnect households unable to pre-pay, was framed by residents and officials as violating the Zimbabwean Constitution's right to water and the UN ICESCR human right to water; under the existing post-paid billing system, ZINWA collected only 8.2% of possible monthly revenue on average across 5 residential areas in 2018 (1.6%-26.8% by area).",
    )

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(EM))
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmppath, EM)

    print("Appended", 1, "evidence_map rows: ['S616']")


if __name__ == "__main__":
    main()
