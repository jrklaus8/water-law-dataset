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

**Scopus is the first Tier 1 database actually searched for real, and as
of 2026-09-11, all 18 planned batches are done, every one with real
abstracts.** **Web of Science is the second — its first batch landed the
same day.** The researcher ran the Scopus pilot string via EUR
institutional access on 2026-08-26 (`SEARCH_018`, 500 records, no
abstracts) and then, on 2026-09-10–11, every batch of
[`01_search/scopus_batch_plan_2026-08-26.md`](01_search/scopus_batch_plan_2026-08-26.md)
(**with** abstracts — see `CHANGELOG.md` 2026-09-10 and 2026-09-11).
**5,984 of ~5,443+ originally estimated matching Scopus records exported**
(the estimate was always approximate) — Scopus is now fully searched per
this plan's design. Web of Science's first batch (`SEARCH_035`,
2026-09-11, **with** abstracts) added **4,058 records** — plus HeinOnline,
Westlaw/Lexis, ProQuest, Sociological Abstracts, CanLII, and
Rechtspraak.nl, none of which have been touched yet.

Deduplication and screening-ingest tooling
([`code/search/deduplicate.py`](code/search/deduplicate.py),
[`code/screening/init_screening_db.py`](code/screening/init_screening_db.py))
has processed all of this together: 37 candidates from three rounds of an
explicitly non-systematic `WebSearch` pilot (logged `SEARCH_003`–`SEARCH_017`,
**not** a substitute for the real search and never to be described as one),
3 `SOURCES.md` exemplars, 5,984 real Scopus records (500 from
`SEARCH_018` plus 5,484 across all 18 planned batches), and 4,058 real
Web of Science records — the 2026-09-11 full re-run of the deduplication
script caught **3,475 duplicates** (2,934 of those from heavy
Scopus/Web-of-Science journal overlap alone — exactly what a working
cross-database dedup should catch — on top of 541 within-Scopus and 1
earlier cross-source duplicate, the Gaikwad & Thomas 2026 exemplar),
leaving **7,145 unique candidate records, 7,109 of which have a real
abstract**. `record_id` is a stable content hash rather than a positional
index (`CHANGELOG.md` 2026-09-10, later still).

**All 7,109 abstract-bearing records have now been screened** against
`INCLUSION_EXCLUSION.md` by Claude acting as a first-pass AI reviewer —
explicitly authorized by the researcher as a methodological choice, per
`PROJECT_SPEC.md` §14.18 — with results independently validated batch by
batch before merging (`CHANGELOG.md` 2026-09-10, final, and 2026-09-11,
two entries). **Result: 1,710 include / 5,151 exclude / 248 unsure.**
(The Web of Science batch's include/unsure rate, ~13%, came in well below
Scopus's ~25-30% — expected, since `TS=` is broader than
`TITLE-ABS-KEY` and this batch is only WoS's non-overlapping residue
after cross-database dedup already removed everything it shared with
Scopus.) This is a **provisional first pass only**: no human `reviewer_2`
or conflict resolution has happened yet, so no record's inclusion is
final — real dual-review PRISMA screening still needs a second, human
pass before Phase 6 (full-text screening) can treat this pool as settled.
A ready-to-use handoff for that pass exists:
[`02_screening/title_abstract/reviewer_2_queue.csv`](02_screening/title_abstract/reviewer_2_queue.csv)
(1,958 include+unsure records) and `exclude_spotcheck_sample.csv` (a
120-record random QA sample of the excludes) — see
[`REVIEWER_2_README.md`](02_screening/title_abstract/REVIEWER_2_README.md).
A non-binding title-only triage memo
([`06_outputs/supplementary/title_only_triage_memo.md`](06_outputs/supplementary/title_only_triage_memo.md),
still only covering the original 37) exists to help a future reviewer
prioritize. Export adapters exist for PubMed and a shared RIS format
covering HeinOnline/ProQuest/Sociological Abstracts/JSTOR/SSRN
(unvalidated — no live export from any of these exists to test against
yet), and for Scopus and Web of Science (**both validated against real
exports**) in `code/search/adapters/`. A schema-validation script
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
