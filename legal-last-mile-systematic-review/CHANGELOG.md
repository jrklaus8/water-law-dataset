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

## 2026-08-25 — Confirmed network egress is blocked; ran exploratory WebSearch pilot

- Tested direct access to PubMed's API (`curl`) and to PubMed, Google
  Scholar, CanLII, Rechtspraak.nl, and SSRN (`WebFetch`) — every one was
  denied by this environment's network egress policy (confirmed via
  `/root/.ccr/agentproxy/status`, a genuine policy denial rather than a
  transient failure, per that tool's own guidance not to retry). This
  environment therefore cannot reach any database, free or paid, by direct
  fetch or API call — only Claude's first-party `WebSearch` tool works.
- Amended the screening-database schema to add a `url` field alongside
  `doi` (`02_screening/title_abstract/screening_database.csv`,
  `code/search/deduplicate.py`, `code/screening/init_screening_db.py`,
  `DATA_DICTIONARY.md`, `PRISMA_WORKFLOW.md`) — real candidate records,
  especially grey literature, routinely have no DOI, and a URL is the only
  way to relocate them.
- Ran six explicitly non-systematic `WebSearch` queries drawn from
  `SEARCH_PROTOCOL.md`'s terms, logged as `SEARCH_003`–`SEARCH_008` in
  `01_search/search_logs/search_log.csv` with the pilot's method and
  limitations stated on every row. Extracted only title + URL from
  WebSearch's structured result data (never from its prose summary, which
  is itself an LLM paraphrase and risks introducing unverified specifics)
  into `01_search/raw_exports/SEARCH_003-008_WEBSEARCH_PILOT_2026-08-25.csv`
  — 25 candidate records, no fabricated authors/years/DOIs (left blank
  where not directly legible from the search result itself).
- Ran `code/search/deduplicate.py` and `code/screening/init_screening_db.py`
  on this real data for the first time (previously only synthetic-data
  tested) — 0 duplicates within the batch, 25 records now in
  `02_screening/title_abstract/screening_database.csv` with no screening
  decision made on any of them.
- Updated `SEARCH_PROTOCOL.md`, `PRISMA_WORKFLOW.md`, `README.md`, and
  `06_outputs/supplementary/preliminary_results.md` to state clearly, in
  each place, that this pilot is not Phase 3 and does not substitute for
  it — it exists so the deduplication/screening tooling has real data to
  operate on and so genuine (if low-recall) candidate studies are already
  identified once real screening capacity exists.

## 2026-08-25 (later) — Second pilot round, schema-validation tooling, triage memo

- Added `code/analysis/validate_schemas.py`: checks every project CSV's
  actual header against its documented (or script-generated) schema.
  Verified it catches real drift with a synthetic test, then confirmed all
  8 checked files are currently consistent — useful given the schema has
  already changed once (the `url` field).
- Ran a second WebSearch pilot round: an approximated backward-citation
  search on all 4 exemplar papers from `SOURCES.md` (WebSearch has no real
  citation-graph capability, so this is a keyword approximation, logged as
  such), plus a World Bank/UN-Habitat grey-literature query and a
  connection/service-refusal query. Logged as `SEARCH_009`–`SEARCH_013`,
  including two searches that found nothing new (Gaikwad/Thomas citations,
  too recent for a citation index; Halling/Bækgaard citations, real hits
  but out of this review's water/sanitation scope — logged as a scope
  demonstration, not a failure).
- Added 6 new genuine candidates from this round to
  `01_search/raw_exports/SEARCH_009-013_CITATION_GREYLIT_PILOT_2026-08-25.csv`;
  total candidate pool now 31 records, still 0 duplicates.
- Added `06_outputs/supplementary/title_only_triage_memo.md`: a title/URL-only,
  explicitly non-binding read of all 31 candidates against
  `INCLUSION_EXCLUSION.md`, since this environment cannot fetch abstracts.
  Does not populate `title_abstract_decision` for any record. Flagged a
  recurring pattern for the eventual reviewer: three law-review articles
  whose doctrinal-vs-empirical status can't be resolved from the title.

