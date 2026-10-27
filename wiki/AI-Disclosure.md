# AI Disclosure

This project was built with the assistance of **Claude** (developed by Anthropic) and, for one repository audit, **Antigravity** (Google DeepMind). This page documents the nature and scope of that assistance in the interest of transparency. It covers the court-decisions dataset first and the systematic review second.

---

## What Claude Did

### 1. Scraper Development
Claude wrote and debugged the web scrapers for:
- **Brazilian state courts** — handling varied backends (ESAJ POST, Elasticsearch REST, Rails GET, ASP.NET WebForms, PHP+Solr)
- **CanLII (Canada)** — REST API integration including pagination and date filtering fixes
- **Rechtspraak.nl (Netherlands)** — Open Data XML API, including the expanded multi-court crawler

Claude also diagnosed and worked around infrastructure issues including CAPTCHA blocks, TLS errors, rate limiting (HTTP 429), and DNS failures across the 27 Brazilian courts attempted.

### 2. Data Pipeline
Claude developed:
- `merge_all_countries.py` / `merge_national.py` — merging per-court JSON files into unified national and international CSV/XLSX
- Deduplication logic (per-country identifier normalization)
- XLSX formatting with per-country color coding and summary/pivot tables

### 3. Jurimetric Coding Engine
Claude designed and implemented `jurimetric_coding.py`, including:
- All ~120 regex patterns across 7 variables and 4 languages
- The text-scope separation (summary-only for HR/sust to reduce false positives)
- UTF-8 encoding handling for Portuguese (`[aáàâã]gua`)

### 4. Repository and Deposit Automation
Claude wrote deposit scripts and ran API calls for:
- Zenodo (via REST API)
- Harvard Dataverse (via Dataverse API)
- DANS Data Station SSH (via Dataverse API)
- OSF (via WaterButler/OSF API)
- Contributed issues and PRs to [worldwidelaw/legal-sources](https://github.com/worldwidelaw/legal-sources) (#74–77, #78–79)

### 5. Quality Control
Claude identified data quality issues during collection and filed them as upstream contributions to the worldwidelaw/legal-sources community repository.

### 6. Validation (v0.3.0)
Claude built the residual-audit and kappa tooling in `validation/`, and an **LLM coder** (not a human) independently relabelled 91 decisions for the reproducibility audit reported on [[Validation]]. The 207-decision gold-standard sample used for the filter's precision estimate was hand-coded by the researcher.

### 7. Dataset consistency audit (Antigravity)
Antigravity audited the repository for contradictions and stale data and corrected documentation discrepancies.

### 8. Research assistant
The Streamlit `research-assistant/` tool uses Claude to answer questions about the dataset; it states that responses reflect dataset patterns and are not legal advice.

---

## What Claude Did NOT Do

- **Research design** — the theoretical framework (Legal Last Mile thesis, MDSD design, jurisdictional selection) was developed entirely by the human researcher
- **Variable definitions** — the 7 jurimetric variables and their theoretical grounding are the researcher's own
- **Interpretation** — all findings, arguments, and conclusions are the researcher's
- **Writing** — the dissertation, conference papers and other academic outputs are written by the human researcher. (The systematic review's reports and syntheses are different: they were drafted by the AI under the researcher's direction; see below.)

---

## The Systematic Review — a different level of AI involvement

The AI-assisted systematic review ([[Systematic Review]]) used AI far more extensively than the dataset work, and says so in its title. Its own `AI_USE_STATEMENT.md` is the authoritative record; in summary:

| Stage | What the AI did | What a human did / checked |
|-------|----------------|----------------------------|
| Searching and de-duplication | Wrote and ran scripts | Designed and ran the database searches and exports |
| Title/abstract screening | First-pass decision and rationale for 26,222 records | Second reviewer on the 3,665 include-or-unsure records only, **not** on the AI's exclusions |
| Full-text screening | Read each supplied full text and decided include/exclude with a coded reason | Supplied the full texts; confirmed includes (197 remain after the principal investigator's scope rulings), and the principal investigator ruled on 262 further decisions (459 of 2,277, or 20.2%, human-verified or adjudicated) |
| Data extraction (92 fields) | Extracted every study, largely from full text | **No second extractor** |
| Risk-of-bias appraisal | Rule-based batch ratings from extracted fields | **No human check**; one instrument is the project's own and is not validated |
| Syntheses, sensitivity analysis, reports | Drafted, with disclosed judgment calls | Approves and decides |

Models used: Claude (Anthropic) for first-pass screening, extraction, appraisal and synthesis drafting; Codex (OpenAI) and Gemini (Google) as blind second reviewers on part of the full-text decisions (112 decisions re-screened, 31 conflicts). A slide summary of the preliminary report was produced by the researcher with Google NotebookLM and is kept unaltered for reference.

**Strict human-verification accounting.** A decision counts as human-verified only if a human actually reviewed the evidence and ruled on it, and the reviewer label `CK` is reserved for the principal investigator's own rulings. Of the 31 studies in the three structured syntheses, 13 have a human-verified inclusion decision, 18 are AI-checked only, and the author has not yet confirmed the direction coding of any.

The AI's outputs have **not** been independently verified in full. The same system produced and audited much of the work, so its checks find inconsistencies and arithmetic errors but cannot confirm that an extracted value matches its source paper. The repository records the errors the AI made and corrected in the open.

---

## Why This Disclosure Matters

Transparency about AI assistance is increasingly important in academic research. The use of AI as a research infrastructure tool (to build scrapers, write ETL pipelines, and automate deposits) is analogous to using statistical software or database tools — it accelerates the work but does not replace the intellectual contribution of the researcher.

This project's source code is fully open at https://github.com/jrklaus8/water-law-dataset, allowing anyone to inspect what was built and how.

---

*Claude version used for the dataset work: Claude Sonnet 4.6 (Anthropic, 2025–2026). Model details for the systematic review are recorded in its `AI_USE_STATEMENT.md`.*
