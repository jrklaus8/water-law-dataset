import csv, tempfile, os

path = "05_analysis/descriptive/evidence_map.csv"

with open(path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

new_rows = [
    {
        "study_id": "S554",
        "study_design_class": "mixed_methods",
        "evidence_level": "Mixed-methods case study (39 interviews, 2 focus groups, 110 tourist surveys, 2010 fieldwork) of tourism-driven water inequity in Canggu, Bali, Indonesia, using Ostrom's social-ecological systems framework. Documents concrete legal-administrative access mechanisms (fragmented multi-department water governance, regency-level decentralization competition, subak irrigation governance, unenforced building/metering regulations) with direct interview and survey evidence; provisional confidence: moderate-high -- substantial interview/focus-group sample triangulated with a 110-respondent tourist survey, though the tourist survey itself is not household-representative.",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "economic_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "civil law",
        "institutional_context": "Bali's 1999 regency-level decentralization produced intense inter-Regency competition and poorly coordinated water policy across 11 government departments; the traditional subak irrigation-governance system manages agricultural water through a democratically elected Pekaseh; building-coverage and water-metering/tariff regulations exist on paper but are widely unenforced against the tourism industry, which consumes 65% of water despite a small population share, while local households face low-pressure intermittent connections, long waitlists for new connections, and reliance on unlicensed private-vendor water at prices far above the regulated tariff.",
    },
    {
        "study_id": "S555",
        "study_design_class": "mixed_methods",
        "evidence_level": "Mixed-methods ethnographic case study (155 participant-observation site visits, 10 informal interviews, 7 semi-structured interviews, water-quality monitoring at 5 sites, 2012-2013) of ecosystem services and disservices accessed by people experiencing homelessness via informal urban waterways in Phoenix, Arizona. Documents concrete legal-institutional mechanisms (anti-camping ordinances criminalizing public water access, locked public facilities, illegality of wetland occupation, Park Ranger enforcement) with direct interview, observational, and water-quality evidence; provisional confidence: moderate -- rich triangulated qualitative and quantitative data, though the interview sample (n=7) is small given the sensitivity/illegality of the population's activity.",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "effective_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "common law",
        "institutional_context": "Phoenix's 2004 anti-camping ordinances criminalize sleeping, storing belongings, and food preparation in public areas; public water fountains and bathrooms are locked at night; the Phoenix Heat Relief Network lacks capacity to serve the full homeless population; and accessing state/federal-owned unplanned waterways used for informal water access and cooling is itself illegal, exposing users to Park Ranger enforcement and threatened arrest, documenting an extra-legal informal water-access strategy for a legally excluded vulnerable population with a serious documented health-risk trade-off.",
    },
    {
        "study_id": "S556",
        "study_design_class": "qualitative",
        "evidence_level": "Qualitative ethnographic case study (24 months of fieldwork, 2006-2014, extended participant-observation and interviews) of everyday negotiation of water, electricity, and building-permission access in Delhi's informal slum settlements and unauthorized colonies, India. Documents concrete legal-institutional mechanisms (illegal utility reconnection via informal negotiation, unauthorized colonies categorically barred from formal connections, state officials operating unregistered borewells in violation of their own regulation, Resident Welfare Associations as informal intermediaries) with direct extended ethnographic evidence; provisional confidence: high -- unusually long (24-month) fieldwork period with detailed longitudinal tracking of specific negotiation episodes across multiple settlement types.",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "effective_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "common law",
        "institutional_context": "A formal bureaucratic hierarchy governs electricity, water, and building-permission decisions but is routinely bypassed or locally reinterpreted; a 2010 Delhi government order bans new borewell drilling in unauthorized colonies (UCs) due to a declining water table, yet Jal Board officials install and operate unregistered borewells there, financed via an MLA's discretionary fund rather than official channels; UCs (20%+ of Delhi's population) fall outside the city master plan and are categorically barred from official municipal water/sewerage connections despite residents holding documented property-purchase records; Resident Welfare Associations, though formally non-state, are relied upon by Municipal Corporation officials as intermediaries controlling construction approval and informal water-delivery coordination.",
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
