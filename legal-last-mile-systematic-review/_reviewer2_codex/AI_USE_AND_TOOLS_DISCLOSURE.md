# AI tools and methods disclosure — independent second-reviewer pass (2026-10-03)

This document exists so another researcher, an editor, or an auditor can see **exactly** what AI tools were
used, how they were configured, what they were and were not allowed to see, and how to reproduce or extend the
work, without having to read the scripts. It supplements `AI_USE_STATEMENT.md` (the repository-wide disclosure)
with the technical detail specific to this pass. Nothing described here changed `full_text_screening_database.csv`
except through the single, auditable path in "What was written to the database" below.

## Why this pass exists

The repository's own `00_admin/DECISIONS_AND_OPEN_ITEMS.md` (items A2 and A6) and `AI_USE_STATEMENT.md` disclosed
a provenance gap: every full-text screening and extraction decision up to 2026-10-03 was made by one model family
(Claude, Anthropic) with no independent second reviewer except a human PI on 200 of 1,159 includes. This pass adds
a **second, architecturally independent review** using two different model families (OpenAI's Codex, Google's
Gemini) so that a disagreement reflects something other than the same model agreeing with itself.

## Tools used

| Tool | Role | Version / model | How invoked |
|---|---|---|---|
| **Codex CLI** (OpenAI) | Primary independent reviewer: blind full-text screening, extraction-field checks, second-extractor checks, one side of the AI-vs-AI debate | `codex-cli` 0.160.0 (updated from 0.130.0 mid-session — the old version could not parse the current OpenAI models API and failed every call); model `gpt-5.6-sol`, `model_reasoning_effort="high"` | `codex exec --skip-git-repo-check -s read-only -m gpt-5.6-sol -c model_reasoning_effort="high" -o <tmpfile> -` with the prompt piped to stdin. The `-s read-only` sandbox flag means Codex cannot write to, or execute anything in, the repository — it can only read the prompt and respond. |
| **Gemini CLI** (Google) | Second independent reviewer (same screening/extraction tasks) and the other side of the AI-vs-AI debate | `gemini-2.5-flash` tried first; hit a hard-coded daily quota of 20 requests on the researcher's free-tier API key (`generativelanguage.googleapis.com` free tier) and was switched to **`gemini-3.1-flash-lite`** (500 requests/day on the same key) for the bulk of the run | `gemini -m gemini-3.1-flash-lite -p "<instruction>"` with the task prompt piped to stdin; `GEMINI_CLI_TRUST_WORKSPACE=true` set so the non-interactive CLI does not block on a workspace-trust prompt it cannot show in a headless run. |
| **Claude Octopus** (`nyldn/plugins` marketplace) | Attempted orchestration layer for multi-model dispatch | v9.38.0 (repo itself is at v11.10.0; not updated) | Its `scripts/orchestrate.sh spawn codex ...` path was tested but is **not actually what ran the work** — see "What Octopus did and did not do" below. |
| `pdftotext` (poppler, via MSYS2/Git-Bash `mingw64`) | PDF text extraction | — | `pdftotext -layout <pdf> <txt>`, plain-text layout mode, no OCR |
| `pypdf` 6.10.2 | PDF validity check only (not used for extraction) | — | Used once to sanity-check that downloaded bytes were real PDFs |

**Claude** (the model running this session, Claude Sonnet 5 at the time of this work) wrote every script in this
directory, decoded and downloaded the PDFs from the researcher's Google Drive, read and interpreted every model
response, decided what to record and how, and wrote this document. Claude did not independently re-screen any
paper as a third rater in this pass — its role here is **orchestrator and auditor of the other two models'
work**, not a third independent voice. That distinction matters: a disagreement in this pass is Codex-vs-Gemini
(or either vs. the original Claude screening decision), never Claude-vs-Claude.

## What Octopus did and did not do

The user asked to use the installed Claude Octopus plugin for this work. In practice:
- Octopus's own multi-agent orchestrator (`orchestrate.sh spawn <agent>`) was tested and did launch a Codex
  subprocess successfully once the Codex CLI itself was updated. But orchestrating ~250 individual model calls
  (one per paper, two providers, two phases) through Octopus's job-tracking layer (state files, PID tracking,
  result files per task ID) added overhead with no benefit over calling the CLIs directly from a Python script,
  and Octopus's installed version (9.38) does not match the cloned reference repo (11.10) the user had looked at.
- **What actually ran the work**: custom Python scripts in this directory (`run_codex_reviewer2.py`,
  `run_second_extractor.py`, `run_debate.py`) that call the Codex and Gemini CLIs directly as subprocesses, with
  the same safety posture Octopus would use (`-s read-only` sandbox for Codex) but with explicit, auditable
  control over the prompt, the model, the blinding (see below), and the retry/caching logic.
