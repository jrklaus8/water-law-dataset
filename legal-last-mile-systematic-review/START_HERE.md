# Start here — what this project is, what was done, and how to check it

**For:** supervisors, examiners, auditors, and researchers who want to build on or challenge this work.
**Reading time:** 10 minutes for this page; the sections below send you to the evidence for every claim.

> **Status: preliminary, AI-assisted and only partly human-verified.** An AI (Claude, Anthropic) did most of the screening, data extraction, risk-of-bias appraisal and synthesis drafting under the researcher's direction and a written protocol. A human checked only part of it. No result here is final. The project says so on its title (*An AI-Assisted Systematic Review*) so that no reader has to discover it.

---

## 1. What this is

A systematic review of the research literature on one question: **how do legal and administrative rules — eligibility criteria, documentation requirements, fees, service-area boundaries, administrative burden, enforcement, discretion, review and appeal — affect whether households obtain and keep water and sanitation services?**

It is the companion to the doctoral dissertation *The Legal Last Mile: Administrative Law as a Mechanism of Connectivity and Exclusion in Sanitation Governance* (Claudio Klaus). It is separate from the court-decisions dataset in the repository root, which is a different evidence base.

The evidence is too varied to pool into one average effect, so the review reports **direction of association** for a small set of comparable studies (structured synthesis without meta-analysis, "SWiM") and describes the rest.

## 2. The numbers at a glance

<!-- BEGIN GENERATED: key figures (code/analysis/build_start_here.py) -->

| Stage | Figure | What to know |
|---|---|---|
| Records found in the database searches | 34,594 | Searches ran 2026-08-25 to 2026-09-11 and were closed by decision; SSRN and Westlaw/Lexis were never searched |
| After removing duplicates | 27,481 |  |
| Passed title and abstract screening to the full-text stage | 3,659 | The AI screened every abstract; a human second pass covered only the include-or-unsure records |
| Full texts actually assessed | 2,277 | 1,382 candidates were never assessed (1,200 could not be retrieved, 182 were the wrong file) |
| **Included studies** | **1,072** | 1,205 full texts were excluded, each with a coded reason |
| Full-text decisions a human checked or ruled on | 459 of 2,277 (20.2%) | 197 includes confirmed by a human second reviewer; 262 further decisions ruled on by the principal investigator |
| Studies with extracted data and a risk-of-bias rating | 1,072 | Extraction and ratings were made by the AI; no second extractor and no human re-appraisal yet |
| Studies in the three structured (SWiM) syntheses | 31 | 13 have a human-verified inclusion decision, 18 are AI-checked only; the author has confirmed the direction coding of 0 |
| Effect sizes pooled into a meta-analysis | 0 | No family met the bar for pooling; 52 effect-size rows are reported by direction of association only |

These figures are rewritten from the databases by `code/analysis/build_start_here.py`; the full list is in `00_admin/CURRENT_FIGURES.md`.

<!-- END GENERATED: key figures -->

## 3. What was done, in order

