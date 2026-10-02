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
pattern as pubmed_adapter.py. The tab-delimited path (the classic "Export
-> Plain Text" file, literally named `savedrecs.txt` by Web of Science's
own UI) is auto-detected by checking whether the header line contains
more tabs than commas, rather than assumed from a CSV file extension.
Validated 2026-09-11 against a real `savedrecs.txt` batch (SEARCH_035).

Web of Science's UI caps a single export at 1,000 records and names
sequential batches from the same result set `savedrecs.txt`,
`savedrecs(1).txt`, `savedrecs(2).txt`, ... -- `--input` accepts more than
one file so all batches of one search can be merged into a single
normalized output in one call.

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
    python3 wos_adapter.py --input savedrecs.txt savedrecs2.txt \\
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


def sniff_delimiter(sample_line: str) -> str:
    """WoS's tab-delimited export (savedrecs.txt) has far more tabs than
    commas in its header line; a real CSV export has the opposite. Simple
    and reliable for this specific choice, unlike csv.Sniffer against
    author-name fields that legitimately contain commas."""
    return "\t" if sample_line.count("\t") > sample_line.count(",") else ","


def load_records(path: Path) -> tuple[list[str], list[dict]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        first_line = f.readline()
        delimiter = sniff_delimiter(first_line)
        f.seek(0)
        # WoS's tab-delimited plain-text export does not escape/quote embedded
        # double-quote characters -- an abstract that happens to quote a term
        # (very common) has a stray " that, under csv's default QUOTE_MINIMAL,
        # gets treated as opening a quoted field and silently swallows every
        # tab and newline until some *later* " closes it, merging or corrupting
        # multiple records. Found this by comparing raw physical line counts
        # against parsed row counts on a real export (1000 lines -> 988 rows).
        # QUOTE_NONE treats every character, including ", as a literal --
        # correct for this format, which has no field-quoting mechanism at all.
        quoting = csv.QUOTE_NONE if delimiter == "\t" else csv.QUOTE_MINIMAL
        reader = csv.DictReader(f, delimiter=delimiter, quoting=quoting)
        header = reader.fieldnames or []
        records = list(reader)
    return header, records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", type=Path, required=True, nargs="+",
                         help="One or more raw Web of Science export files (CSV or tab-delimited "
                              "savedrecs.txt-style) -- pass all batches of one search together")
    parser.add_argument("--output", type=Path, required=True, help="Path to write the normalized CSV")
    parser.add_argument("--search-id", required=True, help="search_id to stamp on every row (e.g. SEARCH_035)")
    args = parser.parse_args()

    for path in args.input:
        if not path.exists():
            print(f"ERROR: {path} does not exist.")
            return 1

    print("WARNING: this adapter's CSV-Excel-export path is unvalidated against a real "
          "Web of Science export -- the tab-delimited savedrecs.txt path was validated "
          "2026-09-11 (SEARCH_035). Spot-check the output below before trusting it.", file=sys.stderr)

    rows = []
    for path in args.input:
        header, records = load_records(path)

        col = {key: find_column(header, candidates) for key, candidates in FIELD_CANDIDATES.items()}
        missing = [key for key in REQUIRED_KEYS if col.get(key) is None]
        if missing:
            print(f"ERROR: expected column(s) not found in {path}: {missing}. "
                  f"Actual header was: {header}. Refusing to guess -- fix the "
                  f"FIELD_CANDIDATES mapping above once you know the real column names.")
            return 1
        if col.get("abstract") is None:
            print(f"WARNING: no Abstract column found in {path} -- exported without abstracts? "
                  "Re-check the WoS export field selection (EXECUTION_CHECKLIST.md). "
                  "Continuing with abstract left blank for every row.", file=sys.stderr)
        if col.get("accession") is None:
            print(f"WARNING: no accession-number column found in {path} -- url will be left "
                  "blank for every row rather than guessed.", file=sys.stderr)

        for record in records:
            # csv.DictReader gives None (not "") for trailing columns missing on a
            # ragged/short row -- WoS's tab-delimited export has these often enough
            # (e.g. a record with no DOI leaves a short row) that this isn't rare.
            def field(key: str) -> str:
                col_name = col.get(key)
                return (record.get(col_name) or "").strip() if col_name else ""

            accession = field("accession")
            rows.append({
                "title": field("title"),
                "authors": field("authors"),
                "year": field("year"),
                "doi": normalize_doi(field("doi")),
                "url": f"https://www.webofscience.com/wos/woscc/full-record/{accession}" if accession else "",
                "abstract": field("abstract"),
                "database": "Web of Science",
                "search_id": args.search_id,
            })

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} normalized record(s) from {len(args.input)} input file(s) to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
