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

**Rewritten 2026-09-28 — the text above was stale (it described a state
from before extraction had even started; extraction now holds 1,162
studies).** Current real state, of 1,162 extracted studies:

- **`risk_of_bias_tool` populated for 1,116 of 1,162** (46 still have no
  tool assigned at all — untouched by this pass, which focused on the 61
  studies in `effect_sizes.csv`).
- **`risk_of_bias_rating` populated (fully or partially) for 33** — 29 are
  explicit "partial pilot" judgments from 2026-09-16 (some domains
  assessed, others marked not-assessable; see
  `04_quality/appraisal_forms/S*_*.md`), and 4 are complete, non-partial
  ratings (S370, S372: AMSTAR 2; S468: CASP Qualitative; S469: MMAT).
- **2026-09-28 pass (this one):** did not add new ratings. It re-examined
  the 61 `effect_sizes.csv` studies' `risk_of_bias_tool` assignments
  against this document's own §1 design-to-tool table and corrected 7
  that did not match: S590, S593 (missing entirely — both cross-sectional
  comparisons, assigned JBI Cross Sectional), S606 (missing — panel/
  longitudinal observational, assigned ROBINS-I, matching this project's
  own established convention for that design), S879 (was tagged the Legal
  Framework despite being a literal randomized controlled trial —
  corrected to RoB 2), S1162 and S1163 (both were tagged RoB 2 despite
  neither being randomized — S1162 corrected to JBI Cross Sectional,
  S1163 to ROBINS-I since its exposure is a genuine program/intervention),
  and S749 (corrected to JBI Cross Sectional to match its two now-linked
  Family C analogues S526/S539 — see
  `06_outputs/supplementary/phase11_quantitative_feasibility_judgment.md`
  §5.1).
- **A broader, unresolved finding from this same pass:** roughly two
  dozen studies are tagged with the project's own **Legal Institutional
  Evidence Appraisal Framework** (§2 above) despite having entirely
  standard designs — RCTs, difference-in-differences, propensity-score
  matching, panel fixed-effects regression — that this document's §1
  table already assigns to RoB 2, ROBINS-I, or a JBI checklist. The Legal
  Framework is meant for studies that *do not fit* any of those six
  designs (doctrinal-empirical hybrids, institutional case studies,
  jurimetric analyses), not as a generic label for "any study with a
  legal/institutional exposure variable." This looks like the Legal
  Framework having been over-applied across several earlier extraction
  batches. **Not corrected in this pass** — it needs a study-by-study
  design re-classification at the same level of care given to the 7
  corrections above, which this pass did not have room for. A future
  pass should audit every `Legal Institutional Evidence Appraisal
  Framework`-tagged row against this document's §1 table before trusting
  its tool assignment.
- **Why no new `risk_of_bias_rating`s were produced today, beyond
  tool-classification fixes:** `04_quality/appraisal_forms/APPRAISAL_FORM.md`
  explicitly requires obtaining the actual current official checklist for
  whichever of the six validated tools applies, and explicitly prohibits
  reconstructing one from memory. This session attempted to fetch the
  official RoB 2 and ROBINS-I pages from `riskofbias.info` and
  `methods.cochrane.org`, and the JBI Critical Appraisal Checklist from
  `jbi.global` and a JBI wiki mirror — **all four domains returned
  `EGRESS_BLOCKED` from this environment's network proxy**, confirming
  (not just inheriting from an earlier note) that this access restriction
  is real and current, not merely historical. Producing "ratings" against
  these tools without the actual instrument would be exactly the
  fabrication this document and `SOURCES.md` §9–13 already warn against.
  Genuine progress on the remaining ~1,083 tool-assigned-but-unrated
  studies (plus the 46 with no tool, plus completing the 29 partial
  pilots) requires either the researcher supplying the official checklist
  documents directly (the same way full-text PDFs have been supplied), or
  a future session with unblocked access to one of those four domains.
- `04_quality/appraisal_forms/` still has `APPRAISAL_FORM.md` (the general
  process guide) and a fillable form for the project's own Legal
  Institutional Evidence Appraisal Framework; `04_quality/risk_of_bias/`
  still has only the template for the end-of-phase cross-cutting
  narrative in §3 above — that narrative has not been written yet, and
  should not be until real ratings exist for enough of the corpus to say
  something evidence-based about it.

**2026-09-28, later the same day — the network blocker above was
resolved: the researcher supplied the official RoB 2 (parallel-trial and
cluster-trial variants), ROBINS-I, MMAT, CASP Qualitative, JBI
Cross-Sectional, and AMSTAR 2 checklists/guidance directly, the same way
full-text PDFs have been supplied throughout this project.** Before using
any of them, two explicit gate-checks were run — an instrument-design
check for every RoB2-tagged study, and an independent eligibility check
for every AMSTAR2-tagged study, neither relying on the existing
`risk_of_bias_tool` field as proof of correctness:

- **RoB 2 design check.** All 5 RoB2-tagged studies (S057, S085, S294,
  S366, S879) turned out to be **cluster-randomized**, not individually
  randomized parallel trials — the parallel-trial instrument that had
  been implicitly assumed by the plain "RoB 2" tag was the wrong variant
  for every single one. 4 of 5 state this explicitly in their own
  `study_design` field; S879 doesn't say "cluster" outright, but its
  recorded unit of intervention ("96 disconnected compounds," "enforcement
  arms") strongly implies compound-level randomization — corrected
  provisionally to the cluster variant but flagged as inferred, not
  confirmed, pending direct verification against the source paper.
  `risk_of_bias_tool` for all 5 now reads "RoB 2 (cluster-randomized
  trials variant)" rather than a bare "RoB 2"/"ROB2", so a future pass
  cannot repeat this mistake by trusting the old tag.
