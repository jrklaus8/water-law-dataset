import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/descriptive/evidence_map.csv"

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing_ids = {r["study_id"] for r in rows}


def add(sid, design_class, evidence_level, mech_family, outcome_family, quant, qual, legal_ctx, inst_ctx):
    assert sid not in existing_ids, f"Duplicate study_id: {sid}"
    rows.append({
        "study_id": sid,
        "study_design_class": design_class,
        "evidence_level": evidence_level,
        "mechanism_family": mech_family,
        "outcome_family": outcome_family,
        "quantitative_synthesis_eligible": quant,
        "qualitative_synthesis_eligible": qual,
        "legal_context": legal_ctx,
        "institutional_context": inst_ctx,
    })


add(
    "S662",
    "cross-sectional institutional case study",
    "moderate",
    "legal provision for operation and maintenance of urban water infrastructure",
    "infrastructure functionality and water supply service status",
    "FALSE",
    "TRUE",
    "Zimbabwe: Urban Councils Act (Chapter 29:15); Water Policy 2012; ZINWA Act (Chapter 20:25)",
    "11 urban local authorities; ZINWA",
)

add(
    "S663",
    "qualitative case study (interviews and focus group discussions)",
    "moderate-high",
    "disability-policy implementation gap in WASH access provision",
    "household/individual water, sanitation and hygiene access and safety",
    "FALSE",
    "TRUE",
    "Zimbabwe: National Disability Policy (2021); constitutional disability-rights provisions",
    "local authorities (community boreholes); disability-service organisations",
)

add(
    "S664",
    "comparative institutional case study (documentary analysis with household survey data)",
    "moderate",
    "concession/affermage/licensing regulatory arrangements for water supply and vending",
    "household water access, coverage and affordability",
    "FALSE",
    "TRUE",
    "Sub-Saharan Africa: concession and affermage contracts; vendor licensing regimes",
    "SODECI (Cote d'Ivoire); Kenya Water Utilities Corporation; independent water vendors",
)

add(
    "S665",
    "comparative institutional case study (four-country documentary analysis)",
    "moderate-high",
    "privatization, concession, and nationalization of water-sector ownership structures",
    "household formal connection and service coverage",
    "FALSE",
    "TRUE",
    "England and Wales: 1989 Water Act privatization; Argentina: 1992 Buenos Aires concession contract; Israel: 1959 Water Law",
    "Ofwat-equivalent regulator; independent Buenos Aires regulatory agency; SODECI; Mekorot",
)

add(
    "S666",
    "descriptive institutional case study (documentary/administrative-data analysis)",
    "moderate-high",
    "statutory water/sewerage provision duty and tariff-approval/cross-subsidy regulatory framework",
    "household formal connection, coverage and affordability",
    "FALSE",
    "TRUE",
    "Sri Lanka: Municipal Councils legislation; NWSDB statutory mandate",
    "National Water Supply & Drainage Board (NWSDB); Municipal Councils; Irrigation Department",
)

add(
    "S667",
    "descriptive institutional case study (documentary/administrative-data analysis)",
    "moderate-high",
    "water-sector legal reform and regulatory-body establishment (tariff-setting, resource-management, consumer protection)",
    "household water access, coverage and affordability",
    "FALSE",
    "TRUE",
    "Ghana: Ghana Water and Sewerage Act (Act 310, 1965); Water Resources Commission Act (Act 522, 1996); Public Utilities Regulatory Commission Act (Act 538, 1997)",
    "Ghana Water and Sewerage Corporation/Ghana Water Company Limited; Water Resources Commission; Public Utilities Regulatory Commission; Community Water and Sanitation Agency",
)

for r in rows[-6:]:
    assert r["study_id"] in {"S662", "S663", "S664", "S665", "S666", "S667"}

fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)

print(f"New total: {len(rows)}")
