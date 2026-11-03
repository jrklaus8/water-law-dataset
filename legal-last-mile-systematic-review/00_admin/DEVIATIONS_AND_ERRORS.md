# Deviations from the protocol, and errors the project found in itself

*Rendered by `code/analysis/build_deviation_error_registers.py` from `DEVIATIONS_REGISTER.csv` and `ERRORS_FOUND_REGISTER.csv`, which are the data (edit those, not this page). The AI drafted both from the repository's own records (the registration draft, the 2026-09-28 audit, the changelog and the decisions log); the researcher has not yet confirmed every entry.*

## Departures from the protocol

19 dated departures, clarifications and added checks. **4 were decided after the results they could affect were visible and 2 partly so** (column "after seeing results"): those are the ones to look at hardest, because eligibility or grouping decisions made with the effect rows in view can shift a result even when made in good faith. The protocol itself was fixed in writing on 2026-08-22 (commit `d591062`), before any database was searched; the research question, the eligibility wording, the codebook fields and the synthesis decision tree were not rewritten.

| ID | Date | Stage | Departure | Kind | After seeing results | Effect on the evidence base |
|---|---|---|---|---|---|---|
| D01 | 2026-09-11 | Search | Search closed before all planned databases were searched or exported | Execution decision (a gap) | no | 34,594 raw records; 27,481 after de-duplication; the gap must be reported (SEARCH_PROTOCOL.md section 7) |
| D02 | 2026-09-12 | Title/abstract screening | Human second reviewer on the include-or-unsure records only, not on the AI exclusions | Departure from the plan | no | 3,659 records advanced to full text; the AI exclusions were not human-checked |
| D03 | 2026-09-28 | Extraction | Separate pilot extraction replaced by extracting every full-text include directly | Departure from the plan | no | No formal pilot-disagreement check was run |
| D04 | 2026-09-28 | Full-text retrieval | Retrieval closed with part of the candidates never assessed | Execution decision (a gap) | no | 2,277 of 3,659 records assessed |
| D05 | 2026-09-28 | Risk of bias | Rule-based batch ratings instead of a signalling-question appraisal of each paper | Departure in depth of method | no | Ratings describe the extraction as much as the paper |
| D06 | 2026-09-28 | Title | Title amended to "AI-Assisted Systematic Review" | Amendment (title only) | no | None |
| D07 | 2026-09-28 | Synthesis | Phase 11 decision tree applied: no family clears the bar for meta-analysis | Pre-specified branch taken | no | Nothing pooled; no pooled claim made |
| D08 | 2026-10-03 | Full-text screening | Blind second-model re-screen added (Codex and Gemini) | Added check (AI versus AI) | no | About half of a stratified sample of AI exclusions read as include by the second models, which led to the scope question (D09) |
| D09 | 2026-10-13 | Eligibility | Criterion 2 read narrowly: a legal or administrative access rule or mechanism (A16 ruling) | Post-hoc interpretive clarification | partly | A16, A22, A24 and A25 passes: 3 excludes reversed to includes and 83 includes reversed to excludes (mostly E03 and E05); two never-assessed records added as includes |
| D10 | 2026-10-14 | Eligibility | Consistency rulings under criteria 3 and 4 (A24, A25, A20 residue) | Post-hoc application of the original criteria | partly | See CHANGELOG.md 2026-10-13 and 14 |
| D11 | 2026-10-14 | Eligibility | Results never decide eligibility (A18) | Post-hoc clarification | no | One exclusion re-coded, one reversed |
| D12 | 2026-10-14 | Synthesis | Families A, B and C retitled as thematic mechanism groupings for vote counting (A21) | Clarification | yes | Headings only |
| D13 | 2026-10-14 | Classification | Controlled vocabularies adopted for mechanism_family, outcome_family and study_design_class (A5, A10) | Post-hoc classification, keyword-based and unvalidated | no | Descriptive tables only |
| D14 | 2026-10-14 | Counting | Linked companion reports kept as separate rows (A3); the SWiM sensitivity analysis made a standing requirement (A4) | Counting convention; added requirement | no | 1,072 reports are 1,070 distinct studies on the definite links |
| D15 | 2026-10-14 | Synthesis | A26 rulings: S358, S590, S606 moved to the reasoned non-fits; S1121 and S1143 excluded; S1038 exposure and comparator corrected | Post-hoc ruling after a scope check of the effect rows | yes | Family A 18 to 16; Family C 20 to 17; included reports 1,080 to 1,078 |
| D16 | 2026-10-14 | Synthesis | A29: S1140 (Family B) and S1136 (Family C) moved to the reasoned non-fits | Post-hoc ruling after the A26 scope check | yes | Family B 6 to 5; Family C 17 to 16 |
| D17 | 2026-10-14 | Synthesis | A28: six synthesis studies excluded (S1020, S1042, S1057, S1144, S1163, S947), four kept, the DRC trial row moved from S294 to S366; A31 relabelled 18 AI-checked confirmations | Post-hoc rulings on the narrow reading | yes | Family A 16 to 13, B 5 to 3, C 16 to 15; 31 studies in the three families; included reports 1,078 to 1,072 |
| D18 | 2026-10-14 | Classification | mechanism_certainty normalised to the design-driven scale of the codebook (A27) | Post-hoc recoding; originals preserved | no | Descriptive tables only |
| D19 | 2026-10-14 | Registration | Protocol not registered before the work; a retrospective OSF registration prepared and not submitted | Execution gap | not applicable | No external timestamp for the protocol |

