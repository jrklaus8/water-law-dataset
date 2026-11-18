# MMAT (Mixed Methods Appraisal Tool, 2018) — Batch — 2026-09-28

202 studies were tagged MMAT when this batch began. None had a `risk_of_bias_rating` except
one partial pilot.

## 14 studies found not genuinely mixed-methods, not appraised here

Checked every tagged study's `study_design` for either (a) an explicit "mixed method(s)"
self-label, or (b) both a qualitative signal (interviews, FGDs, ethnography, documentary/
archival analysis) and a quantitative signal (survey, regression, cross-sectional,
statistical analysis) present together. 14 have neither: S150, S409, S421, S422, S423, S426,
S428, S432, S452, S454, S467, S494, S619, S1153. Most of these are purely quantitative
("cross-sectional observational," "quantitative survey-based logistic regression") with no
qualitative component at all; S421 is the reverse (purely qualitative — "documentary/archival
analysis," no quantitative element). MMAT's own user guide is explicit that a study must
combine "at least one QUAL method and one QUAN method" to be appraised as mixed methods at
all — applying it to a single-method study would misuse the tool. **Not appraised here**;
flagged as a new open item (task #14) for individual reassignment to JBI Cross-Sectional
(the quantitative-only ones) or CASP Qualitative/the Legal Framework (S421).

That leaves **188 studies** genuinely appraised below.

## Source of tool structure

Screening questions (S1, S2) and the 5-criterion Mixed Methods category (5.1-5.5) verified
directly against the official MMAT 2018 user guide the researcher supplied — not
reconstructed from memory. Response options: Yes / No / Can't tell. **The MMAT's own guide
explicitly discourages calculating an overall score** ("It is discouraged to calculate an
overall score from the ratings of each criterion. Instead, it is advised to provide a more
detailed presentation of the ratings of each criterion") — so unlike every other batch today,
**no single Low/Moderate/High-style summary judgement is produced for any MMAT study**. This
is the tool's own recommended practice, not a simplification chosen for this project.

Full rigor would also require rating the qualitative sub-criteria (1.1-1.5) and whichever
quantitative sub-criteria apply (2.1-2.5 for RCTs, 3.1-3.5 for non-randomized, or 4.1-4.5 for
descriptive) for criterion 5.5 ("do the different components adhere to the quality criteria of
each tradition"). **This batch does not do that expansion** — 5.5 is answered only at the
mixed-methods level, not decomposed into 10 further sub-ratings per study across 188 studies.
Disclosed as a real scope limitation, not hidden.

## Methodology (disclosed, rule-based, same approach as prior batches)

- **S1 (clear research questions) / S2 (data address the research questions):** Yes if
  `population` is populated with a real description (185 of 188); Can't tell otherwise (3 of
  188 — S086, S134, S168, which had thinner `population` fields despite otherwise qualifying
  as mixed-methods on `study_design`).
- **5.1 (adequate rationale for the MM design):** Can't tell for all 188 — this project's
  extraction fields were never built to capture a study's own stated justification for
  choosing a mixed-methods design.
- **5.2 (components effectively integrated):** Yes only where `extraction_note`/
  `exact_location` contains an explicit integration signal (triangulated, informed by,
  combined with, cross-validated) — **3 of 188**: S086 (policy document analysis + household
  survey + 30 KIIs + focus groups), S134 (documentary case study with "multiple triangulated
  sources"), S168. Can't tell for the other 185 — genuinely unknown, not assumed absent.
- **5.3 (integration outputs/meta-inference adequately interpreted):** Can't tell for all 188.
- **5.4 (divergences between qual/quant results addressed):** Can't tell for all 188 — this is
  deliberately not defaulted to "Yes" (MMAT's own guide says "Rate this criterion 'Yes' if
  there is no divergence" — but absence of a *reported* divergence in a one-paragraph
  extraction note is not evidence that no divergence occurred).
- **5.5 (components adhere to each tradition's own quality criteria):** Can't tell for all
  188, per the scope limitation above.

## Results

**185 of 188: S1 = Yes, S2 = Yes.** (S086, S134, S168: Can't tell on both.)

**5.1, 5.3, 5.4, 5.5: Can't tell for all 188 studies**, honestly, given what this project's
extraction actually captured about each study's mixed-methods integration practice.

**5.2: Yes for 3 studies (S086, S134, S168); Can't tell for the remaining 185.**

This is, deliberately, a much flatter result than the other batches today — MMAT's
mixed-methods criteria ask about integration practices (rationale, triangulation, handling
divergence, tradition-specific quality) that are simply not things this project's
legal/institutional exposure-outcome extraction fields were designed to record. **This is the
single most honest finding of today's whole risk-of-bias effort**: for 185 of 188 mixed-methods
studies in this corpus, this project currently has no basis to say anything at all about
mixed-methods-specific quality beyond confirming the research question and data are
identifiable. Closing this gap requires returning to each study's actual Methods section, not
a further pass over what's already in `extraction_database.csv`.
