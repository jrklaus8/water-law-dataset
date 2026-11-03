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
        "S609",
        "documentary_policy_review",
        "Chronological documentary/institutional policy review of 12 Indian national water supply policies (1949-2012) against 20 SDG-6-derived sustainability indicators; provisional confidence: moderate -- real government-reported city-level coverage/tariff/metering benchmark data corroborates the policy-gap analysis, but the study is a narrative indicator-based review rather than a quantitative causal test.",
        "water_metering_tariff_policy_gap_household_coverage",
        "service_coverage",
        "FALSE",
        "TRUE",
        "india_national_water_policy_1949_2012_tariff_metering_regulation",
        "National Water Policy (1987, revised 2002 and 2012), Five-Year Plan water programmes, and state/municipal tariff-setting authorities collectively achieved rising household water coverage (35% urban premise-level piped connection by 2014; 91.4% rural improved-water access by 2011) but none of the 12 national policies since 1949 has ever explicitly addressed water metering, and metered-connection extent varies sharply by city (15%-100%), with average unaccounted-for water loss of 20-50% nationally attributed to this institutional-framework gap.",
    )

    add(
        "S610",
        "qualitative",
        "Qualitative participatory-modeling study (14 stakeholder-elicited causal loop diagrams, merged into a validated collective model) of household water vulnerability in rural Alaska; provisional confidence: moderate -- real rate/consumption/hospitalization data corroborates stakeholder-identified regulatory mechanisms, but the causal-loop-diagram method captures stakeholder perception rather than a statistically tested exposure-outcome relationship.",
        "water_quality_regulation_funding_capital_cost_household_access",
        "affordability",
        "FALSE",
        "TRUE",
        "us_alaska_epa_water_quality_regulation_water_rights_permitting",
        "Federal/state water-quality regulation (EPA standards), water rights intake/outtake permitting, and state/federal operations-and-maintenance funding policy were identified by 14 water-policy stakeholders as key drivers of household water vulnerability in rural Alaska, with documented rate disparities of up to 10-fold between metered urban (Anchorage) and hauled rural (Eek) water, and rural households without piped water using barely a quarter of the WHO minimum daily standard.",
    )

    add(
        "S611",
        "mixed_methods",
        "Mixed-methods institutional analysis (2,450-municipality census cross-tabulation, 1950-2010, plus 15 official interviews, 2011-2013) of Mexico's decentralized drinking-water policy; provisional confidence: moderate-high -- concrete municipal-level connection-rate data is cross-tabulated against institutional-capacity indicators, but the author explicitly disclaims a causal-driver interpretation of the descriptive statistics.",
        "water_policy_decentralization_municipal_capacity_household_connection",
        "service_coverage",
        "FALSE",
        "TRUE",
        "mexico_1972_federal_waters_law_1976_1980s_decentralization_reform",
        "Mexico's 1976-1980s decentralization of water policy from the centralized 1972 Federal Waters Law to municipal-level responsibility, combined with a 17-requirement federal funding-proposal process (social, legal, technical), concentrates low household water-connection rates (<26% in 33% of municipalities) among low-technical-capacity, high-indigenous-population, high-dirt-floor-housing municipalities; in Oaxaca, only 10% of federal funding proposals were accepted due to unmet legal/technical requirements.",
    )

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(EM))
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmppath, EM)

    print("Appended", 3, "evidence_map rows: ['S609', 'S610', 'S611']")


if __name__ == "__main__":
    main()
