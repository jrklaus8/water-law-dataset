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
        "S593",
        "quantitative_observational",
        ("Cross-sectional Tobit-regression study (152 South Korean local governments, 2010/2016/2021) testing "
         "administrative-district classification, municipal fiscal autonomy, and local tax burden as determinants "
         "of a Coulter distributional-inequity coefficient across 6 water-service-equity variables; provisional "
         "confidence: high -- consistent, statistically significant coefficients replicated across all 3 study "
         "years and 6 outcome variables, confirmed by a multiple-regression robustness check."),
        "administrative_classification_fiscal_autonomy_service_equity",
        "primary_connection",
        "TRUE",
        "TRUE",
        "administrative_district_classification_municipal_fiscal_autonomy",
        ("South Korea's si (urban-type) vs. gun (rural-type) administrative district classification, and "
         "municipal fiscal autonomy (degree of financial independence) and local tax burden, are institutional/"
         "fiscal-governance variables tested via Tobit regression against a distributional-equity outcome for "
         "6 water-service variables (price, cost-recovery rate, revenue-water ratio, coverage rate, staffing, "
         "customer satisfaction) across 152 local governments and 3 years. Administrative district classification "
         "and local tax burden improve equity; financial independence (own-source revenue autonomy) worsens it, "
         "controlling for mayoral re-election and utility operational structure."),
    )

    add(
        "S594",
        "qualitative",
        ("Ethnographic/semi-structured-interview study (46 older-adult participants, 2016-2018) documenting "
         "legal-institutional mechanisms of the Flint, Michigan water crisis; provisional confidence: high -- "
         "primary interviews with directly affected residents document concrete statutory and court-ordered "
         "mechanisms shaping household water access and safety."),
        "emergency_manager_law_court_ordered_remediation",
        "service_quality",
        "FALSE",
        "TRUE",
        "michigan_emergency_manager_law_consent_decree",
        ("Michigan's Local Financial Stability and Choice Act (Emergency Manager law, Public Act 436) suspended "
         "Flint's local democratic control, enabling the 2014 switch to an inadequately treated water source; "
         "subsequent state/federal water-safety emergency declarations and a court-ordered consent decree "
         "(Concerned Pastors for Social Action v. Khouri) imposed a binding deadline for lead-service-line "
         "replacement. Older-adult residents describe navigating distribution sites, safety-declaration distrust, "
         "and the administrative burdens of the replacement process as compounding pre-existing vulnerability."),
    )

    add(
        "S595",
        "qualitative",
        ("Qualitative case study (10 households + 3 officials) of rights-based water governance during Cape "
         "Town's 2017-2018 Day Zero drought crisis; provisional confidence: high -- primary interviews with "
         "both affected households and municipal officials document concrete constitutional, litigated, and "
         "rationing-device mechanisms."),
        "constitutional_right_rationing_device_settlement_classification",
        "service_quantity",
        "FALSE",
        "TRUE",
        "south_african_constitutional_water_right_free_basic_water",
        ("South Africa's constitutional right to sufficient water (section 27) and Free Basic Water policy "
         "(6kl/household/month) were litigated as inadequate in Mazibuko v. City of Johannesburg; during Day "
         "Zero, prepaid Water Management Devices (flow-restricting meters) were installed disproportionately "
         "in low-income/informal Khayelitsha, enforcing rationing not equally applied elsewhere, while formal "
         "vs. informal settlement classification determined eligibility for a full individual metered connection "
         "versus shared standpipes."),
    )

    add(
        "S596",
        "quasi_experimental",
        ("Mixed-methods comparative study (150-household survey + 9 FGDs/12 IDIs/3 KIIs) of 3 Dhaka slums, "
         "2 with legal DWASA connections and 1 with an illegal connection, exploiting a natural comparison by "
         "legal-connection status; provisional confidence: high -- clean cross-slum comparison with large, "
         "consistent price/consumption/security disparities tied directly to legal connection status."),
        "land_title_connection_requirement_tenure_insecurity",
        "affordability",
        "TRUE",
        "TRUE",
        "dwasa_land_title_connection_requirement_eviction",
        ("Dhaka WASA's water-connection requirement is conditioned on land title/ownership and an approved "
         "building plan, excluding tenure-insecure slum residents from legal connection; Bangladesh's National "
         "Water Policy (1999), Water Act (2013), and Water Rules (2018) declare a right to water without an "
         "enforceable implementation protocol. The frequently-evicted, illegally-connected Tejgaon slum pays "
         "17x the water price, spends 8% of income on water (vs. 0.5-2.0% in the legally-connected slums), and "
         "has the highest Water Security Index (most insecure) of the 3 slums studied."),
    )

    add(
        "S597",
        "qualitative",
        ("Qualitative content-analysis study (257 interviewees, household surveys, FGDs, 4 villages) of "
         "community-led total sanitation (CLTS) program abandonment in rural Burkina Faso, with a natural "
         "single-actor-unsubsidized-province vs. dual-approach-provinces contrast; provisional confidence: "
         "moderate-high -- systematic frequency-coded attribution of abandonment causes to a named "
         "governance/institutional category, but outcome measure is categorical/frequency-based rather than "
         "a formal regression."),
        "clts_policy_ambiguity_institutional_coordination_failure",
        "service_coverage",
        "FALSE",
        "TRUE",
        "burkina_faso_clts_national_guide_subsidy_policy_ambiguity",
        ("Burkina Faso's 2014 national CLTS implementation guide permits a hybrid subsidized/unsubsidized "
         "approach, applied inconsistently across adjoining villages, undermining community acceptance; "
         "inadequate agent training, agent transfers, and inter-agency coordination failure within the "
         "Ministry of Water and Sanitation are cited by content analysis as governance factors in 26.28% of "
         "CLTS-implementation-abandonment cases (787 of 3,546 triggered villages nationally, 22.19% "
         "abandonment rate). Sissili province, the only province using a single actor and the original "
         "unsubsidized approach, achieved 100% open-defecation-free certification with zero abandonments."),
    )

    add(
        "S598",
        "quantitative_observational",
        ("Population-based cross-sectional study (548 households, binary logistic regression) in Osun State, "
         "Nigeria, directly testing a donor-funded (EU/African Development Bank) WASH institutional and "
         "governance reform program as an exposure against household water security; provisional confidence: "
         "moderate -- the institutional-reform variable is tested at the contextual/study-area level rather than "
         "as an individual household-level exposure with a formal coefficient, though wealth and sanitation-"
         "facility-access predictors are individually modeled."),
        "wash_institutional_reform_donor_program_household_security",
        "service_reliability",
        "TRUE",
        "TRUE",
        "nigeria_fmwr_regulatory_framework_eu_afdb_wash_reform",
        ("Nigeria's Federal Ministry of Water Resources regulatory framework and outdated draft National Water "
         "Supply and Sanitation Policy set a 100-meter maximum-distance-to-source planning standard, though "
         "government agencies and donors use 350 meters in practice. An EU/African Development Bank-funded "
         "WASH institutional and governance reform program was directly tested as an exposure against "
         "household water security (548 households); the study concludes the reform program did not "
         "significantly influence water security, while wealth and improved household toilet facilities "
         "were significant predictors."),
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
