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


r = blank_row(fieldnames)
r.update({
    "study_id": "S658",
    "citation": "Jepson W (2012). Claiming Space, Claiming Water: Contested Legal Geographies of Water in South Texas. Annals of the Association of American Geographers 102:614-631.",
    "doi": "10.1080/00045608.2011.641897",
    "publication_year": "2012",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "United States",
    "subnational_unit": "Lower Rio Grande Valley, south Texas (colonias)",
    "legal_system": "common law (United States); Texas state law",
    "urban_rural": "rural and periurban (colonias)",
    "service_provider": "farmer-controlled Water Control and Improvement Districts (WCIDs); Hidalgo WCID 2; Hidalgo & Cameron Counties WCID 9",
    "regulatory_model": "Texas Water Code and 1971 Texas statute (Article 8280-3.2) empowering WCID boards to unilaterally exclude 'urban property' (including unplatted informal colonias) from district territory; companion federal litigation Jimenez et al. v. Hidalgo WCID 2 et al. and Fonseca et al. v. Hidalgo WCID 2 et al. (1972-1976, ending in a failed U.S. Supreme Court appeal, 424 U.S. 950 [1976]), claiming Due Process, Equal Protection, and Voting Rights Act violations; later Texas Colonias Water Bill (1989) and Economically Distressed Areas Program (EDAP)",
    "population": "residents of colonias (predominantly low-income Mexican-American rural/periurban subdivisions) in the Lower Rio Grande Valley, south Texas",
    "sample_size": "documentary/archival analysis (legislative archives, MALDEF/ACLU litigation archives at Stanford University Special Collections, court records); population statistics for 1,350+ colonias",
    "household_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "eligibility": "TRUE",
    "documentation": "TRUE",
    "judicial_review": "TRUE",
    "participation": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "238,000 people in 1,350+ colonias (119,000 facing unknown water/sanitation deficiencies); 1971 exclusion of 39 subdivisions/2,950 lots by Hidalgo WCID 2, including 11 tracts/325 houses without domestic water service",
    "model_type": "documentary/archival legal-geography case study",
    "study_design": "historical-archival/legal institutional case study (litigation trajectory analysis)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "4",
    "outcome_measurement_quality": "3",
    "mechanism_certainty": "High: a rigorously documented legal-institutional exclusion mechanism (WCID board authority under a 1971 Texas statute to unilaterally exclude informal 'urban property' colonias from district territory, thereby denying residents voting rights and the political standing to redirect water-district operations from irrigation to domestic water supply) is evidenced through primary legislative, litigation, and archival records across two companion federal cases (1972-1976) and tied to real population-level water/sanitation access-deficiency statistics for the affected colonias.",
    "source_document": "Jepson 2012, Annals of the Association of American Geographers 102:614-631 (retrieved via Google Drive inbox)",
    "page": "614-631",
    "section": "Colonias and Water Access in South Texas; Claiming Space, Claiming Water; Contesting Water's Territoriality",
    "exact_location": "Sections on the 1971 legislative exclusion, the Jimenez/Fonseca litigation, and colonias population/access statistics",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Legal-geography case study of WCID territorial exclusion of colonias from water-district governance, documenting a real litigated legal-institutional exclusion mechanism against real population-level water/sanitation access-deficiency data, south Texas. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: documentary/legal case-study design, no regression-based causal estimate. Extracted for record_id R110426752017.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})

assert r["study_id"] not in existing_ids, f"Duplicate study_id: {r['study_id']}"
for key in list(r.keys()):
    if key not in fieldnames:
        raise AssertionError(f"Unexpected field not in schema: {key}")

rows.append(r)

fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)
print(f"Appended 1 row. New total: {len(rows)}")
