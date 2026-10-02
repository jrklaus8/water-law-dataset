# Quality Appraisal — Process Guide

Governs how `CODEBOOK.md` §8's quality fields
(`risk_of_bias_tool`, `risk_of_bias_rating`, `selection_bias`,
`measurement_bias`, `confounding`, `attrition`, `reporting_bias`,
`legal_measurement_quality`, `outcome_measurement_quality`) actually get
filled in during extraction (`03_extraction/extraction_form/
EXTRACTION_FORM.md` §8). Appraisal is not a separate phase file-wise —
its results live as columns on the same `extraction_database.csv` row as
everything else about that study — but it needs its own process
discipline, which is what this document is for.

## Why there's no reproduced checklist here

`RISK_OF_BIAS.md` §1 names six validated, design-matched instruments
(RoB 2, ROBINS-I, two JBI checklists, CASP, MMAT) plus one project-owned
framework. **This repository deliberately does not reproduce the six
validated tools' own checklist items, signaling questions, or domain
wording anywhere.** Two reasons: those are living instruments their
publishers revise (JBI in particular updates its checklists periodically
— see `SOURCES.md` §11's caveat), so a copy pasted into this repo would
silently go stale and could contradict the version actually used; and
this project has not independently re-verified any of their citations
against the publisher directly (network access to publisher domains is
blocked from this environment — see each entry in `SOURCES.md` §9–13).
**Obtain the current official version of whichever tool applies directly
from its own source before appraising a study with it** — do not
reconstruct a checklist from memory or from this document.

The one exception is the project's own **Legal Institutional Evidence
Appraisal Framework** (`RISK_OF_BIAS.md` §2) — since this project
authored it, its 13 domains are reproduced in full as a fillable form in
`legal_institutional_evidence_appraisal_framework_form.md` in this same
folder.

## Process, per study

1. **Classify the study's design first**, using `RISK_OF_BIAS.md` §1's
   table. Get this right before picking up any checklist — the wrong
   tool for the design produces a rating that means nothing.
2. **Obtain the current official checklist** for that tool from its
   source (`SOURCES.md` §9–13 gives the citation for each; none of them
   are reproduced here).
3. **Complete the checklist** against the full text of the study. Save
   the completed, filled-in checklist itself (whatever format the tool
   produces — a filled PDF, a scanned form, a filled-in copy of the
   official template) in this `04_quality/appraisal_forms/` folder, named
   `<study_id>_<tool>.<ext>` (e.g. `S014_ROBINS-I.pdf`) — this is the
   underlying evidence for the rating, and should be as retrievable as
   the extracted numbers themselves (`REPRODUCIBILITY.md` §3's provenance
   requirement applies to appraisal too, not just effect sizes).
4. **Record the result** in `extraction_database.csv` for that study's
   row(s):
   - `risk_of_bias_tool` — which tool was actually used (write the name
     plainly, e.g. `ROBINS-I`, `JBI Cross Sectional`, `Legal Institutional
     Evidence Appraisal Framework` — the rating's scale is meaningless
     without knowing which tool produced it, per `CODEBOOK.md` §8).
   - `risk_of_bias_rating` — the tool's own overall rating vocabulary
     (RoB 2: low / some concerns / high; ROBINS-I: low / moderate /
     serious / critical / no information; JBI/CASP/MMAT: per that tool's
     own scale — do not invent a numeric composite across tools, since
     `RISK_OF_BIAS.md` explicitly does not use one universal scale).
   - `selection_bias`, `measurement_bias`, `confounding`, `attrition`,
     `reporting_bias` — the project's own generic domain-level judgments
     (these exist across all tools in some form; map the tool's specific
     domains onto these five in your own words, don't leave them blank
     just because the tool you used doesn't use these exact five labels).
   - `legal_measurement_quality`, `outcome_measurement_quality` —
     project-specific judgments not covered by any of the six standard
     tools: how well did the study operationalize the *legal/
     administrative* exposure, and how well did it measure the water/
     sanitation *outcome*? (Neither RoB 2 nor ROBINS-I nor the JBI tools
     were built with a legal-institutional exposure in mind — this is
     this project's own addition to fill that gap.)
5. **If a study genuinely fits none of the six standard designs** (a
   doctrinal-empirical hybrid, an institutional case study, a jurimetric
   analysis used as an evidence source), use the project's own Legal
   Institutional Evidence Appraisal Framework instead — see
   `legal_institutional_evidence_appraisal_framework_form.md`.
6. **If an included "study" is itself a systematic review or
   meta-analysis** (e.g. Apio, Thiam & Dinar 2025, `SOURCES.md` §4),
   appraise it with AMSTAR 2 instead of any primary-study tool, and set
   `study_design_class = systematic_review_secondary` in
   `05_analysis/descriptive/evidence_map.csv` so it is never treated as
   an independent primary effect for pooling (`RISK_OF_BIAS.md` §1).

## At the end of the phase

Once every included study has been appraised, write the cross-cutting
narrative required by `RISK_OF_BIAS.md` §3 — see
`04_quality/risk_of_bias/EVIDENCE_LIMITATIONS_TEMPLATE.md` in this
repository for the shell to fill in.
