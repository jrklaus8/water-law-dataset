#!/usr/bin/env python3
"""Normalize a RIS-format citation export into this project's common search schema.

**UNVALIDATED** against any real export from any specific platform — but
grounded in the RIS tag format itself, which *is* a real, long-published
standard (unlike guessing a platform's proprietary CSV column names). RIS
is the shared export format offered by several of this project's still-
unsearched databases: HeinOnline, ProQuest and Sociological Abstracts,
JSTOR, and SSRN all offer a "RIS" or "EndNote" citation export option
alongside (or instead of) CSV — see `database_strategies/heinonline.md`,
`proquest_sociological_abstracts.md`, and `jstor_google_scholar_ssrn.md`.
One adapter covers all of them because the format, not the platform,
determines the parsing logic; `--database` stamps which platform a given
file actually came from.

Two databases from `database_strategies/` are deliberately NOT covered by
this adapter, or any other adapter in this project, and that is a
decision, not an oversight:

- **Westlaw and Lexis** (`westlaw_lexis.md`): neither platform offers a
  standard bulk RIS/CSV export the way academic databases do — exports
  are typically to Word/RTF/PDF citation lists. Writing an adapter here
  would mean guessing a structure with no real standard behind it, which
  `PROJECT_SPEC.md` S14 forbids. This needs to be built once a real
  export exists to develop against, whatever shape it turns out to be.
- **CanLII, Rechtspraak.nl, Brazilian court portals, ANA/SNIS**
  (`canlii.md`, `rechtspraak.md`, `brazil_legal_databases.md`): these
  feed the doctrinal/jurimetric strand of the project, not this
  household-level empirical screening pipeline — their own strategy
  files say explicitly not to merge hits from these sources into
  `screening_database.csv` without first classifying them as
  `study_design_class = doctrinal` or `jurimetric`. Normalizing them
  through this adapter into the same pipeline as Scopus/WoS would be
  actively wrong, not just premature.
- **Google Scholar** (`jstor_google_scholar_ssrn.md`): explicitly not
  exportable in bulk with full metadata by default; that file's own
  guidance is to screen by relevance ranking and log a cutoff, not to
  build an export-parsing adapter that doesn't correspond to anything
  the platform actually offers.

RIS tag reference used here (tags vary slightly by exporting platform,
so multiple variants are accepted per field):

    TY  - record type (ignored beyond existence-checking)
    AU  - author (repeatable; joined with "; ")
    TI / T1 - title
    PY / Y1 - year (may include full date, e.g. "2020/03/15" -- only the
              leading year is kept)
    DO  - DOI
    AB / N2 - abstract
    UR / L1 / L2 - URL
    ER  - end of record (required terminator per the RIS spec)

Standard library only, consistent with this repository's existing
scrapers (see ../../../../README.md).

OUTPUT
------
Common schema used by ../deduplicate.py and ../../screening/
init_screening_db.py: title, authors, year, doi, url, abstract, database,
search_id. `database` comes from the required --database flag (e.g.
"HeinOnline", "ProQuest", "JSTOR", "SSRN", "Sociological Abstracts") since
RIS itself doesn't reliably say which platform produced it.

USAGE
-----
    python3 ris_adapter.py --input heinonline-export.ris \\
        --output ../../../01_search/raw_exports/SEARCH_0NN_HEINONLINE_YYYY-MM-DD.csv \\
        --search-id SEARCH_0NN --database HeinOnline
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

OUTPUT_FIELDS = ["title", "authors", "year", "doi", "url", "abstract", "database", "search_id"]

TITLE_TAGS = {"TI", "T1"}
YEAR_TAGS = {"PY", "Y1"}
DOI_TAGS = {"DO"}
ABSTRACT_TAGS = {"AB", "N2"}
URL_TAGS = {"UR", "L1", "L2"}
AUTHOR_TAGS = {"AU", "A1"}

RIS_LINE_RE = re.compile(r"^([A-Z][A-Z0-9])  - (.*)$")


def parse_ris(text: str) -> list[dict]:
    """Parses RIS text into a list of tag->list-of-values dicts, one per record."""
    records = []
    current: dict[str, list[str]] = {}
    for raw_line in text.splitlines():
        line = raw_line.rstrip("\r\n")
        if not line.strip():
            continue
        m = RIS_LINE_RE.match(line)
        if not m:
            # Continuation of the previous tag's value (some exporters wrap long fields)
            if current:
                last_tag = next(reversed(current), None)
                if last_tag and current[last_tag]:
                    current[last_tag][-1] += " " + line.strip()
            continue
        tag, value = m.group(1), m.group(2).strip()
        if tag == "TY":
            if current:
                records.append(current)
            current = {}
        if tag == "ER":
            if current:
                records.append(current)
            current = {}
            continue
        current.setdefault(tag, []).append(value)
    if current:
        records.append(current)
    return records


def first_of(rec: dict, tags: set[str]) -> str:
    for tag in tags:
        if tag in rec and rec[tag]:
            return rec[tag][0].strip()
    return ""


def extract_year(rec: dict) -> str:
    raw = first_of(rec, YEAR_TAGS)
    m = re.match(r"(\d{4})", raw)
    return m.group(1) if m else raw


def extract_authors(rec: dict) -> str:
    for tag in AUTHOR_TAGS:
        if tag in rec and rec[tag]:
            return "; ".join(a.strip() for a in rec[tag])
    return ""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", type=Path, required=True, help="Raw RIS export (.ris or .txt)")
    parser.add_argument("--output", type=Path, required=True, help="Path to write the normalized CSV")
    parser.add_argument("--search-id", required=True, help="search_id to stamp on every row (e.g. SEARCH_035)")
    parser.add_argument("--database", required=True,
                         help="Which platform this export came from, e.g. HeinOnline, ProQuest, JSTOR, SSRN, "
                              "'Sociological Abstracts' -- stamped on every row since RIS itself doesn't say.")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"ERROR: {args.input} does not exist.")
        return 1

    print(f"WARNING: this adapter is unvalidated against a real {args.database} export -- "
          f"no live export from this platform has existed in this project yet. "
          f"Spot-check the output below before trusting it.", file=sys.stderr)

    text = args.input.read_text(encoding="utf-8-sig", errors="replace")
    ris_records = parse_ris(text)
    if not ris_records:
        print(f"ERROR: no RIS records found in {args.input} (no 'ER  - ' terminators, or empty file). "
              f"Is this actually a RIS export? First 200 chars: {text[:200]!r}")
        return 1

    rows = []
    missing_title = 0
    for rec in ris_records:
        title = first_of(rec, TITLE_TAGS)
        if not title:
            missing_title += 1
            continue
        rows.append({
            "title": title,
            "authors": extract_authors(rec),
            "year": extract_year(rec),
            "doi": first_of(rec, DOI_TAGS),
            "url": first_of(rec, URL_TAGS),
            "abstract": first_of(rec, ABSTRACT_TAGS),
            "database": args.database,
            "search_id": args.search_id,
        })

    if missing_title:
        print(f"WARNING: skipped {missing_title} RIS record(s) with no title tag (TI/T1) -- "
              f"malformed record or an unsupported RIS variant, not silently guessed.", file=sys.stderr)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} normalized record(s) to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
