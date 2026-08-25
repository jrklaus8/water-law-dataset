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

**No Tier 1/2 or legal-repository database has been searched natively** —
this environment cannot reach any of them (subscription databases need
credentials it doesn't have; even the free ones, like PubMed, Google
Scholar, CanLII, and Rechtspraak.nl, are blocked by this environment's
network egress policy). Deduplication and screening-ingest tooling
([`code/search/deduplicate.py`](code/search/deduplicate.py),
[`code/screening/init_screening_db.py`](code/screening/init_screening_db.py))
has now been run for real, on 25 candidate records surfaced by an
explicitly non-systematic exploratory pilot using Claude's `WebSearch`
tool (logged as `SEARCH_003`–`SEARCH_008`) — **not** a substitute for the
actual protocol search, and never to be described as one. Those 25 records
sit in the screening database with no screening decision made on any of
them yet.

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
