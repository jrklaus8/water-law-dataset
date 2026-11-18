# Reassignment batch: 26 mistagged-as-JBI + 14 mistagged-as-MMAT studies — 2026-09-28

Closes tasks #13 and #14, the two reassignment queues opened while preparing today's JBI
Cross-Sectional and MMAT batches (`JBI_CrossSectional_batch_2026-09-28.md`,
`MMAT_batch_2026-09-28.md`). Each of the 40 studies was reclassified using the same
evidentiary standard as every other classification today (the study's own recorded
`study_design`, not a guess) and appraised immediately using the already-established
rule-based method for whichever tool it landed on.

## The 26 mistagged-as-JBI (qualitative, not cross-sectional)

- **19 → CASP Qualitative**: S403, S410, S412, S414, S415, S416, S417, S419, S420, S424,
  S431, S433, S441, S446, S447, S451, S456, S459, S460. All confirmed genuinely qualitative
  (case study, comparative case study, multi-site interview study, ethnographic case study).
- **6 → Legal Institutional Evidence Appraisal Framework**: S425, S444, S455, S457, S458,
  S465. These are documentary/policy-document/archival analyses rather than empirical
  qualitative research with a named data-collection method (interviews, FGDs, ethnography)
  — closer to this framework's intended scope (RISK_OF_BIAS.md §2) than to CASP, which
  appraises primary qualitative research.
- **1 → MMAT**: S461 ("qualitative case study with embedded quantitative estimation") —
  the only one of the 26 with a genuine quantitative component alongside its qualitative
  base.

## The 14 mistagged-as-MMAT (not genuinely mixed-methods)

- **11 → JBI Cross-Sectional**: S150, S422, S423, S426, S428, S432, S452, S454, S467, S619,
  S1153 — all purely quantitative cross-sectional/observational designs with no
  qualitative component.
- **1 → Legal Institutional Evidence Appraisal Framework**: S409 ("descriptive program/
  data-collection case study") — closer to an institutional case-study description than to
  either a qualitative-research-methods study or a quantitative model.
- **1 → CASP Qualitative**: S421 ("qualitative comparative case study... with documentary/
  archival analysis") — explicitly led with "qualitative comparative case study" as its
  primary design.
- **1 → returned to MMAT**: S494. On reconsideration, this was a false flag from today's
  MMAT batch: its own quantitative-signal detection regex looked for
  survey/regression/cross-sectional/statistical keywords and missed "standardized indicator
  scoring" as a genuine quantitative signal. Combined with its "stakeholder interviews"
  qualitative component, S494 ("descriptive diagnostic case-study assessment
  [standardized indicator scoring] plus stakeholder interviews") is a genuine mixed-methods
  study after all — corrected back rather than left in the reassignment queue on a
  technicality in the earlier regex.

## Appraisal

All 40 appraised immediately using the exact rule-based methods already documented in
`ROBINS-I_batch_2026-09-28.md`, `JBI_CrossSectional_batch_2026-09-28.md`,
`MMAT_batch_2026-09-28.md`, and `CASP_Qualitative_batch_2026-09-28.md` — see those files for
the full methodology. Results follow the same patterns already established in each tool's
main batch (heavy, honest "Can't tell"/"Unclear" for CASP/MMAT items requiring methodology
detail this project's extraction doesn't capture; a mix of concern levels for the JBI
studies depending on whether `covariates` and a named statistical method were captured at
extraction time).

This closes both reassignment queues. **This does not mean every study in the corpus now has
a `risk_of_bias_rating`** — the 425 studies confirmed as genuinely belonging under the Legal
Institutional Evidence Appraisal Framework (`legal_framework_audit`, earlier today) were only
classified, not individually rated, and the original 29 partial-pilot ratings from
2026-09-16 remain incomplete (tracked separately as task #10). What today's full run of
batches does mean: every study now has a correctly classified `risk_of_bias_tool` (no study
sits with the wrong instrument, or none at all), and every study that was actually appraised
today has an honest rating — a real judgement, an explicit "Not ratable"/"Can't tell"-heavy
verdict, or a `NONE` flag naming a real tooling gap — never a fabricated one.
