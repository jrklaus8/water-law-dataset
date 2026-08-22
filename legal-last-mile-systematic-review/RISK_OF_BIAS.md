# Risk of Bias / Quality Appraisal

No single universal tool is used. **Classify study design first**, then
apply the matched tool. Record `risk_of_bias_tool` and `risk_of_bias_rating`
per study in the extraction database (`CODEBOOK.md` §8).

## 1. Tool selection by design

| Design | Tool |
|---|---|
| Randomized studies | RoB 2 |
| Non-randomized intervention studies | ROBINS-I |
| Cross-sectional studies | JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies |
| Cohort studies | JBI Critical Appraisal Checklist for Cohort Studies |
| Qualitative studies | CASP Qualitative Checklist |
| Mixed methods | MMAT (Mixed Methods Appraisal Tool) |
| Legal empirical studies | Legal Institutional Evidence Appraisal Framework (below — supplementary, not a validated instrument) |

**AMSTAR 2** is *not* used here as a primary-study tool — it critically
appraises other systematic reviews, not primary studies (`SOURCES.md`). If
an included "study" is itself a systematic review or meta-analysis (e.g.
Apio, Thiam & Dinar 2025), appraise it with AMSTAR 2 instead of a
primary-study tool, and flag it in `evidence_map.csv` as
`study_design_class = systematic_review_secondary` so it is never treated as
an independent primary effect for pooling purposes.

## 2. Legal Institutional Evidence Appraisal Framework (supplementary)

This framework is a project-specific appraisal aid for legal-empirical
studies that do not fit a conventional epidemiological/social-science
design (e.g. doctrinal-empirical hybrids, institutional case studies,
jurimetric analyses used as evidence sources). **It is explicitly not
presented as a validated risk-of-bias instrument** — it has no published
psychometric validation, inter-rater reliability testing, or peer-reviewed
methodology paper behind it. Treat its output as a structured, transparent
judgment call, not a citable standardized score.

Domains (rate each narratively — strong / adequate / weak / not assessable
— with a one-line justification, rather than a numeric composite):

1. Legal source accuracy
2. Jurisdictional specificity
3. Exposure definition
4. Outcome definition
5. Sampling transparency
6. Selection process
7. Measurement transparency
8. Causal identification
9. Treatment of confounding
10. Institutional context
11. Replication potential
12. Coding transparency
13. Researcher reflexivity

## 3. Overall evidence limitations

At the end of the risk-of-bias phase, write a short (not per-study)
narrative in `04_quality/risk_of_bias/` summarizing cross-cutting
limitations of the evidence base as a whole (e.g. "most quantitative
studies are observational without a credible identification strategy for
the legal-recognition exposure"; "documentation of sampling frames is weak
across the Brazilian informal-settlement literature"). This narrative feeds
directly into the Discussion/Limitations sections of `PUBLICATION_PLAN.md`.

## 4. Status

No study has yet been appraised — the search has not been executed
(`SEARCH_PROTOCOL.md` §7). `04_quality/appraisal_forms/` and
`04_quality/risk_of_bias/` are currently empty except for `.gitkeep`.
