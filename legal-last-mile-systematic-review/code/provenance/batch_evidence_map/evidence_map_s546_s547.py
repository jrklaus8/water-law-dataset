import csv, tempfile, os

path = "05_analysis/descriptive/evidence_map.csv"

with open(path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

new_rows = [
    {
        "study_id": "S546",
        "study_design_class": "mixed_methods",
        "evidence_level": "Mixed-methods study (350-household survey across Damauli and Tansen municipalities, plus focus group discussions) of Water Users' Associations (WUAs) in Nepal. Documents concrete legal-administrative access mechanisms with direct household-survey and FGD evidence on connection costs, waiting times, and committee governance; provisional confidence: moderate-high -- large household sample (N=350) across two municipalities, triangulated with FGDs, though survey methodology/sampling frame details are limited in the source.",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "economic_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "civil law",
        "institutional_context": "Nepal's Water Resource Act 1992, Water Resource Regulation 1993, and Drinking Water Regulation 1998 govern WUA/DWUA formation and operation for municipal water supply; new household tap connections cost NPR 50,000 (~USD 440) through the standard WUA queue with waits up to 11 years, while paying double (NPR 100,000) secures faster connection; WUA committees were found to collude with private repair agencies and to be politically captured through repeated re-election with little accountability; taps are registered only in the male household head's name, excluding women from formal water rights despite their bearing the burden of water collection (6-7 hrs/day in the dry season); tanker water costs ~Rs 357/1,000L and WUA spring-water pricing rose inequitably from NPR 20 to 80 per 6,000L, with larger WUAs reported to buy out smaller committees' water sources.",
    },
    {
        "study_id": "S547",
        "study_design_class": "mixed_methods",
        "evidence_level": "Mixed-methods case study (73 stakeholder interviews, including 42 household-level, across 7 villages/dusun; 1-month 2013 fieldwork) of adaptive water governance on Merapi volcano's southern slopes, Central Java, Indonesia. Documents concrete legal-institutional mechanisms (Turnover Program, institutional pluralism, undelivered subvention, post-eruption emergency response) with direct interview evidence; provisional confidence: moderate-high -- substantial interview count across multiple villages and stakeholder types, though the single-month fieldwork window limits longitudinal observation of institutional change.",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "effective_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "civil law",
        "institutional_context": "Indonesia's 1987 irrigation reforms and 1998/1999 decentralization framework established the 'Turnover Program,' transferring irrigation governance from customary Ulu-Ulu rights-holders to formal Water Users Associations (WUA) and WUA Federations; resulting institutional pluralism across the Ministry of Public Works, Ministry of Agriculture & Environment, regional water agencies (Perusahaan Daerah Air Minum), the Irrigation Committee, and residual informal Ulu-Ulu authority produced coordination failures, including an undelivered 2013 government subvention payment owed to WUAs; post-2010-eruption lahar damage to sabo-dams and irrigation canals caused drinking- and irrigation-water crises, met by unequal government emergency water-tank distribution and informal Gotong Royong mutual-aid canal repair outside any formal institutional channel.",
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
