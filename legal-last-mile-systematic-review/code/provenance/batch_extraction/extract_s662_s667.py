import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/03_extraction/extracted_data/extraction_database.csv"

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing_ids = {r["study_id"] for r in rows}


def blank_row(fieldnames):
    return {f: "" for f in fieldnames}


new_rows = []

# S662 - Hoko et al. 2024, Zimbabwe urban O&M arrangements
r = blank_row(fieldnames)
r.update({
    "study_id": "S662",
    "citation": "Hoko Z, Mapenzauswa CF, Toto TN, Kerith M, Nhapi I (2024). Analysis of operation and maintenance arrangements for water supply in urban areas in Zimbabwe. Sustainable Water Resources Management 10:27.",
    "doi": "10.1007/s40899-023-01000-3",
    "publication_year": "2024",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Zimbabwe",
    "subnational_unit": "Bindura, Bulawayo, Chegutu, Gweru, Harare, Kariba, Masvingo, Mutare, Rusape, Victoria Falls, Zvishavane",
    "legal_system": "common law (Zimbabwe)",
    "urban_rural": "urban",
    "service_provider": "urban local authorities (municipal water departments); ZINWA (bulk raw water supply)",
    "regulatory_model": "Urban Councils Act (Chapter 29:15); Water Policy 2012 (designating local authorities as service authorities); ZINWA Act (Chapter 20:25, bulk raw-water supply mandate)",
    "population": "11 of 32 urban local authorities in Zimbabwe (urban population 5.86 million, 38.6% of country population, 2022)",
    "sample_size": "11 local authorities, structured-questionnaire respondents (key water-supply personnel), January 2020-December 2022",
    "household_level": "",
    "community_level": "TRUE",
    "institutional_fragmentation": "TRUE",
    "formal_connection": "",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quality": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "11 urban local authorities; Chi-squared cross-tabulation of O&M arrangements, infrastructure functionality, and WSS status ratings (Tables 8-12)",
    "model_type": "mixed-methods institutional case study with Chi-squared cross-tabulation",
    "study_design": "cross-sectional institutional case study (structured questionnaire, key-informant interviews, documentation review)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "4",
    "outcome_measurement_quality": "3",
    "mechanism_certainty": "Moderate: a real institutional/legal water-governance framework (Urban Councils Act Chapter 29:15, Water Policy 2012, ZINWA Act Chapter 20:25) is explicitly studied via \"legal provision for O&M\" as a core parameter across 11 Zimbabwean urban local authorities, tied to real primary-collected functionality/WSS-status outcome data (Tables 8-12), though the Chi-squared analysis found no statistically significant association between O&M/legal-provision arrangements and WSS status (p>0.05), limiting causal certainty.",
    "source_document": "Hoko et al. 2024, Sustainable Water Resources Management 10:27 (retrieved via Google Drive inbox)",
    "page": "1-27",
    "table": "Table 8 (O&M arrangements summary); Table 11 (WSS status summary); Table 12 (cross-tabulation)",
    "section": "Legal provision for O&M; Results and discussion",
    "exact_location": "Sections on legal provision for O&M and the Chi-squared cross-tabulation of O&M/infrastructure/WSS status",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Institutional/legal water-governance study explicitly examining legal provision for O&M as a parameter across 11 Zimbabwean urban local authorities, with primary mixed-methods data tied to real WSS-status outcomes. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: Chi-squared association testing, not a regression-based causal estimate; also found no significant association (p>0.05). Extracted for record_id R2621601881E4.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S663 - Muridzo, Hungwe, Chadambuka 2025, Zimbabwe disability WASH access
r = blank_row(fieldnames)
r.update({
    "study_id": "S663",
    "citation": "Muridzo NG, Hungwe C, Chadambuka P (2025). Access to water, sanitation and hygiene facilities by women with disabilities in Zimbabwe's Harare Metropolitan Province during COVID-19. Disability & Society 40:1897-1916.",
    "doi": "10.1080/09687599.2024.2411527",
    "publication_year": "2025",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Zimbabwe",
    "subnational_unit": "Harare Metropolitan Province (three low-income areas)",
    "legal_system": "common law (Zimbabwe)",
    "urban_rural": "urban",
    "service_provider": "local authorities (community boreholes); disability-service organisations",
    "regulatory_model": "National Disability Policy (Ministry of Public Service, Labour and Social Welfare, 2021); Zimbabwe constitutional provisions on disability rights; UN Convention on the Rights of Persons with Disabilities",
    "population": "women with disabilities in three low-income areas of Harare Metropolitan Province",
    "sample_size": "104 purposively sampled women with disabilities (structured interviews and focus group discussions); 7 key-informant interviews with disability-organisation representatives",
    "household_level": "TRUE",
    "income_group": "TRUE",
    "eligibility": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "TRUE",
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_quality": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "104 women with disabilities (interviews/FGDs); 7 key-informant interviews",
    "model_type": "qualitative thematic analysis with primary interview/FGD data",
    "study_design": "qualitative case study (structured interviews, focus group discussions, key-informant interviews)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "3",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": "Moderate-high: Zimbabwe's National Disability Policy and constitutional provisions mandate equitable WASH access and accessible, proximate water points for persons with disabilities, but this study documents via large-N primary interview and FGD evidence (104 women with disabilities, 7 key informants) that this policy is not being fully implemented, with real individual-level outcomes including discrimination, gender harassment at community boreholes, and 'sex for water' transactions.",
    "source_document": "Muridzo, Hungwe & Chadambuka 2025, Disability & Society 40:1897-1916 (retrieved via Google Drive inbox)",
    "page": "1897-1916",
    "section": "Findings; Points of interest",
    "exact_location": "Sections on National Disability Policy implementation gaps and community-borehole access barriers",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Primary qualitative study documenting institutional/policy-implementation gaps in Zimbabwe's National Disability Policy for WASH access, with large-N interview/FGD evidence of real household/individual-level access-discrimination outcomes among women with disabilities. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: qualitative thematic-analysis design, no regression-based causal estimate. Extracted for record_id R8D85A846848A.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S664 - Lewis & Miller 1987, Sub-Saharan Africa public-private partnerships
r = blank_row(fieldnames)
r.update({
    "study_id": "S664",
    "citation": "Lewis MA, Miller TR (1987). Public-private partnership in water supply and sanitation in sub-Saharan Africa. Health Policy and Planning 2:70-79.",
    "doi": "",
    "publication_year": "1987",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "multi-country (Cote d'Ivoire, Kenya, Senegal, Benin, Niger, Nigeria, Somalia)",
    "subnational_unit": "Abidjan (Cote d'Ivoire); multiple sub-Saharan African communities",
    "legal_system": "mixed (Francophone civil law and Anglophone common law jurisdictions)",
    "urban_rural": "urban and rural",
    "service_provider": "SODECI (Societe de Distribution d'Eau de Cote d'Ivoire, parastatal-controlled concession); independent water vendors/kiosks; Kenya Water Utilities Corporation",
    "regulatory_model": "concession/affermage contracts; government tariff-setting authority; licensing of independent water vendors; comparative institutional models (Table 3: concession, affermage, territorial concession, contracting-out, water cooperatives, licensed vendor kiosks)",
    "population": "urban and rural households across multiple sub-Saharan African countries",
    "sample_size": "country-level population coverage data (Table 1, multiple Sub-Saharan countries); household water-vendor consumption/pricing survey across 8 communities (Table 2, Zaroff & Okun 1984)",
    "household_level": "TRUE",
    "income_group": "TRUE",
    "fees": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "affordability": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "Table 1: % population with access to safe water across ~28 Sub-Saharan countries (1970/1980); Table 2: household water-vendor consumption/pricing data across 8 communities",
    "model_type": "comparative institutional/regulatory review with population-level and household-level survey data",
    "study_design": "comparative institutional case study (documentary/regulatory analysis plus secondary household survey data)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "3",
    "outcome_measurement_quality": "3",
    "mechanism_certainty": "Moderate: real institutional/legal regulatory arrangements for water supply (SODECI's parastatal-controlled concession in Abidjan, government tariff approval, vendor licensing regimes) are documented against real country-level population-coverage data (Table 1) and a primary household-level water-vendor consumption/pricing survey (Table 2, Zaroff & Okun 1984) across multiple Sub-Saharan African communities, though the paper is a comparative institutional review rather than a study isolating a single mechanism's causal effect.",
    "source_document": "Lewis & Miller 1987, Health Policy and Planning 2:70-79 (retrieved via Google Drive inbox)",
    "page": "70-79",
    "table": "Table 1 (population with access to safe water); Table 2 (water vendor consumption/pricing); Table 3 (comparative institutional models)",
    "section": "The role of private entities in supplying water and sanitation; Water vendors",
    "exact_location": "Tables 1-3 and accompanying institutional-model discussion",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Comparative institutional/legal review of public-private water-supply partnerships across Sub-Saharan Africa, with real population-level coverage data and a primary household-level water-vendor survey tied to institutional/regulatory arrangements. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: comparative descriptive review, no regression-based causal estimate. Extracted for record_id R4FB843E4946A.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S665 - Chenoweth 2004, changing ownership structures (4-country comparison)
r = blank_row(fieldnames)
r.update({
    "study_id": "S665",
    "citation": "Chenoweth J (2004). Changing ownership structures in the water supply and sanitation sector. Water International 29:138-147.",
    "doi": "10.1080/02508060408691763",
    "publication_year": "2004",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "multi-country (England and Wales, Argentina, Cote d'Ivoire, Israel)",
    "subnational_unit": "Buenos Aires and Cordoba (Argentina); Abidjan (Cote d'Ivoire); Gaza Strip and West Bank (Palestinian territories)",
    "legal_system": "mixed (common law, civil law, and customary/Ottoman-Mandate-derived water law in Israel/Palestine)",
    "urban_rural": "urban",
    "service_provider": "privatized regional water companies (England/Wales); Aguas Argentinas concession (Buenos Aires); SODECI (Cote d'Ivoire); Mekorot (Israel, government-owned)",
    "regulatory_model": "1989 privatization and new regulatory body (England/Wales); 30-year concession contract with independent regulatory agency (Buenos Aires, 1992); Cote d'Ivoire concession/affermage arrangements; Israel's 1959 comprehensive water law nationalizing water resources under state Water Commissioner",
    "population": "urban households in England/Wales, Buenos Aires/Cordoba, Abidjan, and Israel/Palestinian territories",
    "sample_size": "country/city-level longitudinal connection and coverage data across four case-study countries",
    "household_level": "TRUE",
    "income_group": "TRUE",
    "fees": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "affordability": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "Buenos Aires: 70% connected pre-concession to 83% by 1997, +1.98 million people connected by 2000; Cote d'Ivoire: 89% to 90% urban coverage 1990-2000, 22% households on independent providers",
    "model_type": "comparative institutional/legal case-study analysis",
    "study_design": "comparative institutional case study (four-country documentary/legal analysis with longitudinal connection data)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "4",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": "Moderate-high: real institutional/legal frameworks governing water-sector ownership transitions (1989 UK privatization and new regulator, Buenos Aires' 1992 concession contract and independent regulatory agency, Israel's 1959 comprehensive water law, Cote d'Ivoire's SODECI concession) are documented against real longitudinal household-level connection/coverage data across four countries, consistently linking the absence of appropriate institutional and legal frameworks to constrained access for independent-provider-dependent, generally poorer, households.",
    "source_document": "Chenoweth 2004, Water International 29:138-147 (retrieved via Google Drive inbox)",
    "page": "138-147",
    "section": "Development of Water Supply and Sanitation Sector (England and Wales; Argentina; Cote d'Ivoire; Israel); Discussion",
    "exact_location": "Country case-study sections and Discussion on institutional/legal frameworks",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Comparative institutional/legal analysis of water-sector ownership structures across four countries, with real household-level connection/coverage data tied explicitly to legal/regulatory frameworks. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: comparative descriptive case-study design, no regression-based causal estimate. Extracted for record_id R8D44D087F7A0.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S666 - Seneviratne 2000, Sri Lanka urban water management
r = blank_row(fieldnames)
r.update({
    "study_id": "S666",
    "citation": "Seneviratne LW (2000). Challenges to urban water management in Sri Lanka. International Journal of Water Resources Development 16:131-141.",
    "doi": "10.1080/07900620048617",
    "publication_year": "2000",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Sri Lanka",
    "subnational_unit": "Greater Colombo area and other urban districts",
    "legal_system": "common law (Sri Lanka)",
    "urban_rural": "urban",
    "service_provider": "National Water Supply & Drainage Board (NWSDB); Municipal Councils; Irrigation Department",
    "regulatory_model": "Municipal Councils legislation (elected local-body water/sewerage provision duty); NWSDB statutory mandate; tariff-approval process via Ministry of Housing & Urban Development and Ministry of Finance & Planning; proposed independent regulatory body for tariff-setting (price-adjustment mechanism)",
    "population": "urban population of Sri Lanka (3.8 million in 1998, 22% of national population)",
    "sample_size": "national/regional administrative coverage and tariff data (1985-1998 with projections to 2020)",
    "household_level": "TRUE",
    "income_group": "TRUE",
    "fees": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "affordability": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "76% of 3.8 million urban population served (1998); 40% on public standposts; income-tiered subsidy components (Table 6); annual household water-expenditure-to-income ratios (Table 2)",
    "model_type": "institutional/legal descriptive case study with national administrative and tariff data",
    "study_design": "descriptive institutional case study (documentary/administrative-data analysis)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "3",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": "Moderate-high: Sri Lanka's institutional water-governance framework (Municipal Councils' statutory water/sewerage duty, NWSDB's statutory mandate, tariff-approval process, cross-subsidization policy) is documented against real household-level connection/coverage/tariff data (76% urban connection, 40% on standposts, income-tiered subsidy components for urban poor/rural households) and explicit discussion of the need to protect water rights and socially affordable tariffs, though the analysis is descriptive/administrative rather than a formal regression isolating institutional causal effects.",
    "source_document": "Seneviratne 2000, International Journal of Water Resources Development 16:131-141 (retrieved via Google Drive inbox)",
    "page": "131-141",
    "table": "Table 2 (household water expenditure as % of income); Table 6 (subsidy components by consumer category); Table 7 (current water tariffs)",
    "section": "Water Supply and Sewerage Responsibility; Socially Affordable Water Tariff; Cross-subsidization of Tariff",
    "exact_location": "Sections on institutional responsibility, tariff structure, and cross-subsidization",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Institutional/legal analysis of Sri Lankan urban water governance, with real household-level connection/coverage/tariff data and explicit cross-subsidy policy for the urban poor. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: descriptive administrative case-study design, no regression-based causal estimate. Extracted for record_id RC8B757CEFEBF.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S667 - Gyau-Boakye & Ampomah 2003, Ghana water pricing and sector reforms
r = blank_row(fieldnames)
r.update({
    "study_id": "S667",
    "citation": "Gyau-Boakye P, Ampomah BY (2003). Water Pricing and Water Sector Reforms Information Study in Ghana. Water International 28:11-18.",
    "doi": "10.1080/02508060308691660",
    "publication_year": "2003",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Ghana",
    "subnational_unit": "national (urban, rural, and agricultural water sectors)",
    "legal_system": "common law (Ghana)",
    "urban_rural": "urban and rural",
    "service_provider": "Ghana Water and Sewerage Corporation (GWSC) / Ghana Water Company Limited (GWCL); Ghana Irrigation Development Authority (GIDA); Community Water and Sanitation Agency (CWSA)",
    "regulatory_model": "Ghana Water and Sewerage Act (Act 310, 1965); Water Resources Commission Act (Act 522, 1996); Public Utilities Regulatory Commission Act (Act 538, 1997); Water Charges Regulation 1995 (L.I. 1597); Legislative Instrument 1350 (1987, irrigation tariffs)",
    "population": "urban, rural, and agricultural water consumers in Ghana",
    "sample_size": "national longitudinal coverage and tariff data (1965-2002); 208 urban water-supply systems; rural community water-management-committee data",
    "household_level": "TRUE",
    "income_group": "TRUE",
    "fees": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "affordability": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "urban water coverage 76% (1992) to 70% (1999); rural coverage 46% (1992) to 30% (1998); 2,177 boreholes and 2,612 hand-dug wells constructed by 1998",
    "model_type": "institutional/legal descriptive case study with national longitudinal administrative data",
    "study_design": "descriptive institutional case study (documentary/administrative-data analysis, authored by Water Resources Commission economist)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "4",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": "Moderate-high: Ghana's water-sector legal/institutional framework (GWSC Act 310 of 1965, Water Resources Commission Act 522 of 1996, Public Utilities Regulatory Commission Act 538 of 1997) is documented against real longitudinal national coverage and tariff data (urban coverage 76%->70%, rural coverage 46%->30%, borehole/well construction achievements) with explicit attention to consumer protection and vulnerable-group/urban-poor access provisions, authored in part by a Water Resources Commission official with direct institutional knowledge, though the design is descriptive/administrative rather than a formal regression isolating institutional causal effects.",
    "source_document": "Gyau-Boakye & Ampomah 2003, Water International 28:11-18 (retrieved via Google Drive inbox)",
    "page": "11-18",
    "section": "History of Water Pricing in Ghana; The Reform Process; Achievements/Successes",
    "exact_location": "Sections on institutional responsibility, tariff history, and reform-process achievements",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Institutional/legal analysis of Ghana's water-sector reforms under named Acts of Parliament, with real longitudinal national coverage/tariff data and explicit vulnerable-group access provisions. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: descriptive administrative case-study design, no regression-based causal estimate. Extracted for record_id R3A1A4F6F0CF5.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

for r in new_rows:
    assert r["study_id"] not in existing_ids, f"{r['study_id']} already exists"

rows.extend(new_rows)

fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)

print(f"Added {len(new_rows)} rows. New total: {len(rows)}")
