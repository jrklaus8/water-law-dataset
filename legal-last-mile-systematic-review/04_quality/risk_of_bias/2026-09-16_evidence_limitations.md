# Cross-Cutting Evidence Limitations — 2026-09-16 (preliminary, pre-appraisal)

## Status of this note

`RISK_OF_BIAS.md` §3 instructs that this narrative be written **once every
included study has been individually appraised**
(`04_quality/appraisal_forms/APPRAISAL_FORM.md`). That has not happened:
Phase 9 (risk of bias) has deliberately not been applied to any of the 350
extracted studies yet, because `RISK_OF_BIAS.md` prohibits reconstructing
any of the six validated instruments (RoB 2, ROBINS-I, the two JBI
checklists, CASP, MMAT) or AMSTAR 2 from memory, and the official current
version of each has not yet been fetched and applied (see
`PRISMA_WORKFLOW.md` Phase 9).

What follows is therefore **not** the finished cross-cutting narrative the
template calls for. It is a preliminary corpus-composition analysis, built
entirely from fields that already exist in `extraction_database.csv` and
`05_analysis/descriptive/evidence_map.csv` (study design, jurisdiction,
mechanism family, tool assignment, mechanism certainty) — none of which
require an actual bias *rating* to compute. It is written now because it is
useful for planning the Phase 9 appraisal batches (item below) and because
several of its findings (design mix, jurisdiction skew) will not change
once ratings are added, only the "Overall confidence" section will. That
section is therefore deliberately left as a placeholder. **This file should
be revisited and the confidence section completed once Phase 9 actually
runs** — do not cite this version's absence of a confidence judgment as
itself a confidence judgment.

## Coverage of designs

Of the 350 included studies (`study_design_class`, `evidence_map.csv`):

| Design class | n | % |
|---|---|---|
| qualitative | 140 | 40% |
| mixed_methods | 68 | 19% |
| observational | 43 | 12% |
| doctrinal | 37 | 11% |
| jurimetric | 33 | 9% |
| systematic_review_secondary | 17 | 5% |
| quasi_experimental | 9 | 3% |
| experimental | 3 | 1% |

The evidence base is heavily weighted toward qualitative and mixed-methods
work (59% combined) and doctrinal/jurimetric legal-empirical work (20%
combined). Only 12 of 350 studies (3%) use a quasi-experimental or
experimental design capable of supporting a causal claim about a
legal/administrative mechanism's effect on access. This is corroborated by
`mechanism_certainty` (`CODEBOOK.md` §9, coded per study on extraction, not
a rating that depends on Phase 9): only 26 of 350 studies (7%) reach level 3
("quasi-experimental evidence") or 4 ("experimental evidence"); 183 (52%)
sit at level 1 ("documented association") and 138 (39%) at level 2
("mechanism directly observed" but not causally identified). **The great
majority of this evidence base documents that legal/administrative
mechanisms and access outcomes co-occur or correlate, not that the former
causes the latter.** This is the single most important cross-cutting
limitation for any synthesis drawn from this review, independent of what
Phase 9's ratings eventually say about within-study bias.

## Coverage by jurisdiction / legal system

Country coverage (`extraction_database.csv` `country`, top entries of 350):
Brazil 51 (15%), India 29 (8%), South Africa 23 (7%), Kenya 19 (5%), United
States 17 (5%), Ghana 16 (5%), Mexico 11 (3%), with the remaining ~60
countries each contributing five or fewer studies. Brazil, India, and South
Africa alone account for 30% of the corpus. This roughly tracks the
review's own comparative design (Netherlands–Ontario–Brazil dissertation,
with the broader systematic review casting wider) but means any synthesis
finding should be checked for whether it is really general or is a
Brazil/India/South-Africa finding dressed as a general one.