| Step | What happened | Who did it | Where the evidence is |
|---|---|---|---|
| 1. Protocol | Question, eligibility criteria, search plan, extraction codebook and analysis plan were fixed in writing on **2026-08-22, before any database was searched** | Researcher | `PROTOCOL.md`, `INCLUSION_EXCLUSION.md`, `CODEBOOK.md`, `ANALYSIS_PLAN.md` |
| 2. Search | Scopus, Web of Science, ProQuest, ProQuest Sociological Abstracts, JSTOR and HeinOnline, plus a web-search pilot | Researcher ran the searches and exports | `SEARCH_PROTOCOL.md`, `01_search/` |
| 3. De-duplication | Records matched by DOI and by title/year similarity; every merge logged | Scripts | `01_search/deduplicated/`, `code/search/` |
| 4. Title and abstract screening | Every record with an abstract was screened against the criteria, with a written reason | AI first pass; a human second pass on the include-or-unsure records only | `02_screening/title_abstract/` |
| 5. Full-text screening | Each retrieved full text was read and decided include/exclude with a coded reason | AI; the researcher obtained the papers, confirmed part of the includes and ruled on contested cases | `02_screening/full_text/`, `02_screening/exclusion_log/` |
| 6. Extraction | 92 fields per included study, each with its source location | AI; **no second extractor** | `03_extraction/`, `CODEBOOK.md` |
| 7. Risk of bias | Design-matched instrument chosen and a rating assigned | AI, rule-based from the extracted fields; **no human re-appraisal** | `04_quality/`, `RISK_OF_BIAS.md` |
| 8. Evidence map | Each study classified by design, mechanism family, outcome and certainty | AI, with controlled vocabularies and researcher rulings | `05_analysis/descriptive/` |
| 9. Can anything be pooled? | Judged family by family; **nothing met the bar**, so the three families that could be compared by direction went to structured synthesis | AI drafted; researcher approved | `05_analysis/effect_sizes/`, `06_outputs/supplementary/` |
| 10. Sensitivity analysis | Ten scenarios remove or recode doubtful studies and re-test three conclusion tests written into the script before the scenarios were run (but after the baseline counts existed) | Script | `code/analysis/sensitivity_analysis.py`, the atlas "Robustness" tab |
| 11. Audits and corrections | The project audited itself, corrected its own errors in the open, and the researcher adjudicated contested decisions | AI found; researcher ruled | `00_admin/audits/`, `00_admin/DECISIONS_AND_OPEN_ITEMS.md`, `CHANGELOG.md` |
| 12. Outputs | Interactive atlas, preliminary report, executive summary, manuscript draft | Generated from the databases | `06_outputs/`, `07_manuscript/` |

**Interactive version of all of this:** the *Legal Last Mile Atlas* — https://jrklaus8.github.io/water-law-dataset/atlas/ (also in this folder as `06_outputs/EVIDENCE_ATLAS_INTERACTIVE.html`; it includes a Methodology tab and the full lists of included, excluded and unassessed texts for reproduction).

### Where the project departed from its plan

Disclosed rather than smoothed over: searching was closed early by decision (SSRN and Westlaw/Lexis never searched); full-text retrieval was closed with part of the candidates never assessed; the separate pilot extraction was replaced by extracting every study directly; the protocol was **not registered before the work was done** (a transparent retrospective registration is prepared and not yet submitted); and a narrower reading of one eligibility criterion was adopted after an independent AI reviewer disagreed on many decisions. The best single list is `00_admin/preregistration/osf_preregistration_draft.md`, which separates what was fixed in writing on 2026-08-22 from the dated post-hoc changes in `CHANGELOG.md`.

## 4. What to trust, and what not to

| Treat as | What | Why |
|---|---|---|
| **Re-derivable — check it yourself** | Every count on this page, the PRISMA flow, the tables in the atlas | `python3 code/analysis/verify_repository.py` recomputes them from the CSV databases and checks that the documents quote the same numbers |
| **Human-ruled** | Decisions recorded under reviewer `CK` (the principal investigator) and by a named human second reviewer | A person read the evidence and decided; the share is in the table above |
| **AI-produced, not independently verified** | Extracted values, risk-of-bias ratings, evidence-map labels, the direction coding of each synthesis study, the written syntheses | No second extractor or re-appraiser has checked them. Open items A30 and A32 in `00_admin/DECISIONS_AND_OPEN_ITEMS.md` track the verification the author still owes |
| **Historical snapshot** | Any file with a date in its name, and older entries in `CHANGELOG.md` | They keep the figures that were true when written. When a document and `00_admin/CURRENT_FIGURES.md` disagree, **`CURRENT_FIGURES.md` is right** |
| **Not available** | The source PDFs | Many are under publisher copyright; the manifest and hashes of the 31 synthesis papers are in `05_analysis/effect_sizes/SWIM_31_SOURCE_PDF_MANIFEST.csv` |

