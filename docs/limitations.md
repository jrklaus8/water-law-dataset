# Limitations

This page states, in one place, what the court-decision dataset and the systematic review cannot support, and what this audit could not check. It is meant to be quoted from: a reader or a reviewer should not have to dig for them. Each limitation points to the evidence. Limitations the researcher has already disclosed elsewhere are listed here as well so that nothing is hidden by being spread across files.

*Written by an AI assistant (Claude Code), 2026-10-27. Severity ratings, where given, are that assistant's judgment, not the researcher's or an independent reviewer's.*

## 1. The court-decision dataset

| # | Limitation | Why it matters | Evidence |
|---|---|---|---|
| L-01 | **Coverage was set by technical access, not by a sampling plan.** Only 8 of Brazil's 27 state courts were collected; 19 were blocked (CAPTCHA, single sign-on, server errors, timeouts). | Brazilian results cannot be taken to represent Brazil; courts that are easy to scrape are over-represented. TJDFT alone is 8,421 of the 11,724 Brazilian decisions (72%). | README "Brazilian Courts — Access Status"; [`source-register.md`](source-register.md) |
| L-02 | **Only decisions that reach a published court record are visible.** The research theory itself says the excluded never reach court. | The dataset cannot measure exclusion that does not litigate; any statement about "absorption before litigation" is an interpretation, not a measurement (F-10). | `RESEARCH_CONTEXT.md:55`; README "Known Limitations" |
| L-03 | **Coding uses decision summaries and metadata, not full decision text.** For the Netherlands the stored text is the summary field, truncated to 2,000 characters. | Outcome, reasoning and rights language that appear only in the body are missed; coverage differs by country. | `scrapers/netherlands/rechtspraak_scraper.py` (parse_content); `utils/jurimetric_coding.py` |
| L-04 | **Classification is by regular expressions**, written with AI assistance, applied in a fixed order (first match wins). | Rules can misclassify in ways that are invisible without a sample read by a person. | `utils/jurimetric_coding.py`; `tests/test_offline_helpers.py` |
| L-05 | **Outcome coding has known defects** in the "improper act" patterns (F-08, F-09) and has not been validated; outcome is coded for Brazil only. | Any statement about who wins in Brazil is unreliable until the patterns are corrected and the data re-coded. | `utils/jurimetric_coding.py:581-607`; expected-failure tests |
| L-06 | **Validation is partial and mostly single-coder.** The water/not-water filter was checked on 207 decisions coded by the author who designed the rules; agreement (κ) was checked against an LLM relabelling of 91 decisions, not a human second coder; governance categories and outcomes were not validated. | Reported precision and κ do not establish inter-coder reliability. | `validation/README.md`; F-22 |
| L-07 | **The Dutch collection is much wider than the water set.** About 98.56% of the 68,654 Dutch decisions are classified not water-related. | The headline total (83,596) overstates the number of water-law decisions; the "genuine water" Dutch set is about 989 decisions (RESEARCH_CONTEXT.md). | `wiki_key_findings.md`; `RESEARCH_CONTEXT.md` |
| L-08 | **Heterogeneous sources.** Eight Brazilian portals with different search engines, the CanLII API (metadata, title-based) plus a third-party semantic search, and the Rechtspraak feed. Court systems, languages and publication policies differ. | Cross-country comparisons of shares and counts mix retrieval effects with legal differences. | [`source-register.md`](source-register.md) |
| L-09 | **Not reproducible from the repository alone.** The data are not in the repository, collection dates and request logs were not kept, one scraper is missing, and live sites change. | The dataset can be inspected through its deposits but cannot be rebuilt identically. | F-12, F-23, F-30; [`reproducibility.md`](reproducibility.md) |
| L-10 | **Terms, anonymisation and permission to republish are not documented per source.** | The legal basis for collection and redistribution is unrecorded. | F-11; [`source-register.md`](source-register.md) |
| L-11 | **Software-quality gaps in the collection code**: TLS verification disabled in four scrapers, browser-imitating User-Agent in seven, hard-coded personal paths, no automated tests before this audit. | These affect the trustworthiness of what was recorded and the ease of rerunning it. | F-01, F-02, F-03, F-13 |

## 2. The systematic review

The review's own limits are catalogued, with ways to test each, in `legal-last-mile-systematic-review/00_admin/WEAKNESSES.md` (34 weaknesses at the time of writing; the severity ratings there are also an AI's judgment). The ones that most limit what it can claim:

| # | Limitation | Where stated |
|---|---|---|
| L-12 | AI did most screening, extraction and appraisal; human verification covers 459 of 2,277 full-text decisions (20.2%); no second extractor; extraction accuracy is unmeasured. | `AI_USE_STATEMENT.md`; `00_admin/CURRENT_FIGURES.md` |
| L-13 | Most risk-of-bias ratings are rule-based batch ratings, not a read of each paper against the instrument; one instrument ("Legal Framework") is the project's own and not validated. | `RISK_OF_BIAS.md`; AI-use ledger |
| L-14 | The protocol was fixed before searching but not registered; the decision to close searching and full-text retrieval (2026-09-28) left 1,382 candidates unassessed. | `PROTOCOL.md:3`; `CURRENT_FIGURES.md` |
| L-15 | No effect could be pooled; findings are direction-of-association counts, which ignore effect size, precision and sample size and do not support causal statements. One of the three conclusion tests fails at baseline (Family C raw sign). | `START_HERE.md`; `GLOSSARY.md`; atlas |
| L-16 | The three conclusion tests were written before the sensitivity scenarios but after the baseline counts existed. | `CHANGELOG.md` (review), error E29 |
| L-17 | Prompts, model versions and settings for most AI work are not archived; AI output is not deterministic. | `00_admin/AI_USE_LEDGER.md` |

## 3. What this audit could not check

| # | Not checked | Reason | Consequence |
|---|---|---|---|
| L-18 | Any policy, licence or terms page | No live fetches were made; the university site could not be opened from the audit environment; search summaries were the only source for institutional requirements | Every institutional and source-terms row in [`standards-matrix.md`](standards-matrix.md) is "awaiting confirmation" or "partially verified" |
| L-19 | The deposits at Zenodo, Dataverse, DANS and OSF | Not retrieved (no uploads, downloads or scale requests were authorised) | Deposit contents, licences and hashes are unknown |
| L-20 | The coded dataset | Not in the repository | Effect of the coding defects could not be measured |
| L-21 | The scrapers against live sites | Not authorised; offline fixtures only | Behaviour on real servers (including after the TLS and User-Agent questions are settled) is untested |
| L-22 | Python 3.8–3.10 | Interpreters not available | CI covers 3.8–3.12; locally the tests ran under 3.11, 3.12 and 3.13 only |
| L-23 | All 1,682 tracked files | The audit read the documents, scripts and registers named in the findings and ran pattern scans across the rest | Absence of a finding is not evidence of absence |
| L-24 | Independence | The audit was done by an AI assistant that also wrote parts of the code and documents it examined, and its findings have not been reviewed by a person | Treat the severity ratings and conclusions as a starting point for a human check |
