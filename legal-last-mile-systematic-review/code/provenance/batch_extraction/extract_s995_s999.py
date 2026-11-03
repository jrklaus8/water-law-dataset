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

# S995 - RA92812EC2661 - Mustafa & Reeder 2009 - Belize privatization
r = blank_row(fieldnames)
r.update({
    "study_id": "S995",
    "citation": "Mustafa D, Reeder P (2009). 'People Is All That Is Left to Privatize': Water Supply Privatization, Globalization and Social Justice in Belize City, Belize. International Journal of Urban and Regional Research.",
    "doi": "10.1111/j.1468-2427.2009.00849.x",
    "publication_year": "2009",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Belize",
    "subnational_unit": "Belize City",
    "legal_system": "common law",
    "urban_rural": "urban",
    "service_provider": "Belize Water Supply Limited (BWSL), privatized from a public water/sanitation utility",
    "regulatory_model": "water supply and sanitation privatization; tariff-setting and disconnection policy under the private operator",
    "population": "Belize City residents and water-sector policy makers",
    "sample_size": "extensive ethnographic survey of residents and policy makers",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "fees": "TRUE",
    "disconnection": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "affordability": "TRUE",
    "study_design": "ethnographic survey with qualitative narrative analysis",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: original ethnographic/survey study directly linking the institutional shift from "
        "public to privatized water-supply provision (BWSL) to documented household-level tariff increases and "
        "excessive disconnection rates."),
    "source_document": "Mustafa & Reeder 2009, International Journal of Urban and Regional Research (retrieved via Google Drive)",
    "section": "Findings on tariff increases and disconnection rates under privatization",
    "exact_location": "Throughout results sections",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: ethnographic/survey study of failed water-supply "
        "privatization in Belize City, documenting negative material consequences (tariff increases, excessive "
        "disconnection rates) of the institutional shift to a privatized utility (BWSL). Strong Family C match, "
        "consistent with the PSP/tariff-affordability inclusion precedent. NOT effect_sizes eligible: qualitative "
        "ethnographic/survey study, no regression-based estimate. Extracted for record_id RA92812EC2661."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S996 - RA9D674E9C236 - Scott, Cotton & Khan 2013 - Dakar tenure security
r = blank_row(fieldnames)
r.update({
    "study_id": "S996",
    "citation": "Scott P, Cotton A, Khan MS (2013). Tenure security and household investment decisions for urban sanitation: The case of Dakar, Senegal. Habitat International.",
    "doi": "10.1016/j.habitatint.2013.02.004",
    "publication_year": "2013",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Senegal",
    "subnational_unit": "Dakar",
    "legal_system": "civil law",
    "urban_rural": "urban low-income areas",
    "service_provider": "self-managed on-site sanitation systems (household-level)",
    "regulatory_model": "de facto vs. de jure tenure security regimes for low-income urban households",
    "population": "households in low-income urban areas of Dakar with varying tenure security",
    "sample_size": "household investment-decision survey",
    "household_level": "TRUE",
    "tenure_status": "TRUE",
    "eligibility": "TRUE",
    "fees": "TRUE",
    "sanitation_access": "TRUE",
    "affordability": "TRUE",
    "study_design": "cross-sectional household survey with qualitative analysis",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: original empirical study directly linking household tenure security -- "
        "distinguishing de facto from de jure tenure rights -- to household willingness to invest in capital "
        "sanitation infrastructure versus willingness to pay for operational sanitation costs."),
    "source_document": "Scott, Cotton & Khan 2013, Habitat International (retrieved via Google Drive)",
    "section": "Findings on tenure security and household investment/willingness to pay",
    "exact_location": "Throughout results sections",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: empirical study of the relevance of de facto (rather "
        "than de jure) tenure security as the institutional/legal mechanism shaping household capital-investment "
        "decisions in on-site urban sanitation, Dakar. Strong Family A/C match. NOT effect_sizes eligible: "
        "descriptive survey findings, no regression-based estimate isolating the mechanism's effect. Extracted for "
        "record_id RA9D674E9C236."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S997 - R2F782937787E - Vibhu & James 2010 - South India user charges
r = blank_row(fieldnames)
r.update({
    "study_id": "S997",
    "citation": "Vibhu N, James AJ (2010). Policy insights on user charges from a rural water supply project: A counter-intuitive view from South India. Water Resources Development.",
    "doi": "10.1080/07900627.2010.491973",
    "publication_year": "2010",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "Tamil Nadu",
    "legal_system": "common law",
    "urban_rural": "rural",
    "service_provider": "community-managed rural water supply schemes with government engineer engagement",
    "regulatory_model": "flexible, non-prescriptive tariff/O&M-cost-recovery collection approach vs. rigid 100%-collection-from-the-outset targets",
    "population": "rural communities in Tamil Nadu served by rural water supply schemes",
    "sample_size": "project-based policy analysis across the Tamil Nadu rural water supply program",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "fees": "TRUE",
    "discretion_accommodation": "TRUE",
    "participation": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_continuity": "TRUE",
    "study_design": "project case study/policy analysis",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: original project-based policy analysis directly linking a flexible, community-"
        "engaged institutional approach to O&M cost-recovery tariff collection (as opposed to rigid mandated "
        "100%-collection targets) to improved rural water-supply service delivery sustainability and community "
        "ownership."),
    "source_document": "Vibhu & James 2010, Water Resources Development (retrieved via Google Drive)",
    "section": "Findings on democratization of governance and service delivery outcomes",
    "exact_location": "Throughout results sections",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: project-based policy analysis of Tamil Nadu's rural "
        "water supply program demonstrating that a flexible, community-engaged institutional approach to O&M "
        "tariff collection (rather than a rigid mandated cost-recovery target) improves community ownership and "
        "rural water-supply service delivery sustainability. Family A/C match. NOT effect_sizes eligible: "
        "descriptive project policy analysis, no regression-based estimate. Extracted for record_id "
        "R2F782937787E."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S998 - RAD2F8C9FB199 - Jackson & Barber 2013 - Indigenous water NT Australia
r = blank_row(fieldnames)
r.update({
    "study_id": "S998",
    "citation": "Jackson S, Barber M (2013). Recognition of indigenous water values in Australia's Northern Territory: current progress and ongoing challenges for social justice in water planning. Planning Theory & Practice.",
    "doi": "10.1080/14649357.2013.845684",
    "publication_year": "2013",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Australia",
    "subnational_unit": "Northern Territory (Roper River, Mataranka)",
    "legal_system": "common law",
    "urban_rural": "rural/remote",
    "service_provider": "water allocation planning authority (Northern Territory government)",
    "regulatory_model": "2004 National Water Initiative; Native Title Act 1993 (following the Mabo decision); Strategic Indigenous Reserve water-allocation mechanism; Water Advisory Committee participatory process",
    "population": "indigenous people of the upper Roper River region (Mangarrayi, Yangman, Wubulawun peoples)",
    "sample_size": "18 formal interviews (of 33 approached) plus participant observation and archival research",
    "household_level": "FALSE",
    "community_level": "TRUE",
    "indigenous_population": "TRUE",
    "legal_status": "TRUE",
    "eligibility": "TRUE",
    "documentation": "TRUE",
    "participation": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "extraction_sample_size": "18",
    "study_design": "qualitative case study with semi-structured interviews and participant observation",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: original qualitative case study directly linking Australia's national water-"
        "policy legal framework (National Water Initiative 2004, Native Title Act 1993) and its water-allocation-"
        "planning implementation (Strategic Indigenous Reserve) to a documented, quantified inequity between "
        "indigenous land ownership (>20% of national land mass) and indigenous-specific water entitlements "
        "(<0.01% of Australian water diversions)."),
    "source_document": "Jackson & Barber 2013, Planning Theory & Practice (retrieved via Google Drive)",
    "section": "Water rights, planning and social justice",
    "exact_location": "Throughout, esp. inequity statistics on land ownership vs. water entitlements",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: qualitative case study (18 interviews, Roper River "
        "region) of Australia's National Water Initiative and Native Title Act legal framework as it shapes "
        "indigenous water entitlements, documenting the stark disparity between indigenous land ownership (>20%) "
        "and indigenous-specific water allocation entitlements (<0.01%). Strong Family A match. NOT effect_sizes "
        "eligible: qualitative case study, no regression-based estimate. Extracted for record_id RAD2F8C9FB199."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S999 - RABA8C62B263C - Subbaraman & Murthy 2015 - Mumbai right to water
r = blank_row(fieldnames)
r.update({
    "study_id": "S999",
    "citation": "Subbaraman R, Murthy SL (2015). The right to water in the slums of Mumbai, India. Bulletin of the World Health Organization.",
    "doi": "10.2471/BLT.15.155473",
    "publication_year": "2015",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "Mumbai (Kaula Bandar and other slums)",
    "legal_system": "common law",
    "urban_rural": "urban informal settlements",
    "service_provider": "Mumbai municipal government (chlorinated central water supply); street vendors for excluded households",
    "regulatory_model": "notified vs. non-notified slum status (pre-2000/pre-year-2000 residency cutoff on state/city land); land ownership category (central government land excluded from the notification policy); 2014 Bombay High Court Public Interest Litigation ruling",
    "population": "residents of non-notified slums in Mumbai, particularly Kaula Bandar",
    "sample_size": "case analysis drawing on prior household survey data (811 children survey) and legal case review",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "legal_status": "TRUE",
    "tenure_status": "TRUE",
    "eligibility": "TRUE",
    "documentation": "TRUE",
    "judicial_review": "TRUE",
    "fees": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "affordability": "TRUE",
    "effect_measure": "descriptive price-ratio and mortality-ratio comparison",
    "study_design": "legal/policy case analysis with descriptive epidemiological data",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: original legal/policy analysis directly linking notified/non-notified slum "
        "legal status (tied to pre-2000 residency documentation and land-ownership category) and the 2014 Bombay "
        "High Court PIL ruling (grounding a constitutional Article 21 right to water) to documented household-"
        "level outcomes: non-notified households pay more than 40 times the standard municipal water charge and "
        "experience infant mortality more than twice that of notified slums."),
    "source_document": "Subbaraman & Murthy 2015, Bulletin of the World Health Organization (retrieved via Google Drive)",
    "section": "Perspectives article throughout",
    "exact_location": "Price and mortality comparison statistics; Bombay High Court PIL discussion",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: legal/policy analysis of notified/non-notified slum "
        "status in Mumbai and the 2014 Bombay High Court PIL ruling (Pani Haq Samiti) recognizing a constitutional "
        "right to water under Article 21, documenting a >40x water-price disparity and >2x infant mortality "
        "disparity for non-notified slum residents. Strong Family A/C match, closely parallels and reinforces the "
        "S989 (Gimelli et al) Mumbai informal-settlement inclusion precedent from Batch 196. NOT effect_sizes "
        "eligible: descriptive legal/policy case analysis, no regression-based estimate. Extracted for record_id "
        "RABA8C62B263C."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

for r in new_rows:
    assert r["study_id"] not in existing_ids, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"extraction_database.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
