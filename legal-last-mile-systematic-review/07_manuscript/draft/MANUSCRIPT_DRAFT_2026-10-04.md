# The Legal Last Mile: Legal and Administrative Conditions and Access to Water and Sanitation — An AI-Assisted Systematic Review and Structured Evidence Synthesis

> **DRAFT (generated 2026-10-04) — NOT REVIEWED BY A HUMAN AUTHOR, NOT FOR SUBMISSION.** Every number is computed from the repository's databases by `code/analysis/build_manuscript_draft.py` and checked by `verify_repository.py`. Items in [square brackets] need the author. No literature reference has been invented: each [ref] marks where the author must cite. The review was conducted by an AI under the researcher's direction, largely without independent human verification (see Methods 2.9 and Limitations); the protocol was **not registered before the work was done**. Section 4 (Discussion) contains interpretation, labelled as such.

## Abstract (structured; draft)

**Background.** Physical water and sanitation infrastructure does not guarantee that households can obtain a connection or use it effectively; legal and administrative conditions (eligibility screening, documentation and tenure requirements, fees, discretion, enforcement) may stand between infrastructure and access. [Author: one sentence of context with refs.]

**Objective.** To map and synthesise the empirical evidence on how legal and administrative institutions shape the translation of physical availability of water and sanitation infrastructure into effective household access, and to synthesise quantitative evidence where it is comparable.

**Methods.** An AI-assisted systematic review: 34,594 records from multiple databases (27,481 after deduplication) were screened at title/abstract level and 2,277 full texts assessed; 1,104 studies were included, extracted into a 1,104-row database, and appraised with the instrument matching each design (RoB 2, ROBINS-I, JBI, MMAT, CASP, AMSTAR 2, and a project-specific non-validated framework for legal-documentary studies). Quantitative findings were synthesised without meta-analysis (SWiM). The protocol was not registered in advance; most steps were carried out by a large language model with partial human verification.

**Results.** 1,104 studies (85% since 2010) spanned many countries (India, Brazil, South Africa, the United States and Ghana the most frequent), but only 65 (6%) used designs able to support a causal claim. 59 studies had an extractable effect-size row; none could be pooled. In three SWiM families the direction of association was mostly favourable for legal-status, tenure and recognition mechanisms (Family A, k = 18), uniformly favourable or mixed for assistance, participation, trust and external-support mechanisms (Family B, k = 6), and without a dominant direction for ownership, regulation, institutional-capacity and administrative-structure mechanisms (Family C, k = 20); the families are thematic mechanism groupings, not homogeneous exposure–outcome pairs. Only 199 inclusion decisions and no extracted value have been independently verified.

**Conclusions.** The literature documents associations between legal/administrative conditions and access across many settings far more often than it establishes causal effects; it does not support one pooled estimate. Confidence is low to very low for any causal or comparative claim. [Author to revise after human verification.]

**Registration.** Not registered before conduct [author: state OSF identifier if registered retrospectively and label it retrospective].

## 1. Introduction

[Author: write the background with references. The paragraphs below state the argument the repository supports; they are not cited.]

Access to water and sanitation is usually measured by infrastructure coverage, but a household within reach of a network may still be unable to connect, or to keep and use a connection, because of legal and administrative conditions: who is recognised as eligible, what documents or tenure the application requires, what it costs, how much discretion officials hold, and how rules are enforced or reviewed [ref]. This review calls the gap between physical availability and effective access the *legal last mile*. The term organises the question; it is not assumed to be established by the evidence (`PROJECT_SPEC.md` §14).

The relevant evidence is scattered across disciplines and designs — public administration, economics, law, geography, public health, development studies — and across mechanisms and outcome measures that are rarely comparable [ref]. No prior synthesis, to the authors' knowledge, maps this evidence with a mechanism-based framework [author to verify against the literature].

**Objectives.** (1) Describe the empirical evidence on legal and administrative conditions and access to water and sanitation, by design, setting, mechanism and outcome. (2) Synthesise quantitative evidence where exposure, comparator, outcome and effect measure are comparable enough to do so defensibly, and otherwise report the direction of association transparently. (3) State what the evidence base does and does not allow us to conclude, including how reliable the review's own process is.

### 1.1 Conceptual framework

Structural conditions (legal and property status, documentation, income, geography, institutional capacity) act through an administrative architecture (eligibility screening, administrative burden, discretion, accommodation, enforcement, review, participation) and administrative navigation (understanding requirements, applying, satisfying requirements, obtaining accommodation, challenging decisions) to produce service access (formal connection, continuity, reliability, quantity, affordability, effective use) and, ultimately, inclusion or exclusion (`PROJECT_SPEC.md` §5). Administrative law is the central lens, not the only candidate cause; property, planning, municipal, utility-regulatory and political institutions are in scope.

