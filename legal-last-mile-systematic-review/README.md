# The Legal Last Mile — Systematic Review

**Preliminary Systematic Review and Contingent Meta Analysis**

Companion project to the doctoral dissertation *The Legal Last Mile: Administrative
Law as a Mechanism of Connectivity and Exclusion in Sanitation Governance: A
Comparative Study of the Netherlands, Canada (Ontario), and Brazil* (Claudio Klaus).

Project status: **preliminary methodological design — search not yet executed.**

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

**Scopus is the first Tier 1 database actually searched for real** — the
researcher ran the pilot string via EUR institutional access on 2026-08-26
(`SEARCH_018`), and 500 of the ~5,443 total matching records have been
exported and ingested (see `CHANGELOG.md` 2026-08-26). Still outstanding:
the rest of that result set (batched export), abstracts (missed in this
export's field selection), and every other Tier 1/2/legal-repository
database. **If you have working institutional access,
[`01_search/EXECUTION_CHECKLIST.md`](01_search/EXECUTION_CHECKLIST.md) is a
literal "what to actually click" guide** for the rest — this is the
single highest-value thing that can happen to this project right now.

Deduplication and screening-ingest tooling
([`code/search/deduplicate.py`](code/search/deduplicate.py),
[`code/screening/init_screening_db.py`](code/screening/init_screening_db.py))
has processed all of this together: 37 candidates from three rounds of an
explicitly non-systematic `WebSearch` pilot (logged `SEARCH_003`–`SEARCH_017`,
**not** a substitute for the real search and never to be described as one)
plus the 500 real Scopus records — deduplication caught **1 real
cross-source duplicate** (the Gaikwad & Thomas 2026 exemplar, matched by
DOI), leaving **536 unique candidate records**, none yet screened.
A non-binding title-only triage memo
([`06_outputs/supplementary/title_only_triage_memo.md`](06_outputs/supplementary/title_only_triage_memo.md),
currently covering the original 37) exists to help a future reviewer
prioritize. Export adapters exist for PubMed (unvalidated — no live PubMed
export exists to test against) and Scopus (**validated against the real
2026-08-26 export**) in `code/search/adapters/`. A schema-validation script
([`code/analysis/validate_schemas.py`](code/analysis/validate_schemas.py))
confirms every project CSV currently matches its documented schema.

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
