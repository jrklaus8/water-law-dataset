import csv, tempfile, os

path = "05_analysis/descriptive/evidence_map.csv"

with open(path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

new_rows = [
    {
        "study_id": "S559",
        "study_design_class": "qualitative",
        "evidence_level": "Qualitative case study (interviews with named municipal and regional officials, combined with regulatory/documentary analysis) of municipal water/sanitation service configuration amid urban sprawl in Stockholm County, Sweden, with a Norrtälje case study. Documents concrete legal-institutional mechanisms (2007 Water Services Act service-area boundary, cost-price tariff principle, four-type service-configuration typology, mini-network unanimous-consent model) with named-official interview and regulatory-document evidence; provisional confidence: moderate -- a small number of official interviews combined with documentary/regulatory analysis, without a systematic household-level sample.",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "effective_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "civil law",
        "institutional_context": "Sweden's 2007 Water Services Act establishes municipal responsibility for water/sanitation service within a statutory 'verksamhetsområde' (service area) and a cost-price (self-financing, no-profit) tariff principle; an estimated ~90,000 Stockholm County households rely on individual/alternative solutions outside the municipal service area; four service-configuration types (A-D) range from full municipal connection to individual on-site solutions; municipalities hold permit and enforcement authority over substandard individual installations; and a mini-network (samfällighet) cooperative model requires unanimous consent among neighboring households to jointly connect to the municipal network.",
    },
    {
        "study_id": "S560",
        "study_design_class": "qualitative",
        "evidence_level": "Qualitative case study (field studies conducted 2011-2014 under the ANR Sud II APPI research project, combined with regulatory/institutional documentary analysis) of hybrid water governance and the legal-institutional role of Water Users' Associations in rural/semi-urban Burkina Faso. Documents concrete legal-institutional mechanisms (2001 Water Law, 2009 decentralization decree, AUE homologation criteria, gendered leadership exclusion, affermage delegation) with field-study and documentary evidence over a multi-year research project; provisional confidence: moderate-high -- multi-year field research under a named ANR-funded project, drawing on both institutional documentary analysis and village-level fieldwork, though the precise interview sample size is not individually reported in this synthesis article.",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "effective_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "civil law",
        "institutional_context": "Burkina Faso's 2000 Reform and 2001 Water Law, following 2009 decentralization, transferred water-infrastructure ownership/management competence from the State to communes; Water Users' Associations (AUE) require formal state homologation (30-80 members, gender parity, youth quota, elected 6-member bureau) and hold formal authority to set hand-pump tariffs, control point-of-service operators, and mediate conflicts; simplified-network (AEPS) management is delegated via affermage contracts to private operators or associative structures (e.g. ADAE); and despite formal gender-parity requirements, women remain confined to subordinate bureau roles while migrants are frequently excluded from water-management decision-making.",
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
