import csv, tempfile, os

path = "05_analysis/descriptive/evidence_map.csv"

with open(path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

new_rows = [
    {
        "study_id": "S557",
        "study_design_class": "qualitative",
        "evidence_level": "Qualitative institutional ethnographic case study (40 in-depth interviews with women peasant farmers plus 65 additional stakeholder interviews, participant observation, ~400-document institutional text analysis, 2011 fieldwork) of gendered exclusion from a participatory Water User Association project in rural Uzbekistan. Documents concrete legal-institutional mechanisms (WUA institutionalization, household land-rights formalization, state lease-contract quota system, gendered mobiliser-selection criteria) with direct interview, observational, and documentary evidence; provisional confidence: high -- large interview sample (n=105 total) combined with extensive institutional document analysis using a rigorous, named methodological framework (institutional ethnography).",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "effective_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "civil law",
        "institutional_context": "The Uzbek government institutionalized Water User Associations (WUA) to organize village-level water management after post-1991 decollectivization; 1994 formalized individual household peasant-farm land rights (0.13 hectares, permanent/inheritable); private farmers hold long-term state lease contracts requiring annual cotton/wheat quota submission at state-set prices with fines for shortfall; and a foreign-funded participatory water-management project's 'community mobiliser' selection criteria (public authority, free time) discursively and structurally excluded women -- the majority of household farmers -- despite their extensive unrecognized water-access labor and independent, never-institutionalized self-organized water-user groups.",
    },
    {
        "study_id": "S558",
        "study_design_class": "qualitative",
        "evidence_level": "Qualitative case study (14 in-depth exploratory interviews with sugarcane/ethanol industry stakeholders plus additional interviews with an agricultural researcher and displaced rural residents, June-August 2012) of land and water access under Bonsucro biofuel certification in the Valle del Cauca, Colombia, applying Ribot & Peluso's theory of access. Documents concrete legal-institutional mechanisms (water-concession regulatory regime, regulatory-authority capture, groundwater potability reclassification lobbying, private-certification legal-compliance standard) with direct interview evidence and published water-concession statistics; provisional confidence: moderate-high -- data triangulated across multiple stakeholder types with corroborating published water-use statistics, though the core interview sample (n=14) is modest.",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "economic_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "civil law",
        "institutional_context": "Colombia's water-concession regulatory regime (Decree 1541/78, Agreement 042/2010) is administered by the Cauca Valley Corporation (CVC), described by interviewees as captured by the sugar industry, which holds 64%/88% of surface/underground water concessions versus 26%/2% for household use at lower rates than other users; the industry lobbies to reclassify potable groundwater as non-potable to free it from household-use protections for irrigation; and Bonsucro's private 'obey the law' certification standard is shown to legitimize this disproportionate access without addressing underlying inequitable distribution, weak land-title enforcement, or historical violent dispossession of peasant, indigenous, and Afro-Colombian communities.",
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