- This is disclosed plainly rather than overstating Octopus's role: the user should not read this repository's
  CHANGELOG and conclude Octopus's orchestration layer screened these papers. It did not. The two underlying AI
  CLIs that Octopus is designed to wrap are what did the work, invoked directly.

## The screening protocol given to each model (blinding)

For full-text re-screening, each model call included, verbatim:
1. The complete text of `INCLUSION_EXCLUSION.md` (the project's own criteria).
2. A restated checklist (the same six questions `02_screening/full_text/REVIEWER_2_CHECKLIST.md` gives a human
   second reviewer).
3. The paper's text, extracted by `pdftotext -layout`, truncated to 160,000 characters if longer (no paper in
   this run was long enough for this to matter materially — see token/cost notes below).

**What each model never saw in phase 1:** the original AI's decision (`ai_decision`), its exclusion code, or its
one-line reasoning (`ai_reasoning_READ_AFTER_YOUR_OWN_JUDGMENT`). This is the same blinding principle the human
reviewer-2 checklist itself prescribes ("Form your own decision first... Only then read the last column"). The
model was asked to return a decision, a per-criterion yes/no/unclear breakdown, a 2-4 sentence rationale citing
page/section, and a confidence label, as a single JSON object.

For the subset of papers the first reviewer (the original AI) had marked `include`, a **second, separate call**
(phase 2) showed the model the paper plus ten extracted-database fields (`country`, `study_design`,
`population`, `sample_size`, `urban_rural`, `service_provider`, `regulatory_model`, `effect_measure`,
`effect_estimate`, `extraction_note`) and asked it to say, field by field, whether the paper supports the
extracted value — again returning page/section citations, not a bare yes/no.

The second-extractor pass (`run_second_extractor.py`) used the same blind-then-check pattern but against the
`03_extraction/second_extractor` sample's own nine fields (`publication_year`, `country`, `sample_size`,
`study_design`, `effect_estimate`, `risk_of_bias_tool`, `mechanism_certainty`, `outcome_flags`,
`mechanism_flags`), one call per study covering all nine fields at once.

## How disagreement was handled — nothing was auto-corrected

Every model response is machine-parseable JSON, saved verbatim (`results/<record_id>.json`,
`results_gemini/<record_id>.json`, with the full raw model output preserved alongside the parsed fields, so a
human can always re-read exactly what the model said). A result was only written to
`full_text_screening_database.csv` through `code/screening/update_full_text_record.py` — the repository's own
validated writer, which refuses malformed enum values and writes atomically. The rule applied:

- **Agreement** (independent model's include/exclude matches the original AI's, and for excludes the exclusion
  code also matches): `reviewer_2` set to the model's label, `conflict = false`, `final_decision` set to the
  agreed decision. This mirrors exactly how the 200 human-confirmed includes were already recorded.
- **Disagreement** (different decision, or same decision but a different exclusion code): `reviewer_2` set,
  `conflict = true`, **`final_decision` left blank**. The repository's own `DATA_DICTIONARY.md` reserves
  `final_decision` for "after conflict resolution" — resolving it is explicitly not something this pass does.
  A one-line note was added to the record's `notes` field naming the independent model and its verdict, and
  where the second model's own result (when both Codex and Gemini reviewed the same record) disagreed with the
  first.

No row's `reviewer_1` field was touched (the original screening provenance, including its gaps, is preserved
exactly as audit finding 9 described it). No row's `full_text_decision` — the field that actually drives every
count in `CURRENT_FIGURES.md` — was changed by this pass; only `reviewer_2`, `conflict`, `final_decision` (on
agreement only) and `notes` were written, and every write was pinned to the record by `--record-id` and
validated by the existing script before being committed to disk.

## What was found (summary — see `REVIEWER_2_AGREEMENT_2026-10-04.md` for the full row-by-row report)

| | Tier 1 (no-reviewer includes/excludes) | Tier 2 (stratified sample of AI excludes) | Tier 3 (sample of AI includes) |
|---|---|---|---|
| Reviewed / in tier | 19 / 73 | 62 / 103 | 18 / 50 |
| Independent model's decision differs from the original AI | 3 | **32 (52%)** | 3 |

