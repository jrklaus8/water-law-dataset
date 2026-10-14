# AI-use statement

**This is an AI-assisted systematic review.** A large language model (Claude, from Anthropic) carried out most of the
screening, data extraction, risk-of-bias appraisal, classification and synthesis drafting in this repository, working under
the researcher's direction and within a written protocol. The researcher (Claudio Klaus) set the question, the protocol and
eligibility criteria, ran the database searches, supplied the full texts, made the closing and scoping decisions, and
independently reviewed a part of the screening. The AI's outputs have **not** been independently verified in full. The
title carries the words "AI-Assisted" so that no reader has to discover this from the methods.

## What the AI did, and what a human checked

| Stage | AI role | Human role | Independently checked by a human |
|---|---|---|---|
| Search strategy, exports, deduplication | Wrote and ran scripts for deduplication and audits | Designed searches, ran them in the databases, exported records | Duplicate audits were also run by the AI; not independently re-checked |
| Title/abstract screening | First-pass decision and written rationale for each record | Second reviewer on the 3,665 include-plus-unsure records, not on the AI's 22,557 exclusions (99.8% agreement — flagged in the README as unusually high) | Yes, for those records |
| Full-text screening | Read each supplied full text and decided include/exclude with a coded reason | Obtained and supplied the full texts; confirmed 200 includes (S001–S100 on 2026-09-27, S101–S200 on 2026-10-02; 197 remain includes after the researcher's scope rulings of 2026-10-14) and, on 2026-10-13 and 14, adjudicated 262 further full-text decisions (172 exclusions, 90 inclusions; open items A16, A19, A22 to A25, A28 and A6), applying a narrow reading of criterion 2 adopted after the independent-model disagreement was seen | **The 197 confirmed includes and the adjudicated records**; no other excludes |
| Data extraction (92 fields) | Extracted every study, largely from full text; 10 studies from abstract or metadata only at release 0.2.0-interim (62 originally; the rest were re-extracted from Drive full texts in the campaigns of 2026-09-29 to 2026-10-09; see `code/provenance/audit_and_repair/reextract_2026-10-04/CAMPAIGN_NOTES.md`) (a floor: a 2026-10-04 audit found 71 more rows (after a further 56 were re-extracted or appraised from Drive full texts the same day) with signs of shallow extraction — 11 whose own notes say so and 22 whose recorded location cites only the abstract; see `05_analysis/descriptive/SPARSE_RECORD_AUDIT_2026-10-04.md`) | Supplied documents | **None**; no second extractor |
| Risk-of-bias appraisal | Rule-based batch ratings from extracted fields, using the published instruments' structure | Supplied the official instrument documents | **None**; not a signalling-question read of each paper. One instrument is the project's own and is not validated |
| Classification, effect-size table | Coded and classified | — | None |
| Structured (SWiM) syntheses, feasibility judgment | Drafted, with disclosed judgment calls | Approves and decides | None |
| This repository's audits and corrections | Found and corrected its own errors in the open | Approved merges and exclusions | — |

## Why you should still read it critically

- The same system produced and audited much of the work, so its checks find inconsistencies and arithmetic errors but cannot
  confirm that an extracted value matches its source paper. The source PDFs are not included in this public repository
  because many are subject to publisher copyright and licensing terms that do not permit their redistribution. Their
  absence reflects those legal and licensing restrictions, not a decision by the author to withhold the underlying sources.
- The audit found, and this repository corrected in the open, errors of the AI's own making: stale figures, two papers
  counted twice, a sign-versus-valence error in a synthesis, provenance gaps. See `AUDITING_GUIDE.md` §4 and
  `00_admin/audits/2026-09-28_repository_audit.md`. Assume more exist.
- Reviewer labels in the databases (`Claude-AI-fulltext-YYYY-MM-DD`, `Claude-AI-audit-…`, and older variants such as `Claude`)
  identify AI-made decisions; 73 decided full-text rows had no reviewer label recorded at the time; on 2026-10-14 (open item A2) an AI label, `Claude-AI-fulltext-2026-09-16`, was inferred for them from the exclusion log and extraction records and backfilled with a dated note. That label is inferred, not recorded, and it is not human review.
- No pooled estimate exists and none is claimed; the syntheses report direction of association, not effect size or GRADE certainty.

## A second AI tool appears in one file

`06_outputs/slides/Water_Access_Evidence_Diagnostic_slides_2026-09-29.pdf` is a slide summary of the preliminary report that the researcher produced
with a different AI tool (its footers read "A Gemini Notebook", i.e. Google NotebookLM). It is kept unaltered for reference; where it differs from the
current report the report is right — see `06_outputs/slides/README.md`. Nothing else in the repository was produced with that tool.

## Third and fourth AI tools: two independent second reviewers on part of the full-text decisions (2026-10-03/04)

To begin closing the provenance gap on full-text decisions with no independent check, 121 of the 226 reviewer-2 queue rows
(tiers 1-3; all those whose PDF was available at time of writing) were re-screened **blind** by two different model families — the Codex CLI (OpenAI,
`gpt-5.6-sol`) and the Gemini CLI (Google, `gemini-3.1-flash-lite` / `gemini-2.5-flash`) — each of which saw only the protocol
criteria and the paper, never Claude's decision or reasoning. Decisions are recorded in `full_text_screening_database.csv` under
`reviewer_2` labels `Codex-gpt-5.6-sol-reviewer2-fulltext-2026-10-03` / `Gemini-...`, with `conflict = true` where a model disagreed
and `final_decision` left to the researcher. **This is an AI-versus-AI check, not a human check**: it detects decisions that a
second model reads differently, it does not certify either side as correct.

**The main finding is a substantial disagreement rate on tier 2** (the stratified sample of the AI's own full-text excludes): of
62 excludes independently re-read, 32 (52%) were judged `include` by the independent model, concentrated in exclusion codes E01
"wrong topic" and E06 "engineering only." This has not been human-adjudicated and nothing was auto-corrected — every disagreement
is a `conflict = true` row awaiting the researcher. Full technical disclosure (exact tools, versions, prompts, blinding protocol,
known limitations, and how to reproduce or extend this work) is in `_reviewer2_codex/AI_USE_AND_TOOLS_DISCLOSURE.md`; the row-by-row
report is `_reviewer2_codex/REVIEWER_2_AGREEMENT_2026-10-04.md` (`CHANGELOG.md` 2026-10-03/04).

## Where to check

`AUDITING_GUIDE.md` (how to verify and challenge), `00_admin/DECISIONS_AND_OPEN_ITEMS.md` (what is undecided and what was a
judgment call), `00_admin/CURRENT_FIGURES.md` and `python3 code/analysis/verify_repository.py` (numbers re-derived from the data),
`code/provenance/` (the scripts that wrote the data), `CHANGELOG.md` (every change, dated).

## For manuscripts and citations

Any manuscript based on this work should state the AI use in its title or subtitle and methods, name the tool as "Claude
(Anthropic)", state which stages were AI-conducted using the table above, and report the verification status honestly.
Journals' and funders' AI-disclosure policies vary; check the target venue's before submission.

## Model and tool provenance, as logged

Exact model versions were **not** recorded decision by decision; what the repository does hold is listed here and is generated, with the dates, into the manuscript draft (`code/analysis/build_manuscript_pieces.py`, `ai_provenance_clause`).

| Work | Logged label or string | Dates |
|---|---|---|
| Title/abstract first pass (Claude, Anthropic) | `Claude-AI-1stpass-2026-09-10`, `Claude-AI-1stpass-2026-09-11` | 2026-09-10 to 2026-09-11 |
| Title/abstract second review (human) | `Human-reviewer2-2026-09-12` (3,665 records) | 2026-09-12 |
| Full-text decisions (Claude) | `Claude-AI-fulltext-YYYY-MM-DD`, `Claude-AI-audit-2026-09-28`; 60 early rows `claude_sonnet_5`; 519 legacy rows `Claude` / `claude` | 2026-09-12 to 2026-10-14 |
| Extraction and appraisal (Claude) | `Claude-AI-extraction-YYYY-MM-DD`, `Claude-AI-fulltext-YYYY-MM-DD` in `researcher` | 2026-09-12 to 2026-10-14 |
| Blind full-text second review (OpenAI) | `Codex-gpt-5.6-sol-reviewer2-fulltext-…`; Codex CLI 0.160.0, model `gpt-5.6-sol`, reasoning effort high | 2026-10-03 |
| Blind full-text second review (Google) | `Gemini-gemini-3.1-flash-lite-reviewer2-fulltext-…`; Gemini CLI, model `gemini-3.1-flash-lite` (`gemini-2.5-flash` was tried first and dropped at its daily quota) | 2026-10-03 to 2026-10-04 |

The only Claude version string in the data is `claude_sonnet_5` (60 rows) and "Claude Sonnet 5" in `_reviewer2_codex/AI_USE_AND_TOOLS_DISCLOSURE.md` for the 2026-10-03/04 sessions; for every other Claude decision only the stage and the date are logged, so a journal that requires the exact model version for those cannot be given one from the repository. The costs of Anthropic Claude and OpenAI Codex were paid personally by the author and the Google Gemini runs used the author's free-tier API key; the author has no relationship with any of the vendors (`00_admin/disclosures/FUNDING_AND_COMPETING_INTERESTS_TEMPLATE.md`).

*The per-decision reviewer labels and `CHANGELOG.md` dates identify when each AI decision was made.*
