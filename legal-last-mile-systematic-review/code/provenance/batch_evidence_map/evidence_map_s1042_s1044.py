#!/usr/bin/env python3
import csv, tempfile, os

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

existing = {r["study_id"] for r in rows}

new_rows = [
    {
        "study_id": "S1042",
        "study_design_class": "quantitative multi-stakeholder survey with SUR/ordered-Probit-IV regression",
        "evidence_level": "high",
        "mechanism_family": "participation",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "TRUE",
        "qualitative_synthesis_eligible": "FALSE",
        "legal_context": "non-electoral participation (town hall meetings); community-based organizations (CBOs)",
        "institutional_context": "rural village councils, Dnipropetrowskyy and Ternopilskyy regions, Ukraine",
    },
    {
        "study_id": "S1043",
        "study_design_class": "in-depth qualitative case study",
        "evidence_level": "moderate",
        "mechanism_family": "enforcement",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "provincial Water Agency water-rights administration; grassroots federation advocacy",
        "institutional_context": "Agencia de Aguas (WA); Interjuntas-Chimborazo federation, Chimborazo, Ecuador",
    },
    {
        "study_id": "S1044",
        "study_design_class": "critical institutional analysis (fieldwork + database synthesis)",
        "evidence_level": "moderate",
        "mechanism_family": "fees",
        "outcome_family": "affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Law 7/1985 privatization framework; competitive-tender concession contracts",
        "institutional_context": "Spanish municipalities; private water-service concessionaires",
    },
]

for r in new_rows:
    assert r["study_id"] not in existing, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
