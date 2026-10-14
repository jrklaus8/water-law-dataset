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
        "S614",
        "case_study",
        "Case-study census (98 mechanised boreholes, 89 operator interviews, 2,439 water-user interviews) of informal vs formal water provision in Sunyani West District, Ghana; provisional confidence: moderate-high -- near-complete census of the district's mechanised-borehole population with standardized CWSA service indicators, but a descriptive rather than regression-based exposure-outcome link.",
        "informal_illegal_water_provider_legal_status_household_access",
        "service_reliability",
        "FALSE",
        "TRUE",
        "ghana_water_resources_commission_groundwater_permitting_cwsa_regulation",
        "Privately managed mechanised boreholes in Sunyani West District operate in explicit, unenforced violation of Ghana's Water Resources Commission groundwater-abstraction permitting (L.I. 1692) and CWSA/District Authority approval requirements, yet achieve high reliability (91/93 boreholes functional >=347 days/year), adequate quantity (>=25 L/capita/day), and comparable tariffs to formally regulated GWCL standpipes, filling access gaps left by formal providers.",
    )

    add(
        "S615",
        "cross_sectional_survey",
        "Cross-sectional household survey (108 households, 6 villages, 3 districts) of community-based water management under Cameroon's 1998 water law; provisional confidence: moderate -- concrete per-village consumption/access data, but a descriptive comparison of means with no reported significance test and small per-village samples (n=18).",
        "cbwm_legal_authorization_wmc_eligibility_household_connection_type",
        "service_quantity",
        "FALSE",
        "TRUE",
        "cameroon_1998_water_law_community_based_water_management_authorization",
        "Cameroon's 1998 water law authorized community groups to manage their own rural water systems (CBWM) where centralized utilities CAMWATER/CDE do not reach; Water Management Committee-set upfront cash-eligibility and monthly-fee requirements determine private (34% of households, 35.6 L/capita/day) vs communal-tap (66%, 24.7 L/capita/day) access, with 71 of 108 households unable to afford connection fees and sanctions imposed on non-contributors.",
    )

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(EM))
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmppath, EM)

    print("Appended", 2, "evidence_map rows: ['S614', 'S615']")


if __name__ == "__main__":
    main()
