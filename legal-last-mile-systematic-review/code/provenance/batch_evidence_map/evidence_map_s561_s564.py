import csv, tempfile, os

path = "05_analysis/descriptive/evidence_map.csv"

with open(path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

new_rows = [
    {
        "study_id": "S561",
        "study_design_class": "qualitative",
        "evidence_level": "Qualitative case study (20 semi-structured interviews, 6 focus groups, 2020 fieldwork, 4-day 2021 validation workshop) of Inclusive WASH access and governance in the tourism destination of Labuan Bajo, Indonesia. Documents concrete legal-institutional mechanisms (PDAM tiered tariff structure, national minimum water-requirement service standard, POKJA AMPL multi-stakeholder governance forum) with direct interview evidence and secondary utility/government data; provisional confidence: moderate-high -- multi-scale (hotel/community/government) interview and focus-group triangulation plus a stakeholder validation workshop, though without a systematic household survey.",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "economic_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "civil law",
        "institutional_context": "The municipal water utility PDAM supplies piped water intermittently (twice weekly) amid a documented ~10 L/s deficit; Indonesia's Ministry of Public Works Regulation No. 14/Prt/M/2010 sets a 60 L/person/day minimum service standard; PDAM applies a tiered tariff charging hotels more than households, perceived locally as producing preferential commercial delivery; the multi-stakeholder POKJA AMPL working group formally coordinates WASH governance but convenes irregularly; and community water-service levels have declined since 2015 despite tourism-driven demand growth, with women bearing the primary collection burden.",
    },
    {
        "study_id": "S562",
        "study_design_class": "mixed_methods",
        "evidence_level": "Mixed-methods cross-sectional study (800-household survey, 751 retrieved/93.9% response rate, plus key-informant interviews, observation, and narratives) of household WaSH access across three ecological zones in Cross River State, Nigeria. Documents concrete legal-institutional mechanisms (2025 Water Supply and Sanitation Law, new WaSH regulatory department, 2025 WaSH Policy financing/accountability provisions) with a large, methodologically robust household sample and documentary/policy-analysis triangulation; provisional confidence: high -- large representative multi-stage-sampled household survey (n=751) with high response rate, cross-referenced against a newly enacted statutory framework.",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "effective_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "common law",
        "institutional_context": "Cross River State's 2025 Water Supply and Sanitation Law establishes a statutory guarantee of basic WaSH access and a new regulatory framework; a dedicated WaSH regulatory department was inaugurated to monitor compliance; the 2025 WaSH Policy establishes sustainable-financing, citizen-accountability-dashboard, and differentiated-service-delivery mechanisms; and institutionalized community task groups (e.g. Obubra LGA) formally participate in governance, though 79% of households still report access difficulties and community participation functions largely as unpaid labor substituting for state investment.",
    },
    {
        "study_id": "S563",
        "study_design_class": "mixed_methods",
        "evidence_level": "Mixed-methods study (122 mWater-tool household/community interviews, Empowerment in WASH Index survey, 2023-2024 fieldwork) of gender dynamics in Water Point Committee governance in rural Mbala, Zambia. Documents concrete legal-institutional mechanisms (WPC membership eligibility criteria, election cycles, financial-contribution enforcement gaps) with a quantified empowerment index and thematic interview analysis; provisional confidence: moderate-high -- purposive but data-saturation-guided sample (n=122) with a validated empowerment-index instrument (EWI, Dickin et al. 2021), cross-validated against qualitative interview themes.",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "effective_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "common law",
        "institutional_context": "Water Point Committees (WPCs) are the community-level governance institution responsible for water access point (WAP) management, with formal eligibility criteria for membership and periodic elections, but lack statutory backing or enforceable financial-contribution mechanisms; 53% of surveyed WPCs were non-functional and ~26% of WAPs were non-functional at time of study, with lack of enforced user-fee contribution (not gendered exclusion, per the study's EWI findings) identified as the primary sustainability barrier.",
    },
    {
        "study_id": "S564",
        "study_design_class": "mixed_methods",
        "evidence_level": "Mixed-methods study (221-household survey, 6 FGDs, semi-structured official interviews, 2 detailed village case studies, national-policy document review, 2011-2012 fieldwork) of decentralized community water management in Kondoa and Mpwapwa districts, Tanzania. Documents extensive concrete legal-institutional mechanisms (2002 NAWAPO, 2008 NWSDS, VWC gender-parity requirements, DWD staffing deficits, PO tender processes) with a large representative household sample, official documentary review, and rich village-level case-study detail; provisional confidence: high -- combines a randomly-sampled household survey, direct national-policy-document analysis, and two in-depth village case studies triangulating multiple data sources.",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "effective_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "common law",
        "institutional_context": "Tanzania's 2002 National Water Policy and 2008 National Water Sector Development Strategy devolve full O&M cost-recovery responsibility to Village Water Committees (VWCs) under the 'subsidiarity principle' but do not explicitly define VWC or household-level roles; District Water Departments have only 41-50% of required technical staff; VWCs must maintain gender-parity composition under national guidelines; private-operator tender processes are handled by village councils without District legal-unit oversight; and villages experienced a mean 4.3 months/year of water-infrastructure non-functionality, with documented cases of unaccountable contractors and inactive/unaudited village water-fund accounts.",
    },
]

rows.extend(new_rows)

fd, tmp = tempfile.mkstemp(dir="05_analysis/descriptive")
with os.fdopen(fd, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp, path)

print("done, evidence_map rows now", len(rows))
