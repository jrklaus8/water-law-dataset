# Cross-Cutting Evidence Limitations — 2026-09-16 (preliminary, pre-appraisal; recomputed against 366 studies)

## Status of this note

**Recomputed 2026-09-16 (later the same day) against the full 366-study
corpus.** An earlier version of this file was computed against the
350-study corpus as it stood before that day's Zotero-batch screening
round added 16 further includes (S352–S367, see `CHANGELOG.md`). The
patterns described below did not shift materially with those 16 studies,
but every count and percentage in this version is a fresh computation
against `extraction_database.csv`/`evidence_map.csv` as of 366 studies —
none carried over unchanged from the prior version.

**2026-09-16 (still later the same day) addendum — now 6 studies stale,
not yet re-recomputed.** A sixteenth full-text screening batch (13
researcher-supplied PDFs) added 6 further includes (S368–S373, see
`CHANGELOG.md`), growing the corpus from 366 to 372 studies (+1.6%). Every
count and percentage in the body of this file below still reflects the
366-study corpus and has **not** been recomputed for this small addendum —
flagged here rather than silently left stale, per this project's usual
practice, but a full recomputation was judged not worth the effort for a
1.6% corpus change and is still owed as a follow-up before this note is
treated as current. For reference, what the 6 new studies add to the
picture: 1 quantitative cross-sectional survey (S368, `JBI`), 1 qualitative
PAR/Photovoice study (S369, `CASP`) that is a companion paper to the
already-included S357, 2 secondary systematic/realist reviews (S370, S372,
`AMSTAR2`) — both of which, unusually, received a **positively-determined**
Critically Low rating rather than joining the "Not ratable" 17-study group,
because their own full text explicitly confirms no critical appraisal of
included studies was performed — 1 mixed-methods SWOT-AHP case study
(S371, `MMAT`), and 1 quasi-experimental matched-cohort study (S373,
`ROBINS-I`) that is a strong candidate for a future `effect_sizes.csv`
entry. None of these 6 changes the corpus's overall design-mix skew toward
observational/qualitative evidence described below.

**2026-09-16 (still later the same day) second addendum — now 19 studies
stale (366→385, +5.2%), not yet re-recomputed.** A seventeenth full-text
screening batch (15 more researcher-supplied PDFs) added 13 further
includes (S374–S386, see `CHANGELOG.md`). Every count and percentage in the
body of this file below still reflects the 366-study corpus; still not
recomputed, for the same reason given in the addendum above, though the
cumulative staleness (5.2% of the corpus) is now large enough that the
recomputation should not be deferred indefinitely. For reference, what
these 13 add: 6 quantitative cross-sectional/panel studies (S378, S381,
S382, S383, S384, S385 — `JBI`/`MMAT`/`ROBINS-I`), 6 qualitative case
studies (S374, S375, S377, S379, S380, S386 — `CASP`/`MMAT`), and 1
regulatory-audit-indicator study (S376) appraised with the project's own
Legal Institutional Evidence Appraisal Framework and classified by hand as
`jurimetric` — the first `jurimetric`-classified study in the corpus to
date. None of these 13 changes the corpus's overall design-mix skew toward
observational/qualitative evidence described below.

`RISK_OF_BIAS.md` §3 instructs that this narrative be written **once every
included study has been individually appraised**
(`04_quality/appraisal_forms/APPRAISAL_FORM.md`). That has not happened:
Phase 9 (risk of bias) has been applied to only a first 12-study partial
pilot batch (RoB 2 and ROBINS-I, see `04_quality/appraisal_forms/` and
`CHANGELOG.md` 2026-09-16) — the great majority of the 366 extracted
studies remain unappraised, because `RISK_OF_BIAS.md` prohibits
reconstructing any of the six validated instruments (RoB 2, ROBINS-I, the
two JBI checklists, CASP, MMAT) or AMSTAR 2 from memory, and the official
current version of most has not yet been fetched and applied in full (see
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

Of the 366 included studies (`study_design_class`, `evidence_map.csv`):

| Design class | n | % |
|---|---|---|
| qualitative | 144 | 39% |
| mixed_methods | 73 | 20% |
| observational | 46 | 13% |
| doctrinal | 40 | 11% |
| jurimetric | 33 | 9% |
| systematic_review_secondary | 17 | 5% |
| quasi_experimental | 9 | 2% |
| experimental | 4 | 1% |

The evidence base is heavily weighted toward qualitative and mixed-methods
work (59% combined) and doctrinal/jurimetric legal-empirical work (20%
combined). Only 13 of 366 studies (4%) use a quasi-experimental or
experimental design capable of supporting a causal claim about a
legal/administrative mechanism's effect on access. This is corroborated by
`mechanism_certainty` (`CODEBOOK.md` §9, coded per study on extraction, not
a rating that depends on Phase 9): only 27 of 366 studies (7%) reach level 3
("quasi-experimental evidence") or 4 ("experimental evidence"); 196 (54%)
sit at level 1 ("documented association") and 140 (38%) at level 2
("mechanism directly observed" but not causally identified). **The great
majority of this evidence base documents that legal/administrative
mechanisms and access outcomes co-occur or correlate, not that the former
causes the latter.** This is the single most important cross-cutting
limitation for any synthesis drawn from this review, independent of what
Phase 9's ratings eventually say about within-study bias.

## Coverage by jurisdiction / legal system

Country coverage (`extraction_database.csv` `country`, top entries of 366):
Brazil 51 (14%), India 30 (8%), South Africa 25 (7%), Kenya 20 (5%), United
States 20 (5%), Ghana 16 (4%), Mexico 11 (3%), with the remaining ~65
countries each contributing seven or fewer studies (7 rows blank). Brazil,
India, and South Africa alone account for 29% of the corpus. This roughly
tracks the review's own comparative design (Netherlands–Ontario–Brazil
dissertation, with the broader systematic review casting wider) but means
any synthesis finding should be checked for whether it is really general
or is a Brazil/India/South-Africa finding dressed as a general one.

