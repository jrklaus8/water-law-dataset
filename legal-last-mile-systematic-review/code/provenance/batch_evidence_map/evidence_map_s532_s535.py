import csv, tempfile, os

EM = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/descriptive/evidence_map.csv"

with open(EM, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

new_rows = [
    {
        "study_id": "S532",
        "study_design_class": "qualitative",
        "evidence_level": "Participatory-action-research ethnography/case study (decade of organising, Cape Town, South Africa). CASP rating deferred pending the official instrument; provisional confidence: moderate, direct decade-long organising experience corroborated by municipal policy documents, though authors are also the described intervention's organisers (reflexive activist-academic methodology).",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "economic_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "common law (mixed, post-apartheid constitutional)",
        "institutional_context": "City of Cape Town water demand-management regime built around 'indigent'-status eligibility (itself a 'difficult process') for a higher free allocation via Water Management Devices, replaced in 2021 by a 'drip system' requiring self-managed usage below 15kL/month or escalating flow-restriction/prepaid-meter enforcement, against a steeply regressive block tariff.",
    },
    {
        "study_id": "S533",
        "study_design_class": "doctrinal",
        "evidence_level": "Legal-geographic doctrinal case-law analysis (3 paradigmatic New York Unified Court System cases, 1970-2018) with 20+ corroborating stakeholder interviews. Legal Institutional Evidence Appraisal Framework rating deferred pending completion of the project's own appraisal form; provisional confidence: high, direct analysis of primary court records and fire-investigation documentation.",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "effective_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "common law (US federal/state)",
        "institutional_context": "Migrant farmworker housing excluded from ordinary tenancy protection (occupancy deemed 'incidental to employment'); a two-tier NY Sanitary Code Part 15 enforcement regime discretionarily under-enforced by the local health authority; utility/water shutoff directly weaponised as an eviction tool in a documented case (Mack v. Jim-Cor).",
    },
    {
        "study_id": "S534",
        "study_design_class": "mixed_methods",
        "evidence_level": "Mixed-methods study (240-household survey with adjusted logistic regression + 10 KIIs/12 FGDs + 2023-2024 follow-up investigation, rural West Bengal, India). MMAT rating deferred pending the official instrument; provisional confidence: moderate-high, formal statistical testing triangulated with independent qualitative evidence, though purposive (non-probability) village/household sampling.",
        "mechanism_family": "DISCRETION_ACCOMMODATION",
        "outcome_family": "effective_access",
        "quantitative_synthesis_eligible": "TRUE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "common law (federal/state)",
        "institutional_context": "Multi-level rural drinking-water governance chain (household -> Gram Panchayat -> Block administration -> PHED) producing documented infrastructure-siting failures, funding delays, and caste-differentiated access/treatment at public water points (reported social dominance/untouchability), alongside household income determining capacity to self-finance private water access as an alternative to public provision.",
    },
    {
        "study_id": "S535",
        "study_design_class": "qualitative",
        "evidence_level": "Multi-country qualitative case study (19 primary KIIs across 5 countries + secondary review of 37 prior transcripts and 23 Delphi responses, East/Southern Africa). CASP rating deferred pending the official instrument; provisional confidence: moderate-high, draft findings validated with >70% of key informants confirming resonance, though purposive sampling of 'positive outlier' regulators limits generalisability to current sectoral practice (explicitly acknowledged by the authors).",
        "mechanism_family": "DISCRETION_ACCOMMODATION",
        "outcome_family": "effective_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "mixed common law (former British colonial administrations, East/Southern Africa)",
        "institutional_context": "Multilayered national-local regulatory system for faecal-sludge emptying/transport, with the legal status of manual pit-latrine emptying varying by country and local regulators exercising informal discretionary enforcement (tacit amnesties, engagement rather than sanctioning of informal emptiers, negotiated interim disposal sites) to progressively formalise and scale safe service to low-income areas.",
    },
]
rows.extend(new_rows)

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EM))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp, EM)
print("evidence_map rows:", len(rows))
