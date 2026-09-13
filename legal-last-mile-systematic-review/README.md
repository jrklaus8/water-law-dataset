# The Legal Last Mile — Systematic Review

**Preliminary Systematic Review and Contingent Meta Analysis**

Companion project to the doctoral dissertation *The Legal Last Mile: Administrative
Law as a Mechanism of Connectivity and Exclusion in Sanitation Governance: A
Comparative Study of the Netherlands, Canada (Ontario), and Brazil* (Claudio Klaus).

Project status (2026-09-13): **Search closed, deduplicated, and double-screened
at title/abstract (Phases 1–5 complete). Full-text screening (Phase 6) is
live and ongoing — 193 of 3,659 records assessed so far. Full extraction
(Phase 8) is fully caught up with screening — all 92 current
includes extracted, no outstanding gap. Evidence classification (Phase 10) is populated
for all 92. Risk-of-bias rating (Phase 9) and quantitative-feasibility
assessment (Phase 11) are deliberately not yet started — see below for why.**

---

## What this is

A systematic review of the empirical literature on how legal and administrative
institutions shape the translation of physical water/sanitation infrastructure
into effective household access — plus a *contingent* quantitative evidence
synthesis and restricted meta-analysis, conducted only where the completed
search turns up genuinely comparable study families.

The governing rule, stated once so it is never lost in the detail below:

> **First determine what the existing evidence allows us to conclude. Then
> decide what statistical synthesis, if any, is justified. Do not manufacture
> comparability.**

A conventional single pooled meta-analysis of "administrative law and
sanitation access" is *not* assumed to be justified. See
[`PROJECT_SPEC.md`](PROJECT_SPEC.md) §2 for the reasoning.

## What this is not

This is **not** the [Global Water Law Judicial Decisions Dataset](../README.md)
that occupies the rest of this repository. That dataset is a jurimetric corpus
of court decisions (Brazil/Netherlands/Canada); this review synthesizes
*household- and applicant-level empirical studies* of administrative access.
The two are deliberately kept as separate evidence bases — litigation is a
selected pathway, not a representative sample of administrative exclusion. See
`PROJECT_SPEC.md` §33–34 for why they are not combined, and how they may later
be triangulated.

They live in the same git repository as a matter of convenience (this is the
repository the researcher was working in when the review was commissioned),
not because they share a statistical model.

---

## How this review has been conducted

This section is the "process" account — written so that the researcher, a
future collaborator, or an unrelated reader auditing the method can follow
what was actually done, in what order, and why, without reading every
underlying protocol document first. It is a companion to, not a replacement
for, the full documents linked throughout — those carry the exact numbers,
scripts, and decision rules; this section carries the narrative.

### 1. Protocol first, search second

Before any database was queried, `PROTOCOL.md` fixed the research questions
and conceptual framework, and `PROJECT_SPEC.md` fixed the scope-discipline
rules that everything downstream had to obey — most importantly, the
instruction *not* to assume a pooled meta-analysis is the goal, and to treat
the question of whether one is even justified as itself something the review
has to establish with evidence, not presuppose.

### 2. A closed, disclosed search

`SEARCH_PROTOCOL.md` lays out the databases, concept blocks, and per-database
search strings. The search was run by the researcher (via institutional
access) across Scopus (18/18 planned batches), Web of Science, HeinOnline,
ProQuest, ProQuest/Sociological Abstracts, and JSTOR (partial), and closed on
2026-09-11 **before** two planned databases — SSRN and Westlaw/Lexis — were
ever reached, because the candidate pool was already judged large enough to
move forward. That is recorded as a real, disclosed gap in `SEARCH_PROTOCOL.md`
§7 and `PRISMA_WORKFLOW.md` Phase 3, not smoothed over — a systematic review
that closes its search early should say so plainly, including in any eventual
manuscript.

### 3. Deduplication with a stable, auditable identifier

