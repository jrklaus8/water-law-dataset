import csv, os, tempfile

REPO = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
EXTRACTION = os.path.join(REPO, "03_extraction/extracted_data/extraction_database.csv")
EFFECT_SIZES = os.path.join(REPO, "05_analysis/effect_sizes/effect_sizes.csv")

def atomic_write(path, fieldnames, rows):
    d = os.path.dirname(path)
    fd, tmp = tempfile.mkstemp(dir=d, suffix=".tmp")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    os.replace(tmp, path)

# --- 1. extraction_database.csv: risk_of_bias_tool corrections ---
TOOL_FIXES = {
    "S590": "JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies",
    "S593": "JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies",
    "S606": "ROBINS-I",
    "S879": "RoB 2",
    "S1162": "JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies",
    "S1163": "ROBINS-I",
    "S749": "JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies",
}

with open(EXTRACTION, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)

before = {sid: None for sid in TOOL_FIXES}
touched = 0
for row in rows:
    sid = row["study_id"]
    if sid in TOOL_FIXES:
        before[sid] = row["risk_of_bias_tool"]
        row["risk_of_bias_tool"] = TOOL_FIXES[sid]
        # rating deliberately left as-is (blank for these 7) -- not fabricated
        touched += 1

assert touched == len(TOOL_FIXES), f"expected {len(TOOL_FIXES)} rows touched, got {touched}"
assert len(rows) == 1162, f"row count changed: {len(rows)}"

atomic_write(EXTRACTION, fieldnames, rows)
print("extraction_database.csv risk_of_bias_tool changes:")
for sid, old in before.items():
    print(f"  {sid}: {old!r} -> {TOOL_FIXES[sid]!r}")

# --- 2. effect_sizes.csv: S749 family correction ---
with open(EFFECT_SIZES, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    ef_fieldnames = r.fieldnames
    ef_rows = list(r)

assert len(ef_rows) == 61, f"effect_sizes row count changed: {len(ef_rows)}"

new_note = (
    "ANALYSIS_PLAN.md S2 decision tree -- re-examined 2026-09-28 as part of the "
    "Phase 11 corpus-level family judgment: this study's exposure (private vs. "
    "public/mixed-capital utility ownership) and outcome (a tariff/price-level "
    "measure) are the same KIND of comparison already recorded under Family C for "
    "S526 (private ownership vs. unit-price-ratio progressivity, US) and S539 "
    "(private ownership vs. annual household bill/income-share, US) -- leaving "
    "this row's synthesis_family blank while S526/S539 carry 'C' for the same "
    "ownership-vs-price pairing was an inconsistency, not a principled "
    "distinction, so it is corrected to Family C here. Still not pooled: the "
    "three studies' price outcomes are measured on non-identical metrics (R$/m3 "
    "tariff level here vs. a dimensionless unit-price ratio for S526 vs. a "
    "dollar bill amount/income share for S539), so this remains a "
    "structured-synthesis (SWiM) candidate grouping, not a poolable estimand -- "
    "see 06_outputs/supplementary/phase11_quantitative_feasibility_judgment.md."
)

fixed = False
for row in ef_rows:
    if row["study_id"] == "S749":
        assert row["synthesis_family"] == "", f"S749 synthesis_family was not blank: {row['synthesis_family']!r}"
        row["synthesis_family"] = "C"
        row["exclusion_from_pooling_reason"] = new_note
        fixed = True

assert fixed, "S749 row not found"
atomic_write(EFFECT_SIZES, ef_fieldnames, ef_rows)
print("\neffect_sizes.csv: S749 synthesis_family '' -> 'C', exclusion_from_pooling_reason updated")
