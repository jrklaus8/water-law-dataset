# Task F Report: Search-Gap Strategy Drafting (SSRN, Westlaw, Lexis+)

*AI-generated second-model output. Not human verification.*

- **Date:** 2026-11-18
- **Model:** `gemini-4-carbon-medium` (`Gemini-gemini-4-carbon-medium-search-gap-strings-2026-11-18`)
- **Deliverables:**
  - `gemini_review/search_gap/SSRN_WESTLAW_LEXIS_SEARCH_STRINGS_2026-11-18.md`
  - `gemini_review/search_gap/SEARCH_LOG_TEMPLATE_2026-11-18.csv`
  - `gemini_review/RUN_LOG_search-gap-strings_2026-11-18.md`

---

## 1. Summary of Adapted Search Strings Delivered (`12` Queries)

1. **SSRN (`SEARCH_042a`–`SEARCH_042f`, 6 modular subqueries, each `125–183` characters):**
   - Replaces the single 186-character draft in `jstor_google_scholar_ssrn.md` so no query hits SSRN's ~250-character parser truncation limit, while expanding coverage to tariffs/social tariffs, shutoffs/disconnections, utility ownership/privatization, rate regulation, municipal underbounding, and the protocol's Portuguese (`§3.1`) and Dutch (`§3.2`) vocabularies.
2. **Westlaw Precision / Edge (`SEARCH_043a`–`SEARCH_043c`, Secondary Sources -> Law Reviews & Journals):**
   - Fixes missing `adv:` Terms & Connectors prefix, adds missing `wastewater` / `sewerage` and US municipal/utility access vocabulary (`unincorporated`, `underbound!`, `colonia!`, `shutoff!`, `disconnect!`, `"rate regulation"`, `tariff!`), and pairs a high-precision fielded pass (`TI,PR,SY`, `SEARCH_043a`) with a paragraph-proximity + empirical-methods filter pass (`SEARCH_043b`) plus the syntax-corrected protocol benchmark string (`SEARCH_043c`).
3. **Lexis+ / Lexis Advance (`SEARCH_044a`–`SEARCH_044c`, Secondary Materials -> Law Reviews and Journals):**
   - Replaces document-wide `AND` in `westlaw_lexis.md` (which produces tens of thousands of full-text false positives on long law-review articles, as seen in HeinOnline `SEARCH_036`) with a fielded `TITLE + OVERVIEW` query (`SEARCH_044a`), a same-paragraph `W/p` + empirical-methods query (`SEARCH_044b`), and a Canada/Ontario secondary-scholarship query (`SEARCH_044c`), noting Lexis+'s native `RIS` (500-item) and `.xlsx` (1,000-item) export options.

---

## 2. Repository Discrepancies Spotted During Search Audit (Section 5.3; Protected Files Left Untouched)

1. **Unlogged `NOT RUN` databases (`PubMed`, `Global Health`, `Google Scholar`):** `SEARCH_PROTOCOL.md` §1 explicitly lists **PubMed** and **Global Health (Ovid)** as planned sector-specific databases and **Google Scholar** as a planned Tier 2 database (`01_search/database_strategies/pubmed.md`, `jstor_google_scholar_ssrn.md`, and `code/search/adapters/pubmed_adapter.py` all exist), yet `01_search/search_logs/search_log.csv`, `SEARCH_PROTOCOL.md` §7 (*"Databases never searched at all"*), `START_HERE.md`, and `WEAKNESSES.md` (`W01`) only disclose **SSRN** and **Westlaw/Lexis** as never searched! Claude should add explicit `NOT RUN` rows (`SEARCH_044_PUBMED`, `SEARCH_045_GLOBAL_HEALTH`, `SEARCH_046_GOOGLE_SCHOLAR`) to `search_log.csv` and update `SEARCH_PROTOCOL.md` §7 and `W01` so PRISMA 2020 Item 6/7 reporting is complete.
2. **Multilingual strings in `SEARCH_PROTOCOL.md` §3 were never run in any bibliographic database:** Although `SEARCH_PROTOCOL.md` §5 step 3 specifies running the Portuguese, Dutch, and Canada/Ontario vocabulary blocks (§3), `search_log.csv` shows only English strings were ever run in Scopus, WoS, ProQuest, HeinOnline, and JSTOR (the Portuguese and Dutch terms were used only in 4 non-systematic 8-hit `WebSearch` pilot queries `SEARCH_005/006/015/016`).
3. **Stale `SEARCH_018` next-ID text in `01_search/EXECUTION_CHECKLIST.md` (lines 18, 61–65, 189):** `EXECUTION_CHECKLIST.md` still states *"Everything Claude has done in this project so far has been title-only"* and *"the highest `SEARCH_0NN` used so far is `SEARCH_017`"*, predating `SEARCH_018`–`SEARCH_043`.
