# Preliminary results report — AI-assisted systematic review (generated 2026-09-29)

> **PRELIMINARY — NOT A FINAL RESULT.** Produced by the same AI that screened, extracted and appraised the studies, from the
> repository's own databases, with no human verification of extracted values against the source papers (`AI_USE_STATEMENT.md`).
> Every number below is computed from the data (`code/analysis/build_preliminary_report.py`); every quoted example is an
> AI-extracted field, not a re-reading of the paper. Sections 2A and 3 report what the records contain; **Section 2B is tentative
> interpretation** and is labelled as such. No pooled effect exists and none is claimed.

## 1. Methods and progress in brief

| Step | Status |
|---|---|
| Question | How legal and administrative institutions shape the translation of physical water/sanitation infrastructure into effective household access (`PROTOCOL.md`) |
| Search | Closed 2026-09-11; 34,594 raw records → 27,481 unique (SSRN and Westlaw/Lexis never searched) |
| Title/abstract screening | Final 3,659 include / 6 exclude: 26,222 of 27,481 screened by AI first pass (3,062 include / 22,557 exclude / 603 unsure; 1,259 without an abstract left undecided); a human second pass covered the 3,665 include-plus-unsure records, **not the 22,557 AI excludes**; 99.8% agreement, flagged by the project as unusually high |
| Full-text screening | Closed by researcher decision at **2,276 of 3,659 assessed (62.2%)**: **1,159 include / 1,117 exclude**; 1,383 never assessed. 151 of the excludes are E10 ("full text inaccessible"), so only **2,125** were judged on content. AI decisions; a human confirmed 100 includes and no excludes |
| Extraction | 1,159 studies, 92 codebook fields, by the AI; 37 from abstract/metadata only; no second extractor |
| Appraisal | Rule-based batch ratings from extracted fields with design-matched tools: RoB 2 5, ROBINS-I 63, JBI Cross-Sectional 140, MMAT 205, CASP Qualitative 263, AMSTAR 2 23, Legal Framework 447, NONE 13. Legal Framework is the project's own **non-validated** instrument. No human review of ratings |
| Synthesis | Phase 11: no family clears the bar for meta-analysis. 62 effect-size rows (A 20, B 6, C 20, 16 reasoned non-fits), none pooled; three structured (SWiM) direction-of-association syntheses |

## 2A. Preliminary findings drawn from the extracted evidence

### 2A.1 What the evidence base looks like

