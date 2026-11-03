import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/03_extraction/extracted_data/extraction_database.csv"

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing_ids = {r["study_id"] for r in rows}
assert "S684" not in existing_ids

def blank_row(fieldnames):
    return {f: "" for f in fieldnames}

r = blank_row(fieldnames)
r.update({
    "study_id": "S684",
    "citation": "Hasan A (2006). Orangi Pilot Project: the expansion of work beyond Orangi and the mapping of informal settlements and infrastructure. Environment & Urbanization 18(2):451-480.",
    "doi": "10.1177/0956247806069626",
    "publication_year": "2006",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Pakistan",
    "subnational_unit": "Orangi Town, Karachi; Manzoor Colony, Karachi; 11 other towns nationally",
    "legal_system": "common law (Pakistan)",
    "urban_rural": "urban",
    "service_provider": "Orangi Pilot Project-Research and Training Institute (OPP-RTI, NGO); Karachi Water and Sewerage Board (KWSB); Karachi Municipal Corporation (KMC)",
    "regulatory_model": ("Katchi Abadi Improvement and Regularization Programme (since 1973, World Bank/ADB "
                          "funded, 99-year lease regularization); Devolution Plan 2001 and Local (City) "
                          "Government Ordinance 2001 establishing zila/tehsil/union-council local government "
                          "structure (33% council seats reserved for women/workers/peasants/minorities); "
                          "provincial ombudsman ruling compelling KWSB to assume maintenance of "
                          "community-built sewerage in Manzoor Colony"),
    "population": "residents of katchi abadis (unauthorized informal settlements) in Orangi (population 1.2 million) and other Karachi/Pakistani urban settlements",
    "sample_size": ("cumulative administrative/programme records: 98,527 houses / 5,479 lanes with community-built "
                     "sewers in Orangi by 2004; 41,900 households in 11 other towns; quarterly OPP-RTI progress reports"),
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "legal_status": "TRUE",
    "tenure_status": "TRUE",
    "documentation": "TRUE",
    "eligibility": "TRUE",
    "fees": "TRUE",
    "administrative_review": "TRUE",
    "institutional_fragmentation": "TRUE",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "application_success": "TRUE",
    "study_design": "documentary/institutional case study (programme administrative records, quarterly progress reports, documented negotiation/litigation history)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "4",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": ("High: the study documents, via detailed administrative/programme records and a "
                             "documented ombudsman ruling, how an NGO-mediated 'internal-external' community-"
                             "government partnership model overcame Pakistan's persistently low-performing "
                             "formal katchi abadi regularization programme (only 1.5% of settlements regularized "
                             "per year), securing real sanitation infrastructure and, in Manzoor Colony, a legal "
                             "victory compelling the state utility (KWSB) to take over maintenance of "
                             "community-built sewers. Quantified outcomes directly tied to the institutional "
                             "mechanism: infant mortality fell from 128 to 37 per 1,000 (1983-1993) in "
                             "communities that built sanitation systems; a formally excluded 'Non-OPP area' "
                             "(denied assistance by local government until 1987) shows a measurably lower "
                             "coverage rate (77.9% vs. 97.1% lane-sewer completion) than the OPP-supported area."),
    "source_document": "Hasan 2006, Environment & Urbanization 18(2):451-480 (retrieved via Google Drive inbox)",
    "table": "Box 2 (cumulative sanitation construction by local people 1981-2004, OPP vs. Non-OPP area)",
    "page": "451-480",
    "section": "II.b (housing demand-supply gap); III.d (Manzoor Colony ombudsman ruling; ADB-Orangi project)",
    "exact_location": "Section III.c-d (Manzoor Colony community-councillor dialogue and ombudsman ruling)",
    "extraction_note": ("Extracted from full-text PDF (retrieved via Google Drive inbox). Documentary/"
                         "institutional case study of NGO-mediated community sanitation infrastructure "
                         "development in Pakistani informal settlements, with a real regularization-programme "
                         "legal framework and a documented ombudsman ruling. Included per INCLUSION_EXCLUSION.md "
                         "criteria 1-9. Not effect_sizes eligible: descriptive/administrative-record design, no "
                         "regression-based effect estimate isolating the institutional mechanism (the infant-"
                         "mortality and coverage figures are simple before/after and area comparisons, not "
                         "adjusted estimates). Extracted for record_id R3DF6CF34D9CE."),
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
