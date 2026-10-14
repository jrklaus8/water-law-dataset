#!/usr/bin/env python3
"""
Closes the full-text retrieval phase (Phase 6) by researcher decision,
2026-09-28: the researcher's institutional access to further database
providers is exhausted, and no further full-text retrieval will occur.
This mirrors the search-phase closure of 2026-09-11 (SEARCH_PROTOCOL.md
S7) -- a judgment call to stop, not a claim of exhaustion.

For every record with no final_decision (never screened, because the
correct full text was never obtained):
  - wrong_file_retrieved records keep that status (it remains the most
    informative label -- a delivery WAS attempted and failed) but get a
    closure note appended.
  - every other status (blank, not_retrievable, no_oa_copy_found,
    oa_page_candidate, undecided) is normalized to 'not_retrievable', the
    schema-documented DATA_DICTIONARY.md enum value, with a closure note
    appended.

final_decision is NOT touched -- these records were never screened and
stay correctly blank, per the project's standing rule against forcing a
decision when the correct source material was never in hand.
"""
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"

DATE = "2026-09-28"
CLOSURE_NOTE = (
    "Full-text retrieval phase (Phase 6) formally closed by researcher "
    "decision, 2026-09-28: the researcher's institutional access to "
    "further database providers is exhausted; no further full-text "
    "retrieval attempts will be made for this record. This is a closure "
    "by judgment call (the corpus is judged large and comprehensive "
    "enough for the review's purposes), not a claim that the record is "
    "provably unobtainable by any means -- exactly parallel to the "
    "2026-09-11 database-search closure. See CHANGELOG.md, 'Full-text "
    "retrieval phase closed,' 2026-09-28."
)


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

n_wrong_file = 0
n_reclassified = 0

for row in rows:
    if row.get("final_decision", "") != "":
        continue  # already screened; not part of the closure population

    existing_notes = row.get("notes", "")
    row["notes"] = (existing_notes + " " if existing_notes else "") + CLOSURE_NOTE

    if row.get("full_text_status") == "wrong_file_retrieved":
        n_wrong_file += 1
        # status stays wrong_file_retrieved -- more informative than
        # overwriting it with a generic label
    else:
        row["full_text_status"] = "not_retrievable"
        n_reclassified += 1

atomic_write(PATH, fieldnames, rows)

print(f"Closure applied: {n_wrong_file} wrong_file_retrieved records noted (status unchanged), "
      f"{n_reclassified} other records reclassified to 'not_retrievable'.")
print(f"Total closed population: {n_wrong_file + n_reclassified}")
