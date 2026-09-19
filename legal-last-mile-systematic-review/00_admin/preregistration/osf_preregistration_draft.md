# OSF Generalized Systematic Review Preregistration — Draft

Status: **draft, ready for submission; not yet submitted.** This document
has not been posted to OSF — this environment has no OSF account access,
so the actual submission click can only be done by the researcher. It is
written so the researcher can copy it directly into an OSF Generalized
Systematic Review registration form. Every section below maps to a
section of `PROTOCOL.md`; where the two differ, `PROTOCOL.md` is the
source of truth and this file should be reconciled to it before
submission.

Per `PROTOCOL.md` §11, PROSPERO was considered and ruled out: it is scoped
to health/welfare-outcome reviews and, separately, does not accept
registration once data extraction has begun — both of which foreclose it
here (this review's question is legal/administrative, not a health
intervention, and extraction started 2026-09-12). OSF is the registry
used below.

## Disclosure: this is a retrospective registration, not a fully a priori one

Be direct about this on OSF itself, not just here — it is exactly the
kind of thing this project's own `CHANGELOG.md` has consistently
"flagged, not hidden," and a registration that quietly implied otherwise
would undercut the point of registering at all.

- **The content of this protocol was drafted 2026-08-22**, the day the
  repository was scaffolded, before any database was searched
  (`CHANGELOG.md` "2026-08-22 — Initial scaffold"). At that point the
  research question, eligibility criteria (`INCLUSION_EXCLUSION.md`),
  extraction codebook (`CODEBOOK.md`), risk-of-bias tool assignments
  (`RISK_OF_BIAS.md`), and analysis plan (`ANALYSIS_PLAN.md`) were all
  already fixed in the form found in this repository today — none of them
  have been revised in response to what the search or screening later
  turned up (`PROTOCOL.md` §12 requires any such change to be logged as a
  dated amendment, and none has been).
- **It was not actually submitted to OSF at that time.** By the time of
  this submission, the search has been executed and closed (2026-09-11),
  title/abstract screening is complete (2026-09-12), and full-text
  screening/extraction are live and ongoing (`PRISMA_WORKFLOW.md`). So
  while the plan itself was fixed before any evidence was seen, the
  formal registration timestamp postdates that evidence by roughly three
  weeks.
- **Net effect:** this protects against the main thing preregistration
  guards against — revising your question, codebook, or analysis plan
  after seeing what the data show — but it does not carry the same
  evidentiary weight as a registration whose *timestamp* also precedes
  data collection. State both dates (drafted 2026-08-22; registered
  [fill in actual OSF submission date]) explicitly in the OSF entry
  itself, and reference this section if OSF's form allows free-text
  context.

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

**As originally drafted (2026-08-22):** none of the search, screening, or
extraction had been performed. Eight preliminary methodological/exemplar
sources had been identified and checked against independent sources
(`SOURCES.md`) but were explicitly not treated as the review's evidence
base.

**As of actual OSF submission (2026-09-12):** the plan above was not
revised in light of any of the following, but for full transparency the
review has since progressed to: search executed and closed across five
databases with disclosed gaps (Scopus and Web of Science fully covered;
HeinOnline, ProQuest, and ProQuest/Sociological Abstracts covered with
real limitations; SSRN and Westlaw/Lexis never reached) — 27,481 unique
candidate records after deduplication; title/abstract screening complete
(3,659 records advanced to full-text screening, with a disclosed
near-total reviewer_1/reviewer_2 agreement rate — see
`PRISMA_WORKFLOW.md` Phase 5); full-text screening live and ongoing (175
of 3,659 assessed as of this date); full extraction caught up with
full-text screening (85 of 85 current includes extracted); risk-of-bias
rating and quantitative-feasibility assessment (Phases 9 and 11) not yet
started. `06_outputs/supplementary/preliminary_results.md` is the
up-to-date public account of this progress and should be linked from the
OSF entry.

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

Realized-to-date, per `CHANGELOG.md` (fill in remaining estimates before
submission):

- 2026-08-22: protocol and codebook drafted (this document's content
  originates here).
- 2026-08-25 – 2026-09-11: database searching (pilot rounds, then Scopus,
  Web of Science, HeinOnline, ProQuest, ProQuest/Sociological Abstracts,
  JSTOR); search closed 2026-09-11.
- 2026-09-10 – 2026-09-12: title/abstract screening, including the human
  reviewer_2 pass; complete 2026-09-12.
- 2026-09-12 – ongoing: full-text screening and extraction, running in
  lockstep, dependent on the researcher supplying full-text PDFs on a
  rolling basis (expected to continue for over a month from 2026-09-12).
- Not yet scheduled: risk-of-bias appraisal (Phase 9, blocked on
  obtaining the official versions of RoB 2 / ROBINS-I / JBI / CASP / MMAT
  rather than reconstructing them from memory), quantitative-feasibility
  determination (Phase 11), and manuscript drafting. **Fill in realistic
  target dates for these before submitting** — an OSF registration with
  no forward timeline at all is a weaker record than one with dates the
  researcher is prepared to be a few months off on.

---

## Submission checklist (for the researcher, before posting to OSF)

- [x] Confirm OSF Generalized Systematic Review is the appropriate
      registry — PROSPERO ruled out 2026-09-12 (see top of this document).
- [ ] Reconcile this draft against the current `PROTOCOL.md` — this file is
      a snapshot and does not auto-update.
- [ ] Fill in remaining anticipated-timeline dates (Phase 9, Phase 11,
      manuscript) and named reviewers.
- [ ] On OSF's registration form, state both dates explicitly: protocol
      drafted 2026-08-22; registered [actual submission date] — see the
      "Disclosure" section above for why this distinction matters and
      should not be glossed over.
- [ ] Submit; record the resulting OSF registration DOI/URL back into
      `PROTOCOL.md` §11 and `CHANGELOG.md` (as a new dated entry, not an
      edit to an old one).
- [ ] If also archiving this repository on Zenodo, cross-link the two:
      add the OSF DOI to the Zenodo deposit's "related identifiers" field
      (relation: "isSupplementTo" or "isDocumentedBy"), and add the
      Zenodo DOI back into this OSF entry once it exists.