34,594 raw records were merged and deduplicated (`code/search/deduplicate.py`,
DOI-match + title/year-similarity match) into 27,481 unique candidates, with
every merge logged for auditability. Each record's ID is a **stable content
hash** (of its DOI, or title+year) rather than a row number — so a record's
identity survives re-exports, re-ordering, or partial re-runs. When an
earlier batch-processing run corrupted files through unintended cross-agent
writes, it was caught by record-for-record validation rather than assumed
clean, and every subsequent screening batch was re-run in an isolated
directory with independent validation before merging (`CHANGELOG.md`).

### 4. Two-reviewer screening, at both title/abstract and full-text stages

Every record is meant to clear two independent judgments before being
included, and where that discipline could not be fully maintained, that is
disclosed rather than implied away:

- **Title/abstract** (Phase 5): all 26,222 abstract-bearing records were
  screened by an AI first-pass reviewer (`reviewer_1`) against
  `INCLUSION_EXCLUSION.md`'s twelve exclusion codes (E01–E12), explicitly
  authorized as a methodological choice in `PROJECT_SPEC.md` §14.18. A human
  second reviewer (`reviewer_2`) then reviewed all 3,665 records marked
  `include` or `unsure` via a purpose-built spreadsheet handoff (see
  [`REVIEWER_2_README.md`](02_screening/title_abstract/REVIEWER_2_README.md)).
  The two reviewers agreed 99.8% of the time — unusually high for genuinely
  independent screening. That was flagged to the researcher **before** being
  merged into the record, not treated as routine; the researcher reviewed it
  and confirmed proceeding. Anyone assessing this review's rigor should read
  that caveat alongside the resulting count (`PRISMA_WORKFLOW.md` Phase 5).
- **Full text** (Phase 6, live): the researcher supplies PDFs on a rolling
  basis (expected to take over a month); each is converted to text
  (`pdftotext -layout`), screened by the AI reviewer against the same E01–E12
  codes, and recorded via a single-record CLI
  (`code/screening/update_full_text_record.py`) rather than hand-edited, to
  keep the tracking CSV internally consistent. A human `reviewer_2` for this
  stage has not yet been assigned — an open question the researcher still
  needs to resolve, not a step silently skipped.

### 5. Extraction against a fixed codebook — and a hard rule against filling gaps from memory

Every included study is extracted into a 92-column database
(`03_extraction/extracted_data/extraction_database.csv`) against a single
governing codebook (`CODEBOOK.md`): jurisdiction, population, legal
mechanism family (ELIGIBILITY / BURDEN / DISCRETION_ACCOMMODATION /
ENFORCEMENT), outcome hierarchy (`PROJECT_SPEC.md` §7 — formal connection as
the primary outcome; effective access, economic access, and administrative
outcomes as secondary), mediators, statistical information, and provenance.

The rule that shapes this phase more than any other single rule in the
project: **never fabricate data.** Two studies cleared full-text screening
but their cached text was not available in the working session — rather than
reconstruct their findings from a general sense of what such a paper
"probably" reports, they were deliberately left unextracted and flagged for
re-upload. The same discipline governs risk-of-bias appraisal (next section):
where the correct tool cannot be produced faithfully, the field is left
blank and explained, not approximated.

### 6. Risk-of-bias ratings are deliberately blank, for now

