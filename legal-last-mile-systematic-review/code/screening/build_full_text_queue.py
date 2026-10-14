#!/usr/bin/env python3
"""Build a working retrieval queue from the full-text screening database.

full_text_screening_database.csv (see init_full_text_db.py) is the
authoritative record but is not a convenient work list: it carries every
seeded record regardless of progress, and it lacks the `database` field
(Scopus, ProQuest, JSTOR, ...) that screening_database.csv has -- knowing
which platform a record came from is exactly what lets the researcher
batch retrieval by platform instead of context-switching every row.

This script's only job is to produce that work list. It never writes to
full_text_screening_database.csv itself -- see update_full_text_record.py
for that -- and the queue it produces is disposable and fully
regenerable: rerun this any time to get a fresh, up-to-date queue.

Standard library only, consistent with this repository's existing
scrapers (see ../../../README.md).

INPUT
-----
--full-text-db : path to 02_screening/full_text/full_text_screening_database.csv
--screening-db : path to 02_screening/title_abstract/screening_database.csv
                 (used only to look up each record's source `database`)
--queue-out    : path to write the queue CSV to

BEHAVIOR
--------
Includes only records with no final_decision yet (i.e. still open work):
retrieval not yet done, or retrieved but not yet screened. Sorted by
database, then year descending, so retrieval can be batched one platform
at a time. Already-decided records are left out entirely -- there is
nothing left to do on them.

USAGE
-----
    python3 build_full_text_queue.py \\
        --full-text-db ../../02_screening/full_text/full_text_screening_database.csv \\
        --screening-db ../../02_screening/title_abstract/screening_database.csv \\
        --queue-out ../../02_screening/full_text/full_text_retrieval_queue.csv
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

OUTPUT_FIELDS = [
    "record_id", "database", "title", "authors", "year", "doi", "url",
    "full_text_status", "full_text_location", "notes",
]


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--full-text-db", type=Path, required=True)
    parser.add_argument("--screening-db", type=Path, required=True)
    parser.add_argument("--queue-out", type=Path, required=True)
    args = parser.parse_args()

    if not args.full_text_db.exists():
        print(f"No full-text database at {args.full_text_db} -- run init_full_text_db.py first.")
        return 0

    full_text_records = read_csv(args.full_text_db)
    database_by_id = {r["record_id"]: r.get("database", "") for r in read_csv(args.screening_db)}

    open_records = [r for r in full_text_records if not (r.get("final_decision") or "").strip()]

    def sort_key(r: dict):
        database = database_by_id.get(r["record_id"], "")
        try:
            year = -int(r.get("year") or 0)
        except ValueError:
            year = 0
        return (database, year)

    open_records.sort(key=sort_key)

    args.queue_out.parent.mkdir(parents=True, exist_ok=True)
    with args.queue_out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()
        for r in open_records:
            writer.writerow({
                "record_id": r["record_id"],
                "database": database_by_id.get(r["record_id"], ""),
                "title": r.get("title", ""),
                "authors": r.get("authors", ""),
                "year": r.get("year", ""),
                "doi": r.get("doi", ""),
                "url": r.get("url", ""),
                "full_text_status": r.get("full_text_status", ""),
                "full_text_location": r.get("full_text_location", ""),
                "notes": r.get("notes", ""),
            })

    print(f"Wrote {len(open_records)} open record(s) to {args.queue_out}")
    print(f"({len(full_text_records) - len(open_records)} of {len(full_text_records)} already have a final_decision and were left out.)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
