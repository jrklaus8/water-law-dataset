# The 43 studies with no risk_of_bias_tool at all — classified and appraised — 2026-09-28

S571–S618 (43 studies, the tail end of the extraction range) had never had a
`risk_of_bias_tool` assigned at all — not a misclassification like the rest of today's
findings, simply never reached. Classified by `study_design` against `RISK_OF_BIAS.md` §1's
table, using the same evidentiary standard as every other classification today (explicit
named methods in the study's own recorded design, not a guess), then appraised immediately
under the assigned tool using each tool's own rule-based method already established today.

## Classification

- **CASP Qualitative (15):** S573, S575, S576, S580, S585, S586, S587, S592, S594, S595,
  S597, S608, S610, S612, S616 — all explicitly "qualitative," most with a named method
  (interviews, focus groups, ethnography, semi-structured interviews, participant
  observation).
- **MMAT (16):** S571, S572, S574, S578, S579, S581, S588, S591, S596, S599, S603, S605,
  S611, S613, S614, S615 — all explicitly "mixed-methods" or describing a genuine
  quantitative+qualitative combination (e.g. S571: "647 water-point WSSI quantitative
  assessments + 103 semi-structured qualitative [interviews]"; S615: "structured
  questionnaires combined with qualitative comp[onent]").
- **JBI Cross-Sectional (4):** S577, S598, S600, S617 — purely quantitative cross-sectional
  designs with no qualitative component ("quantitative... cross-sectional tariff/consumption
  microdata analysis," "Population-based cross-sectional study," "Cross-sectional
  questionnaire survey").
- **Legal Institutional Evidence Appraisal Framework (8):** S583, S584, S601, S602, S604,
  S607, S609, S618 — doctrinal/documentary/case-law analyses with no empirical
  qualitative-research method named (interviews, FGDs, ethnography) and no quantitative
  model. S618's own `study_design` field already read "Narrative review/documentary
  synthesis (Legal Institutional Evidence Appraisal Framework)" — the intended tool had been
  written into the design description but never actually copied into `risk_of_bias_tool`,
  evidently an oversight from whichever batch extracted it; corrected here.

## Appraisal

Applied immediately, using the exact same rule-based methods documented in today's four
main tool batches (`ROBINS-I_batch_2026-09-28.md`, `JBI_CrossSectional_batch_2026-09-28.md`,
`MMAT_batch_2026-09-28.md`, `CASP_Qualitative_batch_2026-09-28.md`) — see those files for
the full methodology rather than repeating it here. One addition for the 8 Legal Framework
studies: given the small number, each was appraised with a condensed version of the
project's own 13-domain framework (`RISK_OF_BIAS.md` §2) — jurisdictional specificity is
assessable from the recorded `country` field, but the other 11 domains (legal source
accuracy, exposure/outcome definition, sampling transparency, selection process,
measurement transparency, causal identification, confounding treatment, institutional
context, replication potential, coding transparency, researcher reflexivity) are marked "not
assessable" for all 8, honestly, given what this project's extraction actually captured for
doctrinal/documentary studies.

## Results

- 15 CASP studies: same "Can't tell"-heavy pattern as the main CASP batch, with items 1
  (aims) and 2 (qualitative approach) Yes for all 15, item 5 (data collection method) Yes
  for 12 of 15 (named methods), item 9 (findings) Yes for 12 of 15.
- 16 MMAT studies: screening Yes for all 16; mixed-methods criteria 5.1/5.3/5.4/5.5 "Can't
  tell" for all 16; 5.2 (integration) "Can't tell" for all 16 too — none had an explicit
  triangulation signal in their extraction notes.
- 4 JBI studies: S577 Low concern (7/8 Yes); S598 and S600 Some concern (3/8 Yes each); S617
  High concern (2/8 Yes, sparse extraction).
- 8 Legal Framework studies: condensed appraisal, jurisdictional specificity adequate for
  all 8, all other domains not assessable at this pass.

This closes the "studies with no tool at all" gap entirely — every one of the 1,162 extracted
studies now has a `risk_of_bias_tool` assigned.
