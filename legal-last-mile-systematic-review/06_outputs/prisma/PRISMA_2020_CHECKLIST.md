# PRISMA 2020 Reporting Checklist (Phase 16)

`SOURCES.md` §5 cites PRISMA 2020 (Page et al. 2021, *BMJ*, 372:n71),
confirmed via web search this session. Unlike the six risk-of-bias tools
in `SOURCES.md` §9–13, PRISMA's checklist is designed to be filled in by
the reviews that use it and is openly licensed (CC BY) — reproducing its
structure here is normal practice, not a copyright concern the way
copying RoB 2's own signaling questions would be.

**Still verify exact item wording against the official checklist
(prisma-statement.org, or the BMJ paper directly) before final
submission** — this table was reconstructed from well-established
knowledge of PRISMA 2020's structure without a live fetch against the
publisher in the session that wrote it (the same access-blocked situation
noted throughout `SOURCES.md`), so treat item numbering/wording here as a
close approximation to check, not the authoritative final text.

**Purpose of the "Addressed where" column**: most PRISMA items are
already substantively addressed somewhere in this repository, well before
manuscript writing — this column says where, so drafting the actual
manuscript (`07_manuscript/draft/manuscript_outline.md`,
`PUBLICATION_PLAN.md`) is a matter of writing up what's already recorded,
not starting from a blank page. Check "Reported in manuscript" only once
the actual manuscript text covers that item — this checklist tracks
reporting completeness, not underlying methodological completeness (a
row can have real content "Addressed where" while still being unchecked
because the manuscript hasn't been drafted yet).

| # | Item | Addressed where (this repo) | Reported in manuscript |
|---|---|---|---|
| 1 | Title: identify the report as a systematic review | `manuscript_outline.md` | ☐ |
| 2 | Abstract: structured summary (PRISMA 2020 for Abstracts) | `07_manuscript/draft/manuscript_outline.md` | ☐ |
| 3a | Rationale, in the context of existing knowledge | `PROJECT_SPEC.md` §1–3, `SOURCES.md` | ☐ |
| 3b | Objectives, as an explicit question (PICO or equivalent) | `PROTOCOL.md` §1–2, `PROJECT_SPEC.md` §5–7 | ☐ |
| 5 | Eligibility criteria | `INCLUSION_EXCLUSION.md`, `PROTOCOL.md` §5 | ☐ |
| 6 | Information sources and last-search date | `SEARCH_PROTOCOL.md`, `search_log.csv`, `PRISMA_WORKFLOW.md` Phase 3 | ☐ |
| 7 | Full search strategy for each database | `SEARCH_PROTOCOL.md` per-database strings, `search_log.csv`'s `exact_search_string` | ☐ |
| 8 | Selection process (how many reviewers, independently or not) | `PROTOCOL.md` §6, `PRISMA_WORKFLOW.md` Phase 5 | ☐ |
| 9 | Data collection process | `CODEBOOK.md`, `03_extraction/extraction_form/EXTRACTION_FORM.md`, `REPRODUCIBILITY.md` §3 | ☐ |
| 10a | Data items: outcomes sought | `CODEBOOK.md` §5, `PROJECT_SPEC.md` §7 | ☐ |
| 10b | Data items: other variables sought | `CODEBOOK.md` §1–4, §6–9 | ☐ |
| 11 | Risk-of-bias assessment method | `RISK_OF_BIAS.md`, `04_quality/appraisal_forms/APPRAISAL_FORM.md` | ☐ |
| 12 | Effect measures used | `ANALYSIS_PLAN.md` §4 | ☐ |
| 13a | Synthesis eligibility processes | `ANALYSIS_PLAN.md` §1–2 | ☐ |
| 13b | Data preparation/tabulation methods | `05_analysis/descriptive/EVIDENCE_MAP_README.md`, `code/analysis/build_evidence_map.py` | ☐ |
| 13c | Method for tabulating/visually displaying results | `08_code/R/01_meta_analysis.R` (forest plots), `SWIM_SYNTHESIS_TEMPLATE.md` (harvest plots) | ☐ |
| 13d | Synthesis methods (meta-analysis model, software) | `ANALYSIS_PLAN.md` §5, `08_code/R/01_meta_analysis.R`, `08_code/R/README.md` | ☐ |
| 13e | Method for exploring heterogeneity/inconsistency | `ANALYSIS_PLAN.md` §6–8, `08_code/R/01_meta_analysis.R` | ☐ |
| 13f | Sensitivity analyses | `ANALYSIS_PLAN.md` §10, `08_code/R/02_sensitivity_analysis.R` | ☐ |
| 14 | Reporting-bias assessment methods | `ANALYSIS_PLAN.md` §9, `08_code/R/03_publication_bias.R` | ☐ |
| 15 | Certainty assessment methods | `RISK_OF_BIAS.md` §3, `04_quality/risk_of_bias/EVIDENCE_LIMITATIONS_TEMPLATE.md` | ☐ |
| 16a | Study selection: numbers screened/assessed/excluded, reasons | `06_outputs/prisma/prisma_flow.md` | ☐ |
| 16b | Study selection: excluded studies considered potentially eligible | `02_screening/title_abstract/exclude_spotcheck_sample.csv`, `02_screening/exclusion_log/exclusion_log.csv` | ☐ |
| 17 | Study characteristics | `05_analysis/descriptive/evidence_map.csv`, `03_extraction/extracted_data/extraction_database.csv` | ☐ |
| 18 | Risk of bias in included studies | `extraction_database.csv`'s quality fields, `04_quality/appraisal_forms/` | ☐ |
| 19 | Results of individual studies | `extraction_database.csv`, `05_analysis/effect_sizes/effect_sizes.csv` | ☐ |
| 20a | Synthesis results: study/participant characteristics | `evidence_map.csv` | ☐ |
| 20b | Synthesis results: statistical synthesis, heterogeneity | `05_analysis/meta_analysis/`, `05_analysis/heterogeneity/` (once populated) | ☐ |
| 20c | Synthesis results: sensitivity analyses | `05_analysis/sensitivity/` (once populated) | ☐ |
| 20d | Synthesis results: unpooled/SWiM synthesis | `06_outputs/supplementary/*_swim_synthesis.md` (once written per family) | ☐ |
| 21 | Reporting biases assessed | `05_analysis/publication_bias/` (once populated) | ☐ |
| 22 | Certainty of evidence per outcome | `04_quality/risk_of_bias/` narrative (once written) | ☐ |
| 23a | Interpretation of results in context of other evidence | `07_manuscript/draft/manuscript_outline.md`, `SOURCES.md` | ☐ |
| 23b | Limitations of the included evidence | `RISK_OF_BIAS.md` §3, `EVIDENCE_LIMITATIONS_TEMPLATE.md` | ☐ |
| 23c | Limitations of the review process itself | `PRISMA_WORKFLOW.md` Phase 3's disclosed search gaps (SSRN, Westlaw/Lexis never searched), the reviewer_2 agreement-rate caveat (`CHANGELOG.md` 2026-09-12) | ☐ |
| 23d | Implications for practice/policy/future research | `PROJECT_SPEC.md` §1–2, `07_manuscript/draft/manuscript_outline.md` | ☐ |
| 24a | Registration information | `00_admin/preregistration/osf_preregistration_draft.md` (drafted, not yet submitted — see `PRISMA_WORKFLOW.md` Phase 2) | ☐ |
| 24b | Protocol availability | `PROTOCOL.md`, this repository itself | ☐ |
| 24c | Amendments to protocol/registration, with rationale | `CHANGELOG.md` (`PROTOCOL.md` §12's amendment-logging requirement) | ☐ |
| 25 | Funding/support sources and role | *(not yet recorded anywhere in this repo — add when known)* | ☐ |
| 26 | Competing interests of review authors | *(not yet recorded anywhere in this repo — add when known)* | ☐ |
| 27 | Availability of data, code, and materials | This repository (public git history), `REPRODUCIBILITY.md` | ☐ |

## Two rows with nothing to point to yet

Items 25 (funding/support) and 26 (competing interests) have no existing
home in this repository — they're standard journal-submission
disclosures rather than methodological content this pipeline generates,
so there's nothing to link to until the researcher supplies them. Don't
leave them silently blank at submission time; add the actual disclosure
text directly to this checklist (or a `00_admin/` file) once known.
