# Changelog

All notable methodological and structural decisions for this project are
logged here, per `REPRODUCIBILITY.md` §8 and `PROTOCOL.md` §12 (protocol
amendments in particular must be logged here with rationale).

## [Unreleased]

Nothing yet — no phase past repository setup and source verification has
been reached.

## 2026-09-11 (latest) — ProQuest and JSTOR: two methodological decisions

Cowork's next round surfaced two real, platform-forced compromises that
needed a decision from the researcher rather than being resolved
unilaterally (`PROJECT_SPEC.md` §14.18) — both logged in
`search_log.csv` (`SEARCH_039`, `SEARCH_041`) alongside the technical
detail; the decisions themselves:

- **ProQuest** (`SEARCH_039`, 8,137 total hits): guest/no-account export
  works mechanically but caps at roughly 100–200 records per session
  before a login-required error, and saves under an unrecoverable random
  filename. **Decision: the researcher will create a personal ProQuest
  "My Research" account**, which unlocks a documented 20,000-record bulk
  export — Cowork cannot create the account or enter a password on the
  researcher's behalf. Full ProQuest export is pending that account.
- **JSTOR** (`SEARCH_041`): the full search string is rejected outright
  as "too long," forcing a trim to ~9 terms across 3 clauses (a
  materially smaller vocabulary than every other database in this
  project), and even that returned 5,217 hits until an ad-hoc
  "Subject: Law" filter narrowed it to a workable 356 — excluding
  whatever JSTOR classifies under Development Studies, Public Policy,
  Urban Studies, etc. **Decision: accept the narrower, Subject:Law-only
  JSTOR search as a supplementary source** (consistent with
  `SEARCH_PROTOCOL.md` §1's own Tier 2 framing for JSTOR/SSRN/Google
  Scholar — supplementing, not matching, Tier 1 recall) rather than
  running further subject-filtered sub-searches to widen it. The full
  356 (not just the 7-record sample already pulled) still needs
  exporting — no bulk "select all" exists on JSTOR, so this is manual,
  per-item selection across roughly 15 pages.

## 2026-09-11 (later still) — HeinOnline begins; a SEARCH_035 integrity scare, resolved

