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

# S654 - Packialakshmi, Ambujam & Nelliyat 2011, Chennai peri-urban groundwater market
r = blank_row(fieldnames)
r.update({
    "study_id": "S654",
    "citation": "Packialakshmi S, Ambujam NK, Nelliyat P (2011). Groundwater market and its implications on water resources and agriculture in the southern peri-urban interface, Chennai, India. Environment, Development and Sustainability 13:423-438.",
    "doi": "10.1007/s10668-010-9269-1",
    "publication_year": "2011",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "southern peri-urban interface, Chennai, Tamil Nadu",
    "legal_system": "common law (India)",
    "urban_rural": "peri-urban",
    "service_provider": "Chennai Metropolitan Water Supply and Sewerage Board (CMWSSB); private water tankers; packaged water industries",
    "regulatory_model": "Indian Easements Act 1882 (groundwater rights tied to land ownership, landless left without rights); Chennai Metropolitan Water Supply and Sewerage Act 1978; Chennai Metropolitan Area Ground Water (Regulation) Act 1987, amended 2002 (well registration, extraction/transport licensing, Section 5A extraction prohibition in scheduled areas, Section 12A seizure/confiscation for violations); Tamil Nadu Groundwater (Development and Management) Act 2003",
    "population": "households in 10 water-marketing peri-urban villages (Medavakkam, Perumbakkam, Vengaivasal, Sittalapakkam, etc.)",
    "sample_size": "68-household questionnaire survey (Perumbakkam); groundwater-level records 1971-2007; hydro-chemical sampling at 9 locations; agricultural land-use records 1990-2007; focus group discussions and semi-structured interviews",
    "household_level": "TRUE",
    "income_group": "TRUE",
    "legal_status": "TRUE",
    "eligibility": "",
    "enforcement": "TRUE",
    "documentation": "TRUE",
    "fees": "TRUE",
    "formal_connection": "",
    "water_access": "TRUE",
    "service_quality": "TRUE",
    "service_quantity": "TRUE",
    "affordability": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "68 households (Perumbakkam survey); 9 groundwater sampling locations; village-level agricultural records for 10 villages",
    "model_type": "mixed-methods descriptive study (hydrogeological/water-quality field analysis, household survey, FGD/KII, legal-institutional analysis)",
    "study_design": "mixed-methods case study",
    "risk_of_bias_tool": "MMAT",
    "legal_measurement_quality": "3",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": "Moderate: a real regulatory framework (Chennai Metropolitan Area Ground Water Regulation Act 1987/2002 licensing regime, with a documented tanker-seizure enforcement episode) is weakly enforced against an informal groundwater market, and is documented alongside real household-level survey evidence of income-based water-access bifurcation (wealthier households buying packaged water vs. poorer households dependent on degraded groundwater) and water-related economic stress, though the study does not isolate the regulatory-enforcement-gap mechanism via a formal comparative design.",
    "source_document": "Packialakshmi, Ambujam & Nelliyat 2011, Environment, Development and Sustainability 13:423-438 (retrieved via Google Drive inbox)",
    "page": "423-438",
    "table": "Table 4 (groundwater sampling locations); Table 7 (village-wise agricultural declination)",
    "section": "Groundwater act and governance issues; Socio-economic impacts",
    "exact_location": "Section 7 (Groundwater act and governance issues) and Section 6.2 (Socio-economic impacts, 68-household Perumbakkam survey)",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Mixed-methods case study of Chennai's peri-urban informal groundwater market documenting a weakly-enforced regulatory licensing regime and real household-level income-based water-access/quality/affordability data. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: descriptive mixed-methods study, no regression-based causal estimate. Extracted for record_id RCFD849FB0013.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S655 - Tshishonga & Mafema 2011, South Africa informal settlements gender/water
r = blank_row(fieldnames)
r.update({
    "study_id": "S655",
    "citation": "Tshishonga N, Mafema ED (2011). The impact of neo-liberalism on water and sanitation provision in the informal settlements: Towards the re-enforcement of gendered roles or democratic emancipation? Agenda 25:54-70.",
    "doi": "10.1080/10130950.2011.575997",
    "publication_year": "2011",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "South Africa",
    "subnational_unit": "Banana City (eThekwini/Durban) and Endlovini/Monwabisi Park (Khayelitsha, Cape Town)",
    "legal_system": "common law/mixed (South Africa)",
    "urban_rural": "urban (informal settlements)",
    "service_provider": "eThekwini Municipality; City of Cape Town",
    "regulatory_model": "South African constitutional basic-services mandate; Free Basic Water policy/City of Cape Town Indigent Water Policy 2003 (free, unrestricted standpipe use); landowner-consent requirement for Cape Town Water Services Department to extend infrastructure; tenure-insecurity as a barrier to formal service upgrading; Banana City residents' successful legal defense (via human rights lawyer) against eviction by landowner University of KwaZulu-Natal, followed by municipal land purchase enabling service legalization",
    "population": "women residents of two informal settlements (Banana City, 721 families; Endlovini, population ~100,000)",
    "sample_size": "15 in-depth interviews (comparative case study, one settlement per author) plus participant observation over six consecutive days per site",
    "household_level": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "participation": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "15 in-depth interviews across two informal settlements",
    "model_type": "qualitative comparative case study",
    "study_design": "qualitative comparative case study",
    "risk_of_bias_tool": "CASP",
    "legal_measurement_quality": "3",
    "outcome_measurement_quality": "3",
    "mechanism_certainty": "Moderate: tenure-based institutional barriers to formal water/sanitation infrastructure extension (landowner-consent requirements, tenure insecurity) are documented against real settlement-level infrastructure data (taps/toilets per section serving named family counts) and a documented successful legal tenure-defense case (Banana City), with the gendered access burden as the study's central qualitative focus; the comparative case-study design does not formally isolate the institutional-barrier mechanism from other structural factors.",
    "source_document": "Tshishonga & Mafema 2011, Agenda 25:54-70 (retrieved via Google Drive inbox)",
    "page": "54-70",
    "section": "A snapshot of Endlovini and Banana City; Access to Water and Sanitation",
    "exact_location": "Sections on settlement infrastructure data and the Banana City land-tenure legal case",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Qualitative comparative case study of gendered water/sanitation access in two South African informal settlements, documenting tenure-based institutional barriers and a successful legal tenure-defense case against real settlement-level infrastructure data. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: qualitative comparative case study. Extracted for record_id R762608282964.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S656 - Mudege & Zulu 2011, Nairobi slums water access discourses
r = blank_row(fieldnames)
r.update({
    "study_id": "S656",
    "citation": "Mudege NN, Zulu EM (2011). Discourses of illegality and exclusion: When water access matters. Global Public Health 6:221-233.",
    "doi": "10.1080/17441692.2010.487494",
    "publication_year": "2011",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Kenya",
    "subnational_unit": "Korogocho and Viwandani slum settlements, Nairobi",
    "legal_system": "common law (Kenya)",
    "urban_rural": "urban (informal settlements)",
    "service_provider": "Nairobi City Water and Sewerage Company (NCWSC); informal water vendors/entrepreneurs",
    "regulatory_model": "Kenya Water Act No. 8 of 2002; National Water Services Strategy 2007-2015; Pro-Poor Implementation Plan for Water Supply and Sanitation (PPIP-WSS) 2007; land-tenure illegality of informal settlements barring direct statutory NCWSC connection; documented enforcement actions (2006 large-scale disconnection of illegal water connections; July 2007 riot-police response to a 5-day Kibera water-supply protest)",
    "population": "residents of Korogocho and Viwandani slum settlements, Nairobi, within the Nairobi Urban Health and Demographic Surveillance System (NUHDSS)",
    "sample_size": "36 focus group discussions (256 total participants, Oct-Nov 2004); NUHDSS household survey (23,344 households, water-source data)",
    "household_level": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "enforcement": "TRUE",
    "disconnection": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_quality": "TRUE",
    "service_reliability": "TRUE",
    "affordability": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "36 FGDs (256 participants); NUHDSS survey of 23,344 households",
    "model_type": "mixed-methods discourse analysis with descriptive household survey data",
    "study_design": "qualitative FGD-based study with quantitative survey context",
    "risk_of_bias_tool": "MMAT",
    "legal_measurement_quality": "3",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": "Moderate-high: Kenya's Water Act No. 8 of 2002 and the tenure-based illegality of informal settlements barring statutory NCWSC connection are documented against a large household survey (23,344 households, NUHDSS) showing 91.6%/87.6% of households buying tap water from unauthorized vendors, plus 36 FGDs documenting illegal-connection pricing, quality, and disconnection-enforcement patterns, with two independent real enforcement episodes (2006 mass disconnections; 2007 riot-police response) directly evidencing the institutional-exclusion mechanism.",
    "source_document": "Mudege & Zulu 2011, Global Public Health 6:221-233 (retrieved via Google Drive inbox)",
    "page": "221-233",
    "table": "Table 1 (FGD composition); Table 2 (main water sources by settlement)",
    "section": "Kenyan Government's position on water supply in slum areas; Results",
    "exact_location": "Background section (legal/regulatory framework) and Results section (Table 2, FGD excerpts on illegal connections and disconnection enforcement)",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Mixed-methods discourse-analysis study of tenure-based institutional exclusion from statutory water connection in two Nairobi slums, documenting real enforcement episodes against large-N household survey and FGD evidence. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: qualitative discourse-analysis study with descriptive survey context, no regression-based causal estimate. Extracted for record_id R3551E4A62FAE.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

for r in new_rows:
    assert r["study_id"] not in existing_ids, f"Duplicate study_id: {r['study_id']}"
    for key in list(r.keys()):
        if key not in fieldnames:
            raise AssertionError(f"Unexpected field not in schema: {key}")

rows.extend(new_rows)

fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)
print(f"Appended {len(new_rows)} rows. New total: {len(rows)}")
