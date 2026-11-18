#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/descriptive/evidence_map.csv"

def atomic_write(path, fieldnames, rows):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path))
    with os.fdopen(fd, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp, path)

with open(PATH, newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing_ids = {r["study_id"] for r in rows}

new_rows = [
    {
        "study_id": "S989",
        "study_design_class": "qualitative embedded case study with narrative analysis",
        "evidence_level": "high",
        "mechanism_family": "legal_status",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Maharashtra Slum Areas (Improvement, Clearance and Redevelopment) Act 1971; MCGM notification/documentation eligibility cutoff; Article 21 constitutional right-to-life claim",
        "institutional_context": "Municipal Corporation of Greater Mumbai, Bombay High Court, local NGOs",
    },
    {
        "study_id": "S990",
        "study_design_class": "historical/political-economy case study with document analysis and interviews",
        "evidence_level": "moderate",
        "mechanism_family": "enforcement",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "national water-sector structural reform, public-works tendering regulations",
        "institutional_context": "Commissario for hydraulic emergencies, Ente Acquedotti Siciliani, Palermo Municipal Aqueduct",
    },
    {
        "study_id": "S991",
        "study_design_class": "qualitative case study with interviews and focus groups",
        "evidence_level": "high",
        "mechanism_family": "participation",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Water Authority of Fiji Rural Water Scheme requirements",
        "institutional_context": "village water committees, village chief, Turaga ni koro, provincial offices",
    },
    {
        "study_id": "S992",
        "study_design_class": "program case study/action research",
        "evidence_level": "moderate",
        "mechanism_family": "documentation",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "proposed new by-laws, standard constitutions and legal/banking status for community water-management committees",
        "institutional_context": "Ministry of Water and Environment Learning Alliance, Whave Solutions, local government",
    },
    {
        "study_id": "S993",
        "study_design_class": "cross-sectional mixed-methods household survey with water-quality testing",
        "evidence_level": "moderate",
        "mechanism_family": "service_area",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Malawi Water Works Act 1995, National Water Policy 2005, National Sanitation Policy 2008",
        "institutional_context": "Lilongwe Water Board, small-scale independent providers (SSIPs)",
    },
    {
        "study_id": "S994",
        "study_design_class": "mixed-methods field study with expert/artisan interviews",
        "evidence_level": "high",
        "mechanism_family": "institutional_fragmentation",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "lack of uniform rural water-scheme implementation policy across local government",
        "institutional_context": "local government institutions responsible for scheme operation and maintenance",
    },
]

for r in new_rows:
    assert r["study_id"] not in existing_ids, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
