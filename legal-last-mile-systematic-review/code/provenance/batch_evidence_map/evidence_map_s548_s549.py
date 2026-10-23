import csv, tempfile, os

path = "05_analysis/descriptive/evidence_map.csv"

with open(path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

new_rows = [
    {
        "study_id": "S548",
        "study_design_class": "qualitative",
        "evidence_level": "Qualitative case study (34 semi-structured interviews, 3 community workshops, key informant interviews, documentary review) of local water-related institutional adaptation to climate challenges in Mbire District, Zimbabwe. Documents concrete legal-administrative access mechanisms in operation (institutional non-presence of statutorily mandated Catchment/Sub-Catchment Councils and ZINWA, RDC by-law enforcement and negotiated accommodation, borehole access strain) with direct interview and workshop evidence; provisional confidence: moderate -- district-wide fieldwork across multiple institutional levels, though a single-district case study limits generalizability.",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "effective_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "common law",
        "institutional_context": "Zimbabwe's Water Act 1998 and ZINWA Act 1998 establish Catchment Councils and Sub-Catchment Councils as the formal water-planning/permitting authorities, but these bodies (and ZINWA itself) were found functionally absent in this rural district -- over 90% of residents had no knowledge of them -- leaving the Rural District Council, Environmental Management Agency, traditional authorities, and community Borehole Water Committees as the institutions actually governing access; RDC enforcement of the national streambank-cultivation by-law produced sustained conflict with EMA and residents, resolved through a locally negotiated (but not fully inter-institutionally accepted) accommodation; borehole access was severely strained, with most wards far exceeding the government's recommended 250-persons-per-borehole maximum (up to 2,000 in the worst-affected ward) following the post-2000 collapse of donor-funded drilling/maintenance support.",
    },
    {
        "study_id": "S549",
        "study_design_class": "mixed_methods",
        "evidence_level": "Mixed-methods case study (62 semi-structured household interviews, transect walks, photo diaries, expert and stakeholder interviews) of de facto privatisation and uneven access to land and water in peri-urban Greater Accra, Ghana. Documents concrete legal-administrative access mechanisms in operation (unlicensed groundwater extraction, customary land-tenure exploitation via chieftaincy disputes, informal 'digging fee' payments, income-stratified private-vendor pricing) with direct household-interview and triangulated qualitative evidence; provisional confidence: moderate-high -- substantial interview sample (n=62) triangulated across two case-study sites with multiple qualitative methods.",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "economic_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "common law",
        "institutional_context": "Ghana's Water Resources Commission Act 1996 and Water Use Regulations 2001 require permits/registration for groundwater extraction, but in the peri-urban case-study sites this legal requirement is routinely bypassed, with groundwater access instead controlled de facto by private landowners; private water-vendor pricing runs 3-20x the official GWCL rate, with access stratified by income between bulk tanker purchase and smaller-quantity neighbourhood-vendor purchase. In the land domain, customary allodial-title tenure administered by traditional authorities as fiduciary custodians is exploited through an unresolved 20-year chieftaincy dispute (Oduman) enabling multiple sale of the same land plots; formal land-title registration under the Title Registration Act 1986 is functionally inaccessible to most residents (often because the underlying stool land itself is unregistered), so access is instead maintained through informal practices (immediate construction, land guards, caretakers, litigation) and an extra-legal 'digging fee'/asafo-money payment required before construction can begin.",
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
