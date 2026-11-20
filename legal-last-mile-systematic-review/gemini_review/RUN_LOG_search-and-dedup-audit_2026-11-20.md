# Run Log: Workstream AA — Phase 1 & Phase 2 Search, Adapter, & Deduplication Forensic Audit (`36,307` Raw Rows -> `26,222` Records)

*AI-generated second-model output. Not human verification.*

- **Ledger label:** `Gemini-gemini-4-carbon-medium-search-dedup-audit-2026-11-20`
- **Human-checked count for `AI_USE_LEDGER`:** `0` (`01_search/` and `02_screening/` untouched)
- **Git base commit (`main`):** `2cd44e7`
- **Working branch:** `gemini/search-and-dedup-forensic-audit-2026-11-20`
- **Method:** Deterministic Python replay of `code/search/deduplicate.py` across all `34,594` normalized raw export rows (`28` CSVs in `01_search/raw_exports/`), full reconciliation against `01_search/search_logs/search_log.csv` (`44` rows), and cross-check against `merge_log.csv` (`7,113` merges), `deduplicated_records.csv` (`27,481` unique records), `screening_database.csv`, and `full_text_screening_database.csv`.
- **`GEMINI_HANDOFF_BRIEF_2026-11-17.md` SHA-256:** `988b522f9d5f86c167fc913e5976cb448274fc2e6d526e0733f7c1f1baf31303`
