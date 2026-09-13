# Inclusion and Exclusion Criteria

## Inclusion criteria

A study should generally satisfy **all** of the following:

1. Examines water or sanitation service access.
2. Examines a legal, administrative, institutional, regulatory or governance factor.
3. Contains empirical evidence or a systematic empirical synthesis.
4. Reports an outcome relevant to access, connection, service availability,
   reliability, quantity, affordability or exclusion.
5. Provides enough information to identify the population, exposure, and outcome.
6. For quantitative synthesis specifically, provides enough statistical
   information to extract or calculate an effect estimate (systematic-review
   inclusion does not require this — see criterion 6 is a synthesis-eligibility
   gate, not a review-eligibility gate).
7. Study design is identifiable.
8. Publication is sufficiently accessible for methodological assessment.
9. Language: English, Portuguese, and Dutch are eligible without translation.
10. Other languages may be included if translation is feasible and the study
    is potentially important — log the translation method and translator in
    the extraction record's `extraction_note`.

**Qualitative socio-legal studies are never excluded from the systematic
review merely because they cannot enter the meta-analysis.** They may
contribute to the mechanism synthesis. Do not silently drop a
mechanism-relevant qualitative study for lack of a quantitative effect size.

## Exclusion criteria

Exclude from the main empirical evidence set:

1. Pure doctrinal commentary without empirical access evidence.
2. Pure engineering studies without legal, administrative, or governance relevance.
3. Water-quality studies that do not examine access or governance.
4. Hydrology studies without relevant governance or access analysis.
5. Pure infrastructure engineering.
6. Purely normative human-rights commentary without empirical evidence.
7. Water-resource studies unrelated to household or community service access.
8. Industrial water-access studies unless the mechanism is directly relevant.
9. Duplicate publications (see `REPRODUCIBILITY.md` §"Duplicate publication policy").
10. Conference abstracts without sufficient information.
11. Studies where exposure or outcome cannot be identified.

## Standardized exclusion codes

Used in `02_screening/exclusion_log/exclusion_log.csv` and the
`exclusion_reason` field of `02_screening/title_abstract/screening_database.csv`.
Do not use "not relevant" as a vague, uncoded exclusion reason — every
exclusion at full-text stage must carry one of these codes plus a one-line
`exclusion_reason_detail`.

| Code | Meaning |
|---|---|
| E01 | Wrong topic |
| E02 | Wrong population |
| E03 | Wrong exposure |
| E04 | Wrong outcome |
| E05 | No empirical evidence |
| E06 | Engineering only |
| E07 | Wrong service |
| E08 | Duplicate |
| E09 | Insufficient information |
| E10 | Inaccessible full text |
| E11 | Wrong jurisdiction / context |
| E12 | Wrong study design |

## Scope discipline reminders

- Do not treat drinking-water connection, sewer connection, wastewater
  collection, sanitation service, utility-account eligibility, water
  quality, affordability, service continuity, disconnection, and
  infrastructure availability as interchangeable — record the precise
  service and outcome studied (`CODEBOOK.md` §5).
- Do not conflate unit-of-analysis levels (household, individual, property,
  applicant, settlement, municipality, utility, regulatory institution,
  judicial decision) — record the unit explicitly.
- The judicial decisions dataset elsewhere in this repository is not a
  candidate source of *included studies* for the household-level evidence
  base; see `PROJECT_SPEC.md` §9.
