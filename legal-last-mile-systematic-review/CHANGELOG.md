# Changelog

All notable methodological and structural decisions for this project are
logged here, per `REPRODUCIBILITY.md` §8 and `PROTOCOL.md` §12 (protocol
amendments in particular must be logged here with rationale).

## [Unreleased]

Nothing yet — no phase past repository setup and source verification has
been reached.

## 2026-08-22 (later) — PR opened; preregistration draft + Phase 4/5 tooling

- Opened PR #3 (`claude/legal-last-mile-review-spec-8ri0zs` → `main`) on the
  jrklaus8/water-law-dataset repository.
- Drafted the OSF Generalized Systematic Review preregistration text
  (`00_admin/preregistration/osf_preregistration_draft.md`) — not
  submitted; this environment has no OSF account access.
- Wrote and tested `code/search/deduplicate.py` (DOI-match and
  title/year-similarity-match deduplication, with a full merge log for
  auditability) against synthetic data — not yet run on real data, since
  none exists. Documents that it expects input already normalized to a
  common schema; per-database raw-export adapters remain future work to be
  developed against real exports once Phase 3 produces any.
- Wrote and tested `code/screening/init_screening_db.py` (idempotent merge
  of newly deduplicated records into the persistent screening database,
  never overwriting an existing reviewer decision) against synthetic data.
- Updated `PRISMA_WORKFLOW.md` and `README.md` status tables accordingly.
  Phase 3 (database searching) remains the hard blocker — no credentials
  exist in this environment for any Tier 1 database.

## 2026-08-22 — Initial scaffold

- Repository structure created per the eleven-phase folder architecture
  (`00_admin/` through `11_archive/`, plus `data/` and `code/`).
- Governing documents written: `README.md`, `PROJECT_SPEC.md`,
  `PROTOCOL.md`, `SEARCH_PROTOCOL.md`, `INCLUSION_EXCLUSION.md`,
  `CODEBOOK.md`, `RISK_OF_BIAS.md`, `ANALYSIS_PLAN.md`,
  `PRISMA_WORKFLOW.md`, `DATA_DICTIONARY.md`, `REPRODUCIBILITY.md`,
  `PUBLICATION_PLAN.md`, `SOURCES.md`, `sources.bib`.
- Empty, header-only CSV templates created for the search log, screening
  database, exclusion log, extraction database, evidence map, and effect
  sizes — no data populated.
- Per-database search strings drafted for Scopus, Web of Science, PubMed/
  Global Health, HeinOnline, Westlaw/Lexis, ProQuest/Sociological
  Abstracts, JSTOR/Google Scholar/SSRN, CanLII, Rechtspraak.nl, and
  Brazilian legal/regulatory databases, plus grey-literature guidance —
  **none executed**.
- Eight preliminary methodological sources checked against independent web
  sources (publisher domains and doi.org were unreachable in this
  environment; see `SOURCES.md` for method and caveats). Two sources
  (PRISMA-P 2015, AMSTAR 2) remain unverified beyond the original citation
  and are flagged as such.
- Decided, following `PROJECT_SPEC.md` §3, that no title or framing implying
  a completed meta-analysis will be used until Phase 11–12 of
  `PRISMA_WORKFLOW.md` establishes that pooling is defensible for a given
  evidence family.
- Decided the systematic review's evidence base and the existing Global
  Water Law Judicial Decisions Dataset in this repository will not be
  merged (`PROJECT_SPEC.md` §9); they are cross-referenced but kept as
  separate evidence populations even though they share a git repository.

No search has been executed. No study has been screened, extracted, or
appraised. No effect size exists anywhere in this project.
