import csv, tempfile, os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-21"

DECISIONS = {
    "RB8BD27638F17": ("include", "S532: Murray, Meyer & Fourie 2023, Globalisation, Societies and Education, 'Workshopping Water Justice' -- Cape Town WMD/indigent-status eligibility and 2021 drip-system flow-restriction/prepaid-meter enforcement mechanism."),
    "R589F244C9832": ("include", "S533: Ghertner 2023, Annals AAG, 'Infrastructures of Overlordship' -- NY farm-labor-camp case law documenting tenancy exclusion, discretionary sanitary-code non-enforcement, and utility-shutoff eviction."),
    "RE955C8795F4F": ("include", "S534: Saha & Chakma 2026, SN Social Sciences, 'Co-producing household water insecurity' -- rural West Bengal PHED/Gram Panchayat governance chain and caste-differentiated public-water-point access."),
    "R3858447F3CCC": ("include", "S535: Grisaffi et al. 2026, PLOS Water, 'Regulators as activists' -- East/Southern African road-transported-sanitation regulators' discretionary engagement/tacit-amnesty enforcement of informal pit emptiers."),
}

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

found = set()
for row in rows:
    if row["record_id"] in DECISIONS:
        decision, note = DECISIONS[row["record_id"]]
        row["full_text_status"] = "retrieved"
        row["full_text_decision"] = decision
        row["final_decision"] = decision
        row["reviewer_1"] = REVIEWER
        row["notes"] = (row["notes"] + " " if row["notes"] else "") + note
        found.add(row["record_id"])

missing = set(DECISIONS) - found
if missing:
    raise SystemExit(f"records not found: {missing}")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp, DB)
print("screening db updated (includes):", found)