- **Volume and recency.** 1,159 studies; 985 (85%) published 2010 or later (median year 2018; 30 before 2000).
- **Design mix** (evidence-map `study_design_class`; 349 studies carry free-text values outside the 8-value enum — the commonest are variants of "case study", e.g. ethnographic case study (16); qualitative case study (10); they are not in the counts that follow): qualitative 267, mixed-methods 207, observational 147, quasi-experimental 65, doctrinal 44, jurimetric 39, secondary systematic reviews 36, experimental 5. By appraisal tool: RoB 2 5, ROBINS-I 63, JBI Cross-Sectional 140, MMAT 205, CASP Qualitative 263, AMSTAR 2 23, Legal Framework 447, NONE 13.
- **Designs able to support a causal claim about a legal/administrative mechanism:** 68 (6%) — 63 quasi-experimental studies and 5 randomised trials (which are 4 distinct trials, see §3.4). 35 studies carry a numeric mechanism-certainty of 3 or 4 (the codebook's quasi-experimental or experimental evidence), **but only 10 of them are among the 68 ROBINS-I/RoB 2 studies; the other 25 are other designs, a coding inconsistency the audit flags** (`DATA_QUALITY_AUDIT_2026-09-29.md` §5); 238 sit at level 1 (documented association) and 286 at level 2; 596 carry narrative text instead of a 0–4 code.
- **Geography** (`country` is free text; 124 studies name several countries or a region and are not counted below): India 133, Brazil 87, South Africa 84, United States 71, Ghana 53, Kenya 50, Mexico 37, Indonesia 30, Nigeria 28, Bangladesh 27. The dissertation's comparison countries are unevenly covered: **Brazil 87, Canada 15 (19 counting multi-country entries), Netherlands 1 (3 counting multi-country entries).**
- **Legal systems** (rule-based buckets): blank 28, civil law 394, common law 546, mixed / both / customary 188, other 3.
- **Setting and language:** urban (incl. informal settlements) 525, rural 298, mixed/both 270, peri-urban 29, blank/other 37; English 1073 of 1,159 studies, Spanish 32, Portuguese 22, French 6.

### 2A.2 Mechanisms and outcomes the studies address (AI extraction coding)

Counts are studies for which the extraction coded the field `TRUE` (a blank is *not* `FALSE`; a study can carry many). They show what was coded, not how strong the evidence is.

| Mechanism coded | Studies | | Outcome coded | Studies |
|---|---|---|---|---|
| `institutional_fragmentation` | 664 | | `water_access` | 1,013 |
| `discretion_accommodation` | 597 | | `formal_connection` | 579 |
| `fees` | 543 | | `service_coverage` | 564 |
| `service_area` | 482 | | `affordability` | 507 |
| `political_coordination` | 481 | | `sanitation_access` | 457 |
| `enforcement` | 460 | | `service_reliability` | 382 |
| `participation` | 445 | | `service_quality` | 302 |
| `eligibility` | 423 | | `service_continuity` | 251 |
| `burden` | 419 | | `service_quantity` | 206 |
| `documentation` | 262 | | `refusal` | 107 |
| `bureaucratic_assistance` | 215 | | `delay_outcome` | 95 |
| `administrative_review` | 70 | | `application_success` | 75 |
| `complaint` | 124 | |  |  |
| `judicial_review` | 65 | |  |  |
| `disconnection` | 107 | |  |  |
| `reconnection` | 24 | |  |  |

Institutional fragmentation (664), official discretion/accommodation (597) and fees/tariffs (543) are the most frequently coded mechanisms; formal-connection (579) and affordability (507) outcomes are well represented, while sanitation access (457) is coded about half as often as water access (1,013). Mechanisms concerning redress and review — administrative review (70), judicial review (65), complaint (124), reconnection (24) — and application outcomes (refusal 107, delay 95, success 75) are coded far less often.

### 2A.3 The quantitative subset: three structured syntheses (direction of association, not effect size)

Only 62 studies have an effect-size row; none is pooled. Counts are of the **sign of each study's extracted association** (sign and valence differ for some studies — see the Family A and C documents).

| Family | Studies | Positive / negative / null / mixed (sign) | Documents |
|---|---|---|---|
| A — legal recognition, eligibility and access | 20 | 12 / 6 / 2 / 0 | `family_A_swim_synthesis_2026-09-28.md` |
| B — bureaucratic/administrative assistance | 6 | 5 / 0 / 0 / 1 | `family_B_…` |
| C — administrative/legal barriers, ownership and price | 20 | 7 / 9 / 0 / 4 | `family_C_…` |

**Where studies agree.** In Family A, 15 of 20 (75.0%) are concordant with "legal/institutional recognition or eligibility is associated with better access" on a substantive reading (11 positive-sign studies plus 4 negative-sign studies in which unrecognised or informal status is associated with worse access). All 6 Family B studies report a positive or mixed association between administrative assistance/institutional trust and access, and none is negative. Three studies of private versus public ownership (S526, S539, S749; US ×2 and Brazil) all associate private ownership with worse affordability or progressivity.

**Where they disagree or do not fit.**

- Family A counter-pattern (exposure associated with *worse* access): S1020, S104, S1121; null: S037, S780.
- Family C has no dominant direction (7 positive / 9 negative / 4 mixed) — its exposures and outcomes are heterogeneous, and signs are not comparable across them.

Examples as extracted (exposure and direction are AI-extracted fields):

| Study | Country | Tool | Exposure (extracted) | Direction (extracted) |
|---|---|---|---|---|
| S765 | Peru | ROBINS-I | Household acquisition of a legal land title under Peru's PETT (Proyecto Especial de Titulacion… | positive (statistically significant) |
| S398 | Brazil | ROBINS-I | Household census-tract location within an area designated ZEIS (Zona Especial de Interesse Soci… | positive (ZEIS designation associated with increased water/sewage-network access and homeownership) |
| S1122 | Burkina Faso | ROBINS-I | Legal/administrative zoning status of residence (zoned vs. non-zoned/spontaneous-settlement lan… | negative (non-zoned/informal legal status sharply reduces hazard of gaining piped water access; effect compoun… |
| S142 | United States | ROBINS-I | Municipal incorporation status (incorporated vs. unincorporated), which functions as the legal/… | negative (unincorporated/unrecognized jurisdictional status associated with reduced service access) |
| S057 | Cambodia | RoB 2 | Random offer of a targeted sanitation subsidy to households determined eligible via the Poverty… | positive (subsidy eligibility increases sanitation-product purchase) |
| S104 | Zambia | JBI Cross-Sectional | Household home-ownership / tenure status (owner vs. non-owner) in a multilevel household-neighb… | positive (home ownership associated with higher odds of interruption -- direction counter to a simple "tenure… |
| S1020 | India | ROBINS-I | Household residence in a treatment micro-watershed subject to a government watershed-developmen… | negative (watershed-development intervention associated with increased, i.e. worsened, domestic water collecti… |
| S1121 | United States | ROBINS-I | Local government adoption of a water-adequacy screening policy (an administrative-review growth… | negative (water-adequacy screening reduces new residential water-connection permitting) |
| S085 | India | RoB 2 | Random assignment to bureaucratic-assistance treatment (T1: help completing formalization appli… | positive (bureaucratic assistance increases formalization, conditional on political coordination) |
| S294 | Democratic Republic of Congo | RoB 2 | Random assignment to a community-driven WASH intervention with an institutional-strengthening c… | null (health outcomes); positive (institutional-strengthening outcome) |
| S526 | United States | JBI Cross-Sectional | Utility ownership/governance type: investor-owned (private) water utility with rates set by a s… | negative (private ownership associated with less progressive/more regressive water pricing) |
| S539 | United States | JBI Cross-Sectional | Investor-owned (private) community water utility, with rates set via state Public Utility Commi… | positive (private ownership and pro-private regulation associated with higher price and lower affordability) |
| S749 | Brazil | JBI Cross-Sectional | Private (vs. public) ownership of a Brazilian water and sanitation business corporation -- a go… | positive (private ownership associated with HIGHER water tariffs, i.e. lower affordability, relative to public… |
| S631 | Indonesia | JBI Cross-Sectional | Creation of a new local government (kabupaten/kota) via pemekaran -- the legal/administrative s… | negative (local government proliferation associated with LOWER household water/sanitation access, relative to… |
| S947 | 44 African countries | ROBINS-I | Higher institutional/regulatory governance quality (World Bank Worldwide Governance Indicators… | positive (higher institutional/regulatory quality associated with greater water/sanitation access and smaller… |
| S1146 | multi-country (Africa, Afrob | ROBINS-I | Regional incidence of utilities-sector corruption (Afrobarometer round 7, multi-country Africa… | negative (higher regional utilities-sector corruption reduces likelihood of reported adequate household water… |
| S879 | Kenya | RoB 2 | Randomized assignment to systematic contract enforcement (transparent, credible service-disconn… | positive and significant for payment compliance; null (no significant effect) for water access, connection rat… |
| S1062 | multi-country (22 Sub-Sahara | ROBINS-I | Water-utility operation-and-maintenance (O&M) cost-recovery ratio (a financial/regulatory insti… | positive up to a threshold, then negative (curvilinear/inverted-U) |

**Sensitivity of these counts** (`05_analysis/sensitivity/SENSITIVITY_ANALYSIS_2026-09-28.md`): under every scenario tried — dropping abstract-only extractions, dropping the sparse-audit rows that carry effect sizes, dropping S589 (an unadjusted descriptive comparison in an ineligible-flagged study), collapsing linked reports, and dropping Family A's two coding judgment calls — the pre-stated conclusion tests for A, B and C hold; Family A's concordant share ranges 72.2–77.8%.

### 2A.4 What the qualitative, doctrinal and mixed-methods studies record

A large part of the evidence base (557 studies by design class, plus 349 with free-text design labels, mostly case studies) is qualitative, mixed-methods or documentary rather than quantitative. Using the draft mechanism vocabulary (`FAMILY_VOCABULARY_PROPOSAL_2026-09-28.md`, mechanical and unvalidated), studies whose label maps to a single mechanism family are: eligibility status documentation 157, discretion accommodation 137, institutional structure coordination 115, enforcement sanctions 80, fees tariffs subsidies 47, participation assistance 25, regulatory model ownership 24, procedural burden 18, review redress 4; 520 carry several. The mapping is mechanical and unvalidated, so read the counts as indicative only. Examples of qualitative or doctrinal studies with `mechanism_certainty` 2 or higher ("mechanism directly observed" or above), showing the study's own recorded mechanism label beside the draft family, and the AI-extracted finding text:

| Study | Country | Design | Own recorded mechanism label → draft family | Extracted finding (truncated) |
|---|---|---|---|---|
| S101 | Kenya | qualitative | DISCRETION_ACCOMMODATION → discretion accommodation | Formal water connection through Nairobi's piped grid does not equal reliable water access: neighborhood disparities exist even among neighbors with formally equivalent connections, because water rights are 'con… |
| S253 | United States | qualitative | ENFORCEMENT → enforcement sanctions | Community members and professionals engaged in environmental health literacy (EHL) efforts on Tribal lands face persistent challenges in skill-building, obtaining accessible information, and navigating the laye… |
| S305 | multi-country (Ecuador,  | qualitative | ELIGIBILITY → eligibility status documentation | Comparing successful (Ecuador 2008) and unsuccessful (Chile 2022) constitutional water-change processes, the article argues that where there is no agreement on either science or policy, politicization is requir… |
| S307 | multi-country | qualitative | BURDEN → procedural burden | The dominant perceived driver of subscriber attrition from container-based sanitation services was economic challenges faced by subscribers, and the most common mitigation strategy was developing individual rep… |

### 2A.5 Gaps visible in the records

- **Geographic:** the Netherlands (1 single-country study) and Canada (15) — two of the dissertation's three comparison jurisdictions — are barely represented against Brazil (87); 600 (52%) of studies sit in the ten commonest single countries.
- **Design:** 5 randomised trials (4 distinct) and 63 quasi-experimental studies against 447 (39%) studies appraised with the project's own non-validated framework (the residual category for designs no published instrument fits, including doctrinal and documentary studies).
- **Mechanisms/outcomes:** redress and review mechanisms and application-process outcomes are thinly coded (see 2A.2); sanitation access less than water.
- **Retrieval:** 1,383 title/abstract includes were never assessed. Their median publication year is 2014 versus 2018 for assessed records; 8.9% were published before 2000 versus 3.0%, and 30.9% in 2020 or later versus 42.7% — the unassessed set is older, so the corpus under-represents earlier literature.

## 2B. Tentative interpretations (not findings — each rests on the numbers cited and could be wrong)

1. **The literature documents co-occurrence far more than causation.** With 68 (6%) causal-capable designs (and a certainty-3–4 coding that does not line up with them, see §2A.1), the base can say that legal/administrative features and access outcomes are associated across many settings, but rarely that one causes the other. *Rests on:* §2A.1 counts. *Would change if:* the 1,383 unassessed records or future searches contain many more designs with credible identification.
2. **Recognition and formal status tend to go with better access (Family A), but the pattern is thin.** 15 of 20 concordant, 3 counter-pattern (S104 tenure and interruptions; S1020 a watershed programme and collection time; S1121 water-adequacy screening and permitting): S104 appraised with JBI Cross-Sectional; S1020 appraised with ROBINS-I; S1121 appraised with ROBINS-I. *Rests on:* the SWiM coding, a judgment by the same AI. Not a pooled estimate and not certainty-graded.
3. **Assistance and trust mechanisms look uniformly favourable (Family B) — but on six studies with six different mechanisms.** The consistency may reflect small numbers or reporting of positive findings; nothing here excludes either.
4. **Ownership and price: private ownership goes with worse affordability in the three studies (S526, S539, S749), but the two US samples probably overlap**, so this may be two independent samples, not three (`linked_reports_2026-09-28.csv` LR09, an audit inference).
5. **Most institutional analysis in this corpus is descriptive-qualitative and concentrated on fragmentation, discretion and fees.** This may reflect what the search and the closed retrieval surfaced (English-language, post-2010, database-indexed) as much as what the world contains.
6. **The dissertation's comparative frame (Netherlands, Canada, Brazil) cannot be tested from this base as it stands**: one Dutch and 15 Canadian single-country studies.

## 3. Confidence and limitations

### 3.1 Overall confidence: low to very low for any causal or comparative claim

This is the author's tentative characterisation, not a GRADE judgment (none has been made): the direction-of-association statements rest on a small quantitative subset (20, 6 and 20 studies), AI-extracted and AI-coded values, mostly observational designs, and a screening stage that closed early. Reasons follow.

### 3.2 Incomplete screening

- Full-text retrieval closed at 62.2%: 1,383 of 3,659 records (1,201 not retrievable, 182 wrong file delivered) were never assessed, and the unassessed set is systematically older (§2A.5). Some may be duplicates of included studies, some not eligible; the direction of any bias is unknown.
- 151 of the 1,117 full-text excludes are E10 (inaccessible text), i.e. never judged on content.
- Every full-text decision is the AI's; a human confirmed 200 includes (S001–S200) and no excludes; 73 decided rows carry no reviewer label. A prioritised queue for human review exists (`02_screening/full_text/REVIEWER_2_PRIORITY_QUEUE_README.md`).
- At title/abstract stage the human second pass covered the 3,665 include-plus-unsure records only; the 22,557 records the AI excluded were not human-checked, so any wrongly excluded record is invisible to this review. The 99.8% agreement on the reviewed set is unusually high and was flagged by the project itself. (`AI_USE_STATEMENT.md` and `AUDITING_GUIDE.md` say "all records"; that wording should be checked against the README, which is narrower.)

### 3.3 Missing or thin data

- 37 studies were extracted from abstract or metadata only (3.2%); none has an effect-size row, so the SWiM syntheses are unaffected by them, but descriptive counts and ratings include them. **That count is a floor:** it counts one note prefix, and a sparse-record audit (`05_analysis/descriptive/SPARSE_RECORD_AUDIT_2026-10-04.md`) found 80 more rows with at least one sign of shallow extraction — 12 whose own notes say only the abstract or citation was read and 21 whose recorded location cites the abstract alone (a verification queue, not proof) — of which 2 carry effect-size rows. There is no second extractor: extracted values have not been checked against the source papers.
- 55 of 140 JBI ratings are "High concern", which here means sparse extraction rather than a poor study. For CASP and MMAT, several items are "Can't tell" for every study (for example CASP item 3, research design justified) because extraction did not capture methodological reporting. Ratings are rule-based and unreviewed by a human.
- Of 62 effect-size rows, 7 give a confidence interval and 25 a standard error; estimates are as the papers report them and none is pooled.

### 3.4 Unresolved classifications — the two you asked about

**Are the AMSTAR 2 studies actually systematic reviews? Partly confirmed, partly not.**

- 23 studies carry AMSTAR 2; another 13 studies also had a secondary-review design class but were **reclassified to `NONE`** after an eligibility check found them to be self-described narrative, conceptual or documentary reviews that never claim a systematic search (S079, S320, S321, S322, S326, S429, S430, S436, S440, S466, S479, S480, S482; `RISK_OF_BIAS.md` §4; S326 joined them on 2026-09-29 after its full text, supplied by you, showed no stated search, selection or appraisal method). AMSTAR 2 was not applied to those, and the project has **no validated instrument for a non-systematic review used as an evidence source** — an acknowledged gap.
- Of the 23 that kept AMSTAR 2, each was classed as a secondary systematic review. The recorded fields (publication type, design, method text, sample) support that unevenly: 12 name a registration, PRISMA or JBI method, 19 state a count of included studies, and none is left with only one weak signal — a way to order full-text checks, not a finding (`05_analysis/descriptive/DATA_QUALITY_AUDIT_2026-09-29.md` §3). None of them is now extracted from abstract or metadata only; S319, S324, S325 and S344 were read in full text on 2026-10-02 (S324 is a registered, well-reported review; S319 searched one database; S325 and S344 are single-author reviews with weak methods, but all four state a search, a selection process and a synthesis, so all keep AMSTAR 2); S329 is described as a "narrative review with systematic search" and S418 as a narrative/scoping review with a documented search (hybrids kept eligible with a noted caveat); S326, first flagged as an "evidence survey", was moved to `NONE` once its full text was read; S418, S438, S697, S052 and S327 were read in full text on 2026-10-03 (S697, a meta-analysis, and S438, S052 and S327 all state a search, selection and synthesis, so all keep AMSTAR 2).
- **Only 12 of the 23 received a formal AMSTAR 2 confidence rating** (S052 Critically Low, S319 Critically Low, S324 Critically Low, S325 Critically Low, S327 Low, S328 Critically Low, S344 Critically Low, S370 Critically Low, S372 Critically Low, S418 Critically Low, S438 Critically Low, S697 Critically Low; 11 of the 12 are Critically Low; the others are S327 Low, mostly because of missing protocols, single-database searches, no list of excluded studies or no appraisal of the included studies); the other 11 are "Not ratable" because their extraction lacks the information for the critical items. **So AMSTAR 2 so far tells the reader little beyond "low confidence"; the 11 unrated reviews need their full texts.**
- *Tentative flag (this report's own observation, not a project ruling):* AMSTAR 2 was designed for reviews of healthcare interventions that include randomised or non-randomised studies; several of these reviews are realist, scoping or mapping reviews of qualitative and policy literature, for which a rating would be out-of-design even with full information. A decision on whether to keep AMSTAR 2 for these, or use a different instrument, is open.
- Reviews are secondary evidence and are never pooled as if primary. Whether their primary studies are also separate rows in this corpus was checked on 2026-10-04 for only 7 of the 23 reviews (those whose PDFs were to hand): their reference lists cite 48 distinct corpus studies, S319 (21), S325 (19) cite ten or more. This is an upper bound (background citations count) and does not read the included-studies tables, so the real double-counting risk is **still unresolved**, and 16 reviews are unchecked (`05_analysis/descriptive/AMSTAR2_OVERLAP_CHECK_2026-10-04.md`).

**Do the randomised trials need the cluster version of RoB 2? Yes for all five — one unit is inferred, and S366 has now been re-read in full.**

- All 5 RoB 2 studies (S057, S085, S294, S366, S879) were checked and are **cluster-randomised**, not individually randomised, and were appraised with the cluster-trial variant (`04_quality/appraisal_forms/`). Four state cluster randomisation in their own extracted design field.
- **S879** (Kenya) records only "randomized controlled trial"; cluster randomisation at compound level is *inferred* from the recorded unit of intervention and flagged "verify against source paper before finalizing rating" in its own tool field. Its rating is provisional.
- **S366** was re-extracted and re-appraised on 2026-09-29 from the full-text PDF you supplied (its earlier abstract-only, low-confidence rating is superseded): Domains 1 and 3 Low, Domains 2 and 5 Some concerns, Domain 4 Some concerns for the primary outcomes and High for the self-reported satisfaction/behaviour indices; Figure 1 and the supplement were not read. S366 and S294 report the same DRC cluster trial, so the 5 RoB 2 studies are **4 distinct trials** (but different surveys: 1,312 households in S366, 3,283 in S294). All five rate "Some concerns" overall; S057, S085, S294 and S879 still use many "No information" answers because extraction did not capture trial-conduct details.
- A keyword scan of design fields in the other 1,154 studies found no further randomised design under another tool. **S189** is a process evaluation conducted "in connection with a randomised controlled trial" (Orissa, India); it was appraised with ROBINS-I as a quasi-experimental study, and its full appraisal form covers the confounding domain only. Whether the parent trial itself is in the corpus, and whether any of its outcomes belong under RoB 2 cluster, is worth confirming. (The scan covered design and measure fields only, not full texts.)

### 3.5 Other unresolved items that may matter

- **S589** is in Family A but its row is an unadjusted descriptive comparison for a study not flagged eligible; Family A results are shown with and without it. Decision pending (`DECISIONS_AND_OPEN_ITEMS.md` A1).
- **Linked reports:** the 1,159 rows are about 1,157 distinct studies (S294/S366 one trial; S097/S098 one sample) and 1,155 counting partial overlaps.
- **Free-text classifications:** `mechanism_family` (236 distinct labels) and `outcome_family` (127) are uncontrolled; 349 studies have a design class outside the documented enum; a draft vocabulary is proposed, not adopted. Country and legal-system fields are free text, so the geographic counts here are rule-based.
- **Direction coding** in the SWiM documents is a judgment by the same AI; sign and valence differ for several studies.
- **The "quantitative-synthesis-eligible" flag looks generous.** Of 247 studies flagged, 113 show nothing inferential in their extraction (descriptive or unclear), 27 name an inferential model but hold no interval, SE or p-value, and 107 carry some uncertainty information (heuristic; `05_analysis/descriptive/quantitative_flag_audit_2026-09-29.csv`). Only 62 studies have an effect-size row and none is pooled, so no synthesis result depends on the flag. No flag was changed.
- **Consistency scan of the effect-size rows** found 1 new item(s) besides the known S589 row (S312 adjusted_blank); but an interval could be checked for only 5 of 62 rows, so this is weak assurance.
- **Same-paper duplicates** with different-language titles and blank DOIs were found and merged among included studies; the DOI/title audits cannot detect this class in the wider pool.

## 4. Most useful next steps (in order)

1. **Human check of the AI's screening**: work `full_text_reviewer_2_priority_queue_2026-09-28.csv` (tier 1: the 73 no-reviewer rows; tier 2: a stratified sample of excludes). It bounds the risk that eligible studies were excluded or ineligible ones included.
2. **Obtain the full text of the abstract-only studies that carry the most weight**: (S366, the RoB 2 study, was re-extracted 2026-09-29; the four abstract-only AMSTAR 2 reviews on 2026-10-02), the 11 AMSTAR 2 reviews still unrated (start with the weakest-evidenced in the audit, `DATA_QUALITY_AUDIT_2026-09-29.md` §3), then the 37 remaining abstract-only studies and the 12 further strong candidates from the sparse-record audit; re-extract (`03_extraction/extracted_data/abstract_only_fulltext_request_list_2026-09-29.csv`, `05_analysis/descriptive/sparse_record_audit_2026-10-04.csv`).
3. **Verify S879's randomisation unit against the paper** and confirm S189's parent-trial handling; then finalise or revise the RoB 2 cluster ratings.
4. **Decide the AMSTAR 2 question**: keep it (and obtain full texts so the 11 "Not ratable" reviews can be rated) or replace it for realist/scoping/mapping reviews; decide how to handle the non-systematic reviews now labelled `NONE`. Finish the check of whether these reviews' primary studies are also in the corpus (so far 7 of 23 reviews, reference lists only).
5. **Second-extract the prepared sample** (60 studies from S001–S200, `03_extraction/second_extractor/`) against the source papers to estimate extraction error; the sample cannot speak for later extractions, so a second sample from S201 onward is needed before any whole-corpus claim.
6. **Resolve S589, linked reports and the family vocabulary**, then re-run `sensitivity_analysis.py`.
7. **Reduce the retrieval bias**: prioritise the older, unassessed records (or state the limitation prominently), and consider targeted searches for Dutch and Canadian evidence if the comparative frame is to be tested.
8. **Only then** decide whether any family could support a restricted meta-analysis (`ANALYSIS_PLAN.md` §2); at present none does.

---
*Provenance: `00_admin/CURRENT_FIGURES.md`, `05_analysis/sensitivity/SENSITIVITY_ANALYSIS_2026-09-28.md`, `05_analysis/descriptive/FAMILY_VOCABULARY_PROPOSAL_2026-09-28.md`, `04_quality/risk_of_bias/2026-09-28_evidence_limitations.md`, `00_admin/audits/2026-09-28_repository_audit.md`. Regenerate with `python3 code/analysis/build_preliminary_report.py`.*
