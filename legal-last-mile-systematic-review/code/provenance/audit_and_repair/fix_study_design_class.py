import csv, os, tempfile, sys
csv.field_size_limit(sys.maxsize)

ED_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/03_extraction/extracted_data/extraction_database.csv"
EM_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/descriptive/evidence_map.csv"

with open(ED_PATH, newline="") as f:
    ed_rows = list(csv.DictReader(f))
ed_by_id = {r["study_id"]: r for r in ed_rows}
assert len(ed_rows) == 1162

with open(EM_PATH, newline="") as f:
    reader = csv.DictReader(f)
    em_fieldnames = reader.fieldnames
    em_rows = list(reader)
assert len(em_rows) == 1162

CANON = {
    "RoB2": "experimental",
    "ROBINS-I": "quasi_experimental",
    "JBI": "observational",
    "MMAT": "mixed_methods",
    "CASP": "qualitative",
    "AMSTAR2": "systematic_review_secondary",
}

def tool_bucket(t):
    t = t.strip()
    if t.startswith("NONE"):
        return "NONE"
    if t.startswith("RoB 2"):
        return "RoB2"
    if t.startswith("ROBINS-I"):
        return "ROBINS-I"
    if "JBI" in t:
        return "JBI"
    if t.startswith("MMAT") or "Mixed Methods Appraisal" in t:
        return "MMAT"
    if "CASP" in t:
        return "CASP"
    if "AMSTAR" in t:
        return "AMSTAR2"
    if "Legal Institutional" in t:
        return "LegalFramework"
    return "OTHER"

touched = 0
for row in em_rows:
    sid = row["study_id"]
    ed_row = ed_by_id.get(sid)
    if not ed_row:
        continue
    bucket = tool_bucket(ed_row["risk_of_bias_tool"])
    if bucket not in CANON:
        continue
    canonical = CANON[bucket]
    if row["study_design_class"].strip() != canonical:
        row["study_design_class"] = canonical
        touched += 1

assert touched == 228, touched
assert len(em_rows) == 1162

fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(EM_PATH), suffix=".tmp")
with os.fdopen(fd, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=em_fieldnames)
    writer.writeheader()
    writer.writerows(em_rows)
os.replace(tmp_path, EM_PATH)

print("OK, touched", touched, "rows")