- **AMSTAR 2 eligibility check.** Of the 34 AMSTAR2-tagged studies, an
  independent check against each study's title, `publication_type`, and
  `extraction_note` (not the existing tool tag) confirmed 18 are genuinely
  eligible (systematic reviews, a scoping review, or a meta-analysis), but
  **11 are misclassified** — self-described in their own recorded fields
  as narrative, conceptual, or documentary reviews, never claiming a
  systematic search/screening methodology: S079, S320, S322, S429, S430,
  S436, S440, S466, S479, S480, S482. AMSTAR 2 does not apply to any of
  these — it assumes a systematic review structure these studies never
  had, and scoring one against it would produce a misleading "critically
  low" verdict that conflates "not a systematic review" with "a badly
  conducted one." `risk_of_bias_tool` for all 11 was corrected to `NONE`
  with a study-specific reason; **RISK_OF_BIAS.md itself has no validated
  tool assigned for a non-systematic narrative/conceptual review used as
  an evidence source** — that is a real gap this check surfaced, not
  something resolved here. A further 5 (S321, S325, S326, S329, S418) are
  ambiguous on the evidence available and were left as AMSTAR2-tagged,
  flagged for individual re-verification rather than corrected on a guess
  either way — S325 in particular was extracted from abstract/metadata
  only, its full text never retrieved, so its eligibility can't be
  confirmed at all without going back for the PDF.
- See `CHANGELOG.md`'s dated entry for the full per-study list and the
  prior tool value each corrected study carried (also recoverable from
  git history on `03_extraction/extracted_data/extraction_database.csv`).
**2026-09-28, later still — RoB 2 (5 studies) and AMSTAR 2 (18 studies)
signaling-question-level ratings completed**, using the official
instruments and honest "No information" (NI) answers wherever the
extraction record doesn't capture the needed fact — see the per-study
files in `04_quality/appraisal_forms/` (`S057_RoB2.md` through
`S879_RoB2.md`, `S427_AMSTAR2.md` through `S697_AMSTAR2.md`) and
`CHANGELOG.md`'s dated entries for the full account. All 5 RoB2 studies
land on "Some concerns"; all 18 AMSTAR2 studies land on "Not ratable"
(insufficient critical-item evidence in most cases; two — S475, S521 —
have real Partial Yes evidence on several critical items but still can't
reach a defensible formal label, and both forms note explicitly that
even full resolution would cap them at Low confidence).

**2026-09-28, later still — audit of the 573 studies tagged with the
project's own Legal Institutional Evidence Appraisal Framework.** This
framework is meant only for studies that don't fit a standard design
(doctrinal-empirical hybrids, institutional case studies, jurimetric
analyses) — §4's earlier entry above flagged, without resolving, a
concern that it had been over-applied to studies with entirely standard
designs. A systematic keyword audit of every tagged study's
`study_design`/`model_type` fields (explicit quasi-experimental/panel/
before-after language → ROBINS-I; explicit "mixed-methods" → MMAT;
explicit "cross-sectional" → JBI) found:

- **425 of 573 genuinely belong here** — confirmed by direct inspection
  of a sample, not just the absence of a keyword match: these studies'
  own `study_design` text says things like "doctrinal legal-institutional
  policy analysis," "jurimetric/historical case study," "documentary/
  institutional analysis," "qualitative exploratory" — exactly this
  framework's intended scope.
- **148 were reclassified**: 43 to ROBINS-I (explicit DiD/PSM/panel/
  before-after quasi-experimental structure — e.g. S765, S795, S920,
  S930, S1020, S1102, all genuine quasi-experimental designs with a real
  comparator), 53 to MMAT (explicit "mixed-methods" in their own
  `study_design` field), 12 to JBI Cross-Sectional (explicit
  "cross-sectional" wording, high confidence), and **40 more to JBI
  Cross-Sectional on medium confidence** — a broader regression/survey
  keyword match without an explicit design-type label, spot-checked on a
  sample and found sound, but flagged for individual follow-up rather
  than treated as equally certain as the other three groups.
- None of the 148 have a `risk_of_bias_rating` yet — this audit only
  fixed the tool assignment; the ratings themselves are the next phase
  of work (see `CHANGELOG.md`).

**Signaling-question-level ratings for the remaining populations (the
now-72 ROBINS-I studies, the ~65 JBI Cross-Sectional studies, the ~53
newly-tagged plus ~96 originally-tagged MMAT studies, and the ~230 CASP
Qualitative studies) have not been produced yet.** These are the next,
much larger phases of this work — the checklists themselves are large
(RoB 2 cluster alone has 5 domains and ~25 signalling questions), and
most of `extraction_database.csv`'s fields were built to capture the
legal/institutional exposure-outcome data this review needs, not the
study-conduct or methodology-reporting details (allocation concealment,
duplicate screening, blinding, protocol registration, etc.) these
instruments ask about — expect heavy, honest use of "No information"
across most of the corpus, not a confirmed absence of bias.
