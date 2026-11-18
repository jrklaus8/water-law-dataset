import csv, os, tempfile

EM = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/descriptive/evidence_map.csv"

def main():
    with open(EM, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    existing_ids = {r["study_id"] for r in rows}
    new_rows = []

    def add(sid, design_class, evidence_level, mech_family, outcome_family, quant, qual, legal_ctx, inst_ctx):
        assert sid not in existing_ids
        new_rows.append({
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
        "S605",
        "qualitative",
        ("Qualitative case study of the KENSUP Soweto East slum-upgrading partnership in Kibera, "
         "Nairobi, with an embedded 407-respondent community-priority field survey; provisional "
         "confidence: high -- a formally constituted community institution (SEC) is documented "
         "negotiating and securing concrete legal-tenure and infrastructure outcomes for a real "
         "population over a 15-year, well-documented process including litigation."),
        "formal_community_institution_negotiated_tenure_infrastructure",
        "primary_connection",
        "FALSE",
        "TRUE",
        "kenya_kensup_settlement_executive_committee",
        ("The Kenya Slum Upgrading Programme (KENSUP) established the Settlement Executive Committee "
         "(SEC) as a formally constituted, democratically elected community-institutional body with "
         "defined Terms of Reference; the SEC negotiated housing-unit pricing with government across a "
         "change in political administration, prevailed in a 2-year civil court case brought by "
         "structure owners, and ultimately secured legal property ownership plus water/sanitation "
         "infrastructure (K-WATSAN) for 822 families, allocated via a transparent public balloting "
         "process."),
    )

    add(
        "S606",
        "quantitative_observational",
        ("Panel fixed-effects regression (290 Chinese prefectural cities, 2008-2014) testing hukou "
         "household-registration status against pollution-treatment infrastructure provision; "
         "provisional confidence: high -- consistent, statistically significant coefficients across "
         "the main model and multiple robustness checks (lagged models, cross-sectional change model)."),
        "hukou_registration_status_infrastructure_exclusion",
        "service_coverage",
        "TRUE",
        "TRUE",
        "china_hukou_household_registration_system",
        ("China's household registration system (hukou) is a legal/administrative status ascribed at "
         "birth that determines eligibility for place-specific public services in a city; a "
         "de-facto social-identity-based governance regime holds local governments fiscally "
         "accountable only to officially registered ('local-hukou-holder') residents. A "
         "one-percentage-point increase in the temporary (hukou-unregistered) resident share of a "
         "city's population is associated with significantly lower per-capita wastewater and solid-"
         "waste treatment capacity (p<0.01), controlling for city and year fixed effects and economic/"
         "demographic covariates, across 290 cities and 7 years."),
    )

    add(
        "S607",
        "qualitative",
        ("Comparative documentary/policy review of community-based rural water management (CBWM) legal-"
         "recognition frameworks across Nicaragua, Honduras, and Costa Rica; provisional confidence: "
         "moderate-high -- concrete national registration-rate statistics are reported for all 3 "
         "countries, but the analysis does not directly link registration status to a measured "
         "household-level access outcome."),
        "cbwm_legal_recognition_registration_institutional_capacity",
        "service_coverage",
        "FALSE",
        "TRUE",
        "latin_america_rural_water_committee_legal_recognition_laws",
        ("Nicaragua's 2010 Special CAPS Law (Law 722), Honduras's 2003 General Framework Law for Water "
         "and Sanitation, and Costa Rica's 1939 Law of Associations (underlying the 1997-2000 CAARS-to-"
         "ASADA transformation) each formally recognize community-based rural water management "
         "organizations, but registration rates remain partial across all 3 countries (e.g. 30% of "
         "Nicaraguan CAPS registered within 5 years of Law 722; an estimated 40% of Costa Rican "
         "community water organizations operating outside the law as of 2015), and formal legal "
         "recognition alone does not resolve the financial/technical capacity deficits and institutional "
         "fragmentation that continue to constrain rural water service sustainability in all 3 cases."),
    )

    add(
        "S608",
        "qualitative",
        ("Multi-actor qualitative case study (282 community FGD participants + 33 Gram Panchayat heads + "
         "Block officials, 16 villages, West Bengal, India) of India's decentralized rural-water-"
         "governance framework; provisional confidence: moderate-high -- a specific, directly quoted "
         "instance of caste-based water-access exclusion and a documented discretionary funding-"
         "allocation pattern are linked to water-infrastructure-functionality outcomes across multiple "
         "villages, though descriptive/qualitative rather than a formal regression."),
        "decentralized_panchayat_governance_discretionary_allocation_caste_exclusion",
        "primary_connection",
        "FALSE",
        "TRUE",
        "india_panchayati_raj_decentralized_water_governance",
        ("India's three-tier Panchayati Raj decentralized rural-governance system, operationalized "
         "through the National Rural Drinking Water Programme (2009) and predecessor schemes, devolves "
         "water-infrastructure funding and implementation responsibility to Gram Panchayats, Panchayat "
         "Samitis, and Block/District administration. A documented instance of caste-based exclusion "
         "from a community handpump ('we are not allowed to collect water from the handpumps located "
         "in the area where the upper castes people live') and a discretionary pattern of funding "
         "favoring new-construction schemes over repair/maintenance (with pre-installation hydrogeological "
         "surveys 'completely overlooked') are linked to widespread hand-pump non-functionality and "
         "unequal water-point access across the 16 studied villages."),
    )

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(EM) or ".")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows + new_rows)
    os.replace(tmppath, EM)

    print(f"Appended {len(new_rows)} evidence_map rows: {[r['study_id'] for r in new_rows]}")

if __name__ == "__main__":
    main()
