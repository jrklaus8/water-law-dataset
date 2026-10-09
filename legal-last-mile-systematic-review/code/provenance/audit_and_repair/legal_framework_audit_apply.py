import csv, os, tempfile, json

REPO = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
EXTRACTION = os.path.join(REPO, "03_extraction/extracted_data/extraction_database.csv")

with open("/tmp/claude-0/-home-user-water-law-dataset/13a4d716-bf67-5f8e-b123-127698a45259/scratchpad/legal_framework_reclass.json") as f:
    buckets = json.load(f)

def atomic_write(path, fieldnames, rows):
    d = os.path.dirname(path)
    fd, tmp = tempfile.mkstemp(dir=d, suffix=".tmp")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    os.replace(tmp, path)

TOOL_LABELS = {
    "ROBINS-I": "ROBINS-I (reclassified 2026-09-28 from Legal Institutional Evidence Appraisal Framework -- study_design/model_type names an explicit quasi-experimental, panel/longitudinal, or before-after intervention-comparison structure; see CHANGELOG.md)",
    "MMAT": "MMAT (reclassified 2026-09-28 from Legal Institutional Evidence Appraisal Framework -- study_design explicitly names a mixed-methods design; see CHANGELOG.md)",
    "JBI-CrossSectional": "JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies (reclassified 2026-09-28 from Legal Institutional Evidence Appraisal Framework -- study_design explicitly names a cross-sectional design; see CHANGELOG.md)",
    "JBI-CrossSectional-tentative": "JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies (reclassified 2026-09-28 from Legal Institutional Evidence Appraisal Framework -- study_design names a standard quantitative regression/survey design without an explicit design-type label; MEDIUM CONFIDENCE, flagged for individual follow-up audit rather than the high-confidence explicit-keyword buckets; see CHANGELOG.md)",
}

sid_to_tool = {}
for bucket, ids in buckets.items():
    if bucket in TOOL_LABELS:
        for sid in ids:
            sid_to_tool[sid] = TOOL_LABELS[bucket]

with open(EXTRACTION, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)

assert len(rows) == 1162

touched = 0
before = {}
for row in rows:
    sid = row["study_id"]
    if sid in sid_to_tool:
        assert row["risk_of_bias_tool"].strip() == "Legal Institutional Evidence Appraisal Framework", f"{sid}: {row['risk_of_bias_tool']!r}"
        before[sid] = row["risk_of_bias_tool"]
        row["risk_of_bias_tool"] = sid_to_tool[sid]
        touched += 1

assert touched == len(sid_to_tool), (touched, len(sid_to_tool))
atomic_write(EXTRACTION, fieldnames, rows)
print(f"Reclassified {touched} studies out of 573 Legal-Framework-tagged rows.")
print(f"Remaining under Legal Framework: {573 - touched}")

# Save the full mapping for the CHANGELOG/audit record
with open("/tmp/claude-0/-home-user-water-law-dataset/13a4d716-bf67-5f8e-b123-127698a45259/scratchpad/legal_framework_reclass_applied.json", "w") as f:
    json.dump({sid: {"new_tool": sid_to_tool[sid]} for sid in sid_to_tool}, f, indent=2)
