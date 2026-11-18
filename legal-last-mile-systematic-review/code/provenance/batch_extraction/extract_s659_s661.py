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

# S659 - Lanti 2006, Jakarta water supply concession contracts
r = blank_row(fieldnames)
r.update({
    "study_id": "S659",
    "citation": "Lanti A (2006). A Regulatory Approach to the Jakarta Water Supply Concession Contracts. Water Resources Development 22:255-276.",
    "doi": "10.1080/07900620600648415",
    "publication_year": "2006",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Indonesia",
    "subnational_unit": "Jakarta (DKI Jakarta)",
    "legal_system": "civil law (Indonesia)",
    "urban_rural": "urban",
    "service_provider": "PAM JAYA (former public operator); PALYJA (Ondeo, Western Sector concessionaire); TPJ (RWE Thames, Eastern Sector concessionaire)",
    "regulatory_model": "25-year private concession contracts (1997, renegotiated as Restated Cooperation Agreements 2001); Jakarta Water Supply Regulatory Body (JWSRB) established by Governor Decree No. 95/2001; Indonesia's Law No. 7/2004 on Water Resources; Government Regulation No. 16/2005 on water supply; Presidential Decree No. 67/2005 on Development of Water Supply System",
    "population": "households in Jakarta metropolitan area (population 9.9 million in 2005)",
    "sample_size": "longitudinal administrative data 1993-2022 (targets vs. realizations); documentary/regulatory-body analysis",
    "household_level": "TRUE",
    "income_group": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "fees": "TRUE",
    "affordability": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "longitudinal service-coverage/non-revenue-water/connections data, 1993-2022 (Table 2)",
    "model_type": "descriptive regulatory case study with longitudinal administrative data",
    "study_design": "longitudinal institutional case study (concession-contract regulatory analysis)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "4",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": "Moderate-high: a real institutional/legal regulatory framework (Indonesia's Law No. 7/2004 on Water Resources and implementing regulations, establishment of the Jakarta Water Supply Regulatory Body) governing 25-year private-concession water-supply contracts is documented against real longitudinal household-level connection/coverage data (service coverage rising from 41% in 1996 toward a 100% target by 2022, non-revenue water reduction targets, tariff-adjustment history) and a documented cross-subsidy policy with multiple small-scale provider types serving the urban poor, authored by the regulatory body's own chairman with direct institutional knowledge.",
    "source_document": "Lanti 2006, Water Resources Development 22:255-276 (retrieved via Google Drive inbox)",
    "page": "255-276",
    "table": "Table 2 (targets vs. realizations, 1993-2022)",
    "section": "Past Condition of Water Supply and Expectation in the Future; The Process and Implementation of Private Sector Participation",
    "exact_location": "Sections on service-coverage/NRW targets and small-scale provider types serving the urban poor",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Institutional/regulatory case study of Jakarta's water-supply concession-contract framework, documenting real longitudinal household-level connection/coverage data and a cross-subsidy policy for the urban poor. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: descriptive longitudinal case study, no regression-based causal estimate. Extracted for record_id RC089E19DF34F.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S660 - Graham 2006, Great Britain electricity/water politics
r = blank_row(fieldnames)
r.update({
    "study_id": "S660",
    "citation": "Graham C (2006). The politics of necessity: electricity and water in Great Britain. Journal of Consumer Policy 29:435-448.",
    "doi": "10.1007/s10603-006-9020-3",
    "publication_year": "2006",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "United Kingdom",
    "subnational_unit": "England and Wales (water); England, Wales, Scotland (electricity)",
    "legal_system": "common law (United Kingdom)",
    "urban_rural": "national",
    "service_provider": "privatized water/electricity companies regulated by Ofwat (Director General of Water Services)",
    "regulatory_model": "Water Industry Act 1999 (banning disconnection of water supplies for non-payment of debt to domestic premises, schools, hospitals; prohibiting water-limiting devices/Budget Payment Units; Vulnerable Groups Regulations); Water Act 2003; Utilities Act 2000; judicial review case (six local authorities v. Director General of Water Services, BPU case, ruled unlawful disconnection)",
    "population": "domestic water/electricity consumers in Great Britain, with particular attention to disadvantaged/vulnerable consumers",
    "sample_size": "documentary/policy analysis with administrative statistics",
    "household_level": "TRUE",
    "income_group": "TRUE",
    "legal_status": "",
    "disconnection": "TRUE",
    "judicial_review": "TRUE",
    "complaint": "TRUE",
    "formal_connection": "",
    "water_access": "TRUE",
    "affordability": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "Vulnerable Groups Regulations uptake data: 7,693 successful applications 2003-04, 9,217 in 2004-05 (1.4% take-up rate); historical disconnection statistics",
    "model_type": "documentary/legal-institutional policy analysis",
    "study_design": "historical-institutional case study (regulatory-politics analysis)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "4",
    "outcome_measurement_quality": "3",
    "mechanism_certainty": "High: a real litigated judicial-review case (BPU case, six local authorities v. Director General of Water Services, ruling pre-payment devices constituted unlawful disconnection) directly produced the Water Industry Act 1999's statutory ban on water disconnection for non-payment and its Vulnerable Groups Regulations, with real household-level uptake data (7,693-9,217 successful applications) and historical disconnection statistics documenting the institutional mechanism's effect on household water access and affordability protections.",
    "source_document": "Graham 2006, Journal of Consumer Policy 29:435-448 (retrieved via Google Drive inbox)",
    "page": "435-448",
    "section": "Paying for water",
    "exact_location": "Section on the BPU judicial-review case and Water Industry Act 1999 Vulnerable Groups Regulations",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Legal-institutional policy analysis of British water-disconnection regulation, documenting a real litigated case (BPU judicial review) that produced statutory disconnection protections, with real household-level uptake data. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: documentary/legal case-study design, no regression-based causal estimate. Extracted for record_id R371D7DD278E0.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S661 - Chappells & Medd 2008, England and Wales domestic water consumption equity
r = blank_row(fieldnames)
r.update({
    "study_id": "S661",
    "citation": "Chappells H, Medd W (2008). What is fair? Tensions between sustainable and equitable domestic water consumption in England and Wales. Local Environment 13:725-741.",
    "doi": "10.1080/13549830802475658",
    "publication_year": "2008",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "United Kingdom",
    "subnational_unit": "England and Wales (southeast England drought case)",
    "legal_system": "common law (United Kingdom)",
    "urban_rural": "national (with southeast England drought focus)",
    "service_provider": "privatized water and sewerage companies (regulated by Ofwat/Environment Agency)",
    "regulatory_model": "post-1989 privatization institutional shift from 'social equity'/universal-provision to 'market environmental'/cost-reflective pricing; Water Act 2003 drought-management-plan requirements; EU Water Framework Directive (2000/60/EC); statutory 'right to water' prohibiting household disconnection for non-payment; metering and tariff policy",
    "population": "domestic water consumers in England and Wales, with focus on southeast England during the 2006 drought",
    "sample_size": "22 household interviews and 4 water-resource-team interviews (2006 drought); household bill/consumption data across water company regions 2005-07; micro-component data from 100-home metered sample",
    "household_level": "TRUE",
    "income_group": "TRUE",
    "fees": "TRUE",
    "formal_connection": "",
    "water_access": "TRUE",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "22 household interviews, 4 water-resource-team interviews; household water-bill data across 11+ water companies 2005-07",
    "model_type": "mixed-methods institutional/policy analysis with primary interview data",
    "study_design": "mixed-methods case study (qualitative interviews plus secondary administrative/consumption data)",
    "risk_of_bias_tool": "MMAT",
    "legal_measurement_quality": "4",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": "Moderate-high: the post-1989 privatization institutional shift from social-equity to market-environmental water charging (Water Act 2003, EU Water Framework Directive, statutory no-disconnection right) is documented against real household-level bill/affordability data (51.7% of non-working households without children spending >3% of disposable income on water/sewerage) and primary interview evidence (22 households, 4 water-resource teams) from the 2006 southeast England drought, though the analysis is descriptive/qualitative rather than a formal regression isolating the institutional-charging mechanism's causal effect.",
    "source_document": "Chappells & Medd 2008, Local Environment 13:725-741 (retrieved via Google Drive inbox)",
    "page": "725-741",
    "table": "Table 1 (average household water bills 2005-07)",
    "figure": "Figure 1; Figure 2 (per-capita consumption by region)",
    "section": "Changing the basis of equitable and sustainable consumption; Drought, demand and the boundaries of domestic water use",
    "exact_location": "Sections on household bill/affordability data and the 2006 drought interview findings",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Mixed-methods institutional/policy analysis of England and Wales water-charging privatization, documenting real household-level affordability data and primary interview evidence from the 2006 drought. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: mixed-methods descriptive/qualitative study, no regression-based causal estimate. Extracted for record_id R32DF2C4FFB4F.",
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
