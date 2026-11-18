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

# --- RoB 2 design-variant corrections (all 5 are cluster-randomized) ---
ROB2_FIXES = {
    "S057": "RoB 2 (cluster-randomized trials variant)",
    "S085": "RoB 2 (cluster-randomized trials variant)",
    "S294": "RoB 2 (cluster-randomized trials variant)",
    "S366": "RoB 2 (cluster-randomized trials variant)",
    "S879": "RoB 2 (cluster-randomized trials variant) -- randomization unit (compound-level) inferred from recorded intervention unit, not explicitly confirmed; verify against source paper before finalizing rating",
}

# --- AMSTAR 2 corrections: clear misclassifications (narrative/conceptual/
# documentary reviews, not systematic evidence syntheses) ---
AMSTAR2_FIXES = {
    "S079": "NONE -- narrative/focused review (WIREs Water Focus Article), not a systematic review; AMSTAR 2 does not apply. RISK_OF_BIAS.md S1 has no validated tool for a non-systematic narrative review used as an evidence source (reclassified 2026-09-28 from AMSTAR 2; see CHANGELOG.md)",
    "S320": "NONE -- publication_type is itself 'narrative review', not a systematic review; AMSTAR 2 does not apply (reclassified 2026-09-28 from AMSTAR 2; see CHANGELOG.md)",
    "S322": "NONE -- publication_type is itself 'narrative review', not a systematic review; AMSTAR 2 does not apply (reclassified 2026-09-28 from AMSTAR 2; see CHANGELOG.md)",
    "S429": "NONE -- title itself says 'a narrative synthesis'; not a systematic review, AMSTAR 2 does not apply (reclassified 2026-09-28 from AMSTAR 2; see CHANGELOG.md)",
    "S430": "NONE -- study_design is itself 'narrative critical review', not a systematic review; AMSTAR 2 does not apply (reclassified 2026-09-28 from AMSTAR 2; see CHANGELOG.md)",
    "S436": "NONE -- study_design is 'qualitative documental synthesis / narrative review', not a systematic review; AMSTAR 2 does not apply (reclassified 2026-09-28 from AMSTAR 2; see CHANGELOG.md)",
    "S440": "NONE -- publication_type is itself 'narrative review' (Annual Review of Public Health article), not a systematic review; AMSTAR 2 does not apply (reclassified 2026-09-28 from AMSTAR 2; see CHANGELOG.md)",
    "S466": "NONE -- study_design is itself 'narrative comparative review', not a systematic review; AMSTAR 2 does not apply (reclassified 2026-09-28 from AMSTAR 2; see CHANGELOG.md)",
    "S479": "NONE -- publication_type is 'review article (research and policy agenda)', study_design is 'narrative review'; not a systematic review, AMSTAR 2 does not apply (reclassified 2026-09-28 from AMSTAR 2; see CHANGELOG.md)",
    "S480": "NONE -- study_design is 'documentary/regulatory-compliance review', not a systematic review of empirical evidence; AMSTAR 2 does not apply. Closer to a doctrinal/regulatory-history analysis than an evidence synthesis -- may warrant the Legal Institutional Evidence Appraisal Framework instead, but not assigned here without individual full-text confirmation (reclassified 2026-09-28 from AMSTAR 2; see CHANGELOG.md)",
    "S482": "NONE -- study_design is itself 'conceptual review' (a WIREs Focus Article / conceptual synthesis), not a systematic review of empirical evidence; AMSTAR 2 does not apply (reclassified 2026-09-28 from AMSTAR 2; see CHANGELOG.md)",
}

with open(EXTRACTION, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)

assert len(rows) == 1162

before = {}
touched = 0
for row in rows:
    sid = row["study_id"]
    if sid in ROB2_FIXES:
        before[sid] = row["risk_of_bias_tool"]
        assert row["risk_of_bias_tool"] in ("RoB 2", "ROB2"), f"{sid} unexpected prior value {row['risk_of_bias_tool']!r}"
        row["risk_of_bias_tool"] = ROB2_FIXES[sid]
        touched += 1
    elif sid in AMSTAR2_FIXES:
        before[sid] = row["risk_of_bias_tool"]
        assert "amstar" in row["risk_of_bias_tool"].lower(), f"{sid} unexpected prior value {row['risk_of_bias_tool']!r}"
        row["risk_of_bias_tool"] = AMSTAR2_FIXES[sid]
        touched += 1

assert touched == len(ROB2_FIXES) + len(AMSTAR2_FIXES) == 16, touched
atomic_write(EXTRACTION, fieldnames, rows)

print(f"Applied {touched} risk_of_bias_tool corrections:")
for sid in list(ROB2_FIXES) + list(AMSTAR2_FIXES):
    print(f"  {sid}: {before[sid]!r} -> (see new value)")