## 2026-08-25 (later still) — Third pilot round targeting gaps; exemplars added to pipeline; PubMed adapter

- Ran a third WebSearch round targeting gaps identified in the first two:
  Family B (bureaucratic assistance/political coordination + water),
  Dutch-language empirical studies specifically, Brazilian ANA/SNIS
  regulatory-data studies, and WHO/UNICEF JMP grey literature. Logged as
  `SEARCH_014`-`SEARCH_017`.
- Found a likely duplicate-publication pair: an earlier working-paper
  title appears to be a pre-publication version of the Gaikwad & Thomas
  2026 exemplar. Logged both per `REPRODUCIBILITY.md` §6 (identify, don't
  silently merge) rather than dropping the earlier one.
- Second Dutch-language query in a row surfaced zero empirical studies
  (only primary legal/regulatory sources) — logged as a preliminary,
  WebSearch-only pattern, explicitly caveated as far too thin a basis to
  draw any conclusion about the Dutch empirical literature.
- WHO/UNICEF JMP 2025 report deliberately excluded from the candidate pool:
  relevant background, but per its own summary it doesn't treat legal/
  administrative barriers as a distinct topic, failing inclusion
  criterion 2 — a scope-discipline exclusion, not a search failure.
- **Found and fixed a real gap**: 3 of the 4 substantive exemplar studies
  in `SOURCES.md` (Lubeck-Schricker et al. 2023, Gaikwad & Thomas 2026,
  Apio/Thiam/Dinar 2025) had been cited as methodological context but
  never actually entered the screening pipeline, meaning they'd never be
  formally screened like everything else. Added them with their
  already-verified DOIs. The 4th exemplar, Halling & Bækgaard 2024,
  deliberately was not added — it's administrative-burden methodological
  literature with no water/sanitation content, failing inclusion
  criterion 1; it remains a `SOURCES.md`-only methodological reference.
- Total candidate pool now 37 records, still 0 duplicates found by the
  automated dedup script (the 2 likely-duplicate pairs identified above
  differ enough in title that automated matching correctly can't catch
  them — exactly why they were logged manually instead).
- Added `code/search/adapters/pubmed_adapter.py`: normalizes PubMed's
  documented CSV export format to the project's common schema. Explicitly
  marked **unvalidated against a real export** (PubMed is unreachable from
  this environment) — tested against a synthetic file matching the
  documented format (works) and a deliberately wrong format (correctly
  refuses to guess rather than producing silently-wrong output).
- Updated `06_outputs/supplementary/title_only_triage_memo.md` for the 6
  new records.

## 2026-08-25 (latest) — Execution checklist for real institutional access

- The researcher confirmed a working EUR (Erasmus University Rotterdam)
  institutional research account, which should give real access to
  Scopus, Web of Science, HeinOnline, Westlaw, Lexis, and ProQuest.
- Added `01_search/EXECUTION_CHECKLIST.md`: a literal, step-by-step
  "what to actually click" guide per database — access route (via the
  library, not the database directly), where to paste each search string,
  export format/field selection (emphasizing abstracts, not just
  citations, since every candidate identified so far has been title-only),
  file-naming convention, and exactly what to hand back to Claude. Written
  to be followable without the rest of this repo's context, since the
  researcher intends to execute it via a separate tool (Claude Cowork).
- This does not touch credentials at all: Claude does not have and will
  not request the researcher's institutional login. Two independent
  reasons this has to be human-executed rather than automated from this
  environment: (1) network egress from this environment is blocked for
  every external domain tested, regardless of credentials; (2)
  institutional SSO logins involve MFA/interactive flows a script can't
  drive, and most of these platforms' license terms prohibit automated or
  bulk retrieval even by authorized users.
- Cross-linked from `README.md` and `SEARCH_PROTOCOL.md` §8.

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
