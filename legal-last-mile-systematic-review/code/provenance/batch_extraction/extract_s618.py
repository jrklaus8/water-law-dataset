#!/usr/bin/env python3
import csv, os, tempfile

DB = "03_extraction/extracted_data/extraction_database.csv"
RESEARCHER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-22"


def blank_row(fieldnames):
    return {f: "" for f in fieldnames}


def main():
    with open(DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    existing_ids = {r["study_id"] for r in rows}
    new_rows = []

    # S618: Adams, Sambu & Smiley 2019, Urban water supply in Sub-Saharan Africa
    r = blank_row(fieldnames)
    r.update({
        "study_id": "S618",
        "citation": "Adams EA, Sambu D, Smiley SL (2019). Urban water supply in Sub-Saharan Africa: historical and emerging policies and institutional arrangements. International Journal of Water Resources Development 35(2):240-263.",
        "doi": "10.1080/07900627.2017.1423282",
        "publication_year": "2019",
        "publication_type": "journal article",
        "language": "English",
        "peer_reviewed": "TRUE",
        "country": "multiple Sub-Saharan African countries (documentary synthesis; case examples include Kenya, Malawi, Ghana, Tanzania, Mozambique)",
        "subnational_unit": "City-level case examples: Kisumu (Kenya), Lilongwe/Blantyre (Malawi), Accra/northern Ghana, Dar es Salaam (Tanzania), Maputo (Mozambique)",
        "legal_system": "mixed (common law and civil law across countries reviewed)",
        "urban_rural": "urban",
        "service_provider": "State/public water utilities; private operators; community-public partnerships (water boards + water user associations); delegated management model master operators; community self-help schemes",
        "regulatory_model": "Historical: state-centralized public water utility provision (1960s-1980s); neoliberal privatization and public-private partnerships (1990s-2000s, Dublin Principles 1992); emerging delegated management models (utility-small-scale-provider contracts); community public partnerships (utility-community/WUA partnerships); community self-help institutional arrangements",
        "population": "Urban households in Sub-Saharan African cities, particularly informal settlements and underserved peri-urban areas",
        "sample_size": "Documentary/narrative synthesis of the primary-source literature on urban water institutional arrangements across the SSA region, 1965-2018",
        "household_level": "TRUE",
        "community_level": "TRUE",
        "income_group": "TRUE",
        "tenure_status": "",
        "legal_status": "",
        "indigenous_population": "",
        "migrant_population": "",
        "eligibility": "TRUE",
        "burden": "TRUE",
        "discretion_accommodation": "TRUE",
        "enforcement": "TRUE",
        "documentation": "",
        "tenure": "",
        "property": "TRUE",
        "planning": "TRUE",
        "zoning": "",
        "building_permit": "",
        "service_area": "TRUE",
        "fees": "TRUE",
        "procedural_steps": "TRUE",
        "delay": "",
        "discretion": "TRUE",
        "hardship_exception": "",
        "administrative_review": "TRUE",
        "complaint": "TRUE",
        "judicial_review": "",
        "disconnection": "TRUE",
        "reconnection": "",
        "sanction": "",
        "participation": "TRUE",
        "institutional_fragmentation": "TRUE",
        "political_coordination": "TRUE",
        "bureaucratic_assistance": "TRUE",
        "formal_connection": "TRUE",
        "water_access": "TRUE",
        "sanitation_access": "",
        "service_coverage": "TRUE",
        "service_reliability": "TRUE",
        "service_quantity": "",
        "service_quality": "",
        "affordability": "TRUE",
        "service_continuity": "TRUE",
        "application_success": "TRUE",
        "refusal": "",
        "delay_outcome": "",
        "effect_measure": "Narrative documentary synthesis citing real tracked outcome data from underlying primary studies; descriptive, no independent regression by these authors",
        "effect_estimate": "Household piped-water-on-premises connection rates vary sharply by institutional arrangement and city: 4% in Greater Accra, 9% in Lilongwe, 23% in Ouagadougou, 29% in Dar es Salaam, and 61% in Nairobi, Mombasa and Kakamega; delegated management model (DMM) in Kisumu, Kenya, significantly expanded the piped network, reduced non-revenue water, and reduced water tariffs; community public partnerships in Malawi (Lilongwe/Blantyre) increased operational communal water kiosks and stabilized pricing but left irregular water supply as a persistent challenge; SSA finished the MDG era with only 24% of the region's population using 'safely managed' water and 46% of the urban population, driven primarily by low rates of on-premises household connection.",
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "p_value": "",
        "extraction_sample_size": "Not applicable (documentary/narrative synthesis of the SSA urban-water-institutions literature)",
        "adjusted_or_unadjusted": "not applicable (narrative synthesis of multiple primary studies)",
        "covariates": "",
        "model_type": "Documentary/narrative literature synthesis",
        "study_design": "Narrative review/documentary synthesis (Legal Institutional Evidence Appraisal Framework)",
        "risk_of_bias_tool": "",
        "risk_of_bias_rating": "",
        "selection_bias": "",
        "measurement_bias": "",
        "confounding": "",
        "attrition": "",
        "reporting_bias": "",
        "legal_measurement_quality": "3",
        "outcome_measurement_quality": "3",
        "mechanism_certainty": "Moderate-high: synthesizes documented legal/institutional mechanisms (delegated management model contracts, community-public partnerships, privatization/PPP arrangements) against real tracked city-level household connection rates and service-delivery outcomes drawn from multiple underlying primary studies; however, as a narrative synthesis rather than an independent primary study, mechanism-outcome linkages are documented rather than statistically tested by these authors.",
        "source_document": "Adams, Sambu & Smiley 2019, International Journal of Water Resources Development 35(2):240-263 (retrieved via Google Drive inbox)",
        "page": "240-263",
        "table": "",
        "figure": "Fig. 1 (private water projects by region, 1991-2011)",
        "section": "Emerging institutional arrangements: towards a community-based paradigm; Utility small-scale-provider partnerships and the delegated management model; Community public (utility) partnerships; The SDGs: equitable and universal access to water",
        "exact_location": "Household-connection-rate comparison (Section on SDGs); Kisumu DMM and Malawi community-public-partnership case discussions",
        "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Comprehensive documentary/narrative synthesis of historical and emerging institutional arrangements for urban water supply across Sub-Saharan Africa, with real tracked city-level household connection-rate and service-delivery outcomes cited from the underlying primary literature. Included via the Legal Institutional Evidence Appraisal Framework, consistent with the Mariwah/Sullivan Lemaitre & Stoler/Romano et al. precedent. Not effect_sizes eligible: narrative synthesis, no single regression-based exposure-comparator effect estimate. Extracted for record_id R2D5B15E9481A.",
        "researcher": RESEARCHER,
        "date_extracted": DATE,
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

    print("Appended", len(new_rows), "rows:", [r["study_id"] for r in new_rows])


if __name__ == "__main__":
    main()
