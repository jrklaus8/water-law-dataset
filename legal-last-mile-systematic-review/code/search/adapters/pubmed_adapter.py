#!/usr/bin/env python3
"""Normalize a PubMed CSV export into this project's common search schema.

**UNVALIDATED.** This adapter is written against PubMed's documented,
long-stable CSV export format (PubMed search results -> Save -> Format:
CSV -> Selection: All results), which produces columns:

    PMID, Title, Authors, Citation, First Author, Journal/Book,
    Publication Year, Create Date, PMCID, NIHMS ID, DOI

It has **not** been run against a real export in this session -- this
environment's network egress is blocked for PubMed (see
SEARCH_PROTOCOL.md S7 and CHANGELOG.md, 2026-08-25), so there was no live
export to develop against. A researcher (or anyone with a real export)
should validate this against one before trusting its output for anything
beyond a quick check, and should treat any mismatch as this adapter's bug,
not the export's. It is deliberately defensive (case-insensitive header
matching, tolerant of a missing column) so a small format drift doesn't
crash it outright, but tolerance is not the same as correctness.

Standard library only, consistent with this repository's existing
scrapers (see ../../../../README.md).

OUTPUT
------
Common schema used by ../deduplicate.py and ../../screening/
init_screening_db.py: title, authors, year, doi, url, database, search_id.
`database` is hardcoded to "PubMed"; `search_id` is supplied by the caller
since a PubMed export does not identify which search produced it.

USAGE
-----
    python3 pubmed_adapter.py --input pubmed-export.csv \\
        --output ../../../01_search/raw_exports/SEARCH_0NN_PUBMED_YYYY-MM-DD.csv \\
        --search-id SEARCH_0NN
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

OUTPUT_FIELDS = ["title", "authors", "year", "doi", "url", "database", "search_id"]

# Case-insensitive candidate names per target field, in preference order.
# PubMed's own documented header is first; fallbacks cover minor variants
# seen in the wild (e.g. some export tools rename "Publication Year").
FIELD_CANDIDATES = {
    "title": ["Title"],
    "authors": ["Authors", "Author(s)"],
    "year": ["Publication Year", "Year"],
    "doi": ["DOI"],
    "pmid": ["PMID", "PubMed ID"],
}


def find_column(header: list[str], candidates: list[str]) -> str | None:
    lower_map = {h.lower(): h for h in header}
    for candidate in candidates:
        if candidate.lower() in lower_map:
            return lower_map[candidate.lower()]
    return None


def normalize_doi(doi: str) -> str:
    doi = (doi or "").strip()
    if doi.lower().startswith("doi:"):
        doi = doi[4:].strip()
    return doi


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", type=Path, required=True, help="Raw PubMed CSV export")
    parser.add_argument("--output", type=Path, required=True, help="Path to write the normalized CSV")
    parser.add_argument("--search-id", required=True, help="search_id to stamp on every row (e.g. SEARCH_018)")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"ERROR: {args.input} does not exist.")
        return 1

    print("WARNING: this adapter is unvalidated against a real PubMed export "
          "in this session (network egress to PubMed is blocked here). "
          "Spot-check the output below before trusting it.", file=sys.stderr)

    with args.input.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames or []

        col = {key: find_column(header, candidates) for key, candidates in FIELD_CANDIDATES.items()}
        missing = [key for key, found in col.items() if found is None and key != "pmid"]
        if missing:
            print(f"ERROR: expected column(s) not found in {args.input}: {missing}. "
                  f"Actual header was: {header}. Refusing to guess -- fix the "
                  f"FIELD_CANDIDATES mapping above once you know the real column names.")
            return 1

        rows = []
        for record in reader:
            pmid = record.get(col["pmid"], "").strip() if col["pmid"] else ""
            rows.append({
                "title": record.get(col["title"], "").strip(),
                "authors": record.get(col["authors"], "").strip(),
                "year": record.get(col["year"], "").strip(),
                "doi": normalize_doi(record.get(col["doi"], "")),
                "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else "",
                "database": "PubMed",
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
