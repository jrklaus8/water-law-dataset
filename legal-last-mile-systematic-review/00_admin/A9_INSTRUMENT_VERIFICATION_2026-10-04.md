# A9 — appraisal-instrument wording verified against official publisher sources (2026-10-04)

Open item A9 (`00_admin/DECISIONS_AND_OPEN_ITEMS.md`) asked for the appraisal checklist item wording used in this
repository to be checked against the publishers' official texts; prior sessions could only reach this at
search-snippet level because the working environment's outbound network egress was blocked for direct page/PDF
fetches (`SOURCES.md`). This session ran with a different tool (an interactive `WebFetch`/`WebSearch` capability,
not the sandboxed script environment the rest of the pipeline runs in) that was **not** blocked, and used it to
fetch the primary sources directly rather than relying on search snippets.

## PRISMA 2020 (27-item checklist numbering and lettering)

**Source:** Page MJ, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. *BMJ*
2021;372:n71. Fetched in full from PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC8005924/ (open access, the
publisher-designated free full-text host).

**Result: confirmed correct, no changes needed.** Verbatim text was retrieved for items 8, 10a/10b, 13a-f,
16a/16b, 20a-d, 23a-d, 24a-c, 25, 26 and 27, and the numbering/lettering of every sub-item matches
`06_outputs/prisma/PRISMA_2020_CHECKLIST.md` exactly (including the already-corrected 3/4 split a 2026-09-28
session made from search-snippet evidence — that fix is confirmed right by the full-text source). No further
correction was needed to this file.

## AMSTAR 2 (16-item checklist, critical-domain designation)

**Source:** Shea BJ, et al. AMSTAR 2: a critical appraisal tool for systematic reviews that include randomised or
non-randomised studies of healthcare interventions, or both. *BMJ* 2017;358:j4008. Fetched in full from the
**official AMSTAR 2 guidance document** (the authors' own PDF, linked from amstar.ca, the tool's official site):
`https://amstar.ca/docs/AMSTAR%202-Guidance-document.pdf`. This is the authoritative primary source — the guidance
document is explicitly written to be a stand-alone restatement of the published paper's content, by the same
authors, for exactly this kind of appraisal use.

**Result: confirmed correct on every point checked, no changes needed.**

| Item | Official wording (core question) | Critical? | Matches this repo's appraisal forms (e.g. `04_quality/appraisal_forms/S328_AMSTAR2.md`)? |
|---|---|---|---|
| 1 | PICO components in the research questions and inclusion criteria | No | Yes |
| 2 | Review methods established prior to the review; deviations justified | **Yes** | Yes |
| 3 | Selection of study designs explained | No | Yes |
| 4 | Comprehensive literature search strategy | **Yes** | Yes |
| 5 | Study selection performed in duplicate | No | Yes |
| 6 | Data extraction performed in duplicate | No | Yes |
| 7 | List of excluded studies provided, with justification | **Yes** | Yes |
| 8 | Included studies described in adequate detail | No | Yes |
| 9 | Satisfactory technique for assessing risk of bias in included studies | **Yes** | Yes |
| 10 | Funding sources of included studies reported | No | Yes |
| 11 | Appropriate meta-analytic methods (if meta-analysis performed) | **Yes** | Yes |
| 12 | Impact of risk of bias on meta-analysis results assessed | No | Yes |
| 13 | Risk of bias accounted for when interpreting/discussing results | **Yes** | Yes |
| 14 | Heterogeneity explained and discussed | No | Yes |
| 15 | Publication bias investigated (if quantitative synthesis performed) | **Yes** | Yes |
| 16 | Conflicts of interest and review funding reported | No | Yes |

**The 7 critical domains are items 2, 4, 7, 9, 11, 13, 15** — this exact set is independently confirmed by a second
source (corates.org's AMSTAR 2 resource page, cross-checked separately) and matches the "Critical items: ..." line
already stated in every AMSTAR 2 appraisal form in `04_quality/appraisal_forms/`. The rating rule those forms
state ("no critical flaw = High or Moderate; one critical flaw = Low; more than one = Critically Low") also
matches the official guidance's framing of how critical-domain flaws should be weighted, though the guidance
document does not give that exact High/Moderate/Low/Critically-Low cut rule in so many words in the portions
fetched — that specific rule is standard AMSTAR 2 practice from the published paper's results section, not
something this check could confirm verbatim from the guidance document alone. Worth a researcher's own check
against the original BMJ paper's exact rating-rule wording before final submission, since that is the one detail
this pass could not fully pin down to a verbatim quote.

## SWiM 2020 (9-item synthesis-without-meta-analysis reporting guideline)

Not formally part of A9 (A9 names PRISMA 2020, AMSTAR 2, RoB 2, ROBINS-I, JBI, CASP, MMAT), but the same gap
existed for the same reason: `SOURCES.md` §7 had SWiM's citation and 9-item *structure* confirmed by search
snippet (2026-09-28), with item *wording* explicitly left unconfirmed. Fetched the guideline's own official
supplementary checklist PDF directly this pass.

**Result: confirmed correct, no changes needed.** All 9 items' exact wording matches
`06_outputs/supplementary/SWIM_SYNTHESIS_TEMPLATE.md`'s section mapping, including the "criteria used to
prioritise results for summary and synthesis" section added on 2026-09-28 from the structural check alone — its
wording ("the criteria used, with supporting justification, to select the particular studies ... for the main
synthesis") matches the official item 4 text exactly. `SOURCES.md` §7 and the template updated to record the
full-text confirmation.

## What this does and does not close

- **PRISMA 2020 and AMSTAR 2 wording and numbering are now verified against primary sources**, not search
  snippets. This closes the most consequential part of A9, since AMSTAR 2's item numbers (2, 4, 7, 9, 11, 13, 15)
  are cited by number repeatedly throughout `04_quality/appraisal_forms/` and `RISK_OF_BIAS.md`, and an error in
  which items are "critical" would have silently mis-rated every one of the 23 AMSTAR 2 studies.
- **RoB 2, ROBINS-I, JBI Cross-Sectional, CASP Qualitative and MMAT were not checked this pass** — time did not
  allow it in this session. These collectively drive many more ratings than AMSTAR 2 (JBI 140, MMAT 205, CASP
  263 studies, vs. AMSTAR 2's 23), so verifying them the same way (official tool PDF, not search snippet) is the
  natural next step and should be prioritized over AMSTAR 2 was, precisely because of that larger exposure.
- The source PDF (`AMSTAR 2-Guidance-document.pdf`, the authors' own freely downloadable appraisal guidance, not
  one of the review's primary-study papers) was used for this verification but is **not committed to this
  repository**, consistent with the project's practice of citing and quoting external sources rather than bulk
  storing them; the quoted passages above are the evidentiary record, and the document is a public download at
  the URL cited.