The plan, what was done, the recorded reason, who decided and where it is documented are in `DEVIATIONS_REGISTER.csv`. "After seeing results" is the AI's reading of the dated records.

## Errors the project found in itself

29 errors, by how they were found. Most were found by the project's own audits and corrected in the open; **3 are still open or only fixed on an unmerged branch**. The register is a measure of how much checking was done, not a claim that these are all the errors: assume more exist.

| ID | Found | How | Stage | Error | Introduced by | Effect | Status |
|---|---|---|---|---|---|---|---|
| E01 | 2026-09-11 | caught during processing | Title/abstract screening | Screening 19,085 records as 39 parallel batches sharing one output directory lost or overwrote rows (file collisions) | AI orchestration | None after the rebuild | fixed |
| E02 | 2026-09-12 | QA spot-check | Title/abstract screening | One stored AI rationale and exclusion code belonged to a different, unrelated paper (an oncology study instead of a wastewater-reuse study), misassigned in the same merge; the exclude decision itself was correct | AI orchestration | None on the decision; the code E01 corrected to E07 | fixed |
| E03 | 2026-09-16 | post-hoc duplicate audit | Search | Two papers carried two record IDs each (S227 and S399) | DOI formatting variants | Would have counted the papers twice | fixed |
| E04 | 2026-09-27 | matching studies to reviewer confirmations | Search | A further paper carried two record IDs (S063) | DOI variants or re-indexing | Would have counted the paper twice | fixed |
| E05 | 2026-09-28 | repository audit (finding 1) | Documentation | The tool-distribution table and several derived figures were wrong in three documents | AI | Wrong descriptive figures | fixed |
| E06 | 2026-09-28 | repository audit (finding 2) | Documentation | "1,154 studies with an applicable tool, 8 NONE" was wrong: it was 1,150 and 12 | AI | Wrong descriptive figures | fixed |
| E07 | 2026-09-28 | repository audit (finding 3) | Synthesis | The Family A synthesis conflated the sign of an estimate with its valence: "18 of 20 (90%)" was really 15 of 20 (75%) | AI | Overstated the Family A favourable share by 15 percentage points | fixed |
| E08 | 2026-09-28 | repository audit (finding 4) | Classification | 22 study_design_class values were stale after later risk-of-bias tool reassignments | AI | Wrong design labels in descriptive tables | fixed |
| E09 | 2026-09-28 | repository audit (finding 5) | Synthesis | S589 had an effect-size row although its study was not flagged quantitative-synthesis-eligible (an unadjusted descriptive comparison) | AI | Family A included one ineligible row | fixed |
| E10 | 2026-09-28 | repository audit (finding 6) | Documentation | Re-mining arithmetic ("61 + 187 = 248") and the "62 rows from 248 studies" wording were inaccurate | AI | Wrong counts in text | fixed |
| E11 | 2026-09-28 | repository audit (finding 7) | Extraction | 71 studies had been extracted from an abstract or metadata only with no corpus-level disclosure | AI | Readers could not tell how thin some extractions were | disclosed |
| E12 | 2026-09-28 | repository audit (finding 8) | Risk of bias | 59 of 140 JBI ratings were "High concern", which meant sparse extraction rather than poor conduct, and the narrative did not say so | AI | Could be read as poor-quality studies | disclosed |
| E13 | 2026-09-28 | repository audit (finding 9) | Provenance | 74 decided full-text rows had a blank reviewer_1 and reviewer labels were inconsistent | AI | Provenance gap | mitigated |
| E14 | 2026-09-28 | repository audit (finding 10) | Provenance | 13 decided full-text rows carried a stale full_text_status; S356 was an include decided without a recorded reviewer or full text | AI | Status columns contradicted decisions | fixed |
| E15 | 2026-09-28 | repository audit (finding 11) | Provenance | The one-off scripts cited by the changelog existed only in an ephemeral scratchpad | AI | Earliest decisions cannot be traced to a script | disclosed |
| E16 | 2026-09-28 | repository audit (finding 12) | Documentation | Three preliminary_* outputs described a 509-study snapshot with no superseded banner | AI | Could be mistaken for current results | fixed |
| E17 | 2026-09-28 | repository audit (finding 13) | Search | Two papers were double-counted among the included studies (S233/S1008 and S299/S392); an earlier audit had concluded there was no live double counting | AI | Inflated the included count by two | fixed |
| E18 | 2026-09-28 | repository audit (finding 14) | Extraction | Extraction is per report: four pairs share underlying data and no machine-readable links existed ("5 RoB 2 studies" are 4 trials) | AI | Reports counted as independent studies | mitigated |
| E19 | 2026-09-28 | repository audit (finding 15) | Synthesis | The Family C text said the ownership cluster spans three countries and three independent studies; it is two countries, and S526 and S539 probably share data | AI | Overstated independence of the Family C ownership pattern | fixed |
| E20 | 2026-09-28 | repository audit (finding 16) | Provenance | No study-to-record index existed | AI | Studies could not be traced to screening records without searching | fixed |
| E21 | 2026-10-14 | codebook consistency check | Classification | mechanism_certainty held narrative sentences in 567 rows and a level 3 or 4 on 22 rows of designs that cannot hold it | AI | Certainty levels did not follow the codebook scale | fixed |
| E22 | 2026-10-14 | PDF read for the scope check (A26) | Synthesis | S1038's exposure and comparator were not the contrast the paper reports | AI | A wrong comparison in the effect table | fixed |
| E23 | 2026-10-14 | researcher review (A31) | Verification | Eighteen synthesis studies had been recorded as human (CK) confirmations although the confirmation rested on the AI's own scope and outcome check | AI | The human-verified count would have been overstated by 18 | fixed |
| E24 | 2026-10-14 | PDF read for the dossier | Extraction | Stored numbers not printed in the papers: S037 sample size (a derived sum of 153), S470 robustness estimate (13.5 percentage points; the paper prints 0.1345, 0.1348 and 0.1313 on a 0 to 1 scale), S593 standard error (upper bound 0.6 not printed) | AI | Three stored values differ from the published ones | open |
| E25 | 2026-10-27 | document sweep while writing the reader's guides | Documentation | Eight current-status documents still quoted counts from before the 2026-10-14 scope rulings (release note, registration draft, PRISMA flow, PRISMA workflow, data dictionary, the A6 row of the decisions log, the auditing guide; the analysis plan annotated) | AI | Documents disagreed with the databases (for example 1,078 or 1,159 included, 467 human-verified) | fixed |
| E26 | 2026-10-27 | document sweep | Documentation | CITATION.cff said 1,080 included reports (1,078 distinct); the current figures are 1,072 and 1,070 | AI | A wrong figure in the citation metadata | fixed |
| E27 | 2026-10-27 | arithmetic check against the audit's own reconciliation table | Validation | The v0.2.x other_water residual was stated as 74,607 decisions (89.2%) in the audit, validation README, dashboard banners and supervisor memo; the reconciliation table gives 57,695 (69.0%) and the other figures are v0.3.0 totals | AI | A misstated baseline in a public dashboard and in a memo addressed to the supervisor | fixed on a branch; merge pending |
| E28 | 2026-10-27 | attempt to reproduce the audit's figures | Validation | The sensitivity kappa figures (0.832, 0.932, 0.821) reported in the audit had no code or stored output; the documented intervals differ slightly from a reproducible bootstrap (for example 0.718 versus 0.721); the audit said all 19 UNCERTAIN/WATER disagreements were Brazilian, but 17 are and 2 are Dutch | AI | Unreproducible figures and one wrong count in the validation write-up | fixed on a branch; merge pending |
| E29 | 2026-10-27 | git timestamp check | Synthesis | The conclusion tests were described as "fixed before the numbers were computed", but the family syntheses were committed about 12 hours before the script that states the tests | AI | Overstated the independence of the tests from the baseline result | fixed |

The fix and where each is documented are in `ERRORS_FOUND_REGISTER.csv`.

## Reading these together with the other registers

- Weaknesses that remain (and how to test them): `WEAKNESSES.md`.
- What the AI did and what is not archived: `AI_USE_LEDGER.md`.
- What a human has checked for each study: `STUDY_AUDIT_TRAIL.csv`.
