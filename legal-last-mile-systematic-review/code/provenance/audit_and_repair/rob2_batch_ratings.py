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

UPDATES = {
    "S057": {
        "risk_of_bias_rating": "Some concerns (completed 2026-09-28 against the official RoB 2 cluster-trial cribsheet; see 04_quality/appraisal_forms/S057_RoB2.md -- supersedes the 2026-09-16 partial pilot, which left Domains 3 and 5 not assessable)",
        "attrition": "Low risk, inferred (RoB 2 Domain 3 -- administrative sales-transaction outcome, structurally less prone to differential missingness than a survey; not explicitly confirmed -- completed 2026-09-28)",
        "reporting_bias": "Some concerns (RoB 2 Domain 5 -- no pre-analysis plan or trial-registry ID located in extracted text -- completed 2026-09-28)",
    },
    "S085": {
        "risk_of_bias_rating": "Some concerns (completed 2026-09-28 against the official RoB 2 cluster-trial cribsheet, adding Domain 1b -- identification/recruitment timing, Low risk -- to the 2026-09-16 partial pilot's already-complete 5-domain judgement; see 04_quality/appraisal_forms/S085_RoB2.md)",
        "selection_bias": "Some concerns overall (RoB 2 Domain 1a: some concerns, concealment not documented; Domain 1b: Low risk -- eligible/policy-excluded-lands split is a pre-existing land-type classification set before the trial, not an enumerator judgement made after randomization -- completed 2026-09-28)",
    },
    "S294": {
        "risk_of_bias_rating": "Some concerns (completed 2026-09-28 against the official RoB 2 cluster-trial cribsheet; see 04_quality/appraisal_forms/S294_RoB2.md -- supersedes the 2026-09-16 partial pilot, which left Domains 3 and 5 not assessable)",
        "attrition": "Some concerns (RoB 2 Domain 3 -- outcome-data completeness not confirmed in extracted text for the WASH-institutions-index outcome -- completed 2026-09-28)",
        "reporting_bias": "Some concerns (RoB 2 Domain 5 -- no pre-analysis plan or trial-registry ID located in extracted text -- completed 2026-09-28)",
    },
    "S366": {
        "risk_of_bias_rating": "Some concerns, LOW-CONFIDENCE appraisal (2026-09-28, against the official RoB 2 cluster-trial cribsheet; see 04_quality/appraisal_forms/S366_RoB2.md -- nearly every signalling question is honestly NI because this study was extracted from abstract/introduction text only, full PDF body text never retrieved. Highest-priority re-extraction target among the 5 RoB2 studies.)",
        "selection_bias": "Some concerns (RoB 2 Domains 1a/1b -- randomization inherited as fact from companion paper S294; procedural detail unknown -- appraised 2026-09-28)",
        "measurement_bias": "Some concerns (RoB 2 Domain 4 -- specific outcome measures for this paper never described beyond a category label -- appraised 2026-09-28)",
        "confounding": "N/A (randomized design; confounding is not the relevant RoB 2 concern)",
        "attrition": "Some concerns (RoB 2 Domain 3 -- no completeness information extracted -- appraised 2026-09-28)",
        "reporting_bias": "Some concerns (RoB 2 Domain 5 -- no analysis-plan information extracted -- appraised 2026-09-28)",
    },
    "S879": {
        "risk_of_bias_rating": "Some concerns (2026-09-28, against the official RoB 2 cluster-trial cribsheet; see 04_quality/appraisal_forms/S879_RoB2.md -- CAVEAT: randomization unit (compound-level) is inferred, not explicitly confirmed; if the source paper shows individual/household-level randomization instead, this appraisal must be redone against the individually-randomized parallel-trial instrument)",
        "selection_bias": "Some concerns (RoB 2 Domains 1a/1b -- pre-registered (AEA RCT Registry AEARCTR-0003556) supports random allocation, but concealment and identification-timing detail not extracted -- appraised 2026-09-28)",
        "measurement_bias": "Some concerns (RoB 2 Domain 4 -- consistent with outcome_measurement_quality=1 already on file; billing-panel outcomes better-grounded than survey-based access outcomes -- appraised 2026-09-28)",
        "confounding": "N/A (randomized design; confounding is not the relevant RoB 2 concern)",
        "attrition": "Some concerns (RoB 2 Domain 3 -- administrative billing-panel outcomes likely more complete than the 9-month survey-based water-access outcomes; not collapsed into one judgement -- appraised 2026-09-28)",
        "reporting_bias": "Low risk (RoB 2 Domain 5 -- AEA pre-registration AEARCTR-0003556 is a specific, documented fact -- appraised 2026-09-28)",
    },
}

with open(EXTRACTION, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)

assert len(rows) == 1162

touched = 0
for row in rows:
    sid = row["study_id"]
    if sid in UPDATES:
        for k, v in UPDATES[sid].items():
            row[k] = v
        touched += 1

assert touched == 5, touched
atomic_write(EXTRACTION, fieldnames, rows)
print(f"Updated {touched} rows: {list(UPDATES.keys())}")
