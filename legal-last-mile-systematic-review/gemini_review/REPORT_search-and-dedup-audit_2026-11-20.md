# Report: Workstream AA — Phase 1 & Phase 2 Search, Adapter, & Deduplication Forensic Audit (`01_search/` & `code/search/`)

*AI-generated second-model output. Not human verification.*

> **Why This Audit Was Needed:** Across all prior audits in the repository (`WEAKNESSES.md`, `2026-09-28_repository_audit.md`, and PRs #10–#34), Phase 1 & Phase 2 (`01_search/raw_exports/`, `search_log.csv`, `code/search/adapters/*.py`, and `code/search/deduplicate.py`) had never been replayed end-to-end to test whether adapter normalization and deduplication silently discarded DOIs/URLs, over-merged distinct works, or leaked cross-year/Unicode duplicates into screening.

---

## 1. Headline Findings Across `34,594` Raw Export Rows & `7,113` Merges

| Forensic Dimension | Empirical Result | Downstream Impact on Screening & Retrieval |
|---|---:|---|
| **Normalized raw-export rows replayed (`28` CSVs)** | **`34,594` rows -> `27,481` kept + `7,113` merged** | Exact deterministic reproduction of `deduplicated_records.csv` (`26,222` records) and `merge_log.csv` (`7,113` rows); `318` SHA-1 collision disambiguations |
| ** BUG AA-01 — Discarded DOIs/URLs/Authors on Merge (`deduplicate.py` L191–208)** | **`231` merges discarded metadata (`171` lost a real DOI!)** | When an earlier record without a DOI (e.g., `SEARCH_018` or ProQuest/JSTOR) matched a later Scopus/WoS record *with* a DOI via `title_year_match`, `deduplicate.py` backfilled `abstract` ONLY — **discarding `171` valid DOIs** (`6` on TA-included/unsure records that later stalled as `not_retrievable` in Phase 6, and `0` excluded as `E10`!) and failing to register the dropped DOI in `kept_doi_index`! |
| ** BUG AA-02 — Conflicting DOIs Merged via `title_year_match`** | **`50` pairs** | Two records with *different* non-empty DOIs were merged by `title_year_match` (`>= 0.92` title similarity + same year), collapsing working papers/preprints, book reviews, or multi-part articles with distinct DOIs |
| ** BUG AA-03 — Diacritic/Unicode Deletion (`re.sub(r"[^a-z0-9 ]", "", title)`)** | **`971` records (`3.5%`)** | `deduplicate.py` L95 strips non-ASCII characters *without* `unicodedata.normalize("NFKD")` (`"regularização"` -> `"regularizao"`), causing accented Portuguese/Spanish/French titles to diverge from ASCII transliterations in English indexes (`3` records reduced to empty normalized titles) |
| ** Suspicious Over-Merges in `merge_log.csv`** | **`220` flagged merges** | Includes `doi_match` merges with divergent titles (`sim < 0.65`, e.g., multiple chapters/reviews sharing one book or supplement DOI) and `title_year_match` merges where Part I / II / numeric identifiers differ |
| ** Surviving Exact-Title Cross-Year / Variant Duplicates (`>= 30` chars)** | **`127` multi-record clusters** | **`2` clusters received contradictory screening verdicts** (one copy `include`, the other `exclude`!) and **`0` clusters entered `extraction_database.csv` as multiple `Sxxx` study IDs** |

---

## 2. Recommended Pipeline Fixes (for Claude / PI)

1. **Backfill `doi`, `url`, and `authors` on merge in `code/search/deduplicate.py` (L191–208)** — and immediately insert any newly backfilled `doi` into `kept_doi_index[doi] = match_idx` so a third copy carrying that DOI also links cleanly. Recovering the `6` discarded DOIs on Phase-6 unretrieved records directly unlocks OA/institutional DOI resolution without reopening search.
2. **Normalize Unicode via `unicodedata.normalize("NFKD", ...)` before stripping non-alphanumerics** in `normalize_title()` so Portuguese, Spanish, and French diacritics match ASCII-transliterated Scopus/WoS records.
3. **Guard `doi_match` against book-chapter / book-review DOI collisions** when `SequenceMatcher` title similarity `< 0.50`, and guard `title_year_match` against Roman/Arabic part-number mismatches (`Part I` vs `Part II`).

## 3. Deliverable Files in This PR

- `search_and_dedup_audit/search_log_reconciliation_2026-11-20.csv`
- `search_and_dedup_audit/dedup_discarded_dois_urls_authors_2026-11-20.csv`
- `search_and_dedup_audit/suspicious_overmerges_audit_2026-11-20.csv`
- `search_and_dedup_audit/missed_cross_year_or_unicode_duplicates_2026-11-20.csv`
