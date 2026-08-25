#!/usr/bin/env python3
"""Deterministic deduplication of normalized search-export records.

Per REPRODUCIBILITY.md, every deduplication decision must be reproducible
by another researcher: this script never merges records silently. Two
records are merged only when they match by one of the two ordered rules
below, and every merge is written to a merge log alongside the output so
the decision can be audited.

Standard library only, consistent with this repository's existing
scrapers (see ../../../README.md).

INPUT
-----
This script does not know how to parse a platform-native export from
Scopus, Web of Science, HeinOnline, etc. -- those formats vary too much to
guess without having seen a real export, and this project's operating
rules (PROJECT_SPEC.md S14) forbid inventing structure it hasn't verified.
It instead expects each input file already normalized to a common minimal
schema, one row per record:

    title, authors, year, doi, url, database, search_id

`url` matters as much as `doi` in practice: much grey literature and many
non-indexed sources carry no DOI at all, and without a URL such a record
cannot be relocated later. Writing the per-database "raw export ->
normalized" adapters for the Tier 1 platforms is still future work, to be
done once real exports exist to develop against.

OUTPUT
------
01_search/deduplicated/deduplicated_records.csv -- one row per unique
record, in the schema expected by 02_screening/title_abstract/
screening_database.csv (record_id, database, title, authors, year, doi,
duplicate=false, decision fields blank).

01_search/deduplicated/merge_log.csv -- one row per record that was
merged into another, recording which record_id it was merged into and why
(doi_match or title_year_match), so every dedup decision survives an
audit per REPRODUCIBILITY.md S1.

USAGE
-----
    python3 deduplicate.py \\
        --input-dir ../../01_search/raw_exports_normalized \\
        --output-dir ../../01_search/deduplicated

If --input-dir contains no .csv files, the script reports that and exits
without writing fabricated output.
"""
from __future__ import annotations

import argparse
import csv
import difflib
import re
import sys
from pathlib import Path

NORMALIZED_FIELDS = ["title", "authors", "year", "doi", "url", "database", "search_id"]
OUTPUT_FIELDS = [
    "record_id", "database", "title", "authors", "year", "doi", "url",
    "duplicate", "title_abstract_decision", "full_text_decision",
    "exclusion_reason", "reviewer_1", "reviewer_2", "conflict", "final_decision",
]
MERGE_LOG_FIELDS = ["dropped_record_id", "kept_record_id", "match_rule", "dropped_title", "kept_title"]

TITLE_SIMILARITY_THRESHOLD = 0.92  # difflib ratio; conservative on purpose


def normalize_doi(doi: str) -> str:
    doi = (doi or "").strip().lower()
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi)
    return doi


def normalize_title(title: str) -> str:
    title = (title or "").strip().lower()
    title = re.sub(r"[^a-z0-9 ]", "", title)
    title = re.sub(r"\s+", " ", title)
    return title


def load_records(input_dir: Path) -> list[dict]:
    records = []
    csv_files = sorted(input_dir.glob("*.csv"))
    if not csv_files:
        print(f"No .csv files found in {input_dir} -- nothing to deduplicate.")
        print("This is expected until real, normalized search-export files exist.")
        return records
    for path in csv_files:
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            missing = set(NORMALIZED_FIELDS) - set(reader.fieldnames or [])
            if missing:
                print(f"WARNING: {path.name} is missing required columns {missing} -- skipped.")
                continue
            for row in reader:
                row["_source_file"] = path.name
                records.append(row)
    return records


def deduplicate(records: list[dict]) -> tuple[list[dict], list[dict]]:
    """Returns (kept_records, merge_log_rows). Never mutates input order beyond assignment."""
    kept: list[dict] = []
    kept_doi_index: dict[str, int] = {}
    kept_title_norm: list[str] = []
    merge_log: list[dict] = []

    for i, rec in enumerate(records, start=1):
        rec["record_id"] = f"R{i:04d}"
        doi = normalize_doi(rec.get("doi", ""))
        title_norm = normalize_title(rec.get("title", ""))

        match_idx = None
        match_rule = None

        if doi and doi in kept_doi_index:
            match_idx = kept_doi_index[doi]
            match_rule = "doi_match"
        else:
            for j, existing_title_norm in enumerate(kept_title_norm):
                if not existing_title_norm or not title_norm:
                    continue
                same_year = kept[j].get("year", "") == rec.get("year", "")
                if same_year and difflib.SequenceMatcher(None, existing_title_norm, title_norm).ratio() >= TITLE_SIMILARITY_THRESHOLD:
                    match_idx = j
                    match_rule = "title_year_match"
                    break

        if match_idx is not None:
            merge_log.append({
                "dropped_record_id": rec["record_id"],
                "kept_record_id": kept[match_idx]["record_id"],
                "match_rule": match_rule,
                "dropped_title": rec.get("title", ""),
                "kept_title": kept[match_idx].get("title", ""),
            })
            continue

        kept.append(rec)
        kept_title_norm.append(title_norm)
        if doi:
            kept_doi_index[doi] = len(kept) - 1

    return kept, merge_log


def write_output(kept: list[dict], merge_log: list[dict], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    out_path = output_dir / "deduplicated_records.csv"
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()
        for rec in kept:
            writer.writerow({
                "record_id": rec["record_id"],
                "database": rec.get("database", ""),
                "title": rec.get("title", ""),
                "authors": rec.get("authors", ""),
                "year": rec.get("year", ""),
                "doi": rec.get("doi", ""),
                "url": rec.get("url", ""),
                "duplicate": "false",
                "title_abstract_decision": "",
                "full_text_decision": "",
                "exclusion_reason": "",
                "reviewer_1": "",
                "reviewer_2": "",
                "conflict": "",
                "final_decision": "",
            })

    log_path = output_dir / "merge_log.csv"
    with log_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=MERGE_LOG_FIELDS)
        writer.writeheader()
        writer.writerows(merge_log)

    print(f"Wrote {len(kept)} unique record(s) to {out_path}")
    print(f"Wrote {len(merge_log)} merge decision(s) to {log_path}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input-dir", type=Path, required=True,
                         help="Directory of normalized search-export CSVs (schema: title, authors, year, doi, database, search_id)")
    parser.add_argument("--output-dir", type=Path, required=True,
                         help="Directory to write deduplicated_records.csv and merge_log.csv")
    args = parser.parse_args()

    records = load_records(args.input_dir)
    if not records:
        return 0

    kept, merge_log = deduplicate(records)
    write_output(kept, merge_log, args.output_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
