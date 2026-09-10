#!/usr/bin/env python3
"""Normalize a Web of Science CSV export into this project's common search schema.

**UNVALIDATED.** Written speculatively, ahead of any real Web of Science
export existing in this project -- same status the PubMed adapter had
before SEARCH_018 (see pubmed_adapter.py's own docstring), written now so
ingestion is instant once the researcher runs `database_strategies/wos.md`
per EXECUTION_CHECKLIST.md. Web of Science's web UI offers two different
CSV export shapes depending on the export button used, and this adapter
tries to handle either without guessing wrong:

  1. "Export -> Excel" (the common path, full-record or a custom field
     selection) -- readable full-word headers, e.g. "Authors",
     "Article Title", "Publication Year", "DOI", "Abstract",
     "UT (Unique WOS ID)".
  2. "Export -> Other File Formats -> Tab-delimited/plain text", if saved
     or converted to CSV -- the classic two-letter Web of Science Core
     Collection field tags, e.g. TI (title), AU (authors), PY (year),
     DI (DOI), AB (abstract), UT (accession number).

Both are covered via case-insensitive candidate-name matching, same
pattern as pubmed_adapter.py. A researcher (or anyone with a real export)
should validate this against one before trusting its output for anything
beyond a quick check, and should treat any mismatch as this adapter's
bug, not the export's -- per PROJECT_SPEC.md S14, this project never
guesses structure it hasn't verified and calls that guess validated.

Standard library only, consistent with this repository's existing
scrapers (see ../../../../README.md).

OUTPUT
------
Common schema used by ../deduplicate.py and ../../screening/
init_screening_db.py: title, authors, year, doi, url, abstract, database,
search_id. `url` is built from the WoS accession number ("UT (Unique WOS
ID)" / "UT" / "Accession Number") when present, since Web of Science
records don't reliably carry a stable public URL column of their own;
left blank if no accession number is found -- never fabricated. `database`
is hardcoded to "Web of Science"; `search_id` is supplied by the caller.

USAGE
-----
    python3 wos_adapter.py --input wos-export.csv \\
        --output ../../../01_search/raw_exports/SEARCH_0NN_WOS_YYYY-MM-DD.csv \\
        --search-id SEARCH_0NN
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

OUTPUT_FIELDS = ["title", "authors", "year", "doi", "url", "abstract", "database", "search_id"]

# Case-insensitive candidate names per target field, in preference order.
# Full-word Excel-export headers first (the more common path), then the
# classic two-letter Core Collection field tags.
FIELD_CANDIDATES = {
    "title": ["Article Title", "Title", "TI"],
    "authors": ["Authors", "Author Full Names", "AU", "AF"],
    "year": ["Publication Year", "Year", "PY"],
    "doi": ["DOI", "DI"],
    "abstract": ["Abstract", "AB"],
    "accession": ["UT (Unique WOS ID)", "UT", "Accession Number", "Accession Number (UT)"],
}
REQUIRED_KEYS = ["title", "authors", "year", "doi"]  # abstract/accession optional -- warn, don't fail


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
    parser.add_argument("--input", type=Path, required=True, help="Raw Web of Science CSV export")
    parser.add_argument("--output", type=Path, required=True, help="Path to write the normalized CSV")
    parser.add_argument("--search-id", required=True, help="search_id to stamp on every row (e.g. SEARCH_035)")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"ERROR: {args.input} does not exist.")
        return 1

    print("WARNING: this adapter is unvalidated against a real Web of Science "
          "export -- no live WoS export has existed in this project yet. "
          "Spot-check the output below before trusting it.", file=sys.stderr)

    with args.input.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames or []

        col = {key: find_column(header, candidates) for key, candidates in FIELD_CANDIDATES.items()}
        missing = [key for key in REQUIRED_KEYS if col.get(key) is None]
        if missing:
            print(f"ERROR: expected column(s) not found in {args.input}: {missing}. "
                  f"Actual header was: {header}. Refusing to guess -- fix the "
                  f"FIELD_CANDIDATES mapping above once you know the real column names.")
            return 1
        if col.get("abstract") is None:
            print("WARNING: no Abstract column found -- exported without abstracts? "
                  "Re-check the WoS export field selection (EXECUTION_CHECKLIST.md). "
                  "Continuing with abstract left blank for every row.", file=sys.stderr)
        if col.get("accession") is None:
            print("WARNING: no accession-number column found -- url will be left "
                  "blank for every row rather than guessed.", file=sys.stderr)

        rows = []
        for record in reader:
            accession = record.get(col["accession"], "").strip() if col.get("accession") else ""
            rows.append({
                "title": record.get(col["title"], "").strip(),
                "authors": record.get(col["authors"], "").strip(),
                "year": record.get(col["year"], "").strip(),
                "doi": normalize_doi(record.get(col["doi"], "")),
                "url": f"https://www.webofscience.com/wos/woscc/full-record/{accession}" if accession else "",
                "abstract": record.get(col["abstract"], "").strip() if col.get("abstract") else "",
                "database": "Web of Science",
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
