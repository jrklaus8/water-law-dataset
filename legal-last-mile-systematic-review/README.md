# The Legal Last Mile — Systematic Review

**Preliminary Systematic Review and Contingent Meta Analysis**

Companion project to the doctoral dissertation *The Legal Last Mile: Administrative
Law as a Mechanism of Connectivity and Exclusion in Sanitation Governance: A
Comparative Study of the Netherlands, Canada (Ontario), and Brazil* (Claudio Klaus).

Project status: **Phases 1–5 complete (search closed, deduplication done,
title/abstract screening double-reviewed), Phase 6 (full-text screening)
scaffolding built — see "Current status" below.**

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
7. [`PRISMA_WORKFLOW.md`](PRISMA_WORKFLOW.md) — the 16-phase review workflow and current phase.
8. [`SOURCES.md`](SOURCES.md) — preliminary methodological references, with verification status.

## Current status

**Phase 1 (repository setup) and Phase 2 (source verification) are complete.**
The OSF preregistration is drafted but not submitted
([`00_admin/preregistration/osf_preregistration_draft.md`](00_admin/preregistration/osf_preregistration_draft.md)).

**Phase 3 (database searching) closed 2026-09-11 by researcher decision** —
the candidate pool was judged large enough to move to screening before
every planned database was reached. Databases actually searched: Scopus
(18/18 planned batches, 5,984 records), Web of Science (`SEARCH_035`,
4,058 records), HeinOnline (`SEARCH_036`–`SEARCH_038`, minimal real yield
— most of its identified hits were never exportable or never delivered),
ProQuest (`SEARCH_039`, 7,728 records via a full account-based export),
ProQuest/Sociological Abstracts (`SEARCH_040`, 16,736 records), and JSTOR
(`SEARCH_041`, 50 of 356 identified). **SSRN and Westlaw/Lexis were never
searched at all** — a real, disclosed gap, documented in
`SEARCH_PROTOCOL.md` §7 and `PRISMA_WORKFLOW.md` Phase 3 rather than
omitted from any manuscript output.

Deduplication and screening-ingest tooling
([`code/search/deduplicate.py`](code/search/deduplicate.py),
[`code/screening/init_screening_db.py`](code/screening/init_screening_db.py))
has processed the full closed-search-phase pool — **34,594 raw records**
across the WebSearch pilot, the `SOURCES.md` exemplars, and every database
above — finding **7,113 duplicates** (heavy Scopus/Web of
Science/ProQuest cross-database journal overlap, exactly as expected) and
leaving **27,481 unique candidate records, 26,222 of which have a real
abstract**. `record_id` is a stable content hash rather than a positional
index (`CHANGELOG.md` 2026-09-10, later still).

**All 26,222 abstract-bearing records have been screened at title/abstract
by two reviewers.** Claude's first-pass AI screening (`reviewer_1`,
explicitly authorized by the researcher per `PROJECT_SPEC.md` §14.18, run
as 39 isolated parallel batches with independent per-batch validation
after an earlier shared-directory run suffered real cross-agent file
corruption — see `CHANGELOG.md`) produced **3,062 include / 22,557
exclude / 603 unsure**. A human `reviewer_2` pass over all 3,665
include+unsure records completed 2026-09-12 via a purpose-built Excel
handoff (see
[`REVIEWER_2_README.md`](02_screening/title_abstract/REVIEWER_2_README.md)),
setting `final_decision`: **3,659 include / 6 exclude, zero conflicts**
(strict definition — reviewer_1 `include` vs. reviewer_2 `exclude` — see
`DATA_DICTIONARY.md`). **Flagged, not hidden**: the 99.8% agreement rate
between the two reviewers is unusually high for an independent second
pass; this was raised with the researcher before merging (not merged
silently) and is documented in `CHANGELOG.md` and `PRISMA_WORKFLOW.md`
Phase 5 for anyone assessing this review's rigor.
`exclude_spotcheck_sample.csv` (a 120-record random QA sample of the
excludes) remains available and unreviewed if an independent check on the
exclude population is wanted later.

**Phase 6 (full-text screening) scaffolding is built.**
[`02_screening/full_text/full_text_screening_database.csv`](02_screening/full_text/full_text_screening_database.csv)
was seeded 2026-09-12 from all 3,659 `final_decision == "include"`
records, with retrieval status, decision, and reviewer fields blank
pending the researcher's actual retrieval and screening work — see
[`FULL_TEXT_README.md`](02_screening/full_text/FULL_TEXT_README.md) for
the workflow. Export adapters exist for PubMed and a shared RIS format
covering HeinOnline/ProQuest/Sociological Abstracts/JSTOR/SSRN (validated
against real exports from all but SSRN), and for Scopus and Web of Science
(**both validated against real exports**) in `code/search/adapters/`. A
schema-validation script
([`code/analysis/validate_schemas.py`](code/analysis/validate_schemas.py))
confirms every project CSV currently matches its documented/generated
schema.

All other CSV templates in this tree still carry headers only — there is
no fabricated data anywhere in this project. See
[`06_outputs/supplementary/preliminary_results.md`](06_outputs/supplementary/preliminary_results.md)
for the explicit current-evidence status and
[`PRISMA_WORKFLOW.md`](PRISMA_WORKFLOW.md) for what phase comes next and what
it requires (principally: access to Scopus, Web of Science, HeinOnline,
Westlaw/Lexis, and the other Tier 1/Tier 2 databases listed in
`SEARCH_PROTOCOL.md`, which this environment does not currently have).

## Operating rules for anyone (human or AI) continuing this project

See `PROJECT_SPEC.md` §60 for the full list. The two that matter most:

- Never invent literature, search results, sample sizes, effect sizes,
  confidence intervals, or legal authorities.
- Never pool studies merely because an effect size can mathematically be
  converted to a common metric. Substantive comparability is a separate,
  prior question.

## License

MIT, inherited from the parent repository — see [`../LICENSE`](../LICENSE).