Legal-system coverage (`legal_system`, normalized to absorb free-text
variants): common law (incl. variants) 140 (40%), civil law (incl.
variants) 138 (39%), mixed/hybrid/customary-overlay 43 (12%), blank 28
(8%), international law 1. Common law and civil law systems are close to
evenly represented, which is a genuine strength for the review's
comparative ambitions — but the "mixed/hybrid/customary-overlay" 12% is
itself analytically important (informal/customary tenure institutions are
central to several of this review's own included studies, e.g. S084/S085's
Mumbai slum-notification cases) and should not be collapsed into either
pure category in any cross-system comparison. The 8% blank `legal_system`
field is a real, unaddressed data gap in extraction (not a "no relevant
legal system" finding) and should be revisited before any jurisdiction-level
synthesis claim is made.

**Disclosed search-strategy limitation that likely shapes this
distribution:** SSRN and Westlaw/Lexis were never searched at all, and
CanLII, Rechtspraak.nl, and Brazilian court/regulatory portals were never
reached for this empirical-evidence pipeline (`SEARCH_PROTOCOL.md` §7,
`PRISMA_WORKFLOW.md` Phase 3–4). Jurisdiction coverage here reflects what
five academic/social-science databases plus researcher-supplied PDFs
surfaced, not a deliberate jurisdictional sampling frame — under-
representation of a legal system or country in this corpus is not evidence
that its literature is thin, only that this review's search did not fully
reach it.

## Measurement quality patterns

`legal_measurement_quality` and `outcome_measurement_quality` are recorded
per study in `extraction_database.csv` but, like `risk_of_bias_rating`,
have not been the subject of a dedicated cross-study review pass — that is
deferred to the same Phase 9 pass this file is otherwise anticipating. One
pattern is visible without that pass: **57 of 350 studies (16%) were
extracted from a published abstract or repository/publisher metadata page
only, with `full_text_location` and `extraction_note` disclosing that the
full PDF text was never retrieved** (per this project's standing
abstract-only-extraction policy). Every quantitative or qualitative claim
drawn from those 57 studies is necessarily thinner than for the other 293
— abstracts routinely omit exact sample sizes, full covariate lists, and
confidence intervals, which is why several `effect_sizes.csv` rows added
2026-09-16 (e.g. S057, S174, S142) note a specific numeric effect size could
not be located in the extracted text and was not approximated. This 16% is
not evenly distributed by design class; abstract-only extraction is more
common for older or non-open-access journal articles and less common for
recent open-access/preprint-style sources, which is itself worth flagging
as a possible source of recency/access bias in what could be extracted in
full versus only from an abstract.

Also worth flagging here rather than treated as a Phase-9-only issue:
`legal_system` free text contains many one-off compound descriptions (e.g.
"mixed (Palestinian Authority administration under Israeli military
occupation; Israeli law in settlement)") that are analytically rich but not
machine-comparable across studies — any future cross-jurisdiction tabulation
will need a manual re-coding pass, not a `groupby` on this field as-is.

## Mechanism-family coverage

`mechanism_family` (`evidence_map.csv`, mechanically derived from the four
`CODEBOOK.md` §4 booleans): MULTIPLE 233 (67%), DISCRETION_ACCOMMODATION 70
(20%), ENFORCEMENT 20 (6%), BURDEN 15 (4%), ELIGIBILITY 9 (3%), blank 3.
Two-thirds of studies document more than one mechanism operating together,
which is a realistic feature of the underlying phenomenon (legal/
administrative barriers rarely operate in isolation) but complicates any
attempt to isolate a single mechanism's effect for synthesis — consistent
with `PROJECT_SPEC.md` §8's own caution that Family C ("administrative/
legal barriers and access inequality") may be "too heterogeneous" to pool.
Among single-mechanism studies, DISCRETION_ACCOMMODATION is far better
represented (70) than ELIGIBILITY (9) or BURDEN (15) considered alone. This
mirrors the `effect_sizes.csv` population done 2026-09-16: of the 11 studies
judged to have a genuine, poolable exposure-comparator effect, only S057
tests a clean eligibility-only mechanism and none tests burden alone —
**Family A (legal recognition/eligibility) and Family B (bureaucratic
assistance) each currently rest on a small handful of studies (4 and 2
respectively), and no candidate family yet has enough independent,
comparably-operationalized studies to support pooling** (`ANALYSIS_PLAN.md`
§2). Whether thin ELIGIBILITY/BURDEN-alone coverage reflects a genuine gap
in the literature or an artifact of this review's disclosed search gaps
(SSRN, Westlaw/Lexis never searched) cannot be determined from this corpus
alone.

## Studies appraised with the non-validated framework

70 of 350 studies (20%) carry `risk_of_bias_tool` = "Legal Institutional
Evidence Appraisal Framework" — this project's own instrument for
documentary/doctrinal/jurimetric legal-empirical studies, used precisely
because no validated tool (RoB 2, ROBINS-I, JBI, CASP, MMAT) fits a study
whose primary evidence is legal text, case law, or institutional design
rather than a conventional empirical study population. `RISK_OF_BIAS.md`
§2 is explicit that this framework's 13-domain output is a **narrative
judgment call, not a citable, validated score**, and that caveat must
travel with any synthesis finding drawn from this 20% of the corpus. This
is distinct from — and should not be conflated with — the 37 `doctrinal`
and 33 `jurimetric` `study_design_class` studies in the design table above;
the tool-assignment count (70) and the design-class counts (37+33=70,
coincidentally identical here) track the same underlying group of studies
by construction, since `build_evidence_map.py` derives `study_design_class`
from `risk_of_bias_tool` for exactly this framework.

A related tooling bug was found and fixed while compiling this note: of
the 17 studies flagged `study_design_class = systematic_review_secondary`
(S015, S019, S027, S052, S079, S116, S319–S329 — for which `RISK_OF_BIAS.md`
specifies AMSTAR 2, not a primary-study tool, is the correct instrument),
only 6 (S015, S019, S027, S052, S079, S116) carried an AMSTAR-2-labeled
`risk_of_bias_tool` value as of 2026-09-15. The other 11 (S319–S329, all
added in the 2026-09-16 E12-policy-amendment batch that reinstated them as
legitimate secondary-review includes — see `CHANGELOG.md`) had been left
with `risk_of_bias_tool = CASP`, an apparent carry-over default from that
batch's extraction script rather than a deliberate tool choice. Corrected
in `extraction_database.csv` 2026-09-16 (same date as this note) to the
same AMSTAR-2 label used for the other 6, with each row's
`extraction_note` recording the correction; `study_design_class` in
`evidence_map.csv` was already correctly `systematic_review_secondary` for
all 17 and did not need to change.

## Overall confidence in the body of evidence

**Deliberately not filled in.** Per `RISK_OF_BIAS.md` §3 this must be
reported per candidate synthesis family (`PROJECT_SPEC.md` §8's Families
A/B/C), not globally, and depends on the actual per-study
`risk_of_bias_rating` values that Phase 9 has not yet produced for any
study. What can be said now, from corpus composition alone, is only that
none of Family A, B, or C currently has more than a handful of studies with
a genuine poolable effect (`effect_sizes.csv`, populated 2026-09-16: 4
studies in Family A, 2 in Family B, 1 in Family C), so even a favorable
set of Phase 9 ratings would not, on its own, make pooling within any
family defensible yet — the sample-size problem and the confidence-rating
problem are separate limitations, and this note should not be read as
resolving or standing in for either.
