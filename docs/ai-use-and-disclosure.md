# AI use and disclosure

This repository contains two linked projects that used AI differently. This page lists, in one place, every AI tool and use that the repository records, what is **not** recorded, what material may have left the researcher's control, and what is still undecided. It links to the existing detailed statements instead of repeating them.

*Written by an AI assistant (Claude Code) on 2026-10-27 from the repository's own files. It describes what the files say; it does not know what happened outside them. It is not an official disclosure form for any institution or journal. The researcher must check it and correct it before relying on it.*

## 1. Where the detailed records are

| Project | Statement | Detail |
|---|---|---|
| Court-decision dataset and tools (repository root) | `README.md`, section "AI Disclosure" | this page |
| Systematic review (`legal-last-mile-systematic-review/`) | `AI_USE_STATEMENT.md` | `00_admin/AI_USE_LEDGER.md` and `.csv` (stage by stage, with record counts), `_reviewer2_codex/AI_USE_AND_TOOLS_DISCLOSURE.md` (second-model pass) |
| Research assistant (`research-assistant/`) | `README.md` ("AI Disclosure") | `agents.py`, `app.py` |

## 2. Inventory of AI use

| # | Project | Tool or model (as recorded) | What it did | Evidence in the repository | Human oversight recorded | What is not recorded |
|---|---|---|---|---|---|---|
| 1 | Dataset | Claude (Anthropic) | Wrote and debugged the court scrapers, the merge and normalisation scripts and the regex coding engine; automated deposit scripts; filed issues on an upstream legal-data project | `README.md` AI Disclosure paragraph; the scripts themselves | "All research design decisions, methodological choices, variable definitions and intellectual interpretations are those of the human researcher" (README) | Model versions, dates, prompts and sessions; which lines were AI-written; any human review of the code. The unit tests in `tests/` were written by this audit, not earlier |
| 2 | Dataset | Antigravity (Google DeepMind) | Audited the repository for contradictions and stale data and corrected documentation | README AI Disclosure paragraph | as above | Session records and the corrections it made |
| 3 | Dataset coding | The regex coding engine (`utils/jurimetric_coding.py`) is rule-based, not an AI model, but its rules were written by Claude | Classified 83,596 decisions into 21 governance categories plus rights, outcome and other flags | `utils/jurimetric_coding.py`; `validation/` | Author hand-coded 207 `not_water_related` decisions (May 2026); an LLM relabelled 91 decisions to estimate agreement (`validation/README.md`) | Which LLM and version did the relabelling; the prompts; outcome-coding validation (finding F-08) |
| 4 | Dataset validation | `validation/transformer_classifier.py` (XLM-RoBERTa fine-tuning) | Route A classifier prepared for the residual category | `validation/transformer_classifier.py` | none recorded | Whether it was ever run, and with which results, is not stated in the repository |
| 5 | Research assistant | Claude via the Anthropic API: `claude-haiku-4-5-20251001` (two agents) and `claude-opus-4-7` (one agent) | Answers research questions from the dataset | `research-assistant/agents.py:66,92,118`; `app.py:22` reads `ANTHROPIC_API_KEY` | A disclaimer in its README: "Responses reflect dataset patterns, not comprehensive legal research. It is not legal advice." | Whether any answers were published; what dataset content the agents send to the API (see section 4) |
| 6 | Review | Claude (Anthropic) | Most of title/abstract screening (26,222 records), full-text screening, extraction (92 fields, 1,072 studies), risk-of-bias appraisal, classification, synthesis drafting, and every script and document in the review | `AI_USE_STATEMENT.md`, `00_admin/AI_USE_LEDGER.csv`, `00_admin/STUDY_AUDIT_TRAIL.csv` | A human second reviewer on 3,665 title/abstract records and 197 full-text includes; the researcher adjudicated 262 further full-text decisions; nothing else is human-checked | Conversation prompts, model versions (only 60 early rows carry one), settings and seeds (`AI_USE_LEDGER.md`, "What is NOT archived") |
| 7 | Review | Codex (`gpt-5.6-sol`) | Blind second review of 91 full-text decisions; second-extraction checks | `_reviewer2_codex/` | counted as an AI-versus-AI check, not as human verification | The raw outputs are stored; the account or plan used is not stated |
| 8 | Review | Gemini (`gemini-3.1-flash-lite`; an earlier model hit a free-tier quota) | Blind second review of 21 full-text decisions; debate step | `_reviewer2_codex/AI_USE_AND_TOOLS_DISCLOSURE.md:22,127` | as above | Plan or tier used for the decisions actually kept |
| 9 | Review | An AI browser assistant ("Cowork") | Relayed some database searches the researcher ran through institutional access; helped retrieve full texts | `01_search/cowork_instructions_*`, `02_screening/full_text/COWORK_RETRIEVAL_INSTRUCTIONS.md` | The researcher ran the searches | Which exports passed through the assistant |
| 10 | Wiki and reader's guides, registers, tests, atlas | Claude (Anthropic) | Wrote START_HERE, GLOSSARY, registers, generators, tests, the atlas, the wiki pages and the audit documents | git history; the changelog; this file | The researcher reviewed and approved merges | Line-by-line human code review |