## 2. Methods

### 2.1 Design, protocol and registration

The review followed a written protocol (`PROTOCOL.md`, PRISMA-P style), the PRISMA 2020 reporting guideline [ref], and SWiM guidance for synthesis without meta-analysis [ref]. **The protocol was not registered before the work was done**: an OSF Generalized Systematic Review registration was drafted (`00_admin/preregistration/`) but not submitted [author: if registered now, declare it retrospective]. The title was amended on 2026-09-28 to state AI assistance; the research question, eligibility criteria and synthesis approach were not changed (`PROTOCOL.md` §12).

### 2.2 Research questions and eligibility

The primary question asked how legal and administrative institutions shape the translation of physical availability of water and sanitation infrastructure into effective household access, and what evidence exists on the mechanisms by which eligibility screening, administrative burden, discretion, accommodation and enforcement produce or mitigate exclusion. The secondary question asked, where evidence is sufficiently comparable, for the magnitude of association between specific legal or administrative conditions and access outcomes. Studies were eligible if they examined water or sanitation access, examined a legal, administrative, institutional, regulatory or governance factor, and contained empirical evidence or a systematic empirical synthesis with an access-relevant outcome and an identifiable design; English, Portuguese and Dutch were eligible without translation (`INCLUSION_EXCLUSION.md`). Qualitative socio-legal studies were not excluded for being unpoolable.

### 2.3 Search and selection

Searches closed on 2026-09-11; SSRN and Westlaw/Lexis were not searched (`SEARCH_PROTOCOL.md`, README Known limitations). Selection was by an AI first pass (title/abstract and full text) with written rationales and standardised exclusion codes (E01–E12); a human second reviewer covered the 3,665 title/abstract records the AI marked include or unsure, and confirmed 199 of the 1,104 full-text includes. Full-text retrieval was closed by the researcher's decision with 1,383 title/abstract includes never assessed; the unassessed set is older on average (see 3.1).

### 2.4 Data extraction

A 92-field extraction form (`CODEBOOK.md`) was completed for every included study by the AI, largely from full text; 10 studies were extracted from abstract or metadata only and an audit found further rows with signs of shallow extraction (Limitations). The AI later re-read 127 studies from full texts found in the researcher's Drive; of the 76 rows flagged only by the sparse-record audit, 9 had an abstract-level extraction that was materially wrong or incomplete (`reextract_2026-10-04/CAMPAIGN_NOTES.md`). There was no second extractor. A seeded sample for human second extraction has been prepared (`03_extraction/second_extractor/`) but not yet completed.

### 2.5 Risk of bias and critical appraisal

Each study was appraised with the instrument matching its design: RoB 2 (cluster variant) for randomised trials (5), ROBINS-I (60), JBI cross-sectional (131), MMAT (196), CASP qualitative (251) and AMSTAR 2 for systematic reviews (18). For 433 legal-documentary or doctrinal studies no published instrument fits, and this project's own **non-validated** Legal Institutional Evidence Appraisal Framework was used; 10 studies were judged not appraisable. Ratings were assigned by rule from the extracted fields, not by signalling-question reading of each paper, except for the studies re-appraised from full text (listed in `CHANGELOG.md`). Ratings therefore describe the extraction as much as the paper.

### 2.6 Synthesis

Each study was coded to one of nine mechanism families (eligibility, status and documentation; procedural burden; fees, tariffs and subsidies; discretion and accommodation; enforcement and sanctions; review and redress; institutional structure and coordination; participation and assistance; regulatory model and ownership) or to `multiple`, and to one of four outcome families (primary connection, effective access, economic access, administrative outcome) or `multiple`; the families are not pooled with each other. The labels were mapped from the free-text labels of the extraction by keyword rules, with the rows the rules could not place resolved by the AI and five edge cases left unmapped, and the original labels are preserved; the mapping is mechanical and unvalidated, and a human has not checked it. Free-text study-design labels were mapped to the eight-value design list in the same way. A feasibility judgment (`phase11_quantitative_feasibility_judgment.md`) concluded that no family reaches the bar for meta-analysis, so 59 effect-size rows were compiled into three structured syntheses reporting direction and significance of each study's own estimate (SWiM). The family assignments were made by judgement and organise the write-up only: on a keyword reading of the exposure definitions, 28 of 44 family-assigned rows sit outside the wording of the family they were placed in (`05_analysis/effect_sizes/FAMILY_FIT_AUDIT_2026-10-04.md`), so the families are loose groupings, not tests of the specified constructs. Families A, B and C are therefore reported as thematic mechanism groupings used to organise structured vote counting (SWiM), not as homogeneous exposure–outcome pairs, and their headings describe the clusters actually synthesised (legal status, tenure, recognition and governance arrangements; assistance, participation, trust and external support; ownership, regulation, institutional capacity and administrative structure), which is also why pooling was rejected. No effect was converted to a common scale. Sensitivity analyses removed abstract-only and shallow extractions, the one row for a study not flagged eligible, linked reports and two coding judgment calls.

