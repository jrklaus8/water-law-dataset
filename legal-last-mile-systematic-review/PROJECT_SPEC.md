# The Legal Last Mile — Research Build Specification

Project status: Preliminary methodological design
Principal researcher: Claudio Klaus
Doctoral project: *The Legal Last Mile: Administrative Law as a Mechanism of
Connectivity and Exclusion in Sanitation Governance: A Comparative Study of
the Netherlands, Canada (Ontario), and Brazil*

This is the canonical governing specification for the systematic review. It
is derived from the research build specification supplied to build this
project, reorganized for reference rather than narration. Where a later
document (`PROTOCOL.md`, `ANALYSIS_PLAN.md`, etc.) restates part of this file
in operational form, this file is the source of truth for the *reasoning*
behind the rule; the operational documents are the source of truth for the
*procedure*.

---

## 1. Purpose

This project is a reproducible, publication-oriented systematic review and
possible meta-analysis connected to the doctoral research. It must not assume
a conventional meta-analysis is appropriate. The governing principle:

> **First determine what the existing evidence allows us to conclude. Then
> decide what statistical synthesis, if any, is justified.**

Intended design:

> **Systematic review + structured quantitative evidence synthesis +
> contingent meta-analysis + comparative socio-legal synthesis**

The meta-analysis is an empirical *consequence* of the review, not its
purpose. Do not force heterogeneous evidence into a pooled estimate.

## 2. Doctoral research context

**Research question:** How administrative law, regulatory institutions, legal
procedures and governance structures affect the ability of individuals and
communities to access sanitation services and participate meaningfully in
sanitation governance, compared across the Netherlands, Canada (Ontario), and
Brazil.

**Working concept — the Legal Last Mile:** the legal and administrative space
between the physical availability of an essential service connection and its
formal realization for a household or individual. Treat this as a research
device to be *tested*, not a conclusion the review must prove.

**Initial analytical dimensions** (to be tested, not assumed):
1. legal eligibility
2. administrative burden
3. discretion and accommodation
4. enforcement and sanctions

### Scope discipline

Do not silently treat as interchangeable: drinking water connection, sewer
connection, wastewater collection, sanitation service, utility account
eligibility, water quality, affordability, service continuity, disconnection,
infrastructure availability. Record the precise service and outcome studied.

Do not conflate units of analysis: household, individual, property,
applicant, settlement, municipality, utility, regulatory institution,
judicial decision. For the main evidence synthesis, prioritize the household
or applicant level when examining access.

## 3. Core methodological verdict

A single pooled meta-analysis of "administrative law and sanitation access"
is **not justified at the outset**. A systematic review **is** justified. A
structured quantitative evidence synthesis **is** justified. Restricted
meta-analyses **may** be justified once the search identifies sufficiently
comparable study families.

**Why a universal meta-analysis is inappropriate:** the literature differs in
legal mechanisms, institutional settings, jurisdictions, populations, service
types, outcomes, study designs, causal identification, measurement, and
effect measures. Legal recognition vs. non-recognition, administrative
assistance vs. usual procedure, documentation requirements, land tenure,
service-area eligibility, political coordination, judicial review, and
administrative discretion are not one common intervention. Formal connection,
water quantity, reliability, affordability, application success, and service
continuity are not one common outcome. **A mathematically convertible
statistic is not automatically a substantively comparable effect.**

**Label:** *Systematic Review with Structured Quantitative Evidence Synthesis
and Contingent Meta Analysis.* Do not use "meta-analysis" in any output title
until the evidence supports it. If a restricted meta-analysis is ultimately
justified, the final paper may be titled *The Legal Last Mile: Legal and
Administrative Barriers to Water and Sanitation Access: A Systematic Review
and Meta Analysis.*

### Preliminary feasibility assessment

| Question | Preliminary assessment |
|---|---|
| Relevant empirical literature exists | Yes |
| Quantitative studies exist | Yes |
| Legal and administrative exposures exist | Yes |
| Measurable access outcomes exist | Yes |
| Comparable effect estimates exist | Some |
| Comparable estimates across all jurisdictions | Uncertain |
| Comparable estimates across all mechanisms | No |
| One global pooled estimate | Not currently defensible |
| Restricted meta-analyses | Potentially feasible |
| Quantitative evidence synthesis | Strongly feasible |
| Systematic review | Strongly feasible |
| Scoping review | Fallback only |

This table is a preliminary judgment, not a result — it has not yet been
tested against a completed search. Revisit after Phase 11 of `PRISMA_WORKFLOW.md`.

## 4. Unit of analysis (three levels — never conflate)

