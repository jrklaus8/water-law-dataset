import csv, tempfile, os

path = "05_analysis/descriptive/evidence_map.csv"

with open(path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

new_rows = [
    {
        "study_id": "S550",
        "study_design_class": "mixed_methods",
        "evidence_level": "Mixed-methods comparative case study (document analysis plus 104 household interviews in Dodowa, Ghana and 56 household interviews plus 120 water-point interviews in Arusha, Tanzania) of power dynamics in participatory groundwater governance for the urban poor. Documents concrete legal-administrative access mechanisms in operation (CWSA/WATSAN structure, GWCL connection process and informal resale pricing, Pangani Basin Water Board regulatory shortfall, illegal ACC land permits in groundwater recharge areas) with direct household and organizational interview evidence; provisional confidence: moderate-high -- large combined interview sample (over 280 respondents) across two countries, triangulated with document analysis.",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "effective_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "common law",
        "institutional_context": "In Dodowa, Ghana, the Community Water and Sanitation Agency Act and GWCL's urban piped-supply mandate coexist with WATSAN committees managing boreholes; GWCL connection applications require a site inspection and fee, while households without their own connection pay roughly 10x the regulated tariff to tank resellers with no price monitoring, and WATSAN committee governance was opaque to most residents in the suburbs studied. In Arusha, Tanzania, the Water Resource Management Act assigns the Pangani Basin Water Board regulatory authority over groundwater drilling, but an unfunded monitoring capacity has left a growing number of boreholes unregistered, while the Arusha City Council has issued land permits for development in designated groundwater recharge areas, confirmed by a National Environment Management Council official to be illegal under the Act. In both cities, household-level access to water and to community water governance itself is mediated by informal social hierarchies (traditional chiefs, elder committees, royal families, Balozi, street chairs, landlords), with tenure status, kinship ties, and land ownership determining who can meaningfully participate or complain.",
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
