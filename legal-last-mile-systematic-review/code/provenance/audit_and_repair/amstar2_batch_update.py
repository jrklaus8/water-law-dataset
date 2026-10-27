import csv, os, tempfile

REPO = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
EXTRACTION = os.path.join(REPO, "03_extraction/extracted_data/extraction_database.csv")

def atomic_write(path, fieldnames, rows):
    d = os.path.dirname(path)
    fd, tmp = tempfile.mkstemp(dir=d, suffix=".tmp")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    os.replace(tmp, path)

NEW_RATINGS = {
    "S427": "Not ratable (appraised 2026-09-28 against the official AMSTAR 2 checklist; see 04_quality/appraisal_forms/S427_AMSTAR2.md -- all 5 applicable critical items NI, abstract/conclusion-level extraction only)",
    "S438": "Not ratable (appraised 2026-09-28 against the official AMSTAR 2 checklist; see 04_quality/appraisal_forms/S438_AMSTAR2.md -- all 5 applicable critical items NI)",
    "S475": "Not ratable (appraised 2026-09-28 against the official AMSTAR 2 checklist; see 04_quality/appraisal_forms/S475_AMSTAR2.md -- stronger evidentiary basis than most of this batch: 2 of 5 applicable critical items (search strategy, RoB-assessment technique) have real Partial Yes evidence; the other 3 remain NI. Even full resolution would cap this review at Low confidence, not higher.)",
    "S521": "Not ratable (appraised 2026-09-28 against the official AMSTAR 2 checklist; see 04_quality/appraisal_forms/S521_AMSTAR2.md -- the best-evidenced AMSTAR 2-eligible study in the corpus: 3 of 5 applicable critical items (search strategy, RoB-assessment technique, accounting for RoB when interpreting) have real Partial Yes evidence; 2 remain NI (protocol registration, excluded-studies list). Even full resolution would cap this review at Low confidence, not higher.)",
    "S537": "Not ratable (appraised 2026-09-28 against the official AMSTAR 2 checklist; see 04_quality/appraisal_forms/S537_AMSTAR2.md -- 1 of 5 applicable critical items (search strategy) has real Partial Yes evidence from a very large initial-record count and named PRISMA-ScR methodology; the other 4 remain NI)",
    "S697": "Not ratable (appraised 2026-09-28 against the official AMSTAR 2 checklist; see 04_quality/appraisal_forms/S697_AMSTAR2.md -- all 7 critical items NI, including both meta-analysis-specific items (11, 15) which genuinely apply here since this study is an actual meta-analysis, unlike the narrative/scoping/realist reviews elsewhere in this batch)",
}

GENERIC_DOMAINS = {
    "selection_bias": "See risk_of_bias_rating / 04_quality/appraisal_forms/<id>_AMSTAR2.md for the full AMSTAR 2 item-level record (appraised 2026-09-28)",
    "measurement_bias": "See risk_of_bias_rating / 04_quality/appraisal_forms/<id>_AMSTAR2.md for the full AMSTAR 2 item-level record (appraised 2026-09-28)",
    "confounding": "Not applicable (secondary review of the primary literature, not a primary study)",
    "attrition": "Not applicable (secondary review of the primary literature, not a primary study)",
    "reporting_bias": "See risk_of_bias_rating / 04_quality/appraisal_forms/<id>_AMSTAR2.md for the full AMSTAR 2 item-level record (appraised 2026-09-28)",
}

# Confirmatory note appended to the 10 already-"Not ratable" 2026-09-16 studies and the
# 2 already-complete "Critically Low" studies, confirming the 2026-09-28 eligibility
# re-check found no reason to change their status.
CONFIRM_NOTE = " [Eligibility re-confirmed 2026-09-28 as part of the AMSTAR 2 gate-check across all 34 tagged studies -- this study is genuinely a systematic review/meta-analysis; no change to this rating.]"
CONFIRM_IDS = ["S015","S019","S027","S052","S116","S319","S323","S324","S327","S328","S370","S372"]

with open(EXTRACTION, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)

assert len(rows) == 1162

touched_new = 0
touched_confirm = 0
for row in rows:
    sid = row["study_id"]
    if sid in NEW_RATINGS:
        row["risk_of_bias_rating"] = NEW_RATINGS[sid]
        for field, template in GENERIC_DOMAINS.items():
            row[field] = template.replace("<id>", sid)
        touched_new += 1
    elif sid in CONFIRM_IDS:
        row["risk_of_bias_rating"] = row["risk_of_bias_rating"].rstrip() + CONFIRM_NOTE
        touched_confirm += 1

assert touched_new == 6, touched_new
assert touched_confirm == 12, touched_confirm
atomic_write(EXTRACTION, fieldnames, rows)
print(f"New ratings: {touched_new}; confirmatory notes appended: {touched_confirm}")