`RISK_OF_BIAS.md` assigns each study a design-matched appraisal tool (RoB 2,
ROBINS-I, one of two JBI checklists, CASP, MMAT, AMSTAR 2, or — for
doctrinal/jurimetric legal-institutional studies with no standard tool — this
project's own Legal Institutional Evidence Appraisal Framework). None of
those six validated instruments may be reconstructed from memory: appraising
a study against "roughly what RoB 2 asks" is not the same as appraising it
against the actual current instrument. So every extracted study correctly
records **which** tool applies (`risk_of_bias_tool`) but leaves
`risk_of_bias_rating` blank, with a note deferring the real rating to a
follow-up pass done with the official instrument in hand. This is reported
as a disclosed limitation of the review's current state, not hidden as a
completed step.

### 7. Evidence classification: mechanical where safe, judgment where not

`code/analysis/build_evidence_map.py` derives what can be derived
mechanically and safely — study design class from the appraisal tool
assigned, mechanism family from the extraction's own boolean fields,
legal/institutional context copied straight from the extraction record — and
stops there. Fields that require actual judgment (which outcome family a
study's central finding really belongs to; whether a study's own statistics
are calculable enough to be quantitative-synthesis-eligible; a design class
where the appraisal tool alone is ambiguous between doctrinal and
jurimetric work) are filled by hand, one study at a time, with the reasoning
recorded in commit history and in
[`EVIDENCE_MAP_README.md`](05_analysis/descriptive/EVIDENCE_MAP_README.md).
The script prints an explicit warning for every field it leaves blank for a
human to decide, rather than guessing.

### 8. What has not started yet, and why that is a decision rather than an oversight

Quantitative feasibility assessment (Phase 11) applies `ANALYSIS_PLAN.md`
§2's decision tree to each candidate synthesis family — a corpus-level
methodological judgment, not a per-study fact — and deliberately has no
tooling built ahead of it, because the decision tree itself already *is*
the whole process; there is nothing safe to mechanize the way Phase 10's
script helps with mechanical fields. It will be run once enough of the
corpus is extracted and classified to ask the question meaningfully.
Meta-analysis, structured synthesis, sensitivity analysis, and
publication-bias assessment (Phases 12–15) have templates already built and
committed, but explicitly untested against real data and gated on Phase 11
actually finding a synthesis family eligible.

### 9. Mechanics that keep the record honest, not just the conclusions

A few small engineering choices recur throughout the pipeline because they
are what make the disclosures above credible rather than aspirational:

- **Atomic writes** (`tempfile.mkstemp()` + `os.replace()`) on every script
  that touches a tracked CSV, so a crash mid-write can never leave a
  half-written, silently-corrupt data file behind.
- **Schema validation** (`code/analysis/validate_schemas.py`) run after every
  batch of edits, checking each CSV's real header against its documented or
  generated schema.
- **A single-record CLI**, not hand-editing, for the two screening
  databases — reduces the chance of an off-by-one or copy-paste error
  silently corrupting a neighboring row.
- **Provenance fields on every record** — which reviewer, which model
  version, which date — so a decision can always be traced back to who (or
  what) made it and when.

---

## Repository map

```
00_admin/            protocol, preregistration, ethics, correspondence
01_search/           database-specific search strings, search logs, raw exports, deduplication
02_screening/        title/abstract and full-text screening, exclusion log
03_extraction/       extraction form, codebook, extracted data
04_quality/          risk-of-bias / appraisal tools and completed appraisals
05_analysis/         descriptive evidence map, effect sizes, meta-analysis, heterogeneity,
                     sensitivity, publication bias
06_outputs/          tables, figures, PRISMA flow diagram, supplementary material
07_manuscript/       draft, revisions, response to reviewers
08_code/             R and Python analysis code
09_data_dictionary/  variable definitions and transformation logic
10_reproducibility/  computational environment, version history
11_archive/          superseded material, kept rather than deleted
data/                raw / processed / metadata (canonical machine-readable data)
code/                search / screening / extraction / analysis / figures / tables scripts
```

## Reading order

1. [`PROJECT_SPEC.md`](PROJECT_SPEC.md) — the governing methodological verdict, feasibility
   assessment, scope discipline, and anti-confirmation-bias rule.
2. [`PROTOCOL.md`](PROTOCOL.md) — research questions, conceptual framework, PRISMA-P-style protocol.
3. [`SEARCH_PROTOCOL.md`](SEARCH_PROTOCOL.md) — databases, concept blocks, per-database search strings.
4. [`INCLUSION_EXCLUSION.md`](INCLUSION_EXCLUSION.md) and [`CODEBOOK.md`](CODEBOOK.md) — screening and extraction.
5. [`RISK_OF_BIAS.md`](RISK_OF_BIAS.md) — design-matched appraisal tools.
6. [`ANALYSIS_PLAN.md`](ANALYSIS_PLAN.md) — the quantitative-feasibility decision tree and, contingently, the meta-analytic model.
7. [`PRISMA_WORKFLOW.md`](PRISMA_WORKFLOW.md) — the 16-phase review workflow, phase by phase, with current status and exact figures for each.
8. [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md) — full field-by-field definitions for every tracked CSV.
9. [`02_screening/full_text/FULL_TEXT_README.md`](02_screening/full_text/FULL_TEXT_README.md) and [`02_screening/title_abstract/REVIEWER_2_README.md`](02_screening/title_abstract/REVIEWER_2_README.md) — the two-reviewer screening workflows in operational detail.
10. [`05_analysis/descriptive/EVIDENCE_MAP_README.md`](05_analysis/descriptive/EVIDENCE_MAP_README.md) — exactly which evidence-map fields are mechanically derived vs. hand-judged, and why.
11. [`SOURCES.md`](SOURCES.md) — preliminary methodological references, with verification status.
12. [`CHANGELOG.md`](CHANGELOG.md) — the full dated history of every methodological decision, correction, and status change, in the order it actually happened.

## Current status

**Phases 1–5 are complete.** Search closed 2026-09-11 with documented gaps
(SSRN and Westlaw/Lexis never reached — `SEARCH_PROTOCOL.md` §7).
Deduplication reduced 34,594 raw records to 27,481 unique candidates.
Title/abstract screening is fully double-reviewed: 3,659 include / 6 exclude,
zero conflicts, with the reviewer-agreement caveat above disclosed alongside
the number.

**Phase 6 (full-text screening) is live.**
[`02_screening/full_text/full_text_screening_database.csv`](02_screening/full_text/full_text_screening_database.csv)
holds all 3,659 title/abstract includes; **193 have been assessed so far
(92 include / 101 exclude)**, with exclusions broken down by E01–E12 reason in
`PRISMA_WORKFLOW.md` Phase 6. The remaining 3,466 await the researcher
supplying full text, expected to continue for roughly a month.

**Phase 7 (pilot extraction) was superseded** by the researcher's explicit
decision to extract every full-text include directly as it clears screening,
rather than drawing a separate ~10-study pilot subsample first.

**Phase 8 (full extraction) is fully caught up with screening.**
[`03_extraction/extracted_data/extraction_database.csv`](03_extraction/extracted_data/extraction_database.csv)
holds **all 92 fully-extracted studies (S001–S092)**, matching the 92 current
full-text includes with no outstanding gap.

**Phase 9 (risk of bias) is deliberately not yet applied** to any of the 92
extracted studies — see §6 above for why that is a disclosed limitation, not
an oversight.

**Phase 10 (evidence classification) is populated for all 92 extracted
studies** — [`05_analysis/descriptive/evidence_map.csv`](05_analysis/descriptive/evidence_map.csv),
39 of which are currently judged eligible for quantitative synthesis, all 92
for qualitative synthesis.

**Phase 11 (quantitative feasibility) has not started** — see §8 above.

A schema-validation script
([`code/analysis/validate_schemas.py`](code/analysis/validate_schemas.py))
confirms every project CSV currently matches its documented/generated
schema. See [`06_outputs/prisma/prisma_flow.md`](06_outputs/prisma/prisma_flow.md)
for the full PRISMA 2020 flow-diagram data and
[`PRISMA_WORKFLOW.md`](PRISMA_WORKFLOW.md) for the complete 16-phase table
with exact current figures for every phase.

## Operating rules for anyone (human or AI) continuing this project

See `PROJECT_SPEC.md` §60 for the full list. The ones that matter most:

- Never invent literature, search results, sample sizes, effect sizes,
  confidence intervals, or legal authorities — including by "filling in" a
  plausible-sounding risk-of-bias rating or extraction field when the source
  material or the correct instrument isn't actually in hand. Leave it blank
  and say why.
- Never pool studies merely because an effect size can mathematically be
  converted to a common metric. Substantive comparability is a separate,
  prior question.
- Disclose search, screening, and reviewer-agreement anomalies as soon as
  they're found, rather than merging them silently and letting a clean-looking
  number stand in for the messier real process.
- Keep every status claim traceable to a specific file, script, or dated log
  entry — a systematic review's credibility rests on that link holding for
  every number it reports, not just the convenient ones.

## License

MIT, inherited from the parent repository — see [`../LICENSE`](../LICENSE).
