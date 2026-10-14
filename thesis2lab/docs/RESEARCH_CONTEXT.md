# Research context

Treat everything here as context, not validated findings.

## Project
Working title: *The Legal Last Mile: Sanitation Governance and Administrative Law in Brazil, Canada (Ontario), and the Netherlands.*
Focus: the gap between legal obligations to provide sanitation services and actual access. Intended institution: Erasmus University Rotterdam. The doctoral application is in progress and admission is not confirmed. The thesis is not written; no chapter structure is agreed.

Concepts named by the researcher (not tested here): administrative law and implementation gaps, institutional fragmentation, administrative capacity, Bourdieusian field theory, administrative capital, the "administrative ghost", Most Different Systems Design.

## Known assets (inspected 2026-10-14, commit cf3542e of jrklaus8/water-law-dataset)
| Asset | State |
|---|---|
| Scrapers, jurimetric coding engine (`utils/jurimetric_coding.py`) | Present. Not wrapped as an experiment. |
| Raw decision data (83,596 records) | **Absent.** Excluded by `.gitignore`. EXP-003 is BLOCKED for this reason. |
| Validation folder (kappa inputs and results, residual audit) | Present. Basis of EXP-002. |
| `docs/The_Legal_Last_Mile_Research.pdf` | Present, registered, not extracted. Copyright status marked unknown until confirmed. |
| `legal-last-mile-systematic-review` project and S-prefixed records | **Not found** in the repository. |
| Bibliographic records for a real bibliometric study | Not available. EXP-001 therefore uses synthetic data. |

## Findings of this build about the source repository
1. `validation/kappa_results.json` holds only the 0.568 baseline; the 0.832 headline in README and RESIDUAL_AUDIT is reproducible from the committed labels but has no committed output file.
2. Two published confidence intervals for the same baseline kappa disagree, and neither could be regenerated exactly.
3. The 0.832 figure comes from a rule fixed after seeing the disagreements on the same sample.
4. The second coder is an LLM, so the exercise is a reproducibility audit of the regex filter rather than human inter-coder reliability.
These are reported neutrally in EXP-002 for the researcher to resolve.

## Unresolved questions for the researcher
- Which chapters will the thesis have, and in what order?
- Is the PDF redistributable? Is hashing case identifiers acceptable for public data?
- Name form: "Junior Klaus" (CITATION.cff) or "Claudio Klaus" (RESEARCH_CONTEXT.md)?
- Where do the systematic review records live, and what is their S-identifier scheme?
- Which court data licences allow a public subset of the 83,596 decisions?
- Is a human second coder planned to replace or complement the LLM coder?
- Which verified legal sources (statutes, regulations) should populate the comparative governance matrix?
