# Native (Untouched) Platform Exports

This subfolder holds search-export files exactly as a database platform
produced them, before any adapter normalization — per
`REPRODUCIBILITY.md` §2 ("raw data is never overwritten"). The files
directly in `01_search/raw_exports/` (one level up) are this project's
common normalized schema (title, authors, year, doi, url, database,
search_id), produced by running an adapter in `code/search/adapters/`
against a native file from here.

## SEARCH_018 (Scopus, 2026-08-26)

- `SEARCH_018_SCOPUS_2026-08-26_native.csv` — the actual Scopus export,
  untouched: 500 records, all 19 original Scopus columns (Author(s) ID,
  Cited by, Volume, Issue, Page numbers, Document Type, Open Access
  status, EID, etc. — more than the common schema captures). Normalized
  into `../SEARCH_018_SCOPUS_2026-08-26.csv` via
  `code/search/adapters/scopus_adapter.py`.
- `SEARCH_018_SCOPUS_2026-08-26_analyze-by-year.csv` — not document-level
  data. This is Scopus's own "Analyze results by Year" aggregate feature
  (a count of matching documents per publication year), preserved because
  it's the source for the ~5,443 total-hit-count figure cited in
  `search_logs/search_log.csv` and `CHANGELOG.md` — not because it's
  ingestable as records.

Preserved here (rather than only in the adapter's normalized output)
because these files originally arrived as full-text PDF attachments
alongside the CSVs, uploaded to public GitHub branches — copyrighted
journal-article PDFs cannot stay in a public repository, but the
bibliographic metadata CSVs are not copyrighted content and are the
project's actual raw search-export data, so they're kept here instead of
being lost when those branches/PDFs were removed. See `CHANGELOG.md`
2026-08-26 for the full account.
