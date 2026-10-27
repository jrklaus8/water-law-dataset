import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/03_extraction/extracted_data/extraction_database.csv"

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing_ids = {r["study_id"] for r in rows}
assert "S680" not in existing_ids

def blank_row(fieldnames):
    return {f: "" for f in fieldnames}

r = blank_row(fieldnames)
r.update({
    "study_id": "S680",
    "citation": "Ofer I (2009). La Guerra de Agua: Notions of Morality, Respectability, and Community in a Madrid Neighborhood. Journal of Urban History 35(2):220-235.",
    "doi": "10.1177/0096144208327910",
    "publication_year": "2009",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Spain",
    "subnational_unit": "Orcasitas, Villaverde district, Madrid",
    "legal_system": "civil law (Spain)",
    "urban_rural": "urban",
    "service_provider": "Canal de Isabel II (Madrid water-canal company); Madrid city council; Spanish Ministry of Housing",
    "regulatory_model": ("Informal/illegal shantytown status negotiated over two decades into formal recognition: "
                          "1971 legalization of Orcasitas' Neighborhood Association (Asociacion de Vecinos) as a "
                          "legal public entity; 1970 formal negotiation with the Canal de Isabel II water-canal "
                          "company for canal construction and cost/consent agreement; New Urban Plan (Plan "
                          "Parcial) reconstruction agreed with Madrid city council, completed 1986; Ministry of "
                          "Housing expropriation/property records 1955-1989"),
    "population": "residents of Orcasitas, an illegal shantytown of ~1,500 shacks on Madrid's southern periphery, mostly internal migrants from Castilla la Mancha and Andalusia (1950s-1986)",
    "sample_size": ("archival database of 230 of 1,500 families (Spanish Ministry of Housing property/expropriation "
                     "files, 1955-1989); oral-history interviews (multiple informants, 2006); newspaper reports "
                     "(Cambio 16); 1965 land/water survey; novel and edited-volume testimonies"),
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "legal_status": "TRUE",
    "migrant_population": "TRUE",
    "documentation": "TRUE",
    "participation": "TRUE",
    "discretion_accommodation": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "study_design": "historical-archival/oral-history institutional case study (archival property records, database construction, oral-history interviews, newspaper sources)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "4",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": ("Moderate-high: the study documents, via primary archival property records, a "
                             "constructed 230-family database, and oral-history interviews, how an illegal "
                             "shantytown's residents negotiated formal recognition (1971 legalization of their "
                             "Neighborhood Association) and directly negotiated with the formal water-utility "
                             "company (Canal de Isabel II) and city council for infrastructure, with informal "
                             "'stealing water' workarounds later validated/regularized by local officials (a "
                             "public fountain granted by a sympathetic councilman) - a clear discretion/"
                             "accommodation mechanism linking legal/administrative recognition to real water and "
                             "sanitation access outcomes over a documented 1947-1986 timeline (formal canal "
                             "construction beginning 1970; only 50% of houses with any toilet by 1973). The "
                             "evidence is rich qualitative/archival narrative rather than quantified."),
    "source_document": "Ofer 2009, Journal of Urban History 35(2):220-235 (retrieved via Google Drive inbox)",
    "page": "220-235",
    "section": "Full article, esp. the water-canal negotiation and Neighborhood Association legalization narrative",
    "exact_location": "Sections on the 1970 water-canal company negotiation, 1971 Neighborhood Association legalization, and the 'stealing water' councilman fountain episode",
    "extraction_note": ("Extracted from full-text PDF (retrieved via Google Drive inbox). Historical-archival/"
                         "oral-history institutional case study of an illegal Madrid shantytown's negotiated "
                         "path to formal water/sanitation infrastructure access via Neighborhood Association "
                         "legalization and direct utility-company negotiation. Included per INCLUSION_EXCLUSION.md "
                         "criteria 1-9. Not effect_sizes eligible: qualitative archival/oral-history narrative "
                         "design, no regression-based or otherwise quantified effect estimate. Extracted for "
                         "record_id R2C0C4B70308A."),
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-23",
    "evidence_status": "OBSERVED",
})
rows.append(r)

fd, tmp = tempfile.mkstemp(dir="/home/user/water-law-dataset/legal-last-mile-systematic-review")
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
os.replace(tmp, DB)

print(f"New total: {len(rows)}")