Legal-system coverage (`legal_system`, normalized to absorb free-text
variants): common law (incl. variants) 149 (41%), civil law (incl.
variants) 142 (39%), mixed/hybrid/customary-overlay 46 (13%), blank 28
(8%), international law 1. Common law and civil law systems are close to
evenly represented, which is a genuine strength for the review's
comparative ambitions — but the "mixed/hybrid/customary-overlay" 13% is
itself analytically important (informal/customary tenure institutions are
central to several of this review's own included studies, e.g. S084/S085's
Mumbai slum-notification cases, and S361/S365's community/customary water-
governance case studies from this same day's batch) and should not be
collapsed into either pure category in any cross-system comparison. The 8%
blank `legal_system` field is a real, unaddressed data gap in extraction
(not a "no relevant legal system" finding) and should be revisited before
any jurisdiction-level synthesis claim is made.

**Disclosed search-strategy limitation that likely shapes this
distribution:** SSRN and Westlaw/Lexis were never searched at all, and
CanLII, Rechtspraak.nl, and Brazilian court/regulatory portals were never
reached for this empirical-evidence pipeline (`SEARCH_PROTOCOL.md` §7,
`PRISMA_WORKFLOW.md` Phase 3–4). Jurisdiction coverage here reflects what
five academic/social-science databases plus researcher-supplied PDFs
(chat upload and Drive/Zotero exports) surfaced, not a deliberate
jurisdictional sampling frame — under-representation of a legal system or
country in this corpus is not evidence that its literature is thin, only
that this review's search did not fully reach it.

## Measurement quality patterns

`legal_measurement_quality` and `outcome_measurement_quality` are recorded
per study in `extraction_database.csv` but, like `risk_of_bias_rating`,
have not been the subject of a dedicated cross-study review pass — that is
deferred to the same Phase 9 pass this file is otherwise anticipating. One
pattern is visible without that pass: **69 of 366 studies (19%) were
extracted from a published abstract, introduction, or repository/publisher
metadata page only, with `extraction_note` disclosing that the full PDF
body text (results tables, methods detail) was never retrieved or
converted** (per this project's standing abstract-only-extraction policy).
Every quantitative or qualitative claim drawn from those 69 studies is
necessarily thinner than for the other 297 — abstracts routinely omit exact
sample sizes, full covariate lists, and confidence intervals, which is why
several `effect_sizes.csv` rows (e.g. S057, S174, S142, S142's companion
S353, S356) note a specific numeric effect size could not be located in the
extracted text and was not approximated. This 19% is not evenly distributed
by design class; abstract-only extraction is more common for older or
non-open-access journal articles and less common for recent open-access/
preprint-style sources, which is itself worth flagging as a possible
source of recency/access bias in what could be extracted in full versus
only from an abstract.

Also worth flagging here rather than treated as a Phase-9-only issue:
`legal_system` free text contains many one-off compound descriptions (e.g.
"mixed (Palestinian Authority administration under Israeli military
occupation; Israeli law in settlement)") that are analytically rich but not
machine-comparable across studies — any future cross-jurisdiction tabulation
will need a manual re-coding pass, not a `groupby` on this field as-is.

A second, unrelated provenance gap surfaced during a 2026-09-16 duplicate-
detection audit (see `CHANGELOG.md`): **8 early studies (S076–S083) carry
no `record_id` reference anywhere in their `extraction_note`**, confirmed
by direct substring search rather than a regex-matching failure. This
means those 8 rows cannot currently be traced back to their original
`full_text_screening_database.csv` entry from the extraction record alone.
It does not indicate a duplicate or any data-correctness problem — the
duplicate audit itself came back clean across all 366 studies by four
independent methods (exact DOI, exact title, fuzzy title, record_id) — but
it is a real, disclosed traceability gap for those 8 studies specifically.

## Mechanism-family coverage

`mechanism_family` (`evidence_map.csv`, mechanically derived from the four
`CODEBOOK.md` §4 booleans): MULTIPLE 244 (67%), DISCRETION_ACCOMMODATION 75
(20%), ENFORCEMENT 20 (5%), BURDEN 15 (4%), ELIGIBILITY 9 (2%), blank 3.
Two-thirds of studies document more than one mechanism operating together,
which is a realistic feature of the underlying phenomenon (legal/
administrative barriers rarely operate in isolation) but complicates any
attempt to isolate a single mechanism's effect for synthesis — consistent
with `PROJECT_SPEC.md` §8's own caution that Family C ("administrative/
legal barriers and access inequality") may be "too heterogeneous" to pool.
Among single-mechanism studies, DISCRETION_ACCOMMODATION is far better
represented (75) than ELIGIBILITY (9) or BURDEN (15) considered alone. This
mirrors the `effect_sizes.csv` population (11 studies populated
2026-09-16, extended the same day to 13 with S353 and S358): of those 13
studies judged to have a genuine, poolable exposure-comparator effect,
only S057 tests a clean eligibility-only mechanism and none tests burden
alone — **Family A (legal recognition/eligibility) and Family B
(bureaucratic assistance) each currently rest on a small handful of
studies (6 and 2 respectively), and no candidate family yet has enough
independent, comparably-operationalized studies to support pooling**
(`ANALYSIS_PLAN.md` §2). Whether thin ELIGIBILITY/BURDEN-alone coverage
reflects a genuine gap in the literature or an artifact of this review's
disclosed search gaps (SSRN, Westlaw/Lexis never searched) cannot be
determined from this corpus alone.

## Studies appraised with the non-validated framework

73 of 366 studies (20%) carry `risk_of_bias_tool` = "Legal Institutional
Evidence Appraisal Framework" — this project's own instrument for
documentary/doctrinal/jurimetric legal-empirical studies, used precisely
because no validated tool (RoB 2, ROBINS-I, JBI, CASP, MMAT) fits a study
whose primary evidence is legal text, case law, institutional design, or
(as of this day's batch) cross-country regulatory-policy synthesis without
a documented systematic search methodology (S356, S364), rather than a
conventional empirical study population. `RISK_OF_BIAS.md` §2 is explicit
that this framework's 13-domain output is a **narrative judgment call, not
a citable, validated score**, and that caveat must travel with any
synthesis finding drawn from this 20% of the corpus. This is distinct
from — and should not be conflated with — the 40 `doctrinal` and 33
`jurimetric` `study_design_class` studies in the design table above; the
tool-assignment count (73) and the design-class counts (40+33=73) track
the same underlying group of studies by construction, since
`build_evidence_map.py` derives `study_design_class` from
`risk_of_bias_tool` for exactly this framework (with S356 and S364
manually classified `doctrinal` this same day, since the mechanical
derivation cannot distinguish doctrinal from jurimetric on its own).

The AMSTAR-2/CASP tool-assignment bug found and fixed on 2026-09-15/16 (11
of the 17 `systematic_review_secondary` studies, S319–S329, had carried an
erroneous `risk_of_bias_tool = CASP` default) remains fixed and consistent
in the 366-study corpus: all 17 systematic-review-secondary studies
(S015, S019, S027, S052, S079, S116, S319–S329) now carry an AMSTAR-2-
labeled tool, matching `study_design_class = systematic_review_secondary`
one-for-one. No new instance of this bug was introduced by the 2026-09-16
Zotero-batch extraction (S352–S367 contain no further systematic reviews).

## Overall confidence in the body of evidence

**Deliberately not filled in.** Per `RISK_OF_BIAS.md` §3 this must be
reported per candidate synthesis family (`PROJECT_SPEC.md` §8's Families
A/B/C), not globally, and depends on the actual per-study
`risk_of_bias_rating` values that Phase 9 has, for all but a first
12-study partial pilot batch, not yet produced. What can be said now, from
corpus composition alone, is only that none of Family A, B, or C currently
has more than a handful of studies with a genuine poolable effect
(`effect_sizes.csv`, 13 rows as of 2026-09-16: 6 studies in Family A, 2 in
Family B, 1 in Family C, 4 unassigned to any existing family), so even a
favorable set of Phase 9 ratings would not, on its own, make pooling
within any family defensible yet — the sample-size problem and the
confidence-rating problem are separate limitations, and this note should
not be read as resolving or standing in for either.
