# PRISMA Workflow

Reporting follows PRISMA 2020 (`SOURCES.md`), applicable to systematic
reviews with or without meta-analysis and usable beyond conventional health
intervention questions. PRISMA is a reporting guideline, not a complete
conduct manual — the conduct steps below are this project's own procedure.

## 16-phase workflow

| Phase | Task | Status |
|---|---|---|
| 1 | Develop protocol | **Done** — `PROTOCOL.md` |
| 2 | Preregister (OSF Generalized Systematic Review — see `PROTOCOL.md` §11) | Draft ready — `00_admin/preregistration/osf_preregistration_draft.md`; not yet submitted (no OSF account access from this environment) |
| 3 | Database searching | **Closed 2026-09-11, by researcher decision — candidate pool already large enough to move to screening.** This environment still cannot reach any database directly (confirmed 2026-08-25); all searching was done by the researcher via EUR institutional access, largely relayed through Claude Cowork. Databases actually searched: Scopus (18/18 planned batches), Web of Science (`SEARCH_035`, 4,058 records), HeinOnline (`SEARCH_036`–`SEARCH_038`, minimal real yield — see below), ProQuest (`SEARCH_039`, 7,728 records via a full account-based export) and ProQuest/Sociological Abstracts (`SEARCH_040`, 16,736 records), and JSTOR (`SEARCH_041`, 356 identified, only a partial export ever produced). **SSRN and Westlaw/Lexis were never searched at all** — the phase was closed before either was reached; documented as an intentional gap in `SEARCH_PROTOCOL.md` §7 and `search_log.csv`'s `SEARCH_042`/`SEARCH_043` stub rows, to be reported honestly in any manuscript output rather than omitted. HeinOnline's real yield was small and mostly lost to file-delivery failures: `SEARCH_036` found 71,226 hits with no bulk-export mechanism at that volume (count-only, 0 ingested); `SEARCH_037` yielded 1 ingested record; `SEARCH_038`'s 3 records and most of `SEARCH_041`'s JSTOR batch were reported by Cowork but the export files themselves never reached this pipeline, and recovery was abandoned when the search phase closed. Three earlier rounds of a non-systematic, low-recall **exploratory pilot** were also run via Claude's `WebSearch` tool (`SEARCH_003`–`SEARCH_017`, 2026-08-25, 37 candidate records) — see `SEARCH_PROTOCOL.md` §7; that part never counted toward Phase 3. |
| 4 | Deduplication | **Complete for the closed search phase.** `code/search/deduplicate.py` (DOI-match + title/year-similarity match, full merge log for auditability) has processed **27,481 unique records** across the WebSearch pilot, the `SOURCES.md` exemplars, all 18 Scopus exports, Web of Science, HeinOnline, ProQuest, ProQuest/Sociological Abstracts, and JSTOR — **7,113 duplicates merged** in total (heavy Scopus/WoS/ProQuest cross-database journal overlap, exactly as expected). `record_id` is a stable content hash (DOI, or title+year) rather than positional. A schema-validation script (`code/analysis/validate_schemas.py`) checks every project CSV's header against its documented/generated schema — currently all consistent (11 files). Validated adapters: Scopus, Web of Science (`wos_adapter.py` — found and fixed two real bugs, including a data-corrupting quote-escaping issue), and the shared RIS adapter (`ris_adapter.py`, validated against real HeinOnline/ProQuest/Sociological Abstracts/JSTOR exports this round — also found and fixed a genuine bug: ProQuest conference-abstract-supplement records can carry a single abstract field past Python's default csv module field-size limit, now raised in every downstream script). Deliberately not covered: Westlaw/Lexis (never searched, no standard bulk export to build against) and CanLII/Rechtspraak.nl/Brazilian court portals/ANA-SNIS (feed the doctrinal/jurimetric strand, not this pipeline — see each `database_strategies/*.md`). |
| 5 | Title and abstract screening (two reviewers where feasible) | **Real first-pass screening done on the entire closed-search-phase pool, by one AI reviewer.** `02_screening/title_abstract/screening_database.csv` has **27,481 total records, 26,222 of which have a real abstract**; all 26,222 have now been screened against `INCLUSION_EXCLUSION.md` by Claude as `reviewer_1` (`Claude-AI-1stpass-2026-09-10` and `-09-11`), explicitly authorized by the researcher as a methodological choice per `PROJECT_SPEC.md` §14.18 — **3,062 include / 22,557 exclude / 603 unsure**. The 2026-09-11 ProQuest/Sociological Abstracts round (19,085 newly-screened records) came in with a much lower include+unsure rate (~9%) than the earlier Scopus/WoS rounds (~25-30%), driven by real search-strategy noise (broad `noft()` full-text-adjacent matching, thesaurus-term pulls into unrelated sociology-of-bureaucracy literature) rather than a screening quality issue — see `search_log.csv` and `REVIEWER_2_README.md`. This round was run as 39 parallel ~500-record batches, each isolated to its own scratch directory after an earlier flat-shared-directory attempt suffered real cross-agent file corruption (caught via record-for-record validation, not assumed clean — see `CHANGELOG.md`); every batch was independently verified against its source file before merging. **`reviewer_2` (human) pass completed 2026-09-12** via a purpose-built Excel
worksheet handoff (all 3,665 include+unsure records, one-click Yes/blank
decision column) — see `REVIEWER_2_README.md`. Result: 3,659 `include` /
6 `exclude`, **zero recorded conflicts** by the strict definition in
`DATA_DICTIONARY.md` (reviewer_1 `include` vs. reviewer_2 `exclude`) — all
6 reviewer_2 excludes were resolutions of reviewer_1 `unsure` records, not
disagreements with a firm reviewer_1 decision. **Worth flagging plainly**:
a 99.8% agreement rate between two independent reviewers is far higher
than PRISMA second-pass screening typically produces, and the full
worksheet came back in far less time than reading ~3,700 abstracts
individually would take. This was raised directly with the researcher
before merging (not merged silently) — the researcher confirmed proceeding
with the file as delivered. `final_decision` is populated for all 3,665
records on this basis; treat this as the recorded second-reviewer pass,
with the caveat above on the record for anyone assessing this review's
rigor. **`exclude_spotcheck_sample.csv` (120-record random QA sample,
fixed seed) has now been manually reviewed (2026-09-12)** — 119 of 120
exclusions checked out as correctly reasoned; 1 (`R88194172BEF6`, a
Sicilian wastewater-reservoir bacterial-removal modeling study for
agricultural irrigation reuse) had a stored `ai_rationale` that did not
match its actual title/abstract (it read "Oncology biomarker study;
unrelated to water/sanitation," evidently misaligned during the
39-parallel-batch merge) and an inaccurate `exclusion_reason` (`E01`
instead of `E07`, since the actual content is an irrigation/agricultural
water-reuse study, not an unrelated topic). The `exclude` decision itself
was still correct — corrected the code and rationale in both
`screening_database.csv` and `exclude_spotcheck_sample.csv`, and updated
the title/abstract exclusion-reason breakdown in `prisma_flow.md`
accordingly (E01: 16,667→16,666; E07: 1,039→1,040). No other discrepancy
was found in the 120-record sample. **Follow-up (2026-09-12): scanned the
entire 22,557-record exclude pool's `ai_rationale` text for the same
mismatch signature** (a rationale citing a domain wholly foreign to
water/sanitation/legal-administrative research), rather than relying on
another random sample — 74 records matched; a diverse 18-record manual
check against actual titles/abstracts confirmed all 74 are genuine
off-topic records correctly excluded (e.g., 8 near-duplicate stock-market
newsletter records for ticker "SJW"/South Jersey Industries), not further
instances of the corruption. See `CHANGELOG.md` (cont. 12) for the full
method and result. The 1,259 records without a real abstract were
deliberately left undecided (title-only triage remains
non-binding per `title_only_triage_memo.md`, still only covering the
original 37). |
| 6 | Full-text screening, standardized exclusion reason per record | **In progress, live.** `02_screening/full_text/full_text_screening_database.csv` holds all **3,659** Phase-5 includes. The researcher supplies full-text PDFs via chat upload on a rolling basis (expected to continue for over a month); each is converted (`pdftotext -layout`), screened by Claude as `reviewer_1` (`Claude-AI-fulltext-2026-09-12`/`-09-13`) against `INCLUSION_EXCLUSION.md`'s E01–E12 codes, recorded via `code/screening/update_full_text_record.py`, and any exclusion is also logged to `02_screening/exclusion_log/exclusion_log.csv`. As of this update: **1,091 of 3,659 records decided (538 include / 553 exclude)**; exclusion-reason breakdown so far: E01 (wrong topic) 171, E02 (wrong population) 33, E03 (wrong exposure) 21, E04 (wrong outcome) 50, E05 (no empirical evidence) 56, E06 (engineering only) 41, E07 (wrong service) 20, E08 (duplicate) 6, E09 (insufficient information) 2, E10 (inaccessible full text) 151, E12 (wrong study design) 2. `reviewer_2` (human) has not yet been assigned for this phase — open question for the researcher, but the handoff tooling is now ready: `code/screening/build_full_text_reviewer2_queue.py` generates `02_screening/full_text/full_text_reviewer_2_queue.csv` from every decided-but-unconfirmed record, mirroring the title/abstract stage's queue — see `02_screening/full_text/REVIEWER_2_README.md`. Retrieval remains researcher-driven (institutional/personal access); this environment has no outbound access to fetch full texts itself. |
| 7 | Pilot extraction (~10 studies) | **Superseded by full extraction (Phase 8) proceeding directly** — the researcher explicitly authorized starting extraction on all full-text includes as they clear Phase 6, rather than waiting to draw a separate ~10-study pilot subsample first (`CHANGELOG.md`). `EXTRACTION_FORM.md` and `CODEBOOK.md` are being applied directly per Phase 8 below. `select_pilot_sample.py` and `PILOT_EXTRACTION.md` remain available if a formal pilot-disagreement check is wanted later. |
| 8 | Full extraction | **Fully caught up with Phase 6 — no outstanding gap.** `03_extraction/extracted_data/extraction_database.csv` holds **538 fully-extracted studies (S001–S540, with S227 and S399 documented post-hoc-duplicate gaps — see CHANGELOG.md)**, all 92 `CODEBOOK.md` fields populated per study, matching all **538** current full-text includes. Every new full-text include is extracted in the same session it clears Phase 6, rather than accumulating in a backlog. `reviewer_1` for S001-S085 is `Claude-AI-fulltext-2026-09-12`; for S086-S092 it is `Claude-AI-extraction-2026-09-13`; for S093-S140 it is `Claude-AI-extraction-2026-09-15`; for S352-S400 it is `Claude-AI-extraction-2026-09-16`; for S401-S467 it is `Claude-AI-extraction-2026-09-17`; for S468-S524 it is `Claude-AI-extraction-2026-09-18`; for S525-S530 it is `Claude-AI-extraction-2026-09-19/21`; `reviewer_2`/`final_decision` are blank pending a second extraction pass (see Phase 9 note on the same open reviewer_2 question). Nineteen of the 420 pre-2026-09-17-batch-3 studies (S015, S019, S027, S052, S079, S116, S319–S329, S370, S372) plus S418 (Brown et al. 2023, Lancet Global Health) are themselves secondary/systematic reviews, all flagged `study_design_class = systematic_review_secondary`, never to be pooled as an independent primary effect (S344 and S350 are qualitative studies with CASP as their tool, not secondary reviews, despite an earlier summary conflating them with this group — see `evidence_map.csv`). S356, S364, and S376 are also documentary/policy/regulatory-audit studies appraised with the project's own Legal Institutional Evidence Appraisal Framework rather than AMSTAR 2, since none documents a formal systematic-review search methodology in the sense `RISK_OF_BIAS.md` reserves AMSTAR 2 for (S376's `study_design_class` was resolved by hand as `jurimetric`, a real judgment call the build script cannot make mechanically). The 2026-09-17 Google Drive batch 3 (S423–S467) added 7 further systematic/narrative-review-type studies flagged AMSTAR 2 (S427, S429, S430, S436, S438, S440, S466), all likewise unappraised for `risk_of_bias_rating` pending Phase 9. A further researcher-chat-uploaded systematic review, S475 (Murebwayire et al. 2025, Kigali FSM), was added 2026-09-18, also flagged AMSTAR 2 and likewise unappraised. S476 (Khan & Fenner 2024, Goalmari Bangladesh) is JBI-flagged (observational); S477 (Ouma, Njoroge & Weru, in Di Giovanni & Bercovich eds. 2025, Mukuru Nairobi SPA) is CASP-flagged (qualitative). S479 (Dobbin et al. 2024, Southwestern US unregulated water users) is a further AMSTAR2-flagged narrative review. S480 (Maxcy-Brown et al. 2024, Alabama Black Belt) is also AMSTAR2-flagged. S481 (Machado et al. 2023, Brazil rural CMWS) is MMAT-flagged (mixed-methods Delphi expert panel). S482 (Meehan et al. 2023, homelessness dwelling paradox) is AMSTAR2-flagged (conceptual synthesis). S483 (Mutono et al. 2022, Nairobi water distribution) is ROBINS-I-flagged. S484 (Monyai et al. 2022, South Africa water governance) and S485 (Dektar et al. 2022, Karamoja Uganda private operators) are CASP-flagged (qualitative case studies). S486 (Calderón-Villarreal et al. 2022, Tijuana River homeless deportees) is MMAT-flagged. S487 (Kusi-Appiah & Mkandawire 2022, Malawi urban poor) and S488 (Ahabwe et al. 2022, Uganda HRWS/LNOB) are also CASP-flagged. S489 (Koehler et al. 2021, Kwale Kenya institutional pluralism) is JBI-flagged (observational). S490 (Aliyev 2021, Tajikistan WUA resilience) is MMAT-flagged. S491 (Sempewo et al. 2021, Uganda COVID-19 water WTP) is JBI-flagged (observational). S492 (Millington & Scheba 2020, Cape Town Day Zero) is CASP-flagged (qualitative). S493 (Giner & Pavon 2021, Texas colonias wastewater) is MMAT-flagged (mixed-methods). S494 (Rahmasary et al. 2021, Bandung governance) is MMAT-flagged. S495 (Samuel et al. 2021, Nigeria local WSS governance) is MMAT-flagged. S496 (Komakech et al. 2020, Tanzania prepaid water technologies) is MMAT-flagged. S497 (Shah & Badiger 2020, Darjeeling institutional economics) is CASP-flagged. S498 (Shrestha, Joshi & Roth 2020, Kathmandu Dalit exclusion) is CASP-flagged. S499 (Ekane et al. 2020, Rwanda/Uganda sanitation policy) is CASP-flagged. S500 (Mitlin & Walnycki 2020, 4-city African water informality) is MMAT-flagged. S501 (Sharma et al. 2020, Singtam/Kalimpong Himalaya) is MMAT-flagged. S502 (Chidambaram 2020, Delhi slum collective action) is CASP-flagged. S503 (Fischer et al. 2020, Bangladesh unregulated tubewell self-supply) is MMAT-flagged. S504 (Enqvist & Ziervogel 2019, Cape Town governance/justice overview) uses the Legal Institutional Evidence Appraisal Framework. S505 (Adank et al. 2019, Ethiopia small town sustainability checks) is MMAT-flagged. S506 (Hoque et al. 2019, coastal Bangladesh social-ecological analysis) is MMAT-flagged. S507 (Appiah-Effah et al. 2019, Ghana sanitation overview) uses the Legal Institutional Evidence Appraisal Framework. S508 (Domínguez Serrano & Castillo Pérez 2018, Veracruz community water organizations) is CASP-flagged. S509 (Akwataghibe et al. 2018, SHAWN WASH equity programme Nigeria) is MMAT-flagged. S510 (Adams & Smiley 2018, Malawi urban-rural water access inequalities) is MMAT-flagged. S511 (Poupeau & Hardy 2017, La Paz/El Alto Bolivia water cooperatives) is MMAT-flagged. S512 (Dobbin & Sarathy 2015, Costa Rica ASADA co-management) is MMAT-flagged. S513 (McGranahan 2015, sanitation collective-action/coproduction/tenure synthesis) uses the Legal Institutional Evidence Appraisal Framework, resolved by hand as `doctrinal`. S514 (Chowns 2015, Malawi community water management) is MMAT-flagged. S515 (Ioris 2012, Lima "geography of multiple scarcities") is CASP-flagged (qualitative), a companion paper to already-included S304 (same author, different DOI/journal). S516 (Subbaraman et al. 2012, Mumbai Kaula Bandar "Off the map") is MMAT-flagged, a companion paper to already-included S084. S517 (Morgan 2006, "Turning off the tap," Argentina/South Africa administrative law) is CASP-flagged and explicitly researcher-flagged as a high-priority key reference (see CHANGELOG.md 2026-09-18 entry). S518 (Lee & Floris 2003, four-country Latin American private-sector-participation case study) uses the Legal Institutional Evidence Appraisal Framework, resolved by hand as `jurimetric`. S519 (Birkinshaw 2026, Delhi "smart water" PPP ethnography) is CASP-flagged (qualitative). S520 (Kharmylliem & Kipgen 2025, Shillong village-council/clan water governance) is CASP-flagged (qualitative). S521 (Fono et al. 2025, Aboriginal and Torres Strait Islander drinking-water-policy realist review) is AMSTAR2-flagged (systematic_review_secondary). S522 (Aizannon, Akueson & Moumouni-Moussa 2025, Benin private-actor drinking-water case study) is MMAT-flagged (mixed methods). S523 (Rempel & Dobbin 2025, California AB 685 human-right-to-water policy feedback study) is CASP-flagged (qualitative). S524 (Hernando-Arrese & Ibarra 2025, Toltén Chile decolonial-feminist APR case study) is CASP-flagged (qualitative). S525 (Kachenje 2025, Dar es Salaam institutional-coordination case study) is CASP-flagged (qualitative). S526 (Switzer & Teodoro 2025, US public-enterprise water-pricing redistributive-policy regression study) is flagged with the JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies (observational). S527 (Khadam et al. 2024, Pakistan gender/water-rights expert-panel study) is CASP-flagged (qualitative). S528 (Santos & Ioris 2024, São Francisco River transposition/hydrosocial territory ethnography) is CASP-flagged (qualitative). S529 (Wagle 2024, Mumbai water-access spatial-conditionality study) is CASP-flagged (qualitative). S530 (Hofstetter, Bolding & Boelens 2023, Rooted Water Collectives South Africa/Switzerland comparative case study) is CASP-flagged (qualitative). S531 (Aigbavboa, Addo, Ebekozien, Thwala & Arthur-Aidoo 2025, Ghana urban water institutional-management stakeholder-engagement mixed-methods study) is MMAT-flagged. S532 (Murray, Meyer & Fourie 2023, Cape Town water-justice organising case study) is CASP-flagged (qualitative). S533 (Ghertner 2023, New York farm-labor-camp legal-geographic case-law analysis) uses the Legal Institutional Evidence Appraisal Framework. S534 (Saha & Chakma 2026, rural West Bengal household-water-insecurity co-production study) is MMAT-flagged (mixed methods). S535 (Grisaffi, Leinster, Sipuma, Owako & Parker 2026, East/Southern African road-transported-sanitation regulators' discretionary-enforcement study) is CASP-flagged (qualitative). S536 (Abrams, Carden, Teta & Wagsaether 2021, South Africa rural/small-town WASH climate-vulnerability case-study comparison, HaSinari Limpopo and Prince Albert Western Cape) is CASP-flagged (qualitative). S537 (Alam, Rahat, Nawaz et al. 2025, sewer-connectivity behaviour-change-intervention scoping review across 8 countries) is AMSTAR2-flagged (systematic_review_secondary). S538 (Dallasheh 2022, Nazareth water-infrastructure archival case study, Journal of Palestine Studies) uses the Legal Institutional Evidence Appraisal Framework. All were added 2026-09-18/19/21 and likewise unappraised. RD864629E91F7 (Nkiaka 2022, macro cross-national water-security-index determinants study) and R2C5270DE77D8 (Laitinen et al. 2022, Finnish urban water utility PESTEL/SWOT governance analysis) were screened the same day and excluded E01 -- no household/applicant-level legal-administrative access mechanism examined. S539 (Zhang, Gonzalez Rivas, Grant & Warner 2022, US public-vs-private water utility pricing/affordability OLS regression, 500 largest systems) is JBI Analytical Cross Sectional-flagged (observational) and is the review's second effect_sizes.csv-eligible study of ownership/regulation effects on pricing, alongside S526. S540 (Silva-Novoa Sanchez, Bossenbroek, Schilling & Berger 2022, Morocco water-policy governance study, Middle Draa Valley) is CASP-flagged (qualitative). R397656949E83 (Viljoen, South African water-law property-paradigm doctrinal commentary) was excluded E05 -- pure doctrinal commentary without empirical access evidence. R98A0DCEA5699 (Mamokhere et al., municipal service-partnerships conceptual paper) was excluded E07 -- self-described non-empirical secondary-literature synthesis, not water-specific. R1BF978DC83F1 (Shadabi & Ward, predictors of safe-drinking-water access) was excluded E01 -- same macro cross-national governance-index rationale as the Nkiaka exclusion, wrong unit of analysis. R8821B3A63A95 (Nithammer, Mahabir & Dikgang 2022, South African water-utility double-bootstrap DEA technical-efficiency study) was excluded E04 -- the outcome measured is a DEA efficiency/inefficiency score (utility-level input-output productivity), not a household/applicant-level access, connection, affordability, or reliability outcome. |
| 9 | Risk of bias | **Process scaffolding built 2026-09-12; deliberately not yet applied to the great majority of the 538 extracted studies.** `RISK_OF_BIAS.md` is explicit that none of the six validated appraisal tools (RoB 2, ROBINS-I, the two JBI checklists, CASP, MMAT) or AMSTAR 2 may be reconstructed from memory — the current official version of each must be obtained before appraising a study with it. Accordingly, every one of the 538 extracted studies has `risk_of_bias_tool` correctly identified (design-matched per `RISK_OF_BIAS.md` §1, or the project's own Legal Institutional Evidence Appraisal Framework per §2 where no conventional tool fits) but `risk_of_bias_rating` deliberately left **blank**, with an `extraction_note` on each row deferring the actual rating to a follow-up pass conducted with the official instrument in hand. `04_quality/appraisal_forms/APPRAISAL_FORM.md` documents that process; a fully worked fillable form exists for the project-owned Legal Institutional Evidence Appraisal Framework (`legal_institutional_evidence_appraisal_framework_form.md`). This is a real, reportable limitation at this stage of the review, not an oversight — disclose it as such in any manuscript output. A **preliminary** cross-cutting evidence-limitations narrative (`04_quality/risk_of_bias/2026-09-16_evidence_limitations.md`) was written 2026-09-16 from corpus-composition fields alone (design mix, mechanism_certainty, jurisdiction coverage) — it explicitly leaves the "overall confidence" judgment as a placeholder pending actual per-study ratings from this phase. While compiling it, 11 systematic-review studies (S319–S329) were found to carry a mis-assigned `risk_of_bias_tool` (CASP instead of AMSTAR 2) and were corrected. **2026-09-16: a first, explicitly partial appraisal pilot batch was completed for the two smallest tool groups** — RoB 2 (S057, S085, S294) and ROBINS-I (S037, S121, S142, S143, S169, S189, S213, S219, S235) — after `WebFetch` to every domain hosting the official checklists returned `EGRESS_BLOCKED` in this environment (an organization network-egress policy, not something routed around) and the researcher twice confirmed how to proceed (first on using `WebSearch` snippets at all, then again once `APPRAISAL_FORM.md`'s own prohibition on reconstructing a checklist from incomplete sources was surfaced). Ratings are written as explicit lower bounds (e.g. "Some concerns (partial pilot appraisal...)") with any domain lacking real signalling-question text marked "not assessable" rather than guessed; the completed forms are in `04_quality/appraisal_forms/`. **2026-09-16: continued to the next tool group — AMSTAR 2 for all 17 `systematic_review_secondary` studies** (S015, S019, S027, S052, S079, S116, S319–S329). This time the tool text itself came back complete via `WebSearch` (all 16 items, 7 critical items, full rating algorithm), but the studies did not: all 17 were extracted at citation/abstract level, not from their own Methods sections, so every item lacking extracted evidence was marked "Not assessable" rather than guessed. Result: every one of the 17 is rated **"Not ratable"** — at most 1 of each study's 7 critical items has any extracted evidence (S015's OSF pre-registration, confirmed via its `extraction_note`), so AMSTAR 2's rating algorithm cannot run. This is a disclosed finding in its own right: a real AMSTAR 2 appraisal of these 17 studies requires retrieving and extracting their full Methods sections first. **2026-09-16 (later the same day): 2 further systematic-review studies extracted from full text — S370 and S372 — each received a positively-determined AMSTAR 2 rating of "Critically Low"**, not "Not ratable": in both cases the review's own full text explicitly states no critical appraisal of individual included studies was conducted, a directly confirmed (not merely unassessed) AMSTAR 2 item-9 critical weakness, which is a fundamentally different evidentiary situation than the 17-study batch's abstract-only extraction limit. The much larger CASP (119+26=145 studies) and MMAT (68+6=74 studies) groups remain fully unappraised. |
| 10 | Evidence classification | **Populated 2026-09-12, kept current as extraction grows (512 studies as of this update).** `code/analysis/build_evidence_map.py` derived what can safely be derived mechanically (`study_design_class` from `risk_of_bias_tool`, `mechanism_family` from the four top-level mechanism booleans, `legal_context`/`institutional_context` copied from extraction); the remaining judgment-call fields were then filled by hand for all 512 rows: `study_design_class` for the studies using the project's own Legal Institutional Evidence Appraisal Framework (resolved doctrinal vs. jurimetric per study), `outcome_family` mapped to `PROJECT_SPEC.md` §7's hierarchy based on each study's actual central/tested outcome (not a mechanical restatement of the outcome booleans), `evidence_level` written as prose per `DATA_DICTIONARY.md`'s instruction that it is a narrative tier rather than a score, and `quantitative_synthesis_eligible`/`qualitative_synthesis_eligible` set per study. S085 (Gaikwad & Thomas) is a genuine cluster-randomized field experiment — the strongest-design study in the set — and a clean empirical instance of `PROJECT_SPEC.md` §8 candidate Family B (bureaucratic assistance → connection/application success), though it shows that mechanism only operates jointly with political coordination, not as a simple main effect. See `05_analysis/descriptive/EVIDENCE_MAP_README.md` for the full derivation/judgment-call rationale. |
| 11 | Quantitative feasibility assessment | **Corpus-level family judgment not started; a first per-study screening pass completed 2026-09-16.** `ANALYSIS_PLAN.md` §2's decision tree is a corpus-level methodological judgment applied per candidate synthesis family (`PROJECT_SPEC.md` §8), not a per-study mechanical fact, so the family-level judgment itself remains undone and deliberately has no speculative tooling built ahead of it. What was done instead: `05_analysis/effect_sizes/effect_sizes.csv` (previously header-only) was populated with the **20 of 177** `quantitative_synthesis_eligible` studies that actually have a defined exposure, a meaningful comparator, an in-scope outcome, and a locatable effect estimate — the per-study prerequisite the decision tree's first three branches require before any family-level question can even be asked (population began 2026-09-16 and continued through the 2026-09-17 Zotero Drive-folder batches, most recently adding S434, S435, S445 and S448 from Google Drive batch 3). 11 of the 20 map to Families A/B/C (8 to Family A, 2 to Family B, 1 to Family C); 9 (including all 4 of this latest batch's additions) do not match any existing family. Every row has `included_in_pooled_estimate = FALSE` — no family has more than one study sharing a genuinely comparable exposure-comparator definition yet, so none is close to clearing the full decision tree. See `CHANGELOG.md` 2026-09-16 and `05_analysis/descriptive/EVIDENCE_MAP_README.md`'s closing section. |
| 12 | Meta-analysis where justified | **R template built 2026-09-12** (`08_code/R/01_meta_analysis.R`) implementing `ANALYSIS_PLAN.md` §§5–8 (random effects, heterogeneity + prediction interval, subgroup analysis gated on a minimum study count, meta-regression gated at the ~10-studies-per-moderator threshold). **Not yet run against real data — no R interpreter was available in the environment that wrote it** (see `08_code/R/README.md`'s "Status" section); validate it before trusting any output. Blocked on Phase 11 actually judging a synthesis family eligible. |
| 13 | Structured quantitative synthesis of unpoolable evidence (SWiM) | **Template built 2026-09-12** (`06_outputs/supplementary/SWIM_SYNTHESIS_TEMPLATE.md`) — deliberately does not reproduce SWiM's own reporting-guideline checklist verbatim (unverified against the publisher, same caveat as the risk-of-bias tools); check the official guideline directly. Blocked on Phase 11 routing a family here instead of to meta-analysis. |
| 14 | Sensitivity analysis | **R template built 2026-09-12** (`08_code/R/02_sensitivity_analysis.R`), implementing the five specific checks `ANALYSIS_PLAN.md` §10 names. Same untested-in-this-environment caveat as Phase 12. |
| 15 | Publication bias assessment where appropriate | **R template built 2026-09-12** (`08_code/R/03_publication_bias.R`), enforcing `ANALYSIS_PLAN.md` §9's ~10-studies-per-family threshold as a hard refusal rather than a suggestion. Same untested-in-this-environment caveat as Phase 12. |
| 16 | PRISMA reporting | **Checklist built 2026-09-12** (`06_outputs/prisma/PRISMA_2020_CHECKLIST.md`) — all 27 items mapped to where each is already substantively addressed in this repository, so manuscript drafting is writing up what's recorded, not starting blank. Two items (funding, competing interests) have no home yet and need the researcher's actual disclosures. Exact item wording should be checked against the official PRISMA 2020 checklist before final submission. |

**Current phase (updated 2026-09-13): 1–5 complete; Phase 6 (full-text screening) in progress, live; Phase 8 (full extraction) caught up with Phase 6, no outstanding gap; Phase 7 superseded; Phase 10 (evidence classification) populated for all 144 studies extracted so far; Phase 9 (risk of bias) deliberately not yet applied to any study; Phases 12–16 scaffolding built.** Phase 3 closed by researcher decision,
with documented gaps (SSRN and Westlaw/Lexis never searched). Phase 5's
human `reviewer_2` pass is done — see the flagged caveat on its near-total
agreement rate with reviewer_1 in the Phase 5 row above, which any
manuscript output should disclose alongside the result rather than
presenting as an unremarkable independent second pass.
Repository/documentation scaffolding is complete, the OSF preregistration
is drafted (not submitted), and the deduplication and screening-ingest
scripts have processed the full raw-export pool: 37 `WebSearch`-pilot
records (not a Tier 1/2 database search, see `SEARCH_PROTOCOL.md` §7), 3
`SOURCES.md` exemplars, `SEARCH_018`'s 500 abstract-less records, 5,484
records across all 18 Scopus batches, 4,058 from Web of Science, 1 from
HeinOnline, 7,728 from ProQuest's full account-based export, 16,736 from
ProQuest/Sociological Abstracts, and 50 from JSTOR — **34,594 raw records
total**. The final 2026-09-11 re-run of `code/search/deduplicate.py`
found 7,113 of those to be duplicates (heavy cross-database journal
overlap, as expected); the screening database now holds **27,481 unique
candidate records, 26,222 of which have a real abstract**. All 26,222
have now been screened against `INCLUSION_EXCLUSION.md` by Claude as a
first-pass AI reviewer (explicitly authorized by the researcher —
`CHANGELOG.md`): **3,062 include / 22,557 exclude / 603 unsure**. The
human `reviewer_2` pass over the 3,665 include+unsure records is now
complete (`CHANGELOG.md` 2026-09-12): **3,659 include / 6 exclude, zero
conflicts** by the strict reviewer_1-vs-reviewer_2 disagreement definition
in `DATA_DICTIONARY.md`. `final_decision` is populated for all 3,665
records on this basis. **Flagged, not hidden**: this agreement rate is
unusually high for an independent second pass and the review turnaround
was fast relative to the volume — documented in `CHANGELOG.md` and the
Phase 5 row above so it's visible to anyone assessing this review's rigor,
including in any manuscript reporting this step. Phase 6 (full-text
screening) is now live and ongoing: of the 3,659-record included set,
**1,091 have been screened (538 include / 553 exclude)**, with the researcher
supplying full-text PDFs on a rolling basis expected to continue for over
a month — see the Phase 6 row above for the exclusion-reason breakdown.
Phase 7 (pilot extraction) was superseded by the researcher's explicit
instruction to proceed directly to full extraction on every full-text
include rather than drawing a separate pilot subsample first. Phase 8
(full extraction) is likewise live and now fully caught up: **all 538
current full-text includes (S001–S540, S227 and S399 documented gaps) are fully extracted** into
`extraction_database.csv` against `CODEBOOK.md`'s full 92-field schema.
Phase 9 (risk of bias) is
intentionally not yet applied to the great majority of the 538 (a first
12-study partial pilot batch was appraised 2026-09-16, plus 2 further
studies -- S370, S372 -- with a positively-determined AMSTAR 2 rating of
Critically Low, see the Phase 9 row above) — `risk_of_bias_tool` is
identified per study but `risk_of_bias_rating` is deliberately left blank
for the remainder pending the official version of each appraisal instrument, per
`RISK_OF_BIAS.md`'s explicit prohibition on reconstructing a validated
tool from memory; this is a disclosed limitation of the review's current
state, not an oversight. Phase 10 (evidence classification) has been run
against all 512 extracted studies, both the mechanically-derivable fields
(via
`build_evidence_map.py`) and the judgment-call fields (`outcome_family`,
`evidence_level`, and the two synthesis-eligibility flags) filled by hand
per study — see `05_analysis/descriptive/EVIDENCE_MAP_README.md`. Phase
11 (quantitative feasibility) is deliberately left without
speculative tooling, since its decision tree is a corpus-level judgment
call that already **is** the complete process — see the Phase 10/11 rows
above. Phases 12, 14, and 15 have R analysis templates
(`08_code/R/`) implementing `ANALYSIS_PLAN.md`'s already-specified models
and thresholds, explicitly marked **not yet run** (no R interpreter was
available to test them); Phase 13 has a SWiM synthesis template; Phase 16
has the full PRISMA 2020 checklist pre-mapped to where each item is
already addressed in this repository. All of Phases 12–16 remain blocked
on real evidence existing to run them against.

## Screening database schema

`02_screening/title_abstract/screening_database.csv`:

```
record_id, database, title, authors, year, doi, url, abstract, duplicate,
title_abstract_decision, full_text_decision, exclusion_reason,
reviewer_1, reviewer_2, conflict, final_decision
```

(`url` was added 2026-08-25, after the schema's first use, once real
candidate records surfaced sources with no DOI at all — mostly grey
literature. Without a URL such a record cannot be relocated. `abstract`
was added 2026-09-10, once the first export with Abstract selected in the
field picker arrived — optional, blank on anything ingested before that
date. See `CHANGELOG.md` for both amendments.)

Standardized exclusion codes: `INCLUSION_EXCLUSION.md` §"Standardized
exclusion codes" (E01–E12).

`02_screening/full_text/full_text_screening_database.csv` (Phase 6, a
separate file — see `DATA_DICTIONARY.md` and `FULL_TEXT_README.md` for why
`screening_database.csv`'s own `full_text_decision`/reviewer columns are
not reused):

```
record_id, title, authors, year, doi, url, full_text_status,
full_text_location, full_text_decision, exclusion_reason,
exclusion_reason_detail, reviewer_1, reviewer_2, conflict, final_decision,
notes
```

## Evidence classification matrix

Every included study receives, in `05_analysis/descriptive/evidence_map.csv`:

```
study_id, study_design_class, evidence_level, mechanism_family,
outcome_family, quantitative_synthesis_eligible, qualitative_synthesis_eligible,
legal_context, institutional_context
```

Worked example (illustrative only — not real extracted data):

| Study type | Design | Mechanism | Outcome | Meta-eligible |
|---|---|---|---|---|
| Legal-recognition observational study | Observational | Eligibility | Water access | Potentially |
| Bureaucratic-assistance field experiment | Experimental | Burden/facilitation | Formal connection | Potentially |
| Doctrinal article | Doctrinal | Eligibility | Normative | No |
| Interview study | Qualitative | Discretion | Administrative experience | No, but mechanism-synthesis eligible |
| Judicial decisions dataset | Jurimetric | Litigation | Judicial outcome | Never — separate study (`PROJECT_SPEC.md` §9) |

## PRISMA flow diagram

`06_outputs/prisma/prisma_flow.md` is the live flow-diagram source. It is
currently a stub with all counts at zero, updated only as each phase above
actually produces a count — never pre-filled with placeholder or estimated
numbers.
