# OSF Generalized Systematic Review Preregistration — Draft

Status: **draft, not submitted.** This document has not been posted to OSF —
this environment has no OSF account access. It is written so the
researcher can copy it directly into an OSF Generalized Systematic Review
registration form. Every section below maps to a section of `PROTOCOL.md`;
where the two differ, `PROTOCOL.md` is the source of truth and this file
should be reconciled to it before submission.

Per `PROTOCOL.md` §11, PROSPERO is not assumed to be the right registry
(the primary question is not a conventional health-intervention question);
re-confirm current PROSPERO scope before ruling it out, but proceed with
OSF here as the working plan.

---

## Title

*The Legal Last Mile: Legal and Administrative Barriers to Water and
Sanitation Access — A Systematic Review and Structured Quantitative
Evidence Synthesis*

("...and Meta-Analysis" is added only if Phase 12 of `PRISMA_WORKFLOW.md`
concludes a restricted pooled estimate is defensible for at least one
evidence family.)

## Research questions

**Primary:** How do legal and administrative institutions shape the
translation of physical availability of water and sanitation infrastructure
into effective household access, and what evidence exists concerning the
mechanisms through which eligibility screening, administrative burden,
discretion, accommodation and enforcement produce or mitigate exclusion?

**Secondary (quantitative synthesis):** Where sufficiently comparable
evidence exists, what is the magnitude of the association between specific
legal or administrative access conditions and household water or
sanitation access outcomes?

Full rationale for this framing over the two alternatives considered:
`PROTOCOL.md` §2.

## Condition or domain being studied

Access to water and sanitation services as shaped by legal and
administrative institutions (eligibility rules, administrative burden,
discretion/accommodation, enforcement, and related mechanisms — see
`PROJECT_SPEC.md` §5–6). Comparative scope centers on Brazil, the
Netherlands, and Canada (Ontario) per the parent doctoral project, but the
search is not restricted to these three jurisdictions (`SEARCH_PROTOCOL.md`
§1–3).

## Existing data / prior work

None of the search, screening, or extraction has been performed as of this
draft. Eight preliminary methodological/exemplar sources have been
identified and checked against independent sources (`SOURCES.md`) but are
explicitly not the review's evidence base.

## Hypotheses

None specified as directional hypotheses to be confirmed — this is
explicitly an evidence test, not a confirmatory study of the Legal Last
Mile framework (`PROJECT_SPEC.md` §11, "anti-confirmation-bias rule"). The
review instead pre-specifies a mechanism framework to be tested, supported,
qualified, or rejected by the evidence (`PROJECT_SPEC.md` §2).

## Eligibility criteria

Full criteria and standardized exclusion codes (E01–E12):
`INCLUSION_EXCLUSION.md`.

## Information sources

Tier 1/Tier 2 academic databases, sector-specific databases, legal/
institutional repositories, and grey literature: `SEARCH_PROTOCOL.md` §1.
Per-database search strings: `01_search/database_strategies/`.

## Study records

- **Data management:** `02_screening/title_abstract/screening_database.csv`.
- **Selection process:** two reviewers where feasible; conflicts resolved
  by discussion or a third reviewer.
- **Data collection process:** `03_extraction/extraction_form/` +
  `CODEBOOK.md`, piloted on ~10 studies before full extraction.

## Risk of bias (individual studies)

Design-matched tools: RoB 2, ROBINS-I, JBI (cross-sectional/cohort), CASP,
MMAT, plus a supplementary, explicitly non-validated Legal Institutional
Evidence Appraisal Framework for legal-empirical studies. Full detail:
`RISK_OF_BIAS.md`.

## Data synthesis

Quantitative-feasibility decision tree, effect-size strategy, contingent
meta-analytic model, heterogeneity, subgroup/moderator rules, sensitivity
analyses, and publication-bias thresholds: `ANALYSIS_PLAN.md`. Where
meta-analysis is not justified for a given evidence family, synthesis
follows SWiM (2020) reporting guidance.

**Binding commitment for this preregistration:** no title, abstract, or
manuscript section produced from this review will assert or imply a pooled
meta-analytic finding unless the quantitative-feasibility decision tree in
`ANALYSIS_PLAN.md` §2 was actually satisfied for that specific evidence
family, with the determination documented in `05_analysis/`.

## Meta-bias(es)

Publication bias assessed only where ≥ ~10 studies contribute to a
synthesis family (`ANALYSIS_PLAN.md` §9).

## Amendments

Any change to the research question, eligibility criteria, or planned
synthesis approach after this registration is submitted must be logged as
a dated, reasoned amendment on OSF itself (not just in this repository's
`CHANGELOG.md`) — per `PROTOCOL.md` §12, changes are never made silently.

## Anticipated timeline

Not specified in this draft. To be filled in by the researcher based on
actual database access and reviewer availability, since Phase 3
(database searching) is currently blocked in the automated-tooling
environment on lack of credentials for Scopus, Web of Science, HeinOnline,
Westlaw, Lexis, ProQuest, Sociological Abstracts, CanLII, and
Rechtspraak.nl (`SEARCH_PROTOCOL.md` §7).

---

## Submission checklist (for the researcher, before posting to OSF)

- [ ] Confirm OSF Generalized Systematic Review is still the appropriate
      registry (re-check PROSPERO scope as an alternative).
- [ ] Reconcile this draft against the current `PROTOCOL.md` — this file is
      a snapshot and does not auto-update.
- [ ] Fill in anticipated timeline and named reviewers.
- [ ] Submit; record the resulting OSF registration DOI/URL back into
      `PROTOCOL.md` §11 and `CHANGELOG.md`.