## 5. Pick a reading path

**Supervisor or examiner (about 30 minutes)**
1. This page, then the atlas (summary, methodology and robustness tabs).
2. `AI_USE_STATEMENT.md` — what the AI did and what a human checked, stage by stage.
3. `README.md` → "Known limitations" — the project's own list of what it cannot claim.
4. `00_admin/DECISIONS_AND_OPEN_ITEMS.md` — what is still undecided and who decides.

**Auditor or methodologist (about 2 hours)**
1. `AUDITING_GUIDE.md` — how to check the numbers, trace one study from search hit to synthesis, and challenge a result.
2. `PROTOCOL.md`, `INCLUSION_EXCLUSION.md`, `ANALYSIS_PLAN.md` — what was promised before searching.
3. Run the verifier. Then pick a study ID from the atlas and follow it through the folders using `AUDITING_GUIDE.md` §3.
4. `05_analysis/effect_sizes/SWIM_31_SOURCE_VERIFICATION_DOSSIER.md` — the 31 synthesis studies against verbatim passages of their PDFs.

**Researcher who wants to reproduce or extend it**
1. `REPRODUCIBILITY.md` and `SEARCH_PROTOCOL.md` (exact search strings per database).
2. `bash code/analysis/regenerate_all.sh` rebuilds every derived file, runs the unit tests and then the verifier.
3. `CODEBOOK.md` and `DATA_DICTIONARY.md` for every field; `code/provenance/README.md` before opening anything under `code/provenance/` (those scripts are a record of what was run, not a pipeline to re-run).
4. The full lists of included, excluded and unassessed texts in the atlas's last tab.

Unfamiliar label such as `A28`, `CK` or "AI-checked"? See `GLOSSARY.md`.

## 6. The folders

Each numbered folder has its own `README.md` saying what is in it, which file matters, and who checked it.

| Folder | In one line |
|---|---|
| [`00_admin/`](00_admin/README.md) | Decisions, open items, audits, current figures, the interim-release note |
| [`01_search/`](01_search/README.md) | Search strategies, raw exports, de-duplication |
| [`02_screening/`](02_screening/README.md) | Title/abstract and full-text decisions, exclusion log, human adjudication sheets |
| [`03_extraction/`](03_extraction/README.md) | The 92-field extraction database and the second-extractor materials |
| [`04_quality/`](04_quality/README.md) | Risk-of-bias appraisal forms and batch notes |
| [`05_analysis/`](05_analysis/README.md) | Evidence map, effect sizes, SWiM verification dossier |
| [`06_outputs/`](06_outputs/README.md) | Atlas, reports, PRISMA flow, figures, supplementary syntheses |
| [`07_manuscript/`](07_manuscript/README.md) | Manuscript drafts |
| [`08_code/`](08_code/README.md) | R templates for meta-analysis (not run: nothing was poolable) |
| [`09_data_dictionary/`](09_data_dictionary/README.md) | Placeholder; the data dictionary is `DATA_DICTIONARY.md` |
| [`10_reproducibility/`](10_reproducibility/README.md) | Placeholder; reproducibility is `REPRODUCIBILITY.md` and `code/analysis/regenerate_all.sh` |
| [`11_archive/`](11_archive/README.md) | Material removed from the live databases, kept for the record |
| `code/` | All scripts; `code/provenance/` holds the one-off scripts that wrote the data |
| `_reviewer2_codex/` | Records of the independent second-AI-reviewer runs |

## 7. If you find a mistake

The project has already found and corrected errors of its own making (stale figures, two papers counted twice, a sign error in a synthesis), and assumes more exist. To challenge a value, follow `AUDITING_GUIDE.md` §3 to the extraction row and its source location, compare with the paper, and report the study ID, the field and the page. Corrections are logged, dated, in `CHANGELOG.md`; nothing is silently overwritten.
