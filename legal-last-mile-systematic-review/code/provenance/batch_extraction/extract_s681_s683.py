import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/03_extraction/extracted_data/extraction_database.csv"

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing_ids = {r["study_id"] for r in rows}
for sid in ("S681", "S682", "S683"):
    assert sid not in existing_ids

def blank_row(fieldnames):
    return {f: "" for f in fieldnames}

new_rows = []

# S681 - Singh 2006, Women Society and Water Technologies: Lessons for Bureaucracy
r = blank_row(fieldnames)
r.update({
    "study_id": "S681",
    "citation": "Singh N (2006). Women, Society and Water Technologies: Lessons for Bureaucracy. Gender, Technology and Development 10(3):341-360.",
    "doi": "10.1177/097185240601000303",
    "publication_year": "2006",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "Madhya Pradesh, Bihar, Jharkhand, West Bengal",
    "legal_system": "common law (India)",
    "urban_rural": "rural",
    "service_provider": "Public Health Engineering Department (PHED); Panchayati Raj Institutions (PRI)",
    "regulatory_model": ("Accelerated Rural Water Supply Program (ARWSP, since 1972-73, technology-mission "
                          "status 1986 as Rajiv Gandhi National Drinking Water Mission) implementing National "
                          "Water Policy (1987, 2002) coverage criteria (40 lpcd; one source per 250 persons; "
                          "priority for SC/ST habitations under 100 persons); site-selection formally routed "
                          "through PRI (33% women-reserved seats) since mid-1990s"),
    "population": "rural water users, 162 women and 149 men across caste/ethnic groups in 32 villages (12 in M.P., 15 in W.B., 3 in Bihar, 2 in Jharkhand)",
    "sample_size": "162 women, 149 men (interviews, 12 FGDs); case studies from 4 villages; 46 handpumps studied in M.P./Bihar; 182 arsenic removal plants studied in W.B.",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "legal_status": "TRUE",
    "indigenous_population": "TRUE",
    "eligibility": "TRUE",
    "discretion_accommodation": "TRUE",
    "service_area": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "study_design": "ethnographic institutional case study (participant observation, semi-structured interviews, focus group discussions, case studies)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "4",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": ("High: the study documents, via ethnographic fieldwork across 32 villages, how "
                             "India's formal ARWSP statutory coverage criteria (40 lpcd, one source per 250 "
                             "persons) and PRI-routed site-selection process were systematically undermined by "
                             "caste-based social-space norms at the implementation level - only 9 of 46 "
                             "handpumps installed under the program actually fell within SC/ST localities "
                             "despite formal coverage criteria being met numerically, with quantified "
                             "confirmatory data (80%/16% public-vs-poor-area disparity from a 1980 government "
                             "evaluation of 99 villages). The discretion/accommodation mechanism (bureaucratic "
                             "site-selection on 'officially public' land that is socially elite territory) is "
                             "directly and richly evidenced."),
    "source_document": "Singh 2006, Gender, Technology and Development 10(3):341-360 (retrieved via Google Drive inbox)",
    "page": "341-360",
    "table": "table of 46 handpumps by caste-locality access",
    "section": "Choosing the Site: Numerical Criteria or Social Boundaries?; Technology Management: Who Participates and Why?",
    "exact_location": "Section on site-selection numerical criteria vs. social boundaries (46-handpump caste-access analysis)",
    "extraction_note": ("Extracted from full-text PDF (retrieved via Google Drive inbox). Companion paper to "
                         "S682 (Singh, Women's Participation in Local Water Governance, 2006) drawing on "
                         "overlapping fieldwork in M.P./W.B. but distinct in analytic focus (bureaucratic "
                         "technology-siting failure vs. institutional participation contradictions); both are "
                         "distinct peer-reviewed publications with distinct DOIs and are extracted as separate "
                         "studies per standard practice. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not "
                         "effect_sizes eligible: ethnographic/case-study design with descriptive counts, no "
                         "regression-based effect estimate. Extracted for record_id R0D499B7D1D12."),
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-23",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S682 - Singh 2006, Women's Participation in Local Water Governance
r = blank_row(fieldnames)
r.update({
    "study_id": "S682",
    "citation": "Singh N (2006). Women's Participation in Local Water Governance: Understanding Institutional Contradictions. Gender, Technology and Development 10(1):61-76.",
    "doi": "10.1177/097185240501000104",
    "publication_year": "2006",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "Madhya Pradesh, West Bengal",
    "legal_system": "common law (India)",
    "urban_rural": "rural",
    "service_provider": "Panchayati Raj Institutions (PRI); Village Water and Sanitation Committees (VWSCs)",
    "regulatory_model": ("Panchayati Raj Institution statutory framework (73rd Constitutional Amendment 1993), "
                          "with 33% women-reserved seats (one-third SC/ST); Water and Child Welfare and Health "
                          "Committee (WCWHC) at district/block/village level; Swajaldhara community-driven "
                          "demand-based program; Village Water and Sanitation Committees (VWSCs)"),
    "population": "rural water users in 12 villages (2 districts, Madhya Pradesh) and 15 villages (3 districts, West Bengal), India",
    "sample_size": "12 FGDs (5 women-specific); ~two-thirds of committee-involved informants interviewed; 2 detailed village case studies",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "legal_status": "TRUE",
    "indigenous_population": "TRUE",
    "eligibility": "TRUE",
    "discretion_accommodation": "TRUE",
    "participation": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "study_design": "ethnographic institutional case study (participant observation, semi-structured interviews, focus group discussions, opinion survey)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "4",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": ("High: the study documents, via ethnographic fieldwork (2002-2004) across 27 "
                             "villages in two Indian states, how India's formal PRI water-governance "
                             "institutions (33% women-reserved seats) failed to secure equitable water access "
                             "for the intended beneficiaries because of caste-based social norms - two detailed "
                             "case studies show hand pumps sited by Panchayat decision within dominant-caste "
                             "social space despite being formally intended for SC/Jatav women, who continued to "
                             "depend on distant unsafe sources; quantified attendance data (only 30% of female "
                             "PRI members attended meetings; a district WCWHC president absent all four "
                             "consecutive meetings) corroborates the token-participation mechanism."),
    "source_document": "Singh 2006, Gender, Technology and Development 10(1):61-76 (retrieved via Google Drive inbox)",
    "page": "61-76",
    "section": "Social and Gender Differences in Participatory Water Management in Indian Villages (Case 1, Case 2)",
    "exact_location": "Case studies of hand-pump siting in villages Lamkana and Saprar",
    "extraction_note": ("Extracted from full-text PDF (retrieved via Google Drive inbox). Companion paper to "
                         "S681 (Singh, Women, Society and Water Technologies, 2006), drawing on overlapping "
                         "fieldwork but distinct in analytic focus (institutional participation contradictions "
                         "vs. bureaucratic technology-siting failure); both are distinct peer-reviewed "
                         "publications with distinct DOIs and are extracted as separate studies per standard "
                         "practice. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: "
                         "ethnographic/case-study design with descriptive counts, no regression-based effect "
                         "estimate. Extracted for record_id RDCEF86AF76DC."),
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-23",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S683 - Avila Garcia 2006, Water society and environment - Morelia
r = blank_row(fieldnames)
r.update({
    "study_id": "S683",
    "citation": "Avila Garcia P (2006). Water, society and environment in the history of one Mexican city. Environment & Urbanization 18(1):129-140.",
    "doi": "10.1177/0956247806063969",
    "publication_year": "2006",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Mexico",
    "subnational_unit": "Morelia, Michoacan",
    "legal_system": "civil law (Mexico)",
    "urban_rural": "urban",
    "service_provider": "colonial ayuntamiento (municipal council); post-revolutionary Mexican State; Morelia Potable Water System (SAPA)",
    "regulatory_model": ("Colonial-era Crown-issued water concessions (mercedes) restricting legal access to "
                          "hacendados/merchants/officials/clergy while excluding Indians, mestizos and blacks "
                          "under penalty of whipping/fines; Porfiriato-era juridical-institutional framework for "
                          "water/sanitation; post-1921 State water nationalization (water as national patrimony) "
                          "and modified legal-institutional framework for irrigation/potable-water/sewer "
                          "systems; 1990s water-legislation reform on exploitation and pollution control"),
    "population": "residents of Morelia, Mexico across four historical periods (Colonial 16th-19th c.; Porfiriato ca.1874-1910; post-revolutionary 1921-1979; modern 1980-2000)",
    "sample_size": ("historical-archival documentary analysis (municipal/state archives, prior historical "
                     "scholarship); 2000 census (549,996 inhabitants, 230 neighborhoods); municipal water-system "
                     "flow/coverage records"),
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "legal_status": "TRUE",
    "eligibility": "TRUE",
    "documentation": "TRUE",
    "fees": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "affordability": "TRUE",
    "study_design": "historical-documentary/archival institutional case study",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "4",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": ("High: the study documents, via four centuries of archival/documentary evidence, how "
                             "a succession of real legal/institutional water-rights frameworks - colonial Crown "
                             "concessions (mercedes), Porfiriato-era juridical-institutional reform, post-"
                             "revolutionary State water nationalization, and 1990s legislation - produced "
                             "persistent, quantifiable differential water access by socioeconomic/racial status: "
                             "colonial-era exclusion of Indians/mestizos/blacks from legal water permits under "
                             "penalty of corporal punishment, through to the modern era's quantified 89% "
                             "household-connection rate with sharply unequal distribution (300 lpcd in wealthy "
                             "neighborhoods vs. under 100 lpcd in poor ones, and 21% of 230 neighborhoods reliant "
                             "on irregular tanker-truck service)."),
    "source_document": "Avila Garcia 2006, Environment & Urbanization 18(1):129-140 (retrieved via Google Drive inbox)",
    "table": "Table 1 (Morelia population growth 1793-2000)",
    "page": "129-140",
    "section": "II-VIII (four historical periods)",
    "exact_location": "Sections III (17th-century unequal access/mercedes) and VII (1980-2000 scarcity/socioenvironmental deterioration)",
    "extraction_note": ("Extracted from full-text PDF (retrieved via Google Drive inbox). Historical-documentary "
                         "institutional case study of Morelia, Mexico documenting a real, evolving legal/"
                         "institutional water-rights framework across four centuries with quantified differential "
                         "access outcomes. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes "
                         "eligible: historical-documentary design with descriptive statistics, no regression-"
                         "based effect estimate. Extracted for record_id RA1695DE0E546."),
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-23",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

rows.extend(new_rows)

fd, tmp = tempfile.mkstemp(dir="/home/user/water-law-dataset/legal-last-mile-systematic-review")
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
os.replace(tmp, DB)

print(f"New total: {len(rows)}")
