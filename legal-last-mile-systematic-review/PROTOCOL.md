# Review Protocol

Status: **draft, not yet registered.** Written in PRISMA-P (2015) style. See
`SOURCES.md` for the PRISMA-P citation and verification status.

## 1. Title (working)

*The Legal Last Mile: Legal and Administrative Barriers to Water and
Sanitation Access — A Systematic Review and Structured Quantitative Evidence
Synthesis.* ("...and Meta-Analysis" is added only if Phase 12 of
`PRISMA_WORKFLOW.md` concludes a restricted pooled estimate is defensible —
see `PROJECT_SPEC.md` §3.)

## 2. Research questions

### 2.1 Primary question (socio-legal systematic review)

> How do legal and administrative institutions shape the translation of
> physical availability of water and sanitation infrastructure into
> effective household access, and what evidence exists concerning the
> mechanisms through which eligibility screening, administrative burden,
> discretion, accommodation and enforcement produce or mitigate exclusion?

Selected over two alternatives that were explicitly considered and rejected
as primary:

- *Conventional framing* ("What empirical evidence exists concerning legal,
  administrative and institutional factors that influence household access
  to water and sanitation services...") — a strong general systematic-review
  question, but less analytically specific than the mechanism-based framing
  above.
- *Quantitative-synthesis framing* ("...what is the association between
  legal or administrative eligibility conditions and effective service
  access, and how does the magnitude vary across institutional and
  governance contexts?") — best if the quantitative literature turns out to
  be substantial, but risks excluding useful qualitative socio-legal
  evidence if used as the primary question.

The primary question was chosen because it fits the doctoral project, does
not assume the dissertation's hypothesis, admits both qualitative and
quantitative evidence, supports restricted quantitative synthesis where
warranted, and provides a clear mechanism framework (§5 of `PROJECT_SPEC.md`).

### 2.2 Secondary question (quantitative synthesis)

> Where sufficiently comparable evidence exists, what is the magnitude of
> the association between specific legal or administrative access
> conditions and household water or sanitation access outcomes?

### 2.3 Protocol language on quantitative synthesis

> A quantitative synthesis will be undertaken where a sufficiently
> homogeneous subset of studies reports compatible exposure, comparator,
> outcome and effect measures. Where quantitative pooling is inappropriate
> because of substantive or methodological heterogeneity, findings will be
> synthesized using structured quantitative evidence synthesis and
> transparent narrative or qualitative synthesis.

## 3. PECO (Population / Exposure / Comparator / Outcome)

- **Population:** households, individuals, applicants, or communities with
  potential physical access to water or sanitation infrastructure (unit of
  analysis explicit per study — see `PROJECT_SPEC.md` §2, `CODEBOOK.md` §3).
- **Exposure:** legal and administrative access conditions (eligibility
  screening, administrative burden, discretion/accommodation, enforcement,
  and related mechanisms — full list in `CODEBOOK.md` §5).
- **Comparator:** varies by study family — usual/standard procedure, absence
  of the legal/administrative condition, or a recognized/unrecognized
  contrast. The comparator must be recorded explicitly per study; "no
  comparator" studies are eligible for the systematic review's qualitative
  synthesis but not for effect-size extraction.
- **Outcome:** formal connection, effective access (quantity, reliability,
  continuity, quality), economic access (cost, affordability), or
  administrative outcomes (application success, refusal, delay, appeal) —
  hierarchy in `PROJECT_SPEC.md` §7. Each outcome is coded to its outcome
  family; outcome families are not pooled across each other.

## 4. Eligibility criteria

See `INCLUSION_EXCLUSION.md` for the full, operational inclusion and
exclusion criteria and the standardized exclusion-reason codes (E01–E12).

## 5. Information sources

Tier 1 / Tier 2 academic databases, sector-specific databases, legal/
institutional repositories, and grey literature — full list and search
strings in `SEARCH_PROTOCOL.md`.

## 6. Study records

- **Data management:** `02_screening/title_abstract/screening_database.csv`
  (schema in `PRISMA_WORKFLOW.md` §"Screening database").
- **Selection process:** two reviewers where feasible (title/abstract, then
  full text); conflicts resolved by discussion or a third reviewer; every
  decision recorded with a reviewer ID and, for exclusions, a standardized
  code.
- **Data collection process:** `03_extraction/extraction_form/` +
  `CODEBOOK.md`; piloted on ~10 studies before full extraction
  (`PRISMA_WORKFLOW.md` Phase 7).

## 7. Outcomes and prioritization

Primary outcome and secondary outcome hierarchy: `PROJECT_SPEC.md` §7.

## 8. Risk of bias in individual studies

Design-matched tools (RoB 2, ROBINS-I, JBI cross-sectional/cohort, CASP,
MMAT) plus a supplementary, explicitly non-validated Legal Institutional
Evidence Appraisal Framework for legal-empirical studies. Full detail:
`RISK_OF_BIAS.md`.

## 9. Data synthesis

Quantitative-feasibility decision tree, effect-size strategy, meta-analytic
model (contingent), heterogeneity, subgroup/moderator rules, sensitivity
analyses, and publication-bias assessment: `ANALYSIS_PLAN.md`. Where
meta-analysis is not justified for a given evidence family, synthesis follows
SWiM (2020) reporting guidance (`SOURCES.md`).

## 10. Meta-bias(es) and confidence in cumulative evidence

Publication bias assessed only where ≥ ~10 studies contribute to a synthesis
family (`ANALYSIS_PLAN.md` §"Publication bias"). Confidence in the body of
evidence is reported per synthesis family, not globally, given the expected
heterogeneity across mechanism and outcome families.

## 11. Registration

**Planned:** OSF Generalized Systematic Review registration. PROSPERO is not
assumed to be an appropriate registry because the primary question is not a
conventional health-intervention question; this will be re-checked against
current PROSPERO scope before a final registry decision (`PRISMA_WORKFLOW.md`
Phase 2). No registration has yet been submitted — this document is the
pre-registration draft.

## 12. Amendments

Any change to the research question, eligibility criteria, or planned
synthesis approach after registration must be logged in `CHANGELOG.md` with
a date, rationale, and the registration/version it amends. Do not silently
change the research question or inclusion criteria (`PROJECT_SPEC.md` §14).
