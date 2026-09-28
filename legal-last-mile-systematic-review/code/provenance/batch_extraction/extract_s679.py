import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/03_extraction/extracted_data/extraction_database.csv"

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing_ids = {r["study_id"] for r in rows}
assert "S679" not in existing_ids

def blank_row(fieldnames):
    return {f: "" for f in fieldnames}

r = blank_row(fieldnames)
r.update({
    "study_id": "S679",
    "citation": "Goldin JA (2010). Water Policy in South Africa: Trust and Knowledge as Obstacles to Reform. Review of Radical Political Economics 42(2):195-212.",
    "doi": "10.1177/0486613410368496",
    "publication_year": "2010",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "South Africa",
    "subnational_unit": "Breede-Overberg Water Management Area, Western Cape (Ruensveld/Duivenhoks; Kassiesbaai/Arniston)",
    "legal_system": "common law (South Africa)",
    "urban_rural": "rural",
    "service_provider": "Department of Water Affairs and Forestry (DWAF); Catchment Management Agency (CMA); Water User Associations (WUAs); Overberg Water Board",
    "regulatory_model": "National Water Act (No. 36 of 1998) and Water Services Act (No. 108 of 1997) establishing catchment-based Water Management Areas governed by Catchment Management Agencies with multi-stakeholder forums (WUAs); 1996 Cabinet abolition of riparian water rights and private land-based water ownership",
    "population": "water users in the Breede-Overberg Water Management Area: white commercial farmers (Ruensveld/Duivenhoks irrigation scheme) and residents of Kassiesbaai, a colored fishing village of ~230 households near Arniston",
    "sample_size": "two paired ethnographic case narratives; semi-structured interviews with farmers, councilors, DWAF officials and consultants (2001-2004); documentary/archival sources (Wilson 1999)",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "legal_status": "TRUE",
    "participation": "TRUE",
    "institutional_fragmentation": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "study_design": "qualitative institutional case study (narrative/ethnographic, semi-structured interviews, documentary analysis)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "4",
    "outcome_measurement_quality": "3",
    "mechanism_certainty": ("Moderate-high: the paper documents, via paired ethnographic case narratives and "
                             "interviews, how differential access to social networks and 'scientific' knowledge "
                             "under South Africa's post-1998 catchment-governance institutions (CMAs/WUAs "
                             "established under the National Water Act and Water Services Act) reproduced "
                             "apartheid-era racial disparities in water-scheme access and institutional "
                             "participation - white commercial farmers' historical networks secured a 540,000-hectare "
                             "irrigation scheme, while Kassiesbaai residents remained excluded from meaningful "
                             "participation in catchment decision-making despite the formal post-apartheid "
                             "legal framework's stated equity goals; the mechanism (discretionary/informal "
                             "accommodation via elite networks within nominally participatory formal institutions) "
                             "is well-evidenced qualitatively but not quantified."),
    "source_document": "Goldin 2010, Review of Radical Political Economics 42(2):195-212 (retrieved via Google Drive inbox)",
    "page": "195-212",
    "section": "Narratives of Inclusion and Exclusion (§4); Institutions Can Reinforce Patterns of Exclusion (§5); Conclusion (§8)",
    "exact_location": "§4.1-4.3 (Ruensveld/Duivenhoks vs. Kassiesbaai case narratives); §5 (institutional exclusion mechanism)",
    "extraction_note": ("Extracted from full-text PDF (retrieved via Google Drive inbox). Qualitative institutional "
                         "water-governance case study documenting a real statutory framework (National Water Act "
                         "1998, Water Services Act 1997) and CMA/WUA participation structures alongside differential, "
                         "network-mediated institutional access tied to real settlement-level water-scheme outcomes. "
                         "Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: qualitative "
                         "narrative/interview evidence with no regression-based or otherwise quantified effect "
                         "estimate isolating the institutional-access mechanism. Extracted for record_id R8F361F312043."),
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
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
