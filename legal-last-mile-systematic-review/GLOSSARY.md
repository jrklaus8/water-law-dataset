# Glossary — the project's labels and terms in plain language

Files, columns and notes in this project use short labels (`A28`, `CK`, `reviewer_2`, "AI-checked", `S404`). This page says what each means. Where a term has a defining document, it is named.

## Who and what

| Term | Meaning |
|---|---|
| **The researcher, the author, the PI** | Claudio Klaus, who set the question and protocol, ran the database searches, supplied the full texts and makes every decision that needs a person. "PI" is *principal investigator* |
| **The AI** | Claude (Anthropic), which did most of the screening, extraction, appraisal and synthesis drafting under the researcher's direction. Other AI models (Codex, Gemini) acted as blind second reviewers on part of the full-text decisions. Details: `AI_USE_STATEMENT.md` |
| **AI-assisted** | Most of the work was done by an AI and only part was independently checked by a human. This is in the project's title so it is never a surprise |
| **Human-verified** | A person actually read the evidence and recorded a decision. Counted strictly: a record is not human-verified because the AI re-checked it |
| **AI-checked** | The AI re-read it and found no problem. This is **not** a human confirmation and is never counted as one |
| **`CK`** | The reviewer initials used for the PI's own rulings. Written to a record only when the PI reviewed the evidence and instructed that the ruling be recorded |
| **Preliminary** | Nothing here is a final result. Every output says so |
| **Release `0.2.0-interim`** | The 2026-10-14 snapshot of the repository. Searching and full-text retrieval were closed; extraction and appraisal are complete for what was retrieved; verification is partial. Described in `00_admin/RELEASE_0.2.0-interim_2026-10-14.md` |

## Identifiers

| Term | Meaning |
|---|---|
| **`R…` (for example `R0E4C0CE0DA80`)** | A **record ID**: one search result, assigned when the searches were merged. It follows the record through screening |
| **`S…` (for example `S404`)** | A **study ID**: one included report in the extraction database. A gap in the numbering is a retired ID (a study that was assigned a number and later excluded). Not to be confused with the sensitivity scenarios below, which also start with S |
| **Linked reports** | Companion papers that describe the same underlying study. Extraction is per report, not per study; `03_extraction/extracted_data/linked_reports_2026-09-28.csv` lists the links |
| **`reviewer_1`, `reviewer_2`** | Columns in the screening databases. `reviewer_1` is the first decision (the AI, labelled `Claude-AI-fulltext-<date>`). `reviewer_2` is the second: a person (`Human-…` or `CK`) **or** another AI model (`Codex-…`, `Gemini-…`). A `Codex-` or `Gemini-` entry is **not** human review |
| **`E01` … `E12`** | Standardised exclusion codes, defined in `INCLUSION_EXCLUSION.md` (for example `E01` wrong topic, `E04` wrong outcome, `E05` no empirical evidence, `E06` engineering only, `E10` inaccessible full text) |

## The decision log

| Term | Meaning |
|---|---|
| **`A1`, `A16`, `A28` …** | Numbered items in table A of `00_admin/DECISIONS_AND_OPEN_ITEMS.md`. Each is a decision or a verification task, marked **OPEN** (waiting for the author) or **CLOSED** with a date and the ruling. Files named `A16_…`, `A28_…` belong to that item |
| **`A16`** | The researcher's adjudication of full-text exclusions, started after an independent AI model disagreed with the first AI reviewer on a large share of a stratified sample of its exclusions. `A19`, `A22`–`A26` and `A28` apply the same kind of ruling to further groups of decisions |
| **`A6`** | The human second-review pass on full-text decisions, done in priority tiers. Tier 1 is complete; tiers 2 and 3 are not |
| **`A28`** | The ten synthesis studies the AI had flagged on a narrow check of scope and outcome, settled by the researcher from the verbatim PDF passages |
| **`A30`** | **Open.** The author's own check of the synthesis studies against their PDFs, including the direction coding, and a blind second extraction |
| **`A31`** | The researcher's instruction that the `CK` count be kept strictly to records they reviewed. The 18 synthesis studies whose inclusion had been recorded as confirmed on the strength of an AI check were relabelled AI-checked |
| **`A32`** | **Open.** Three proposed corrections to stored numbers so they match the published papers; none applied until approved |
| **Narrow reading of criterion 2** | Criterion 2 (`INCLUSION_EXCLUSION.md`) requires a legal, administrative, institutional, regulatory or governance factor; the researcher adopted a narrow reading (a legal or administrative *access rule or mechanism*) after the independent-model disagreement was seen. It is a disclosed departure, not a change made quietly |
| **Borderline include** | An included report the researcher kept but flagged because its link to the rule-type mechanism is thin. Flagged in a note on the row; not removed |

## The transparency files

| Term | Meaning |
|---|---|
| **Weakness register (`W01` …)** | `00_admin/WEAKNESSES.md`: each known weak point with its evidence, a concrete way to test or break it, and what would resolve it. The severity ratings are the AI's judgment, not an independent reviewer's |
| **Deviations register (`D01` …)** | `00_admin/DEVIATIONS_REGISTER.csv`: every dated departure from the protocol, with whether it was decided after the results it could affect were visible |
| **Errors-found register (`E01` …)** | `00_admin/ERRORS_FOUND_REGISTER.csv`: every error the project found in itself, how it was found, its effect and its fix. Not a claim that these are all the errors |
| **Study audit trail** | `00_admin/STUDY_AUDIT_TRAIL.csv`: one row per included study showing who decided its inclusion and how far extraction, appraisal and synthesis were checked |
| **AI-use ledger** | `00_admin/AI_USE_LEDGER.md`: which AI tool or model did what at each stage, how many decisions carry its label, and what is not archived (prompts, model versions, settings) |
| **Data manifest** | `10_reproducibility/DATA_MANIFEST.csv`: size, shape and SHA-256 of every data file, so a reader can confirm they hold the analysed files |