### 2.7 Secondary reviews

Systematic reviews in the corpus are treated as secondary evidence and never pooled as if primary; their primary studies may also be in the corpus (a double-counting risk assessed only in part, Limitations).

### 2.8 Data and code

All databases, scripts and generated figures are in the project repository; `python3 code/analysis/verify_repository.py` re-derives every quoted figure and checks that generated files are current.

### 2.9 Use of artificial intelligence

This is an AI-assisted systematic review. A large language model (Claude, Anthropic) performed most of the title/abstract first-pass screening, full-text screening, data extraction, risk-of-bias appraisal and synthesis drafting, under the direction of the human researcher, who defined the question, protocol and eligibility criteria, ran the database searches, supplied the full texts and made the closing and scoping decisions. Independent human verification was partial: a human second reviewer covered the 3,665 title/abstract records the AI marked include or unsure (not the AI's exclusions), and confirmed 199 of the 1,104 full-text includes; no full-text exclusion, extracted value or risk-of-bias rating has been independently verified against source papers. [Model version and dates of use: add per journal policy.] The stage-by-stage division of labour is tabulated in `AI_USE_STATEMENT.md`.

## 3. Results

### 3.1 Search and selection

The database and grey-literature searches identified 34,594 records; 27,481 remained after deduplication. 26,222 had an abstract and were screened at title/abstract level (1,259 without an abstract were not decided); 3,659 were retained for full-text assessment. Full-text retrieval was closed by the researcher's decision: 2,277 of 3,659 records were assessed and 1,382 were never assessed (1,200 not retrievable, 182 for which the wrong file was obtained). Of the 2,277 assessed, 1,173 were excluded (151 because the full text was inaccessible; reasons for the others are in `exclusion_log.csv`) and 1,104 were included (1,104 extraction rows, corresponding to 1,102 distinct studies after collapsing definite companion reports).

Reasons for full-text exclusion (standardised codes; per-record rationale in `exclusion_log.csv`):

| Code | Reason (as labelled in the README) | Full-text exclusions |
|---|---|---|
| E01 | wrong topic | 492 |
| E02 | wrong population | 34 |
| E03 | wrong exposure | 82 |
| E04 | wrong outcome | 84 |
| E05 | no empirical evidence | 139 |
| E06 | engineering only | 106 |
| E07 | wrong service | 29 |
| E08 | duplicate | 8 |
| E09 | insufficient information | 2 |
| E10 | inaccessible full text | 151 |
| E12 | wrong study design | 46 |

### 3.2 Characteristics of the included evidence

*Figures 1–3 and 5 (`06_outputs/figures/fig1_design_mix.svg`, `fig2_publication_years.svg`, `fig3_countries.svg`, `fig5_appraisal_tools.svg`) show the design mix, publication years, countries and appraisal instruments; Figure 4 (`fig4_direction_by_family.svg`) shows the direction of association in the three syntheses (Section 3.5). All are generated from the databases by `code/analysis/build_figures.py`.*

- **Volume and recency.** 1,104 studies; 933 (85%) published 2010 or later (median year 2018; 30 before 2000).
- **Design mix** (evidence-map `study_design_class`; the free-text design labels of 328 studies were mapped onto the 8-value enum on 2026-10-14 under open item A20, with the original strings kept in `evidence_map_original_labels_2026-10-14.csv`, so `qualitative` lumps ethnographic, historical, institutional and documentary case studies; 10 studies keep a free-text label the rules could not map (essays, theory, policy analyses) and are not in the counts that follow): qualitative 530, mixed-methods 229, observational 142, quasi-experimental 64, doctrinal 57, jurimetric 37, secondary systematic reviews 30, experimental 5. By appraisal tool: RoB 2 5, ROBINS-I 60, JBI Cross-Sectional 131, MMAT 196, CASP Qualitative 251, AMSTAR 2 18, Legal Framework 433, NONE 10.
- **Designs able to support a causal claim about a legal/administrative mechanism:** 65 (6%) — 60 quasi-experimental studies and 5 randomised trials (which are 4 distinct trials, see Section 3.4). 33 studies carry a numeric mechanism-certainty of 3 or 4 (the codebook's quasi-experimental or experimental evidence), **but only 10 of them are among the 65 ROBINS-I/RoB 2 studies; the other 23 are other designs, a coding inconsistency the audit flags** (`DATA_QUALITY_AUDIT_2026-09-29.md` §5); 222 sit at level 1 (documented association) and 270 at level 2; 575 carry narrative text instead of a 0–4 code.
- **Geography** (`country` is free text; 116 studies name several countries or a region and are not counted below): India 126, Brazil 81, South Africa 78, United States 67, Ghana 51, Kenya 47, Mexico 37, Indonesia 30, Nigeria 27, Bangladesh 24. The dissertation's comparison countries are unevenly covered: **Brazil 81, Canada 15 (18 counting multi-country entries), Netherlands 1 (3 counting multi-country entries).**
- **Legal systems** (rule-based buckets): blank 13, civil law 385, common law 522, mixed / both / customary 181, other 3.
- **Setting and language:** urban (incl. informal settlements) 517, rural 275, mixed/both 257, peri-urban 28, blank/other 27; English 1021 of 1,104 studies, Spanish 31, Portuguese 21, French 6.

### 3.3 Mechanisms and outcomes addressed

Counts are studies for which the extraction coded the field `TRUE` (a blank is *not* `FALSE`; a study can carry many). They show what was coded, not how strong the evidence is.

| Mechanism coded | Studies | | Outcome coded | Studies |
|---|---|---|---|---|
| `institutional_fragmentation` | 632 | | `water_access` | 972 |
| `discretion_accommodation` | 593 | | `formal_connection` | 566 |
| `fees` | 542 | | `service_coverage` | 549 |
| `service_area` | 483 | | `affordability` | 499 |
| `political_coordination` | 463 | | `sanitation_access` | 433 |
| `enforcement` | 461 | | `service_reliability` | 369 |
| `participation` | 420 | | `service_quality` | 294 |
| `eligibility` | 421 | | `service_continuity` | 243 |
| `burden` | 416 | | `service_quantity` | 206 |
| `documentation` | 263 | | `refusal` | 106 |
| `bureaucratic_assistance` | 196 | | `delay_outcome` | 95 |
| `administrative_review` | 69 | | `application_success` | 74 |
| `complaint` | 124 | |  |  |
| `judicial_review` | 64 | |  |  |
| `disconnection` | 105 | |  |  |
| `reconnection` | 22 | |  |  |

Institutional fragmentation (632), official discretion/accommodation (593) and fees/tariffs (542) are the most frequently coded mechanisms; formal-connection (566) and affordability (499) outcomes are well represented, while sanitation access (433) is coded about half as often as water access (972). Mechanisms concerning redress and review — administrative review (69), judicial review (64), complaint (124), reconnection (22) — and application outcomes (refusal 106, delay 95, success 74) are coded far less often.

### 3.4 Risk of bias and confidence in the evidence

Appraisal ratings are rule-based and, for most studies, depend on what was extracted (Methods 2.5). Of the 131 JBI cross-sectional studies, 50 were rated 'high concern', largely reflecting sparse extraction rather than demonstrated weakness. ROBINS-I ratings: Moderate 51, Serious 9. RoB 2 ratings: Some concerns 5; two of the randomised-trial studies (S294 and S366) report the same trial. A numeric mechanism-certainty code of 3 or 4 (quasi-experimental or experimental) was recorded for 33 studies, but only some of these are ROBINS-I or RoB 2 studies, a coding inconsistency reported in `DATA_QUALITY_AUDIT_2026-09-29.md` §5.

**Are the AMSTAR 2 studies actually systematic reviews? Partly confirmed, partly not.**

- 18 studies carry AMSTAR 2; another 10 studies also had a secondary-review design class but were **reclassified to `NONE`** after an eligibility check found them to be self-described narrative, conceptual or documentary reviews that never claim a systematic search (S079, S320, S326, S429, S430, S436, S440, S466, S479, S482; `RISK_OF_BIAS.md` §4; S326 joined them on 2026-09-29 after its full text, supplied by the researcher, showed no stated search, selection or appraisal method). AMSTAR 2 was not applied to those, and the project has **no validated instrument for a non-systematic review used as an evidence source** — an acknowledged gap.
- Of the 18 that kept AMSTAR 2, each was classed as a secondary systematic review. The recorded fields (publication type, design, method text, sample) support that unevenly: 12 name a registration, PRISMA or JBI method, 14 state a count of included studies, and 1 (S521) show at most one weak signal (the word "systematic" or a review type) — a way to order full-text checks, not a finding (`05_analysis/descriptive/DATA_QUALITY_AUDIT_2026-09-29.md` §3). None of them is now extracted from abstract or metadata only; S319, S324, S325 and S344 were read in full text on 2026-10-02 (S324 is a registered, well-reported review; S319 searched one database; S325 and S344 are single-author reviews with weak methods, but all four state a search, a selection process and a synthesis, so all keep AMSTAR 2); S329 is described as a "narrative review with systematic search" and S418 as a narrative/scoping review with a documented search (hybrids kept eligible with a noted caveat); S326, first flagged as an "evidence survey", was moved to `NONE` once its full text was read; S418, S438, S697, S052 and S327 were read in full text on 2026-10-03 (S697, a meta-analysis, and S438, S052 and S327 all state a search, selection and synthesis, so all keep AMSTAR 2).
- **Only 18 of the 18 received a formal AMSTAR 2 confidence rating** (S015 Critically Low, S019 Critically Low, S027 Critically Low, S052 Critically Low, S116 Critically Low, S319 Critically Low, S325 Critically Low, S344 Critically Low, S350 Critically Low, S370 Critically Low, S372 Critically Low, S418 Critically Low, S427 Critically Low, S438 Critically Low, S475 Critically Low, S521 Critically Low, S537 Low, S1168 Critically Low; 17 of the 18 are Critically Low; the others are S537 Low, mostly because of missing protocols, single-database searches, no list of excluded studies or no appraisal of the included studies); the other 0 are "Not ratable" because their extraction lacks the information for the critical items. **So AMSTAR 2 so far tells the reader little beyond "low confidence"; the 0 unrated reviews need their full texts.**
- *Tentative flag (an observation of this draft, not a project ruling):* AMSTAR 2 was designed for reviews of healthcare interventions that include randomised or non-randomised studies; several of these reviews are realist, scoping or mapping reviews of qualitative and policy literature, for which a rating would be out-of-design even with full information. A decision on whether to keep AMSTAR 2 for these, or use a different instrument, is open.
- Reviews are secondary evidence and are never pooled as if primary. Whether their primary studies are also separate rows in this corpus was checked on 2026-10-04 for only 7 of the 18 reviews (those whose PDFs were to hand): their reference lists cite 48 distinct corpus studies, S319 (21), S325 (19) cite ten or more. This is an upper bound (background citations count) and does not read the included-studies tables, so the real double-counting risk is **still unresolved**, and 11 reviews are unchecked (`05_analysis/descriptive/AMSTAR2_OVERLAP_CHECK_2026-10-04.md`).

### 3.5 Quantitative evidence: three structured syntheses

Only 59 studies have an effect-size row; none is pooled. Counts are of the **sign of each study's extracted association** (sign and valence differ for some studies — see the Family A and C documents).

| Family | Studies | Positive / negative / null / mixed (sign) | Documents |
|---|---|---|---|
| A — legal status, tenure, recognition and governance arrangements | 18 | 11 / 5 / 2 / 0 | `family_A_swim_synthesis_2026-09-28.md` |
| B — assistance, participation, trust and external support | 6 | 5 / 0 / 0 / 1 | `family_B_…` |
| C — ownership, regulation, institutional capacity and administrative structure | 20 | 7 / 9 / 0 / 4 | `family_C_…` |

The families are thematic mechanism groupings used to organise structured vote counting (SWiM), not homogeneous exposure–outcome pairs: their headings describe the mechanism clusters actually synthesised and are not the protocol's original titles (`PROJECT_SPEC.md` §8, dated note; open item A21).

**Where studies agree.** In Family A, 13 of 18 (72.2%) are concordant with "legal/institutional recognition or eligibility is associated with better access" on a substantive reading (10 positive-sign studies plus 3 negative-sign studies in which unrecognised or informal status is associated with worse access). All 6 Family B studies report a positive or mixed association between administrative assistance/institutional trust and access, and none is negative. Three studies of private versus public ownership (S526, S539, S749; US ×2 and Brazil) all associate private ownership with worse affordability or progressivity.

**Where they disagree or do not fit.**

- Family A counter-pattern (exposure associated with *worse* access): S1020, S104, S1121; null: S037, S780.
- Family C has no dominant direction (7 positive / 9 negative / 4 mixed) — its exposures and outcomes are heterogeneous, and signs are not comparable across them.

Per-study results (exposure, outcome, direction, appraisal rating) are tabulated in the three family documents (`06_outputs/supplementary/family_*_swim_synthesis_2026-09-28.md`).

**Sensitivity analyses.** (`05_analysis/sensitivity/SENSITIVITY_ANALYSIS_2026-09-28.md`): under every scenario tried — dropping abstract-only extractions, dropping the sparse-audit rows that carry effect sizes, dropping effect-size rows of studies not flagged eligible (none remains since S589's row was removed on 2026-10-14; the scenario is kept as a check), collapsing linked reports, and dropping Family A's two coding judgment calls — the pre-stated conclusion tests for A, B and C hold; Family A's concordant share ranges 68.8–72.2%.

**Reporting bias and certainty.** No publication-bias assessment was possible: although Families A and C each contain 20 studies, no common effect metric exists, so no funnel-plot or small-study analysis is defined (`ANALYSIS_PLAN.md` §9 requires about ten studies on a common scale). Certainty of evidence was **not** graded with GRADE; the direction-of-association syntheses carry no certainty rating and the overall confidence statement in Section 5.1 is qualitative.

### 3.6 Qualitative, doctrinal and mixed-methods evidence

A large part of the evidence base (853 studies by design class, plus 10 with unmapped free-text design labels) is qualitative, mixed-methods or documentary rather than quantitative. Using the mechanism vocabulary adopted on 2026-10-14 (`FAMILY_VOCABULARY_PROPOSAL_2026-09-28.md`, mechanical and unvalidated), studies whose label maps to a single mechanism family are: eligibility status documentation 156, discretion accommodation 122, institutional structure coordination 115, enforcement sanctions 80, fees tariffs subsidies 49, regulatory model ownership 27, participation assistance 22, procedural burden 17, review redress 4; 507 carry several. The mapping is mechanical and unvalidated, so read the counts as indicative only. Examples of qualitative or doctrinal studies with `mechanism_certainty` 2 or higher ("mechanism directly observed" or above), showing the study's own recorded (original) mechanism label beside the adopted family, and the AI-extracted finding text:

| Study | Country | Design | Own recorded mechanism label (original) → adopted family | Extracted finding (truncated) |
|---|---|---|---|---|
| S101 | Kenya | qualitative | DISCRETION_ACCOMMODATION → discretion accommodation | Formal water connection through Nairobi's piped grid does not equal reliable water access: neighborhood disparities exist even among neighbors with formally equivalent connections, because water rights are 'con… |
| S253 | United States | qualitative | ENFORCEMENT → enforcement sanctions | Each case illustrates one literacy level in tribal water-quality contexts: Apsaalooke (functional EHL: accessible information and skills), Anishinaabe (interactive EHL), Hoopa Valley (critical EHL; the tribal o… |
| S305 | multi-country (Ecuador,  | qualitative | ELIGIBILITY → eligibility status documentation | Comparing successful (Ecuador 2008) and unsuccessful (Chile 2022) constitutional water-change processes, the article argues that where there is no agreement on either science or policy, politicization is requir… |
| S307 | multi-country | qualitative | BURDEN → procedural burden | The dominant perceived driver of subscriber attrition from container-based sanitation services was economic challenges faced by subscribers, and the most common mitigation strategy was developing individual rep… |

### 3.7 Gaps in the evidence base

- **Geographic:** the Netherlands (1 single-country study) and Canada (15) — two of the dissertation's three comparison jurisdictions — are barely represented against Brazil (81); 568 (51%) of studies sit in the ten commonest single countries.
- **Design:** 5 randomised trials (4 distinct) and 60 quasi-experimental studies against 433 (39%) studies appraised with the project's own non-validated framework (the residual category for designs no published instrument fits, including doctrinal and documentary studies).
- **Mechanisms/outcomes:** redress and review mechanisms and application-process outcomes are thinly coded (see Section 3.3); sanitation access less than water.
- **Retrieval:** 1,382 title/abstract includes were never assessed. Their median publication year is 2014 versus 2018 for assessed records; 8.9% were published before 2000 versus 3.0%, and 30.8% in 2020 or later versus 42.7% — the unassessed set is older, so the corpus under-represents earlier literature.

## 4. Discussion

*This section is interpretation. Each point rests on the numbers cited in Section 3 and could be wrong.*

1. **The literature documents co-occurrence far more than causation.** With 65 (6%) causal-capable designs (and a certainty-3–4 coding that does not line up with them, see Section 3.2), the base can say that legal/administrative features and access outcomes are associated across many settings, but rarely that one causes the other. *Rests on:* Section 3.2 counts. *Would change if:* the 1,382 unassessed records or future searches contain many more designs with credible identification.
2. **Recognition and formal status tend to go with better access (Family A), but the pattern is thin.** 13 of 18 concordant, 3 counter-pattern (S104 tenure and interruptions; S1020 a watershed programme and collection time; S1121 water-adequacy screening and permitting): S104 appraised with JBI Cross-Sectional; S1020 appraised with ROBINS-I; S1121 appraised with ROBINS-I. *Rests on:* the SWiM coding, a judgment by the same AI. Not a pooled estimate and not certainty-graded.
3. **Assistance and trust mechanisms look uniformly favourable (Family B) — but on six studies with six different mechanisms.** The consistency may reflect small numbers or reporting of positive findings; nothing here excludes either.
4. **Ownership and price: private ownership goes with worse affordability in the three studies (S526, S539, S749), but the two US samples probably overlap**, so this may be two independent samples, not three (`linked_reports_2026-09-28.csv` LR09, an audit inference).
5. **Most institutional analysis in this corpus is descriptive-qualitative and concentrated on fragmentation, discretion and fees.** This may reflect what the search and the closed retrieval surfaced (English-language, post-2010, database-indexed) as much as what the world contains.
6. **The dissertation's comparative frame (Netherlands, Canada, Brazil) cannot be tested from this base as it stands**: one Dutch and 15 Canadian single-country studies.

## 5. Limitations

- **Incomplete full-text screening.** 1,382 of 3,659 records (37.8%) were not assessed, and those not assessed are older on average; the review is not exhaustive and may under-represent earlier literature.
- **AI-conducted judgments with partial verification.** Screening decisions, extraction, appraisal and coding of direction of association were made by the same AI system; only 199 full-text includes were human-confirmed, 73 decided rows carry no recorded reviewer, and the title/abstract exclusions were not human-checked. A blind re-read by two non-Claude models (Codex, Gemini) of 70 of the AI's full-text excludes (a stratified sample, limited to records whose PDF was available) judged 34 of them to be includes; this is an AI-versus-AI check, it was not human-adjudicated, and, scaled by exclusion code, the rate would imply roughly 520 further includes if the models were right, and an AI triage of the same records puts about 37 under a narrow reading of the criteria (arithmetic only), so the exclusion log may understate the eligible literature substantially; in the other direction, the models would exclude 3 of 40 sampled unconfirmed includes, roughly 68 of the unconfirmed includes if the rate held (open item A16; `02_screening/full_text/A16_ADJUDICATION_SHEET_2026-10-04.md`).
- **Thin extraction for some studies.** 10 studies were extracted from abstract or metadata only; there was no second extractor. The AI re-read 127 studies from full texts after the first extraction (an AI check of AI work, not independent verification); in 9 of the 76 sparse-audit rows among them the abstract-level extraction was materially wrong or incomplete (`CAMPAIGN_NOTES.md`).
- **Appraisal validity.** Ratings are rule-based; 433 studies were appraised with a non-validated project instrument; 50 of 131 JBI ratings are 'high concern' largely reflecting sparse extraction; only 18 of 18 AMSTAR 2 reviews could be given a confidence rating (17 Critically Low and 1 Low).
- **No pooled estimate.** Direction-of-association syntheses rest on 59 effect-size rows and are neither effect estimates nor certainty-graded (GRADE).
- **Uncontrolled classifications.** Free-text country, legal-system, mechanism and outcome fields; a proposed controlled vocabulary is a mechanical draft.
- **Search scope.** SSRN and Westlaw/Lexis were not searched (`README.md`, Known limitations).

*Source of every figure: `00_admin/CURRENT_FIGURES.md`; checked by `python3 code/analysis/verify_repository.py`.*

### 5.1 Confidence in the evidence and in the review's own process

This is the author's tentative characterisation, not a GRADE judgment (none has been made): the direction-of-association statements rest on a small quantitative subset (20, 6 and 20 studies), AI-extracted and AI-coded values, mostly observational designs, and a screening stage that closed early. Reasons follow.

### 5.2 Incomplete screening

- Full-text retrieval closed at 62.2%: 1,382 of 3,659 records (1,200 not retrievable, 182 wrong file delivered) were never assessed, and the unassessed set is systematically older (Section 3.7). Some may be duplicates of included studies, some not eligible; the direction of any bias is unknown.
- 151 of the 1,173 full-text excludes are E10 (inaccessible text), i.e. never judged on content.
- Every full-text decision is the AI's; a human confirmed 199 includes (S001–S200) and no excludes; 73 decided rows carry no reviewer label. A prioritised queue for human review exists (`02_screening/full_text/REVIEWER_2_PRIORITY_QUEUE_README.md`).
- **An AI-versus-AI check found many contested excludes.** Two non-Claude models (Codex, Gemini), blind to the original decision, re-read 121 full-text decisions whose PDF was available; of the 70 the AI had excluded, 34 were judged includes (concentrated in E01 wrong topic and E06 engineering only). This was not human-adjudicated, the models may read the criteria too loosely, and nothing was changed; scaled by exclusion code the rate would imply roughly 520 further includes if the models were right, and about 37 even under a narrow reading of criterion 2 by an AI triage of the same records (arithmetic only, against 1,104 current includes); if even a fraction are eligible, the exclusion log and every count built on it are understated. In the other direction the models would exclude 3 of 40 sampled includes beyond S001–S200, roughly 68 (range 23–180) of the unconfirmed includes if the rate held — a precision question that the human second-screening of includes would settle. The researcher's reading list is `02_screening/full_text/A16_ADJUDICATION_SHEET_2026-10-04.md` (open item A16).
- At title/abstract stage the human second pass covered the 3,665 include-plus-unsure records only; the 22,557 records the AI excluded were not human-checked, so any wrongly excluded record is invisible to this review. The 99.8% agreement on the reviewed set is unusually high and was flagged by the project itself. (`AI_USE_STATEMENT.md` and `AUDITING_GUIDE.md` say "all records"; that wording should be checked against the README, which is narrower.)

### 5.3 Missing or thin data

- 10 studies were extracted from abstract or metadata only (0.9%); none has an effect-size row, so the SWiM syntheses are unaffected by them, but descriptive counts and ratings include them. **That count is a floor:** it counts one note prefix, and a sparse-record audit (`05_analysis/descriptive/SPARSE_RECORD_AUDIT_2026-10-04.md`) found 55 more rows with at least one sign of shallow extraction — 1 whose own notes say only the abstract or citation was read and 15 whose recorded location cites the abstract alone (a verification queue, not proof) — of which 1 carry effect-size rows. There is no second extractor: extracted values have not been checked against the source papers.
- 50 of 131 JBI ratings are "High concern", which here means sparse extraction rather than a poor study. For CASP and MMAT, several items are "Can't tell" for every study (for example CASP item 3, research design justified) because extraction did not capture methodological reporting. Ratings are rule-based and unreviewed by a human.
- Of 59 effect-size rows, 8 give a confidence interval and 26 a standard error; estimates are as the papers report them and none is pooled.

## 6. Conclusion

The evidence assembled here shows that legal and administrative conditions are studied in association with water and sanitation access across a wide range of settings, most often descriptively and rarely with designs able to support causal claims (65 of 1,104 studies). Where quantitative estimates exist they are too heterogeneous to pool, and their direction is most consistent for legal-status, tenure and recognition mechanisms and for assistance and participation mechanisms, least consistent for ownership, regulation and administrative-structure mechanisms. These statements are provisional: extraction and appraisal were AI-conducted and only partly verified, screening of the full-text pool is incomplete, and the protocol was not registered in advance. The review does not establish the *legal last mile* as a general mechanism; it describes where evidence exists, where it is thin, and what a human-verified update would need to check first. [Author to revise.]

### 6.1 Implications for research and practice

*Conditional on human verification.* (1) Policy readers should not take this review as evidence that any single legal or administrative reform causes better access; the designs that could show that are few. (2) The next research step the repository supports is verification, not expansion: complete the human second pass of screening and a second extraction, fetch the full texts of the shallow extractions and the unassessed older records, and finish the check of overlap between the AMSTAR 2 reviews and the primary studies. (3) If the comparative frame of the underlying doctoral project (Netherlands, Canada, Brazil) is to be tested, targeted searches for Dutch and Canadian evidence are needed, because the corpus holds very few single-country studies for the first two (Section 3.7).

## 7. Declarations

- **Funding and competing interests:** [author to complete — prompts in `00_admin/disclosures/FUNDING_AND_COMPETING_INTERESTS_TEMPLATE.md`; PRISMA items 25 and 26].
- **AI use:** Claude (Anthropic) performed most screening, extraction, appraisal and synthesis drafting; see `AI_USE_STATEMENT.md` for the stage-by-stage table. [Model versions and dates: add per journal policy.]
- **Author contributions:** [author to complete; AI is not an author].
- **Data and code availability:** repository (`README.md`); source PDFs are not redistributed.
- **Ethics:** secondary analysis of published literature; [author to confirm no approval required].

## References

[Author: references to be added where marked [ref]. The repository's `SOURCES.md` lists the methodological sources already used (PRISMA 2020, SWiM, RoB 2, ROBINS-I, JBI, CASP, MMAT, AMSTAR 2).]

