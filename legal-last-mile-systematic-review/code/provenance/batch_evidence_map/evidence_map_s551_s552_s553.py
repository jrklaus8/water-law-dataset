import csv, tempfile, os

path = "05_analysis/descriptive/evidence_map.csv"

with open(path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

new_rows = [
    {
        "study_id": "S551",
        "study_design_class": "mixed_methods",
        "evidence_level": "Mixed-methods statistical study (487-household survey across four underserved settlements: Ashaiman and Teshie in Accra, Ghana; Khayelitsha and Philippi in Cape Town, South Africa) of gender-differentiated water access, uses, knowledges, governance, and experiences. Documents concrete legal-administrative access mechanisms (GWCL/AVRL urban-supply history in Ghana; South Africa's Free Basic Water policy and RDP housing-formalization process) with direct survey and qualitative evidence; provisional confidence: moderate-high -- large household sample (N=487) across two countries and four settlements, triangulated with qualitative interviews, though the source is a descriptive/cross-tabulated survey without a formal regression-based effect estimate.",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "economic_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "common law",
        "institutional_context": "Ghana's GWCL holds the statutory urban piped-supply mandate, with operations managed under a private AVRL consortium contract 2006-2011; South Africa's Constitution enshrines a right to water and sanitation, implemented via the Free Basic Water policy's flat 6kl/household/month allocation regardless of household size, with access in the case-study settlements still shaped by apartheid-era infrastructure siting and an ongoing RDP housing-formalization process determining formal-connection eligibility. Women in both countries bear disproportionate responsibility for water collection, storage, and negotiation of access, with differentiated governance participation and infrastructure knowledge by gender.",
    },
    {
        "study_id": "S552",
        "study_design_class": "qualitative",
        "evidence_level": "Qualitative case study (18 semi-structured interviews with rural water committees plus NGO/multilateral/government staff interviews, 12 months of fieldwork 2007-2010, plus 2014 follow-up) of the legal recognition and organic empowerment of Nicaragua's community-based water committees (CAPS). Documents concrete legal-institutional mechanisms (Law 722 recognition, Law 620 prior exclusion, absence of personeria juridica, informal fee/shutoff negotiation, legal-gray-area land access negotiation) with direct interview evidence; provisional confidence: moderate-high -- multi-year fieldwork with a 2014 follow-up across national policy change, though the 18-committee interview sample is modest.",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "effective_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "civil law",
        "institutional_context": "Nicaragua's Special Law of Potable Water and Sanitation Committees (Law 722, 2010) formally recognized over 5,000 previously unrecognized CAPS serving more than 1 million rural residents, superseding the exclusionary General Water Law (Law 620, 2007); individual CAPS still generally lack personeria juridica (legal personality), preventing legal receipt of constructed water systems; CAPS set user fees ($0.23-$2.85/household/month) with informally negotiated non-enforcement of shutoff rules for seasonal-labor households, and negotiate legally ambiguous land/water-source access agreements with private landowners.",
    },
    {
        "study_id": "S553",
        "study_design_class": "qualitative",
        "evidence_level": "Qualitative case study (48 semi-structured and focus-group interviews with commercial farmers, emerging farmers, and local community members, plus document analysis, fieldwork 2011 and 2015) of power asymmetries in the establishment of a Water User Association (WUA) in the Groot Marico catchment, South Africa. Documents concrete legal-institutional mechanisms (National Water Act 1998 WUA guidelines, the 'existing lawful use' provision, a documented exclusionary WUA-establishment meeting) with direct interview and document evidence; provisional confidence: moderate-high -- substantial interview sample (n=48) across two fieldwork periods (2011, 2015) triangulated with document analysis of the WUA-establishment process.",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "effective_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "common law",
        "institutional_context": "South Africa's National Water Act 1998 establishes Water User Associations as the local collaborative-governance vehicle intended to redress apartheid-era water-access inequality; the Act's 'existing lawful use' provision ties commercial-farmer water entitlements to land ownership from the 1996-1998 baseline period, continuing to advantage the white minority of commercial irrigation farmers despite the NWA's stated intent to separate water rights from land ownership. A documented WUA-establishment meeting functionally excluded Black rural community members and emerging farmers via short notice, an inaccessible venue, and English-only proceedings, resulting in commercial-farmer domination of WUA leadership and a pre-drafted constitution.",
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