## Verification tools

| Term | Meaning |
|---|---|
| **`verify_repository.py`** | Recomputes every headline figure from the CSV databases, checks that the databases agree with each other, and checks that the documents quote the same figures. Run it first |
| **`CURRENT_FIGURES.md`** | The figures the verifier computed, in readable form. When a document disagrees with it, it is right |
| **`regenerate_all.sh`** | Rebuilds every derived file, runs the unit tests, then the verifier |
| **Dossier** | `05_analysis/effect_sizes/SWIM_31_SOURCE_VERIFICATION_DOSSIER.md`: for each synthesis study, the stored values next to verbatim passages of its PDF with page numbers, and blank boxes for the author to confirm |
| **Second extractor** | A person who would extract a sample of studies blind and be compared with the AI. Prepared (`03_extraction/second_extractor/`), not yet done |
| **Provenance scripts** | `code/provenance/`: the one-off scripts that wrote data into the databases, kept as a record. They are not a pipeline to re-run |

## The synthesis

| Term | Meaning |
|---|---|
| **PRISMA 2020** | The reporting guideline for systematic reviews. The flow diagram and checklist are in `06_outputs/prisma/` |
| **SWiM** | *Synthesis Without Meta-analysis* (Campbell et al. 2020): the reporting guideline used because effects could not be pooled |
| **Vote counting by direction** | Counting studies by whether the association is favourable, unfavourable, null or mixed. It ignores effect size, precision and sample size, and it is not causal. It supports only a statement about direction |
| **Raw sign** | Whether the reported estimate is positive or negative as published |
| **Substantive direction** | Whether the association is *Favourable*, *Unfavourable*, *Null* or *Mixed* **for households**, derived (never typed) as the raw sign multiplied by the outcome's polarity (a higher tariff or interruption is worse; a higher coverage or access rate is better) and the exposure's orientation. Both codings are kept so a reader can disagree with one without the other |
| **Families A, B, C** | Groupings of comparable studies. **A**: recognition and formal status. **B**: assistance, participation and trust. **C**: ownership, regulation and institutional structure |
| **Reasoned non-fit** | A study with an effect-size row whose exposure or outcome does not fit any of the three families. It is described, not synthesised, and the reason is recorded |
| **Harvest plot** | A display that shows each study as a tile in its direction column (Ogilvie et al. 2008). Solid tiles are human-verified inclusions; dashed tiles are AI-checked only |
| **Conclusion tests** | Three statements: more than half of Family A Favourable; no Family B study Unfavourable or Null; no single direction holding a majority in Family C. They were written into `code/analysis/sensitivity_analysis.py` before the scenarios were run, so the scenarios cannot be tuned to them, but **not** before the baseline counts existed (the family documents were committed a day earlier), so they are not blind to the baseline result. Each is re-tested under every scenario |
| **Scenarios `S0`, `S1`, `S1b`, `S2`, `S3`, `S4`, `S4c`, `S4e`, `S5`, `S4d`** | The ten sensitivity scenarios (sensitivity analysis), each removing or recoding doubtful studies. **They are scenario names, not study IDs** |
| **Pooling, meta-analysis** | Combining effect sizes into one estimate. Not done: no family met the bar |
| **GRADE** | A method for rating certainty of a pooled body of evidence. Not applied, because nothing was pooled |
| **Mechanism certainty (0–4)** | The AI's code for how well a study identifies the mechanism it reports, from 0 (none) to 4 (strong). A coarse label, not a GRADE rating |

## Risk-of-bias instruments

| Term | Meaning |
|---|---|
| **RoB 2**, **ROBINS-I** | Cochrane instruments for randomised and non-randomised studies of interventions |
| **AMSTAR 2** | For systematic reviews |
| **JBI Cross-Sectional**, **MMAT**, **CASP Qualitative** | Checklists for cross-sectional, mixed-methods and qualitative studies |
| **Legal Framework** | This project's own appraisal for doctrinal and legal studies. **Not validated** |
| **Rule-based batch rating** | A rating assigned by a rule applied to the extracted fields, not by reading each paper against the instrument's signalling questions. Most ratings are of this kind; `RISK_OF_BIAS.md` §4 says what depth they reflect |

## Other terms you will meet

| Term | Meaning |
|---|---|
| **Cowork** | An AI browser assistant that relayed some database searches the researcher ran through institutional access |
| **Drive inbox** | The shared folder through which the researcher delivered full-text PDFs; the batch logs are in `00_admin/` |
| **Atlas** | `06_outputs/EVIDENCE_ATLAS_INTERACTIVE.html`, the interactive results page, also at https://jrklaus8.github.io/water-law-dataset/atlas/ |
| **Historical snapshot** | A dated file that keeps the figures true on its date. It is not wrong; it is old. `CURRENT_FIGURES.md` is current |