The tier 2 figure is the one that matters for the review's validity, because tier 2 is specifically a sample of
papers the AI chose to **exclude** — a wrong exclude silently removes an eligible study with no trace. Reading
the rationales (quoted in full in the agreement report), these look like genuine scope disagreements rather than
a model error: the independent reviewer typically points to an institutional/administrative determinant or an
empirical method in the paper that the original one-line exclusion reasoning did not address. This is now logged
as an addition to open item A2 and flagged prominently in `CHANGELOG.md` — **it is not resolved**, and resolving
it (reading the disputed papers and deciding) is explicitly left to the researcher, consistent with how every
other conflict in this database has always been handled.

## Cost, scale and timing

- 121 of the 226 tier 1-3 queue rows had a PDF available in the researcher's Google Drive at the time of this
  run (the rest need the researcher to supply full text before they can be checked this way).
- Each Codex call took roughly 15-90 seconds depending on paper length and reasoning effort; Gemini flash-lite
  calls took roughly 10-20 seconds. Both ran with 2-4 concurrent workers (a `ThreadPoolExecutor`), not
  sequentially.
- **Codex hit a usage-based quota mid-run** (ChatGPT/Codex plan limit, reset communicated as "Oct 4th, 2026
  3:23 AM"). Any call that failed this way was detected (the model's own error text, not a parse failure) and
  its cache entry deleted rather than kept as a false "no disagreement" result, so those records will retry
  cleanly once the quota resets rather than being silently skipped.
- **Gemini's free-tier daily quota (20 requests) was exhausted on the first model tried** (`gemini-2.5-flash`,
  which the quota dashboard reports under the billing name `gemini-3.5-flash`); switching to
  `gemini-3.1-flash-lite` (500/day on the same key, confirmed via the Gemini AI Studio dashboard) let the run
  continue. **Anyone reproducing this should check their own key's quota** at https://ai.dev/rate-limit before
  choosing a model, rather than assuming the model name in this document still has free-tier headroom by the
  time they read it — Google's free-tier model lineup and limits change over time.

## Known gaps and honest limitations

- **No human has adjudicated a single one of the 38 conflicts this pass created.** The independent model's
  verdict is not more authoritative than the original AI's — both are AI judgments on the same criteria, and
  the disagreement itself is the finding, not a resolution.
- **This is an AI-versus-AI check, not a human check.** It cannot certify an error rate the way a human
  reviewer-2 pass could (the queue README's own limits section already says this about sampling in general).
- **105 of the 226 tier 1-3 rows still have no PDF and were not touched.** The sample reviewed here is not
  guaranteed representative of those, though tier 2 and 3 are seeded random samples, so the 62-of-103 and
  18-of-50 reviewed so far are a reasonable (if partial) draw from an already-representative sample.
- **Two different Gemini models were used across the run** (a handful of early tier-1 records under
  `gemini-2.5-flash` before the quota was discovered, the remainder under `gemini-3.1-flash-lite`) — each
  record's own `results_gemini/<id>.json` records exactly which model produced it, so this is fully traceable,
  but it means "the Gemini reviewer" is not a single fixed model across every record.
- **The second-extractor pass and the AI-vs-AI debate on open items A3/A5/narrative-reviews were still running
  or had partial results at the time this document was first written** — check `run_2ndextractor_codex.log`,
  `run_debate.py`'s `debate/debate_summary.json`, and this file's own git history for whether they completed and
  what they found.

## How to extend or reproduce this

All scripts are plain Python (standard library plus `subprocess`), committed to `_reviewer2_codex/`:
- `decode_drive.py` — decodes base64 Drive downloads (saved by the Drive MCP tool when a file is too large to
  return inline) into real PDFs in `pdfs/`, skipping non-PDF payloads (Drive sometimes returns an HTML error
  page instead of a file; the script detects and skips these rather than writing corrupt PDFs).
- `run_codex_reviewer2.py --provider {codex,gemini} --tiers 1,2,3 [record_id ...]` — the main screening pass.
  Environment variables `R2_MODEL` and `R2_EFFORT` (Codex only) override the default model.
- `run_second_extractor.py --provider {codex,gemini} [study_id ...]` — the second-extractor field-check pass.
- `run_debate.py [question_key ...]` — the two-round AI-vs-AI debate on open methodological questions.
- `build_filled_queue.py` — compiles all `results*/` JSON into the FILLED queue CSV and the agreement report;
  safe to re-run at any time, reads only, never writes to the database.
- Every script caches its own results by file existence (`results/<id>.json` etc.) so re-running after adding
  more PDFs or after a quota resets only processes what is missing — it will not re-spend quota on records
  already done, but note the quota-exhaustion cache bug this session hit and fixed (search this file's git
  history, or `CHANGELOG.md` 2026-10-03, for "quota-error cache entries").
