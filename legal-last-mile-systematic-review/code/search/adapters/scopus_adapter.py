#!/usr/bin/env python3
"""Normalize a Scopus CSV export into this project's common search schema.

**Validated against a real export** (2026-08-26, 500 records, pilot search
string from database_strategies/scopus.md) -- unlike pubmed_adapter.py,
this one is not a guess against documentation. The confirmed real Scopus
CSV header is:

    Authors, Author full names, Author(s) ID, Title, Year, Source title,
    Volume, Issue, Art. No., Page start, Page end, Cited by, DOI, Link,
    Document Type, Publication Stage, Open Access, Source, EID

Note: this export did NOT include an Abstract column -- the Scopus export
field-picker apparently needs Abstract selected explicitly and separately
from the default citation fields (see EXECUTION_CHECKLIST.md's emphasis on
this). If a future export does include one, this adapter should be
extended to map it through rather than silently dropping it -- check the
header for an "Abstract" column before assuming it's absent.

Standard library only, consistent with this repository's existing
scrapers (see ../../../../README.md).

OUTPUT
------
Common schema used by ../deduplicate.py and ../../screening/
init_screening_db.py: title, authors, year, doi, url, database, search_id.
`url` is taken from Scopus's own "Link" column (a stable scopus.com
permalink) rather than constructed. `database` is hardcoded to "Scopus";
`search_id` is supplied by the caller.

USAGE
-----
    python3 scopus_adapter.py --input scopus-export.csv \\
        --output ../../../01_search/raw_exports/SEARCH_018_SCOPUS_2026-08-26.csv \\
        --search-id SEARCH_018
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

OUTPUT_FIELDS = ["title", "authors", "year", "doi", "url", "database", "search_id"]
REQUIRED_COLUMNS = ["Authors", "Title", "Year", "DOI", "Link"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", type=Path, required=True, help="Raw Scopus CSV export")
    parser.add_argument("--output", type=Path, required=True, help="Path to write the normalized CSV")
    parser.add_argument("--search-id", required=True, help="search_id to stamp on every row (e.g. SEARCH_018)")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"ERROR: {args.input} does not exist.")
        return 1

    with args.input.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames or []
        missing = [c for c in REQUIRED_COLUMNS if c not in header]
        if missing:
            print(f"ERROR: expected column(s) not found: {missing}. Actual header: {header}. "
                  f"Scopus may have changed its export format -- fix REQUIRED_COLUMNS/the field "
                  f"mapping below once you know the real column names, don't guess.")
            return 1

        has_abstract = "Abstract" in header
        if has_abstract:
            print("NOTE: this export includes an Abstract column, but this adapter does not yet "
                  "map it through (see module docstring) -- extend it before relying on this run "
                  "for real title/abstract screening.", file=sys.stderr)

        rows = []
        for record in reader:
            rows.append({
                "title": record.get("Title", "").strip(),
                "authors": record.get("Authors", "").strip(),
                "year": record.get("Year", "").strip(),
                "doi": record.get("DOI", "").strip(),
                "url": record.get("Link", "").strip(),
                "database": "Scopus",
                "search_id": args.search_id,
            })

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} normalized record(s) to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
