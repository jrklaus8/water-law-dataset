# Legal Institutional Evidence Appraisal Framework — Batch — 2026-09-28

The 425 studies confirmed (not just presumed) to genuinely belong under this project's own
13-domain framework, following the design audit earlier today
(`legal_framework_audit`/`CHANGELOG.md`'s "148 of 573 reclassified" entry). That audit fixed
*tool assignment*; none of the 425 had a `risk_of_bias_rating` until this pass.

## What makes this batch different from today's other condensed Legal Framework appraisals

Earlier today, the small Legal Framework groups found while auditing other batches (8 studies
in the "unassigned 43" batch, a handful in the reassignment batch) were given the thinnest
possible condensed appraisal — jurisdictional specificity only, everything else "not
assessable" — because nothing richer was on hand for those specific studies.

**This 425-study batch has real additional evidence already sitting in
`extraction_database.csv`, populated during the original extraction work months before
today's risk-of-bias session began**: `legal_measurement_quality`, `outcome_measurement_quality`,
and `mechanism_certainty` — three project-specific quality judgments that map directly onto
three of the framework's 13 domains (3. Exposure definition, 4. Outcome definition, 8. Causal
identification). Using them here is not new judgment invented for this appraisal; it is
citing already-extracted, non-fabricated data that happens to answer these specific
questions.

Population: `legal_measurement_quality` and `outcome_measurement_quality` are populated for
365 of 425 (60 blank — extracted before these fields existed in the codebook, or genuinely
not assessed at the time); `mechanism_certainty` is populated for all 425; `country` for 424
(S513 is the one exception).

## Method

Five of the 13 domains are populated from real, disclosed sources per study; the other 8
are marked "not assessable," honestly, rather than guessed:

- **2. Jurisdictional specificity:** "adequate" if `country` is recorded (424/425).
- **3. Exposure definition:** the study's own `legal_measurement_quality` value, verbatim
  (365/425; "not assessable" for the 60 without it).
- **4. Outcome definition:** the study's own `outcome_measurement_quality` value, verbatim
  (365/425; same caveat).
- **8. Causal identification:** the study's own `mechanism_certainty` value, verbatim
  (425/425) — reported as recorded, not reinterpreted; this field uses a mix of a 0-4 numeric
  scale and narrative text across different extraction batches (a real, disclosed
  data-cleanliness inconsistency inherited from the original extraction work, not smoothed
  over here).
- **10. Institutional context:** "adequate" if both `country` and `legal_system` are
  recorded.
- **1, 5, 6, 7, 9, 11, 12, 13** (legal source accuracy, sampling transparency, selection
  process, measurement transparency, treatment of confounding, replication potential, coding
  transparency, researcher reflexivity): **not assessable for all 425** — this project's
  extraction fields were never built to capture these specifically, and no study-by-study
  differentiation is possible without returning to each source document.

## Follow-up: 9 studies missed by an exact-string-match gap, then fixed

The script that generated this batch filtered on `risk_of_bias_tool.strip() ==
"Legal Institutional Evidence Appraisal Framework"` — an exact match. The 9 studies reverted
to this framework earlier today (S462, and the 8 no-comparator case studies S646, S659,
S687, S787, S832, S858, S927, S950) carry extra explanatory text appended to that same tool
name ("... (reverted 2026-09-28 -- ...)"), so the exact-match filter silently skipped them,
leaving all 9 with no `risk_of_bias_rating` at all. Caught by checking for any remaining
blank ratings after this batch ran, and fixed in a follow-up pass using the identical
5-domains-from-real-data method described above. Noted here rather than left implicit,
consistent with this project's practice of disclosing its own process errors alongside the
substantive findings.

## What this is and is not

This is a genuine, disclosed, source-cited risk-of-bias appraisal — 5 of 13 domains answered
from real prior extraction work, not invented for this batch. It is **not** a full
signalling-question-level read of each of the 425 studies' actual legal/methodological
reasoning, and the 8 "not assessable" domains are a real, substantial gap, not a formality.
A future researcher wanting the full 13-domain picture for any individual study should start
from that study's `04_quality/appraisal_forms/legal_institutional_evidence_appraisal_framework_form.md`
template and its original source document, not from this batch alone.
