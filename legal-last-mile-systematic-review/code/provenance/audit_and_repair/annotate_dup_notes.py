import csv, os, tempfile, sys
csv.field_size_limit(sys.maxsize)

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"

with open(PATH, newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

assert len(rows) == 3659

ANNOTATIONS = {
    "RF25B3781B68F": (
        " Title/author-similarity audit, 2026-09-28: this record's title and authors "
        "(Coville, Galiani, Gertler, Yoshida, 'Financing Municipal Water and Sanitation "
        "Services in Nairobi's Informal Settlements') closely match already-included "
        "record R4D81D56EA98B (S879, final_decision=include), an earlier/alternate "
        "database indexing of the same underlying paper (2020 ProQuest vs. 2025 Scopus). "
        "Not independently confirmed by full-text comparison, since this record's own "
        "full text was never retrieved (not_retrievable) -- flagged as a probable "
        "duplicate on title/author grounds only, per "
        "01_search/deduplicated/title_author_duplicate_audit_2026-09-28.md. Left "
        "not_retrievable rather than reclassified to exclude/E08, since that would claim "
        "a certainty (direct full-text comparison) this audit does not have; this note "
        "exists so the record's non-retrieval is not read as unqualified lost evidence."
    ),
    "RA62BAA92506A": (
        " Title/author-similarity audit, 2026-09-28: this record's title and authors "
        "(Coville, Galiani, Gertler, Yoshida, 'Financing Municipal Water and Sanitation "
        "Services in Nairobi's Informal Settlements') closely match already-included "
        "record R4D81D56EA98B (S879, final_decision=include), a further alternate "
        "database indexing of the same underlying paper (2021 ProQuest vs. 2025 Scopus; "
        "see also RF25B3781B68F, a 2020 ProQuest indexing of the same paper). Not "
        "independently confirmed by full-text comparison, since this record's own full "
        "text was never retrieved (not_retrievable) -- flagged as a probable duplicate on "
        "title/author grounds only, per "
        "01_search/deduplicated/title_author_duplicate_audit_2026-09-28.md."
    ),
    "R80C0C7C65752": (
        " Title/author-similarity audit, 2026-09-28: this record's title and sole author "
        "(Taing L., 'Policy implementation considerations for basic services: A South "
        "African urban sanitation case') closely match already-included record "
        "RAE15E6363DF0 (final_decision=include), an earlier Scopus indexing of the same "
        "paper (2019 vs. this record's 2020). Not independently confirmed by full-text "
        "comparison, since this record's own full text was never retrieved (the wrong "
        "file arrived, as this record's own note above already documents) -- flagged as "
        "a probable duplicate on title/author grounds only, per "
        "01_search/deduplicated/title_author_duplicate_audit_2026-09-28.md."
    ),
    "R962EAA5E4835": (
        " Title/author-similarity audit, 2026-09-28: this record's title and sole author "
        "(McCullough, Jason, 'Square peg, round hole: Ontario First Nations technical "
        "staff perspectives on federal drinking water infrastructure policies, programs "
        "and processes') are a probable duplicate/alternate-title indexing of "
        "already-included record R05D446594BE6 ('Square Peg, Round Hole: First Nations "
        "Drinking Water Infrastructure and Federal Policies, Programs, and Processes', "
        "same author, same year, final_decision=include) -- likely the same underlying "
        "dissertation/thesis indexed under a shortened title in one database export. Not "
        "independently confirmed by full-text comparison, since this record's own full "
        "text was never retrieved (not_retrievable) -- flagged as a probable duplicate on "
        "title/author grounds only, per "
        "01_search/deduplicated/title_author_duplicate_audit_2026-09-28.md. See also "
        "R40E7D0B743D0, a further indexing of the same underlying work."
    ),
    "R40E7D0B743D0": (
        " Title/author-similarity audit, 2026-09-28: this record's title and sole author "
        "(McCullough, Jason, 'Square peg, round hole: Ontario First Nations technical "
        "staff perspectives on federal drinking water infrastructure policies, programs "
        "and processes') are a probable duplicate/alternate-title indexing of "
        "already-included record R05D446594BE6 ('Square Peg, Round Hole: First Nations "
        "Drinking Water Infrastructure and Federal Policies, Programs, and Processes', "
        "same author, similar year, final_decision=include) -- likely the same underlying "
        "dissertation/thesis indexed under a shortened title in one database export. Not "
        "independently confirmed by full-text comparison, since this record's own full "
        "text was never retrieved (not_retrievable) -- flagged as a probable duplicate on "
        "title/author grounds only, per "
        "01_search/deduplicated/title_author_duplicate_audit_2026-09-28.md. See also "
        "R962EAA5E4835, a further indexing of the same underlying work."
    ),
}

touched = 0
for row in rows:
    rid = row["record_id"]
    if rid in ANNOTATIONS:
        assert ANNOTATIONS[rid][:1] == " "
        row["notes"] = row["notes"] + ANNOTATIONS[rid]
        touched += 1

assert touched == 5, touched
assert len(rows) == 3659

fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(PATH), suffix=".tmp")
with os.fdopen(fd, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp_path, PATH)

print("OK, touched", touched, "rows")
