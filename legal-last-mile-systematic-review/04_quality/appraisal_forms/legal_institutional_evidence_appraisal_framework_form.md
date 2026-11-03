# Legal Institutional Evidence Appraisal Framework — Fillable Form

For studies that don't fit any of the six conventional
epidemiological/social-science designs in `RISK_OF_BIAS.md` §1
(doctrinal-empirical hybrids, institutional case studies, jurimetric
analyses used as evidence sources). **This is explicitly not a validated
risk-of-bias instrument** — it has no published psychometric validation,
inter-rater reliability testing, or peer-reviewed methodology paper
behind it (`RISK_OF_BIAS.md` §2). Treat its output as a structured,
transparent judgment call, not a citable standardized score, and say so
plainly in any manuscript reporting a study appraised with it.

Copy this template once per study appraised with this framework; save
the filled copy as `04_quality/appraisal_forms/<study_id>_LIEAF.md`
(e.g. `S014_LIEAF.md`).

Rate each domain **strong / adequate / weak / not assessable**, each with
a one-line justification — no numeric composite across domains
(`RISK_OF_BIAS.md` §2 is explicit that a composite score would overstate
this framework's rigor).

```
study_id:
appraiser:
date:

1. Legal source accuracy
   Rating:
   Justification:

2. Jurisdictional specificity
   Rating:
   Justification:

3. Exposure definition
   Rating:
   Justification:

4. Outcome definition
   Rating:
   Justification:

5. Sampling transparency
   Rating:
   Justification:

6. Selection process
   Rating:
   Justification:

7. Measurement transparency
   Rating:
   Justification:

8. Causal identification
   Rating:
   Justification:

9. Treatment of confounding
   Rating:
   Justification:

10. Institutional context
    Rating:
    Justification:

11. Replication potential
    Rating:
    Justification:

12. Coding transparency
    Rating:
    Justification:

13. Researcher reflexivity
    Rating:
    Justification:

Overall narrative summary (2-4 sentences, no numeric composite):
```

Once filled, record in `extraction_database.csv` for this study:
`risk_of_bias_tool = Legal Institutional Evidence Appraisal Framework`,
`risk_of_bias_rating` = the overall narrative summary's key judgment in a
few words (not a manufactured number), and map the 13 domains onto the
generic `selection_bias`/`measurement_bias`/`confounding`/`attrition`/
`reporting_bias` fields as best fits (`APPRAISAL_FORM.md` step 4) — some
domains here (e.g. legal source accuracy, jurisdictional specificity)
have no clean generic-field equivalent and belong instead in
`legal_measurement_quality` or `extraction_note`.