## 3. What the researcher decides and the AI does not

From the repository's own statements: the research question, protocol and eligibility criteria; running the database searches; supplying full texts; every ruling recorded under reviewer `CK` (made only after reviewing the evidence); closing and scoping decisions; approval of merges. The review's standing rule is that no `CK` confirmation is recorded unless the researcher has reviewed the evidence and instructed it.

## 4. Material that may have been sent to external AI services

This is the part of the AI use with the most serious open questions (finding F-19). From the records:

- **Licensed full texts and records.** The review's AI screening, extraction and second-model passes read full-text articles supplied by the researcher and bibliographic records exported from subscription databases. The records do not say, per file, which texts were sent to which service.
- **Unpublished material.** Screening decisions, adjudication sheets and working documents were exchanged with the services in interactive sessions.
- **Third-party personal data.** Records contain author names and, in some exports, e-mail addresses (finding F-05).
- **Dataset content.** The research assistant passes dataset content to the Anthropic API; what exactly is sent was not examined in this audit.

Not established by this audit, and not claimed either way: whether each service's terms at the time allowed the use, whether any service retained or trained on the inputs, whether any publisher's licence forbids AI processing of its text, and whether EUR's generative-AI guidance requires approval or a particular disclosure for such use. The terms and guidance were not read. See [`standards-matrix.md`](standards-matrix.md), rows S-04, S-05, S-10, S-14 and S-15.

## 5. Gaps and what to do

| Gap | Why it matters | Action | Who |
|---|---|---|---|
| Model versions, dates and prompts for the dataset-side work are not recorded | An AI-assisted result cannot be rerun or assessed | From now on record, for each AI task, the model identifier, the date, the instruction file and where the transcript is kept; add any transcripts that still exist | Researcher |
| Compliance with service terms and publisher licences is unknown | Possible breach; loss of control of unpublished work | Read the terms in force on the dates of use; ask the library about publisher text-and-data-mining terms; stop sending licensed text until confirmed | Researcher and library |
| EUR guidance on generative AI not compared with practice | Possible disclosure or approval duty | Read the guidance named in [`standards-matrix.md`](standards-matrix.md) and the graduate-school policy that applies; record the result | Researcher; graduate school |
| AI listed as an author in both `CITATION.cff` files (finding F-17) | Many venues do not accept AI authors | Move the AI tools to an acknowledgement unless the venue allows otherwise | Researcher |
| The words "AI-assisted" appear in the review's title but not in the dataset's | A reader of the dataset may not notice the AI role in the coding rules | Add a one-line note to the dataset's description (the README already has the AI Disclosure section) | Researcher |

## 6. Suggested wording for a methods section

*This is a draft for the researcher to adapt. It states only what the repository supports.*

> Scrapers, the coding engine and the data-processing scripts were written with the assistance of Claude (Anthropic) and reviewed by the author. The coding rules classify decision summaries by regular expressions; their precision for the water/not-water filter was estimated on a hand-coded sample of 207 decisions, and agreement on a 91-decision sample was estimated against an LLM relabelling, not against a second human coder. Outcome coding for Brazilian decisions has not been validated. The systematic review companion project used AI models for most screening, extraction and appraisal; the extent of human verification is stated in `00_admin/AI_USE_LEDGER.md`. Model versions and prompts for most AI work were not archived.

If the sentences above are changed, change them for a reason you can state; do not add claims of review or validation that did not happen.