- **`SEARCH_037` (HeinOnline, Title-restricted secondary search per
  `heinonline.md`)** ingested: 1 record ("Hear Their Voices: Australia's
  First Nations Women and the Legal Recognition of Their Rights to
  Water," O'Bryan & Harriden 2023). No structured abstract available
  from HeinOnline for this record — left blank, not fabricated; gets
  title-only triage like other abstract-less records.
- **`SEARCH_036` (HeinOnline, main three-clause full-text search)**
  logged as **count-only**: 71,226 hits, far too many to hand-compile
  and no bulk results-list export exists on HeinOnline at that volume.
  Per `REPRODUCIBILITY.md`, a real search that ran and produced a real
  total is logged even when it yields no exportable records — no records
  added under this `search_id`.
- **A serious, since-resolved integrity question on `SEARCH_035`.** A
  run log received the same day claimed the Web of Science export
  ingested in the previous round had never actually succeeded ("no
  download was ever produced... confirmed nothing in Downloads"),
  directly contradicting the 4,058 real-looking records already screened
  and pushed. Flagged to the researcher rather than resolved
  unilaterally either way (`PROJECT_SPEC.md` §14.18); a technical
  read at the time (realistic WOS accession-number entropy, correct
  journal/ISSN/publisher metadata, WoS-internal ResearcherID/GA-code
  fields very hard to fabricate at scale) suggested the data was
  genuine, but this was not independently verifiable from this
  environment.
  - **Conclusively resolved**: checked directly on the researcher's
    machine, file by file. The 5 files exist under Windows' standard
    duplicate-naming convention (`savedrecs.txt`, `savedrecs (1).txt`,
    `savedrecs (2).txt`, `savedrecs (3).txt`) rather than the 4 distinct
    names originally assumed — 1000+1000+1000+58 = 4,058 records, zero
    WOS-ID overlap, timestamped 03:52–03:57 UTC, predating the later
    session that logged the HTTP 500 failures. **The originally-ingested
    4,058 records are genuine and stand as final — nothing in this
    project's data was ever wrong.**
  - **A second, smaller instance of the same failure mode surfaced
    during the resolution itself**: the later session's own retry
    produced a `savedrecs (4).txt` that returned HTTP 200 (apparent
    success) but was a byte-for-byte duplicate of the first batch — no
    new file actually written despite the "successful" network
    response. Worth carrying forward as a standing caution for future
    rounds: a Cowork session's own claim of export success (status
    code, dialog closing normally) is not sufficient on its own for
    this platform — confirm against the actual file on disk.

## 2026-09-11 (later) — SEARCH_035 ingested: first Web of Science batch, second Tier 1 database

- **Web of Science is the second Tier 1 database actually searched for
  real** (`SEARCH_035`, 2026-09-11) — sent as 5 sequential tab-delimited
  `savedrecs.txt`-style export batches (WoS's native 1,000-record export
  cap; the researcher used `cowork_instructions_2026-09-11_wos_heinonline.md`
  to run it), zero overlap between batches confirmed via UT/accession
  number comparison, totaling 4,058 records after removing one exact
  internal repeat.
- **Found and fixed two real bugs in `wos_adapter.py`, previously
  unvalidated speculative code, while processing this batch:**
  1. It only handled a single CSV file; added tab-delimited
     auto-detection (comparing tab vs. comma counts in the header line)
     and multi-file merging (`--input` now takes one or more files).
  2. **A real data-corruption bug**: WoS's tab-delimited export has no
     quote-escaping at all, so a literal double-quote inside an abstract
     (common — quoting a term) was being misread by Python's csv module
     under its default quoting mode as *opening* a quoted field, which
     then silently swallowed every subsequent tab and newline as literal
     text until some *later* stray quote happened to close it —
     corrupting or merging an unpredictable number of downstream records.
     Caught by comparing each file's raw physical line count (1,000)
     against its parsed row count (as low as 988 before the fix) rather
     than assuming a clean parse; fixed by switching to
     `csv.QUOTE_NONE` for the tab-delimited path, which is actually
     correct for this format. Re-verified exact 1,000/1,000 parsing
     after the fix, then spot-checked field alignment on real records.
     `wos_adapter.py` is now genuinely validated against a real export,
     not just written speculatively.
- Full-corpus re-dedup (10,079 raw records now that WoS is in) found
  **2,934 duplicates** — far more than any prior round, as expected:
  Scopus and Web of Science index a lot of the same journal literature,
  so heavy cross-database overlap is exactly what a working dedup should
  catch. Leaves **7,145 unique records, 7,109 with a real abstract**.
  Same benign `record_id` flag as the previous round (`R36A2B99DC8AD`,
  the SEARCH_026/SEARCH_027 Scopus year-metadata quirk) recurred and was
  left untouched, as before — not a new issue.
- Screened the 1,664 newly-unique records (5 more batches, same
  independent-validation method as every prior round) against
  `INCLUSION_EXCLUSION.md`: **201 include / 1,404 exclude / 59 unsure**.
  Notably lower yield than the Scopus batches (~13% include/unsure vs.
  ~25-30%) — expected, not a screening-quality problem: `TS=` is broader
  than Scopus's `TITLE-ABS-KEY` (also searches Keywords Plus), and this
  batch is only the WoS-unique residue *after* cross-database dedup
  already removed everything WoS shared with Scopus, so it's
  disproportionately the noise Scopus's narrower field didn't also catch.
- Screening database now has **7,145 total records, 7,109 screened**
  (36 still lack a real abstract and remain deliberately undecided).
  Cumulative first-pass totals: **1,710 include / 5,151 exclude / 248
  unsure.** Refreshed `reviewer_2_queue.csv` (1,958 rows) and
  `exclude_spotcheck_sample.csv` (120-row sample, seed `20260911035`,
  regenerated fresh over the full exclude population) accordingly.
  `code/analysis/validate_schemas.py` confirms all 11 checked project
  CSVs still match their documented schema.
- `search_log.csv`'s `SEARCH_035` row documents what's confirmed (exact
  query string, per-batch counts, zero-overlap verification) and flags
  what wasn't reported back (Core Collection index selection, the
  platform's own on-screen total count) rather than guessing either —
  worth the researcher confirming for the record.

## 2026-09-11 — SEARCH_026 ingested: Scopus batch plan complete (18 of 18)

- Received and ingested `SEARCH_026` (2020, 274 records) — the one
  outstanding gap from `scopus_batch_plan_2026-08-26.md` flagged in the
  previous entry. Record count cross-checked against the researcher's run
  log (`scopus_batch_run_log_20260910.csv`, 274 shown/exported) and an
  independent file row count, both matching exactly. **All 18 planned
  Scopus batches are now done.**
- Full-corpus re-dedup (5,747 → 6,021 raw records, +274 from SEARCH_026) found 541 duplicates
  (2 more than the previous round), leaving **5,480 unique records**. One
  of the 2 new duplicates is worth noting: the same DOI appeared in both
  `SEARCH_026` (PUBYEAR=2020) and `SEARCH_027` (PUBYEAR=2019) with a
  trivial title-capitalization difference and a one-year metadata
  discrepancy — a Scopus indexing quirk (same paper, inconsistent
  year field across two of Scopus's own query contexts), not a data
  error on this project's side. Correctly DOI-matched and merged;
  `init_screening_db.py`'s existing safety check flagged the resulting
  text mismatch against the already-screened `SEARCH_027` copy rather
  than silently overwriting it — verified benign and left as-is, no
  action needed since the underlying study was already screened
  (`title_abstract_decision = include`) under its existing `record_id`.
- Screened the 272 newly-added records (batch 16, following the same
  15-batch method and validation as the previous round) against
  `INCLUSION_EXCLUSION.md`: **73 include / 182 exclude / 17 unsure**.
  Screening database now has **5,480 total records, 5,445 with a real
  abstract, all 5,445 screened** (35 records still lack an abstract and
  remain deliberately undecided). Cumulative first-pass screening
  totals: **1,509 include / 3,747 exclude / 189 unsure.**
- Refreshed `reviewer_2_queue.csv` (now 1,698 rows) and
  `exclude_spotcheck_sample.csv` (regenerated fresh over the full 3,747
  excludes, seed `20260911`) to cover the complete corpus; appended
  `SEARCH_026`'s rationale to `ai_first_pass_rationale.csv` (now 5,445
  rows). `code/analysis/validate_schemas.py` confirms all 11 checked
  project CSVs still match their documented schema.

## 2026-09-10 (final) — Reviewer 2 prep packet, PRISMA flow diagram, RIS adapter

- **Built the reviewer_2 handoff.** `02_screening/title_abstract/
  reviewer_2_queue.csv`: every `include`/`unsure` record from the AI
  first pass (1,608 rows), with title/abstract/authors/year/doi/url and
  the first-pass rationale attached, so a human second reviewer works
  from one file instead of filtering a 5,208-row database by hand.
  `exclude_spotcheck_sample.csv`: a random, fixed-seed (`20260910`,
  reproducible) 100-record sample of the 3,565 first-pass excludes, for
  false-negative spot-checking rather than a full second pass over every
  exclude — standard systematic-review QA practice. `REVIEWER_2_README.md`
  explains how to use both and is explicit that screening only these
  1,608 does not by itself satisfy `PROTOCOL.md`'s two-reviewer
  requirement for the whole title/abstract stage. Both new CSVs added to
  `validate_schemas.py` and `DATA_DICTIONARY.md`.
- **Populated `06_outputs/prisma/prisma_flow.md`** (previously an
  all-placeholder stub) with real counts through the title/abstract
  screening stage: 5,710 records identified from Scopus, 37 from the
  WebSearch pilot/exemplars, 539 duplicates removed, 5,173 screened (35
  left unscreened — no abstract), 3,565 excluded (full E01–E12 code
  breakdown), 1,608 carried forward. Everything from "reports sought for
  retrieval" onward is left genuinely blank — that work hasn't started —
  and every screening-stage number is explicitly flagged provisional
  (reviewer_1/AI only, no `reviewer_2` yet).
- **Added `code/search/adapters/ris_adapter.py`**: one shared,
  **unvalidated** adapter for the RIS citation-export format, covering
  HeinOnline, ProQuest, Sociological Abstracts, JSTOR, and SSRN — all of
  which offer RIS export per their `database_strategies/*.md` files.
  Grounded in the RIS format itself (a real, long-published standard),
  not a guessed platform-specific CSV layout, which is why one adapter
  can responsibly cover five platforms at once. Handles multiple authors,
  wrapped/continuation lines, and both common tag variants per field
  (TI/T1, PY/Y1, AB/N2, UR/L1/L2) — tested against synthetic RIS data
  covering all of that plus a missing-title record and a not-actually-RIS
  file, both of which fail cleanly rather than silently producing
  garbage.
- **Deliberately did not** build adapters for Westlaw/Lexis (neither
  platform offers a standard bulk export to build against without
  guessing — `PROJECT_SPEC.md` §14) or for CanLII/Rechtspraak.nl/
  Brazilian court portals/ANA-SNIS (these feed the doctrinal/jurimetric
  strand of the project, not this screening pipeline — merging their
  hits through this pipeline would be wrong, not just premature). Each
  `database_strategies/*.md` file now says so explicitly rather than
  leaving the absence unexplained.

## 2026-09-10 (earlier) — First-pass AI title/abstract screening, all 5,173 abstract-bearing records

- **Real title/abstract screening against `INCLUSION_EXCLUSION.md` has now
  actually happened**, for the first time in this project, on every
  record with a real abstract. This is a first pass by Claude, explicitly
  authorized by the researcher as an AI reviewer (`reviewer_1`) — per
  `PROTOCOL.md` §"Selection process" ("two reviewers where feasible") and
  `PROJECT_SPEC.md` §14.18 ("ask for human confirmation when a major
  methodological choice is genuinely ambiguous"), this was surfaced to
  the researcher as a choice rather than decided unilaterally, then
  proceeded on explicit instruction. **`reviewer_2` (a human) and
  conflict resolution have not happened — these decisions are
  provisional, not final**, exactly like any single reviewer's pass in a
  real dual-review PRISMA process.
- Method: the 5,173 records with a real abstract were split into 15
  batches of ~350 and screened independently by subagents, each reading
  `INCLUSION_EXCLUSION.md` directly and applying its 9 inclusion criteria,
  11 exclusion criteria, and E01–E12 exclusion-code table. Every batch's
  output was validated before merging: exact record_id order and coverage
  match against its input, every `exclude` decision carries exactly one
  valid E01–E12 code, no `include`/`unsure` row carries a stray code, no
  duplicate record_ids across batches, and no already-decided row was
  ever touched (the merge script refuses outright on any of these). The
  35 records without a real abstract (grey literature / older exports)
  were deliberately left undecided — this project's own convention (see
  `title_only_triage_memo.md`) is that title-only triage is non-binding,
  never a substitute for reading an abstract.
- **Results: 1,436 include / 3,565 exclude / 172 unsure**, out of 5,173
  screened (35 of 5,208 total records left undecided, no abstract).
  Exclusion code breakdown: E01 wrong topic 1,555; E06 engineering only
  780; E05 no empirical evidence 487; E04 wrong outcome 255; E07 wrong
  service 320; E03 water-quality-only 65; E09 insufficient information
  63; E02 wrong population 21; E08 duplicate 18; E11 wrong
  jurisdiction/context 1. Consistent with the batch plan's own
  expectation (`scopus_batch_plan_2026-08-26.md`, `EXECUTION_CHECKLIST.md`)
  that this broad, high-recall OR-heavy Boolean search would surface a
  lot of engineering/hydrology/water-quality noise alongside the
  genuinely on-topic records.
- `reviewer_1` is set to `Claude-AI-1stpass-2026-09-10` on every screened
  row, so it's always traceable which decisions came from this pass
  versus a human reviewer. `title_abstract_decision` of `unsure` should
  be treated the same as `include` for full-text-stage purposes (proceed
  to read it) — these are records the first-pass reviewer explicitly
  could not confidently resolve from title+abstract alone, not a
  rejection.
- **What this is not**: not a final inclusion/exclusion decision (needs
  `reviewer_2` and conflict resolution per `PROTOCOL.md`), not full-text
  screening, not data extraction, not risk-of-bias appraisal. The 1,436
  (+172 unsure = up to 1,608) candidate records are the pool that Phase 6
  (full-text screening) will actually work from once a human reviewer's
  pass exists to compare against.
- `code/analysis/validate_schemas.py` confirms all 8 checked project CSVs
  still match their documented schema after this round.

## 2026-09-10 (later still) — Stable record_id migration; Web of Science adapter

- **Replaced positional `record_id` assignment with a stable content
  hash**, closing the follow-up flagged in the previous entry.
  `code/search/deduplicate.py`'s `compute_record_id()` now keys on the
  normalized DOI when present, else normalized title+year — the same
  fields the duplicate matcher itself already uses — so a record's ID no
  longer depends on which files happen to be present or what order they
  sort in. Collision-checked: three genuine content collisions surfaced
  during the full re-run (two different generic-titled records sharing a
  normalized title+year, e.g. a recurring report-series title), correctly
  disambiguated with a `-1` suffix rather than silently merged.
- Did this migration now specifically because it was still safe to:
  confirmed **zero rows** in `screening_database.csv` had any decision
  field set (`title_abstract_decision`, `full_text_decision`,
  `reviewer_1`, `reviewer_2`, `final_decision`) before touching a single
  ID. Regenerated `deduplicated_records.csv` and
  `screening_database.csv` in full from a fresh re-run across all of
  `01_search/raw_exports/` under the new scheme, then verified **zero
  orphans**: every one of the previous 5,314 rows matches (by DOI or
  normalized title+year) something in the new 5,208-row output. The
  106-row reduction is not data loss — it's genuine duplicates that had
  slipped past the old positional-ID incremental matching across earlier
  rounds, now correctly collapsed by one clean full-corpus dedup pass.
  Remapped the 37 `record_id`s referenced in
  `06_outputs/supplementary/title_only_triage_memo.md` to match.
- Added `code/search/adapters/wos_adapter.py`: **unvalidated** (no real
  Web of Science export exists in this project yet, same status
  `pubmed_adapter.py` carried before SEARCH_018), written ahead of time so
  ingestion is instant once the researcher runs
  `database_strategies/wos.md`. Handles both CSV shapes Web of Science's
  UI can produce (full-word "Export → Excel" headers, and the classic
  two-letter Core Collection field tags), tested against synthetic data
  covering both plus a missing-required-column failure case.
- `code/analysis/validate_schemas.py` confirms all 8 checked project CSVs
  still match their documented schema after the migration.

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

## 2026-08-26 — First real Tier 1 database data (Scopus)

- The researcher ran the pilot Scopus string for real via EUR institutional
  access (Claude Cowork assisted) and uploaded the results as two GitHub
  PRs (#4, #5) containing PDFs and CSVs. **Flagged immediately: PR #4/#5
  contain 24 copyrighted journal-article PDFs (Nature, Springer, BMC)
  pushed to public branches — a likely redistribution problem independent
  of this project. Recommended deleting those branches/files rather than
  merging; only bibliographic metadata belongs in this repo.**
- Of the uploaded files, one was actually usable as review data:
  `export_d3841da0-...csv`, a genuine 500-record Scopus export (Authors,
  Title, Year, Source title, DOI, Link, Document Type, etc. — confirmed
  real Scopus export header). `Scopus-200-Analyze-Year.csv` was not a
  document-level export at all — it's Scopus's "Analyze results by Year"
  aggregate count feature, useful only for reconstructing the *total* hit
  count (summed to ~5,443 for the unrefined pilot string) and not ingested
  as data.
- Wrote and ran `code/search/adapters/scopus_adapter.py` — **validated
  against a real export**, unlike the still-unvalidated PubMed adapter.
  Normalized 500 records into `01_search/raw_exports/SEARCH_018_SCOPUS_2026-08-26.csv`,
  logged as `SEARCH_018` with the real query, the ~5,443 total count, and
  the gaps (no abstracts in this export; only 500 of ~5,443 exported).
- Ran the full pipeline on the combined pool (37 WebSearch-pilot + 500
  Scopus records): `deduplicate.py` found **1 real cross-source
  duplicate** — the Gaikwad & Thomas 2026 exemplar, independently added
  earlier from `SOURCES.md`, also appeared in the live Scopus results,
  correctly matched by DOI. This is the first real validation of the
  dedup logic against two independent real sources, not synthetic test
  data. Screening database now has **536 unique records**.
- Spot-checked the first 15 Scopus titles: a healthy mix of clearly
  on-topic hits and expected noise from a broad, sensitive Boolean string
  (corona-discharge hardware, blockchain, coastal-ecosystem valuation) —
  normal at this stage; screening exists to filter exactly this.
- Two follow-ups flagged for the researcher: (1) re-export with the
  Abstract field explicitly selected — none of these 500 records have one;
  (2) only ~9% of the total ~5,443 matching documents were exported —
  getting the rest needs either batching (e.g. by year range, since
  Scopus's bulk-export UI appears to cap a single CSV well below the full
  result count) or narrowing the query.

## 2026-08-26 (later) — Removed all 43 copyrighted PDFs from every branch

- 43 full-text journal-article PDFs (Nature, Springer, BMC/BioMed Central)
  had accumulated across three separate uploads: 10 on `jrklaus8-patch-1`
  (PR #4), 13 on `jrklaus8-patch-2` (PR #5), and 20 directly on this
  review branch. Flagged to the researcher as a copyright/redistribution
  concern independent of the research use itself.
- Closed PR #4 and PR #5 without merging.
- Removed the 10 and 13 PDFs from `jrklaus8-patch-1`/`jrklaus8-patch-2` via
  a direct git push updating each branch (GitHub's file-delete API choked
  on the large binaries; branch *deletion* was blocked by the same
  ruleset that blocked branch creation earlier in this project, but a
  normal branch *update* was not).
- Removed the 20 PDFs from this branch the same way.
- Before removing anything, recovered all 43 from git history and sent
  them directly to the researcher (not through GitHub) for them to store
  privately, per their request — see
  `01_search/raw_exports/native/README.md` for the accounting. None of
  the 43 remain in this repository in any form; their bibliographic
  metadata (for the 10+13 that came from the Scopus session) is preserved
  in `01_search/raw_exports/native/SEARCH_018_SCOPUS_2026-08-26_native.csv`.
- Confirmed via `git ls-tree` on both upload branches after the push that
  no PDF remains reachable from either branch tip. Noted as a caveat to
  the researcher: this doesn't purge the blobs from git's object history
  (recoverable by anyone with the old commit SHA) — a harder guarantee
  would need branch deletion (blocked here) or a GitHub-side history purge.

## 2026-09-10 — First abstracts; SEARCH_021b ingested

- Received the first batch from `scopus_batch_plan_2026-08-26.md`:
  `SEARCH_021b` (2025, non-article/non-review document types — the
  "everything else" half of the 2025 split; `SEARCH_021a`, articles and
  reviews, has not been run yet), 106 records. **This export includes
  Abstract, Author Keywords, and Index Keywords** — the first real
  abstract-bearing data in this project.
- Amended the project schema to actually carry this through, since
  neither the adapter nor the screening database had an `abstract` field
  before now:
  - `code/search/deduplicate.py`: added `abstract` as an *optional*
    normalized field (not required — older files without it still load).
    Also fixed a latent correctness bug this surfaced: when two sources
    describe the same record and only one has an abstract, the dedup
    logic was keeping whichever file sorted first alphabetically and
    discarding the other's abstract along with the duplicate. Now the
    kept record is backfilled with the abstract if it was missing one —
    verified with a synthetic test using filenames ordered the way they
    actually appear in production (abstract-less source sorting first),
    which is the case that would have silently failed before.
  - `code/screening/init_screening_db.py`: same backfill logic for a
    record already sitting in the screening database from an earlier,
    abstract-less run — the one narrow exception to "never touch an
    existing row," since backfilling a blank abstract isn't touching a
    decision field.
  - `code/search/adapters/scopus_adapter.py`: now maps the Abstract
    column through when present (previously just warned that it existed
    and dropped it).
  - Migrated all 536 existing `screening_database.csv` rows to the new
    16-field schema (blank `abstract`) rather than leaving them on an
    incompatible header.
- Ran the full pipeline on the combined pool: 0 new duplicates from this
  batch specifically (the one duplicate in the log is the pre-existing
  Gaikwad & Thomas exemplar match from 2026-08-26). Screening database now
  has **642 unique records, 106 of which have a real abstract** for the
  first time — real title/abstract screening against
  `INCLUSION_EXCLUSION.md` is now possible on that subset, though it
  hasn't been done yet.
- Note on this specific batch's composition: because `SEARCH_021b` is
  deliberately the non-article/review half of 2025 (book chapters,
  conference papers, an erratum, etc. — see the batch plan), it is not
  representative of Scopus's 2025 output as a whole; `SEARCH_021a`
  (articles + reviews) is where the more substantive primary research is
  expected to land.

## 2026-09-10 (later) — 17 of 18 Scopus batches ingested

- Received and processed the remaining 16 batches of
  `scopus_batch_plan_2026-08-26.md` in one round: `SEARCH_019` (2027, 2),
  `SEARCH_020a` (2026 articles+reviews, 556), `SEARCH_020b` (2026
  everything else, 100), `SEARCH_021a` (2025 articles+reviews, 477),
  `SEARCH_022` (2024, 392), `SEARCH_023` (2023, 337), `SEARCH_024` (2022,
  326), `SEARCH_025` (2021, 324), `SEARCH_027` (2019, 254), `SEARCH_028`
  (2018, 241), `SEARCH_029` (2016–2017, 375), `SEARCH_030` (2014–2015,
  315), `SEARCH_031` (2012–2013, 293), `SEARCH_032` (2009–2011, 367),
  `SEARCH_033` (2003–2008, 388), `SEARCH_034` (1928–2002, 357). All 16
  were exported with Abstract, Author Keywords, and Index Keywords, same
  as `SEARCH_021b`. Every native file preserved untouched in
  `01_search/raw_exports/native/`; every normalized file in
  `01_search/raw_exports/`; every batch logged as its own row in
  `search_log.csv`, built from the researcher's own authoritative run log
  (`scopus_batch_run_log_20260910.csv`) rather than reconstructed — every
  exported-record count cross-checked against that log and against an
  independent row count of each raw file, all matching exactly. Confirms
  `SEARCH_020a`/`SEARCH_021a`'s earlier finding that there is no hard
  500-record export ceiling when signed in via EUR proxy — both
  oversized DOCTYPE halves (556 and 477 records) exported whole.
- 17 of the 18 planned batches are now done. `SEARCH_026` (2020, ~274
  records per the run log) was run by the researcher but its export CSV
  has not been uploaded to this project yet — flagged in
  `scopus_batch_plan_2026-08-26.md` as the one remaining gap.
- Re-ran `code/search/deduplicate.py` across the full accumulated corpus
  (all `01_search/raw_exports/*.csv`): **5,208 unique records kept, 539
  duplicates merged** (mostly by DOI match; several backfilled a missing
  abstract from the surviving record's duplicate per the existing
  backfill rule). Re-ran `code/screening/init_screening_db.py`: 4,659 new
  records appended, 501 existing records backfilled with an abstract they
  previously lacked.
- **Found and fixed a latent record_id collision bug** surfaced by this
  round's scale: `deduplicate.py` assigns `record_id` positionally
  (`R0001`, `R0002`, ...) by file-processing order across
  `01_search/raw_exports/`. Adding 16 new files shifted that ordering
  enough that 13 IDs in the new dedup run collided with unrelated,
  already-screened-pool records from earlier rounds (same ID, different
  title/DOI). `init_screening_db.py`'s existing safety check correctly
  refused to overwrite the 13 old rows (so nothing was corrupted), but
  also silently skipped appending the 13 legitimately-new records under
  those colliding IDs — a real (if narrow) data-loss risk, not a
  duplicate. Manually verified all 13 were genuinely different
  title+DOI pairs, then appended them under 13 fresh unused IDs
  (`R5748`–`R5760`). **This is a structural limitation of the current
  positional ID scheme, not a one-off bug** — it will recur any time a
  new file is added whose sort position is before existing files' tail
  end and the corpus is large enough for a same-position collision;
  a content-hash-based `record_id` would eliminate it, but that is a
  larger migration (it would need to remap 5,300+ existing IDs) and is
  left as a known follow-up rather than done inline here.
- Screening database now has **5,314 unique records, 5,279 of which have
  a real abstract**. `code/analysis/validate_schemas.py` confirms all 8
  checked project CSVs still match their documented schema after this
  round. No screening decision has been made on any of them — this is
  still search, not screening.

## 2026-08-26 (latest) — Scopus batch export plan

- Added `01_search/scopus_batch_plan_2026-08-26.md`: 16 ready-to-paste
  batch queries to capture the remaining ~4,944 of ~5,444 total matching
  Scopus records, computed from the real year-by-year breakdown (not a
  guess) so each batch stays comfortably under the 500-record ceiling the
  first export hit. Flags that 2026 and 2025 alone (619 and 583 records)
  exceed that ceiling even as single years and need a further
  `DOCTYPE`-based split.
- Cross-linked from `EXECUTION_CHECKLIST.md`. Every batch still needs
  Abstract selected explicitly in the export field picker — the one gap
  that actually blocks real screening, and the main reason to finish
  Scopus before moving to a second database.
- Not yet executed — this is a plan, not new data.

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
