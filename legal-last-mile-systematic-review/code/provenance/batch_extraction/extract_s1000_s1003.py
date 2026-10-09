#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/03_extraction/extracted_data/extraction_database.csv"
RESEARCHER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

def blank_row(fieldnames):
    return {k: "" for k in fieldnames}

def atomic_write(path, fieldnames, rows):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path))
    with os.fdopen(fd, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp, path)

with open(PATH, newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing_ids = {r["study_id"] for r in rows}
new_rows = []

# S1000 - R2E4979185A18 - Bakker, Kooy, Shofiani & Martijn 2008 - Jakarta governance failure
r = blank_row(fieldnames)
r.update({
    "study_id": "S1000",
    "citation": "Bakker K, Kooy M, Shofiani NE, Martijn E-J (2008). Governance Failure: Rethinking the Institutional Dimensions of Urban Water Supply to Poor Households. World Development.",
    "doi": "10.1016/j.worlddev.2007.09.015",
    "publication_year": "2008",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Indonesia",
    "subnational_unit": "Jakarta",
    "legal_system": "civil law",
    "urban_rural": "urban",
    "service_provider": "PAM Jaya (municipal water utility) under both public and private (post-1998) management",
    "regulatory_model": "'governance failure' institutional framework: utility governance norms, land-use policy, connection-fee/tariff policy, discriminatory connection policies, tenure/residency status requirements",
    "population": "poor households in Jakarta lacking networked water supply access",
    "sample_size": "household survey, archival research, GIS mapping, and interviews with water managers/officials/NGOs",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "eligibility": "TRUE",
    "fees": "TRUE",
    "documentation": "TRUE",
    "discretion": "TRUE",
    "institutional_fragmentation": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "affordability": "TRUE",
    "study_design": "mixed-methods case study (household survey, archives, GIS, interviews)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: original mixed-methods study directly linking institutional 'governance failure' "
        "-- utility governance norms, land-use/municipal decision-making, discriminatory connection-fee policies, "
        "and household tenure/residency status requirements -- to persistent low rates of networked water-supply "
        "connection among poor households in Jakarta, under both public and private utility management."),
    "source_document": "Bakker, Kooy, Shofiani & Martijn 2008, World Development (retrieved via Google Drive)",
    "section": "Sections 2-4: differentiation of access, governance failures pertaining to the utility, governance failures pertaining to households",
    "exact_location": "Throughout results sections",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: mixed-methods study developing and applying a "
        "'governance failure' institutional framework to Jakarta, documenting how utility governance norms, "
        "land-use policy, discriminatory tariff/connection-fee policies, and household tenure/residency status "
        "jointly create disincentives for connecting poor households to networked water supply, under both public "
        "and private utility management. Strong Family A/C match. NOT effect_sizes eligible: mixed-methods case "
        "study, no regression-based estimate. Extracted for record_id R2E4979185A18."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1001 - RAF43F1049CAC - Kooy & Bakker 2008 - Jakarta splintered networks
r = blank_row(fieldnames)
r.update({
    "study_id": "S1001",
    "citation": "Kooy M, Bakker K (2008). Splintered networks: The colonial and contemporary waters of Jakarta. Geoforum.",
    "doi": "10.1016/j.geoforum.2008.07.012",
    "publication_year": "2008",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Indonesia",
    "subnational_unit": "Jakarta (Batavia)",
    "legal_system": "civil law",
    "urban_rural": "urban",
    "service_provider": "colonial and postcolonial government water utility; private management from 1998",
    "regulatory_model": "colonial-era institutional classification of citizenship/race governing water infrastructure provision; postcolonial government 'modernization' projects; private-sector management from 1998",
    "population": "residents of Jakarta across the colonial and postcolonial periods, differentiated by class and (historically) race",
    "sample_size": "archival and interview-based historical case study",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "legal_status": "TRUE",
    "documentation": "TRUE",
    "institutional_fragmentation": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "study_design": "historical case study with archival and interview data",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: original archival/interview-based historical study directly linking colonial "
        "and postcolonial institutional 'governmentality' -- legal/administrative classification of urban "
        "citizens and water-infrastructure rationalities -- to the origins and sustained persistence of highly "
        "unequal, fragmented water-supply access in Jakarta, less than 50% of whose inhabitants the formal system "
        "reaches, a pattern the study shows was not significantly altered by 1998 private-sector management."),
    "source_document": "Kooy & Bakker 2008, Geoforum (retrieved via Google Drive)",
    "section": "Sections 2-4: colonial governmentality and the differentiation of water supply",
    "exact_location": "Throughout, esp. section 2 on fragmentation of access",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: archival/interview-based historical case study "
        "tracing colonial-era institutional/legal classification of urban citizens to the origins and sustained "
        "postcolonial persistence of highly unequal, fragmented water-supply access in Jakarta, unaltered by 1998 "
        "private-sector management. Extends the colonial-institutional-legacy inclusion precedent (Njoh & Akiwumi, "
        "S969). Strong Family A/C match. NOT effect_sizes eligible: qualitative historical case study, no "
        "regression-based estimate. Extracted for record_id RAF43F1049CAC."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1002 - R2E27CA42816D - Statman-Weil, Nanus & Wilkinson 2020 - SDWA compliance disparities
r = blank_row(fieldnames)
r.update({
    "study_id": "S1002",
    "citation": "Statman-Weil Z, Nanus L, Wilkinson N (2020). Disparities in community water system compliance with the Safe Drinking Water Act. Applied Geography.",
    "doi": "10.1016/j.apgeog.2020.102264",
    "publication_year": "2020",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "United States",
    "subnational_unit": "Pennsylvania",
    "legal_system": "common law",
    "urban_rural": "statewide (urban and rural community water systems)",
    "service_provider": "community water systems (CWS) of varying size and ownership",
    "regulatory_model": "U.S. Safe Drinking Water Act (1974, amended 1986/1996), EPA-enforced maximum contaminant levels and administrative rules",
    "population": "populations served by Pennsylvania community water systems, analyzed by race, socioeconomic status, system size, ownership and water source",
    "sample_size": "statewide community water system-level spatial/regression analysis (Pennsylvania)",
    "household_level": "FALSE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "enforcement": "TRUE",
    "documentation": "TRUE",
    "service_area": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_quality": "TRUE",
    "effect_measure": "negative binomial regression coefficient",
    "model_type": "negative binomial regression",
    "adjusted_or_unadjusted": "adjusted",
    "covariates": "system size, ownership, water source, sociodemographic characteristics (race, SES) estimated via spatial analysis methods",
    "study_design": "quantitative spatial/regression analysis",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: original quantitative regression study directly testing whether sociodemographic "
        "and institutional/system characteristics predict community water systems' compliance with the Safe "
        "Drinking Water Act, a specific federal legal/regulatory framework, finding small (<200 connections) and "
        "rural systems significantly less likely to comply, independent of race/SES."),
    "source_document": "Statman-Weil, Nanus & Wilkinson 2020, Applied Geography (retrieved via Google Drive)",
    "section": "Results on negative binomial regression of SDWA violations",
    "exact_location": "Regression results section",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: quantitative negative-binomial-regression study of "
        "disparities in community water systems' compliance with the U.S. Safe Drinking Water Act (Pennsylvania), "
        "finding small and rural systems significantly less likely to comply with this legal/regulatory framework, "
        "independent of race or socioeconomic status. Strong Family A/C match (institutional/administrative "
        "capacity and legal-compliance-linked access/quality outcome). Provisionally NOT added to effect_sizes: "
        "the regression isolates system-characteristic (not a legal/institutional-reform) predictors of regulatory "
        "violations rather than a water-access outcome per the strict Family A/B/C framework; flagged for review "
        "at the analysis stage. Extracted for record_id R2E27CA42816D."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1003 - RAE2EE524BC5B - Anand 2007 - Right to water and access assessment
r = blank_row(fieldnames)
r.update({
    "study_id": "S1003",
    "citation": "Anand PB (2007). Right to water and access to water: an assessment. Journal of International Development.",
    "doi": "10.1002/jid.1386",
    "publication_year": "2007",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "cross-national comparative (countries with and without a promulgated right to water)",
    "subnational_unit": "national-level comparison",
    "legal_system": "mixed (comparative across common law and civil law jurisdictions)",
    "urban_rural": "national",
    "service_provider": "national water-sector institutions across compared countries",
    "regulatory_model": "formal legal promulgation of a right to water (Hohfeldian rights framework: powers, privileges, claims, immunities) versus absence of such a right; governance-quality indicators (Governance Matters V)",
    "population": "poor populations across a small sample of countries with and without a legally promulgated right to water",
    "sample_size": "small cross-country comparative sample using WHO-UNICEF JMP and Governance Matters V datasets",
    "household_level": "FALSE",
    "community_level": "TRUE",
    "legal_status": "TRUE",
    "eligibility": "TRUE",
    "documentation": "TRUE",
    "enforcement": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "study_design": "cross-country comparative analysis using secondary datasets",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: original comparative empirical analysis directly testing, with cross-country "
        "WHO-UNICEF JMP access data and Governance Matters V governance indicators, whether legal promulgation of "
        "a right to water is associated with improved water access, finding that broader governance mechanisms "
        "matter more than the formal legal right's articulation alone."),
    "source_document": "Anand 2007, Journal of International Development (retrieved via Google Drive)",
    "section": "Empirical analysis of right-to-water promulgation and access outcomes",
    "exact_location": "Throughout results sections",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: comparative empirical study applying a Hohfeldian "
        "legal-rights framework to cross-country access and governance data, directly testing whether formal legal "
        "promulgation of a right to water improves water access, finding governance mechanisms matter more than "
        "the right's formal articulation. Strong Family A match. NOT effect_sizes eligible: descriptive cross-"
        "country comparative analysis, no locatable regression-based point estimate isolating the legal "
        "mechanism's effect. Extracted for record_id RAE2EE524BC5B."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

for r in new_rows:
    assert r["study_id"] not in existing_ids, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"extraction_database.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