| Level | Unit | Use |
|---|---|---|
| Review level | Primary empirical study | Systematic review |
| Meta-analytic level | Independent effect estimate | Meta-analysis |
| Judicial-empirical level | Judicial decision | Separate jurimetric study |

A single study can report multiple effect estimates. Do not treat multiple
estimates from the same study as independent observations unless the
analysis explicitly models dependence (see `ANALYSIS_PLAN.md` §"Dependent
effect sizes"). For the first publication, prefer one prespecified effect per
study and outcome family wherever possible.

## 5. Conceptual framework

```
STRUCTURAL CONDITIONS
  legal status · property status · documentation · income · geography · institutional capacity
        v
ADMINISTRATIVE ARCHITECTURE
  eligibility screening · administrative burden · discretion · accommodation · enforcement · review · participation
        v
ADMINISTRATIVE NAVIGATION
  understand requirements · apply · satisfy requirements · obtain accommodation · challenge decisions
        v
SERVICE ACCESS
  formal connection · continuity · reliability · quantity · affordability · effective use
        v
INCLUSION / EXCLUSION
```

Administrative law is not treated as the only possible causal factor —
evidence may involve property law, planning law, municipal law, identity
systems, land regularization, utility regulation, public administration,
regulatory governance, and political institutions. The broad exposure
category is therefore **legal and administrative access conditions**, with
administrative law as the central analytical lens.

## 6. Mechanism coding framework

Initial mechanism families: `ELIGIBILITY`, `BURDEN`,
`DISCRETION_ACCOMMODATION`, `ENFORCEMENT`.

Full code list, mediators, and moderators are specified in `CODEBOOK.md` §5–6.
Do not add variables merely to make the model more quantitative; many
moderators should remain contextual codes rather than statistical variables.

## 7. Outcome hierarchy

Primary outcome: formal household connection to a networked water or
sanitation service (connected vs. not, probability of connection/
formalization, approval/refusal).

Secondary outcomes: effective access (quantity, reliability, continuity,
service hours, quality, distance to source); economic access (connection
cost, expenditure, affordability, tariff burden); administrative outcomes
(submission, completion, approval, refusal, delay, appeal, complaint,
enforcement action). **Do not pool these simply because they all use the
word "access."**

## 8. Candidate meta-analytic families

The search must determine whether any of the following contain enough
comparable studies to pool. Do not pool causal intervention effects with
observational associations in the same primary model — these are different
estimands and belong in separate synthesis families even when they are about
the same broad topic.

**Family A — Legal recognition and access.** Exposure: legal recognition,
recognized vs. unrecognized settlement, formal vs. informal tenure, service
eligibility, land title. Outcome: formal connection, water/sanitation access,
quantity, reliability. Likely measures: OR, RR, risk difference, MD. Strong
candidate.

**Family B — Administrative assistance and access.** Exposure: bureaucratic
assistance, administrative facilitation, procedural simplification.
Comparator: usual procedure. Outcome: formal service connection, application
success. Potentially highly causal, but study count may be too small to pool
— use structured quantitative synthesis if so.

**Family C — Administrative/legal barriers and access inequality.** Exposure:
legal or administrative barriers, documentation, eligibility restrictions,
formalization barriers. Outcome: unequal access, connection probability,
service quality/reliability. Conceptually attractive but potentially too
heterogeneous; treat as secondary synthesis unless evidence is unusually
consistent.

## 9. Relationship with the Global Water Law Judicial Decisions Dataset

This repository also hosts the **Global Water Law Judicial Decisions Dataset**
(v0.3.0; Brazil 11,724 / Netherlands 68,654 collected / Canada 3,218 ≈ 83,596
records total — see `../RESEARCH_CONTEXT.md`). The dataset has known coverage
and record-quality differences across jurisdictions, including substantial
title-only material in the Canadian sub-dataset and filtering issues in the
Dutch corpus (`../SUPERVISOR_REPORT_v0.3.0.md`, `../FUTURE_WORK.md`).

**The judicial dataset must not enter the meta-analysis.** The systematic
review observes households, communities, applicants, and administrative/
service-access outcomes. The judicial dataset observes litigation — a
*selected* pathway. A household can experience administrative exclusion
without ever producing a court decision, so judicial decisions cannot be
treated as a representative sample of access problems, and case counts must
never be used as evidence of population prevalence unless the research
question specifically concerns litigation itself.

Recommended role of the judicial dataset:

| Role | Use it? |
|---|---|
| Included in the meta-analysis | **No** |
| Separate empirical dataset | Yes |
| Triangulation | Yes — "a separate source of evidence concerning the legal visibility and adjudication of water governance disputes," never "statistical validation of household-level evidence" |
| Basis for a second, distinct paper (jurimetric comparison) | Strongly recommended |
| Hypothesis generation | Yes |
| Mixed-methods doctoral architecture | Yes, at the programme level |

Doctoral mixed-methods architecture:

```
SYSTEMATIC REVIEW → identifies empirical mechanisms
        v
COMPARATIVE DOCTRINAL ANALYSIS → specifies jurisdictional legal mechanisms
        v
JUDICIAL DECISIONS DATASET → identifies litigation visibility and adjudication patterns
        v
THEORY DEVELOPMENT (Legal Last Mile, administrative exclusion, institutional connectivity)
        v
FUTURE EMPIRICAL WORK (administrative records, process tracing, interviews if justified, spatial/service data)
```

These components remain methodologically distinct.

## 10. What stays primarily in the dissertation

Not duplicated into the standalone review paper: full comparative doctrinal
analysis; detailed Netherlands/Ontario/Brazil chapters; full judicial dataset
analysis; the full Legal Last Mile typology; the Administrative Ghost theory;
administrative capital theory; detailed reform proposals; jurisdiction-
specific policy recommendations. The review paper answers what the empirical
literature shows — it does not attempt to prove the dissertation, and it is
not a compressed version of the whole dissertation.

## 11. Anti-confirmation-bias rule

The project must actively search for evidence that:
- contradicts the Legal Last Mile framework
- finds no association between legal status and access
- finds administrative barriers do not matter
- finds infrastructure availability is the dominant explanation
- finds socioeconomic or political factors explain the association
- finds legal intervention or administrative discretion *improves* access
- finds administrative requirements protect legitimate safety or fiscal objectives

The review is an evidence test, not a confirmation exercise.

## 12. Search stopping rule

Do not claim the search is exhaustive until: all protocol databases have been
searched; all jurisdiction-specific searches are complete; backward and
forward citation searching are complete; relevant grey literature has been
searched; deduplication and screening are complete; search documentation is
preserved. Until then, label it **"Preliminary systematic search."**

## 13. Evidence status labels

Every result must be classifiable as one of:

- **OBSERVED** — directly reported by the primary study.
- **CALCULATED** — derived by the review team from reported information.
- **ASSUMED** — a necessary methodological assumption (e.g., a reconstructed
  standard error).
- **INTERPRETED** — conceptual interpretation of the evidence.

Never blur these categories. See `REPRODUCIBILITY.md` for provenance fields
that must accompany every extracted statistic.

## 14. Operating instructions (binding on any contributor, human or AI)

1. Never invent literature.
2. Never invent database results.
3. Never invent sample sizes.
4. Never invent effect sizes.
5. Never invent confidence intervals.
6. Never invent legal authorities.
7. Never claim an exhaustive search unless it was actually completed.
8. Never silently change inclusion criteria.
9. Never silently change the research question.
10. Never pool studies merely because an effect size can mathematically be converted.
11. Never treat judicial decisions as representative household-level observations.
12. Never treat the Legal Last Mile hypothesis as established.
13. Always distinguish observed, calculated, assumed, and interpreted evidence.
14. Preserve raw data — never overwrite an original search export or extraction.
15. Record provenance for every extracted statistic.
16. Document every methodological decision.
17. Flag uncertainty rather than filling gaps.
18. Ask for human confirmation when a major methodological choice is genuinely ambiguous.
19. Prefer reproducibility over convenience.
20. Prefer a defensible non-meta-analytic synthesis over a weak meta-analysis.

## 15. Definition of success

The project succeeds if it produces a defensible answer to:

> **What does the existing empirical evidence actually allow us to conclude
> about the relationship between legal and administrative conditions and
> access to water and sanitation services?**

Any of the following are legitimate scholarly outcomes — a meta-analysis is
not the success criterion, methodological defensibility is:

- **A.** A restricted meta-analysis.
- **B.** Several restricted meta-analyses.
- **C.** A systematic review with structured quantitative evidence synthesis but no pooled estimate.
- **D.** A systematic review with qualitative mechanism synthesis and a small quantitative evidence map.

## 16. Provisional central contribution (revise after the search)

> Existing empirical research provides evidence that legal and administrative
> conditions can shape access to water and sanitation services, but the
> evidence is fragmented across disciplines, jurisdictions, mechanisms,
> populations and outcome measures. The literature does not justify treating
> administrative exclusion as a single homogeneous exposure or producing one
> universal pooled effect. However, restricted evidence families may support
> quantitative synthesis, while the broader literature supports a structured
> socio-legal account of the mechanisms through which eligibility, burden,
> discretion, accommodation and enforcement influence the translation of
> infrastructure availability into effective access.

This is provisional until the search is complete, and must be revised —
including toward disconfirmation — if the evidence does not support it.
