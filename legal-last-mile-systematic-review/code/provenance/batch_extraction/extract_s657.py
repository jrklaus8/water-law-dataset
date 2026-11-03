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
    "study_id": "S657",
    "citation": "Toubkiss J (2010). Meeting the Sanitation Challenge in Sub-Saharan Cities: Lessons Learnt from a Financial Perspective. In: van Vliet B et al. (eds), Social Perspectives on the Sanitation Challenge, Chapter 10, pp. 163-176. Dordrecht: Springer.",
    "doi": "10.1007/978-90-481-3721-3_10",
    "publication_year": "2010",
    "publication_type": "book chapter",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Mali, Burkina Faso, Senegal, Niger, Uganda (Sub-Saharan Africa)",
    "subnational_unit": "Bamako, Ouagadougou, Bobo-Dioulasso, Dakar, Rufisque, Filingue, Dogondoutchi, Kampala",
    "legal_system": "mixed (multiple Sub-Saharan African civil-law/common-law jurisdictions)",
    "urban_rural": "urban and peri-urban",
    "service_provider": "national water/sanitation utilities; municipal governments; NGOs (ENDA-rup, WaterAid); Office National de l'Eau et de l'Assainissement (Burkina Faso)",
    "regulatory_model": "decentralization of water/sanitation responsibility to local authorities without corresponding transfer of financial means; household subsidy schemes vs. micro-finance for on-site sanitation investment; sanitation-surcharge fee mechanism on water bills (implemented in Burkina Faso, Senegal, Tunisia); land-tenure/title-document requirements barring informal-settlement residents from demanding infrastructure",
    "population": "urban and peri-urban households across 12 Hydroconseil/pS-Eau field case studies in 5 Sub-Saharan African countries",
    "sample_size": "12 in-depth case studies (Table 10.1), 2007-2010 field research",
    "household_level": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "",
    "fees": "TRUE",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "",
    "formal_connection": "",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "affordability": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "12 case studies; Ouagadougou/Bobo-Dioulasso subsidy scheme (~900,000-1,000,000 people served over 14-15 years); Dakar PAQPUD programme (500,000 targeted, 56% of registered requests unfulfilled after 3-year interruption)",
    "model_type": "comparative multi-case-study synthesis drawing on primary field research",
    "study_design": "narrative synthesis of primary case-study field data",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "3",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": "Moderate-high: real institutional/financing mechanisms (targeted household-subsidy schemes vs. micro-finance, sanitation-surcharge fee mechanisms, decentralization without financial transfer, land-tenure/title-document barriers) are documented against real tracked household-level sanitation-access outcome data across 12 primary field case studies, including a large-scale subsidy scheme reaching ~900,000-1,000,000 people over 14-15 years and a documented 56% unfulfilled-request rate following an ODA-financed programme's premature interruption, though the chapter is a narrative synthesis rather than a formal comparative/regression design isolating any single mechanism's independent effect.",
    "source_document": "Toubkiss 2010, in van Vliet et al. (eds), Social Perspectives on the Sanitation Challenge, Chapter 10, pp. 163-176 (retrieved via Google Drive inbox)",
    "page": "163-176",
    "table": "Table 10.1 (list of 12 case studies)",
    "section": "10.6 pS-Eau and Hydroconseil Financing Sanitation Case Studies; 10.7 Conclusions",
    "exact_location": "Section 10.6 (case-study findings) and Section 10.7 (subsidy-scheme and PAQPUD outcome data)",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Comparative multi-case-study synthesis of Sub-Saharan African sanitation-financing institutional mechanisms drawing on 12 primary Hydroconseil/pS-Eau field case studies, documenting real tracked household-level sanitation-access outcomes. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: narrative case-study synthesis, no regression-based causal estimate. Extracted for record_id RFDCD6A65E245.",
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
