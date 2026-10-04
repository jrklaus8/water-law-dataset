#!/usr/bin/env python3
"""Assemble a full manuscript DRAFT (title, abstract, introduction, methods, results, discussion, limitations, conclusion, declarations) from
the verifier-checked generators, so every number in it is computed and the draft cannot drift from the data.

Sources, all generated: build_manuscript_pieces (methods, PRISMA paragraph, limitations), build_preliminary_report (evidence description, syntheses,
interpretations, confidence), current_figures (headline numbers). Prose that is neither computed nor lifted from those generators is limited to the
framing sentences below, marked [author to confirm] where it asserts something the repository cannot. No literature citations are invented: every
place a reference is needed is a bracketed [ref] for the author.

Output: 07_manuscript/draft/MANUSCRIPT_DRAFT_2026-10-04.md. Nothing here has been reviewed by a human author; it is a starting point, not a submission.
Run from the project root: python3 code/analysis/build_manuscript_draft.py
"""
import re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402
import build_manuscript_pieces as bmp  # noqa: E402
import build_preliminary_report as bpr  # noqa: E402

ROOT = cf.ROOT
OUT = ROOT / '07_manuscript/draft/MANUSCRIPT_DRAFT_2026-10-04.md'


def sections(md, level):
    """Split markdown into {heading text: body} at the given heading level ('##' or '###')."""
    parts = re.split(rf'^{level} (.+)$', md, flags=re.M)
    out = {parts[i].strip(): parts[i + 1].strip('\n') for i in range(1, len(parts) - 1, 2)}
    if level == '###':  # a ### body must stop where the next ## section starts
        out = {k: re.split(r'^## ', v, flags=re.M)[0].strip('\n') for k, v in out.items()}
    return out


def pick(d, prefix):
    for k, v in d.items():
        if k.startswith(prefix):
            return v
    raise KeyError(prefix)


def demote(text, by=1):
    return re.sub(r'^(#+) ', lambda m: '#' * (len(m.group(1)) + by) + ' ', text, flags=re.M)


def exclusion_table(F):
    flat = re.sub(r'\s+', ' ', (ROOT / 'README.md').read_text(encoding='utf-8'))
    m = re.search(r'E01 wrong topic.*?E12 wrong study design \d+', flat)
    labels = {c: l.strip() for c, l in re.findall(r'(E\d\d) ([a-z][a-z ,/\-]*?) \d+', m.group(0))} if m else {}
    rows = ["| Code | Reason (as labelled in the README) | Full-text exclusions |", "|---|---|---|"]
    rows += [f"| {c} | {labels.get(c, '')} | {k} |" for c, k in F['exclusion_by_code'].items()]
    return "\n".join(rows)


def build():
    F = cf.compute()
    n, inc = F['extraction_rows'], F['full_text_include']
    rpt = bpr.build()
    top = sections(rpt, '##')
    sub = sections(rpt, '###')
    man = sections(bmp.build(), '##')
    fam = F['effect_size_by_family']
    T = F['tools']
    mcn = F['mechanism_certainty_numeric']
    L = ["# The Legal Last Mile: Legal and Administrative Conditions and Access to Water and Sanitation — An AI-Assisted Systematic Review and Structured Evidence Synthesis", "",
         "> **DRAFT (generated 2026-10-04) — NOT REVIEWED BY A HUMAN AUTHOR, NOT FOR SUBMISSION.** Every number is computed from the repository's databases by `code/analysis/build_manuscript_draft.py` and checked by `verify_repository.py`. "
         "Items in [square brackets] need the author. No literature reference has been invented: each [ref] marks where the author must cite. The review was conducted by an AI under the researcher's direction, "
         "largely without independent human verification (see Methods 2.9 and Limitations); the protocol was **not registered before the work was done**. Section 4 (Discussion) contains interpretation, labelled as such.", "",
         "## Abstract (structured; draft)", "",
         "**Background.** Physical water and sanitation infrastructure does not guarantee that households can obtain a connection or use it effectively; legal and administrative conditions (eligibility screening, documentation and tenure requirements, fees, discretion, enforcement) may stand between infrastructure and access. "
         "[Author: one sentence of context with refs.]", "",
         "**Objective.** To map and synthesise the empirical evidence on how legal and administrative institutions shape the translation of physical availability of water and sanitation infrastructure into effective household access, "
         "and to synthesise quantitative evidence where it is comparable.", "",
         f"**Methods.** An AI-assisted systematic review: 34,594 records from multiple databases (27,481 after deduplication) were screened at title/abstract level and {F['full_text_decided']:,} full texts assessed; {inc:,} studies were included, extracted into a {n:,}-row database, and appraised with the instrument matching each design "
         "(RoB 2, ROBINS-I, JBI, MMAT, CASP, AMSTAR 2, and a project-specific non-validated framework for legal-documentary studies). Quantitative findings were synthesised without meta-analysis (SWiM). The protocol was not registered in advance; most steps were carried out by a large language model with partial human verification.", "",
         f"**Results.** {n:,} studies (85% since 2010) spanned many countries (India, Brazil, South Africa, the United States and Ghana the most frequent), but only {F['causal_capable_designs']} ({100 * F['causal_capable_designs'] / n:.0f}%) used designs able to support a causal claim. "
         f"{F['effect_size_rows']} studies had an extractable effect-size row; none could be pooled. In three SWiM families the direction of association was mostly favourable to recognition/eligibility (Family A, k = {fam['A']}), uniformly favourable or mixed for administrative assistance (Family B, k = {fam['B']}), and without a dominant direction for administrative barriers and ownership (Family C, k = {fam['C']}). "
         f"Only {F['reviewer_2_confirmed_includes']} inclusion decisions and no extracted value have been independently verified.", "",
         "**Conclusions.** The literature documents associations between legal/administrative conditions and access across many settings far more often than it establishes causal effects; it does not support one pooled estimate. Confidence is low to very low for any causal or comparative claim. [Author to revise after human verification.]", "",
         "**Registration.** Not registered before conduct [author: state OSF identifier if registered retrospectively and label it retrospective].", "",
         "## 1. Introduction", "",
         "[Author: write the background with references. The paragraphs below state the argument the repository supports; they are not cited.]", "",
         "Access to water and sanitation is usually measured by infrastructure coverage, but a household within reach of a network may still be unable to connect, or to keep and use a connection, because of legal and administrative conditions: "
         "who is recognised as eligible, what documents or tenure the application requires, what it costs, how much discretion officials hold, and how rules are enforced or reviewed [ref]. "
         "This review calls the gap between physical availability and effective access the *legal last mile*. The term organises the question; it is not assumed to be established by the evidence (`PROJECT_SPEC.md` §14).", "",
         "The relevant evidence is scattered across disciplines and designs — public administration, economics, law, geography, public health, development studies — and across mechanisms and outcome measures that are rarely comparable [ref]. "
         "No prior synthesis, to the authors' knowledge, maps this evidence with a mechanism-based framework [author to verify against the literature].", "",
         "**Objectives.** (1) Describe the empirical evidence on legal and administrative conditions and access to water and sanitation, by design, setting, mechanism and outcome. "
         "(2) Synthesise quantitative evidence where exposure, comparator, outcome and effect measure are comparable enough to do so defensibly, and otherwise report the direction of association transparently. "
         "(3) State what the evidence base does and does not allow us to conclude, including how reliable the review's own process is.", "",
         "### 1.1 Conceptual framework", "",
         "Structural conditions (legal and property status, documentation, income, geography, institutional capacity) act through an administrative architecture (eligibility screening, administrative burden, discretion, accommodation, enforcement, review, participation) "
         "and administrative navigation (understanding requirements, applying, satisfying requirements, obtaining accommodation, challenging decisions) to produce service access (formal connection, continuity, reliability, quantity, affordability, effective use) and, ultimately, inclusion or exclusion (`PROJECT_SPEC.md` §5). "
         "Administrative law is the central lens, not the only candidate cause; property, planning, municipal, utility-regulatory and political institutions are in scope.", "",
         "## 2. Methods", "",
         "### 2.1 Design, protocol and registration", "",
         "The review followed a written protocol (`PROTOCOL.md`, PRISMA-P style), the PRISMA 2020 reporting guideline [ref], and SWiM guidance for synthesis without meta-analysis [ref]. "
         "**The protocol was not registered before the work was done**: an OSF Generalized Systematic Review registration was drafted (`00_admin/preregistration/`) but not submitted [author: if registered now, declare it retrospective]. "
         "The title was amended on 2026-09-28 to state AI assistance; the research question, eligibility criteria and synthesis approach were not changed (`PROTOCOL.md` §12).", "",
         "### 2.2 Research questions and eligibility", "",
         "The primary question asked how legal and administrative institutions shape the translation of physical availability of water and sanitation infrastructure into effective household access, and what evidence exists on the mechanisms by which eligibility screening, administrative burden, discretion, accommodation and enforcement produce or mitigate exclusion. "
         "The secondary question asked, where evidence is sufficiently comparable, for the magnitude of association between specific legal or administrative conditions and access outcomes. "
         "Studies were eligible if they examined water or sanitation access, examined a legal, administrative, institutional, regulatory or governance factor, and contained empirical evidence or a systematic empirical synthesis with an access-relevant outcome and an identifiable design; "
         "English, Portuguese and Dutch were eligible without translation (`INCLUSION_EXCLUSION.md`). Qualitative socio-legal studies were not excluded for being unpoolable.", "",
         "### 2.3 Search and selection", "",
         f"Searches closed on {bmp.SEARCH_CLOSED}; SSRN and Westlaw/Lexis were not searched (`SEARCH_PROTOCOL.md`, README Known limitations). "
         "Selection was by an AI first pass (title/abstract and full text) with written rationales and standardised exclusion codes (E01–E12); a human second reviewer covered the "
         f"{bmp.TA_HUMAN_PASS:,} title/abstract records the AI marked include or unsure, and confirmed {F['reviewer_2_confirmed_includes']} of the {inc:,} full-text includes. "
         "Full-text retrieval was closed by the researcher's decision with 1,383 title/abstract includes never assessed; the unassessed set is older on average (see 3.1).", "",
         "### 2.4 Data extraction", "",
         f"A 92-field extraction form (`CODEBOOK.md`) was completed for every included study by the AI, largely from full text; {F['abstract_only_extractions']} studies were extracted from abstract or metadata only and an audit found further rows with signs of shallow extraction (Limitations). The AI later re-read {bmp.reextraction_counts()[0]} studies from full texts found in the researcher's Drive; of the {bmp.reextraction_counts()[1]} rows flagged only by the sparse-record audit, {bmp.reextraction_counts()[2]} had an abstract-level extraction that was materially wrong or incomplete (`reextract_2026-10-04/CAMPAIGN_NOTES.md`). There was no second extractor. "
         "A seeded sample for human second extraction has been prepared (`03_extraction/second_extractor/`) but not yet completed.", "",
         "### 2.5 Risk of bias and critical appraisal", "",
         f"Each study was appraised with the instrument matching its design: RoB 2 (cluster variant) for randomised trials ({T['RoB 2']}), ROBINS-I ({T['ROBINS-I']}), JBI cross-sectional ({T['JBI Cross-Sectional']}), MMAT ({T['MMAT']}), CASP qualitative ({T['CASP Qualitative']}) and AMSTAR 2 for systematic reviews ({T['AMSTAR 2']}). "
         f"For {T['Legal Framework']} legal-documentary or doctrinal studies no published instrument fits, and this project's own **non-validated** Legal Institutional Evidence Appraisal Framework was used; {T['NONE']} studies were judged not appraisable. "
         "Ratings were assigned by rule from the extracted fields, not by signalling-question reading of each paper, except for the studies re-appraised from full text (listed in `CHANGELOG.md`). Ratings therefore describe the extraction as much as the paper.", "",
         "### 2.6 Synthesis", "",
         "Studies were coded to four mechanism families (eligibility, burden, discretion/accommodation, enforcement) and outcome families (formal connection, effective access, economic access, administrative outcomes) that are not pooled with each other. "
         f"A feasibility judgment (`phase11_quantitative_feasibility_judgment.md`) concluded that no family reaches the bar for meta-analysis, so {F['effect_size_rows']} effect-size rows were compiled into three structured syntheses reporting direction and significance of each study's own estimate (SWiM). "
         + bmp.family_fit_clause() + " "
         "No effect was converted to a common scale. Sensitivity analyses removed abstract-only and shallow extractions, the one row for a study not flagged eligible, linked reports and two coding judgment calls.", "",
         "### 2.7 Secondary reviews", "",
         "Systematic reviews in the corpus are treated as secondary evidence and never pooled as if primary; their primary studies may also be in the corpus (a double-counting risk assessed only in part, Limitations).", "",
         "### 2.8 Data and code", "",
         "All databases, scripts and generated figures are in the project repository; `python3 code/analysis/verify_repository.py` re-derives every quoted figure and checks that generated files are current.", "",
         "### 2.9 Use of artificial intelligence", "",
         demote(man['1. Methods — AI-assisted conduct and disclosure'].split('\n\n')[0], 0), "",
         "## 3. Results", "",
         "### 3.1 Search and selection", "",
         pick(man, '2. Results').split('\n\n')[0], "",
         "Reasons for full-text exclusion (standardised codes; per-record rationale in `exclusion_log.csv`):", "",
         exclusion_table(F), "",
         "### 3.2 Characteristics of the included evidence", "",
         "*Figures 1–3 and 5 (`06_outputs/figures/fig1_design_mix.svg`, `fig2_publication_years.svg`, `fig3_countries.svg`, `fig5_appraisal_tools.svg`) show the design mix, publication years, countries and appraisal instruments; Figure 4 (`fig4_direction_by_family.svg`) shows the direction of association in the three syntheses (Section 3.5). All are generated from the databases by `code/analysis/build_figures.py`.*", "",
         demote(pick(sub, '2A.1'), 0).replace('**Volume and recency.**', '**Volume and recency.**'), "",
         "### 3.3 Mechanisms and outcomes addressed", "",
         pick(sub, '2A.2'), "",
         "### 3.4 Risk of bias and confidence in the evidence", "",
         f"Appraisal ratings are rule-based and, for most studies, depend on what was extracted (Methods 2.5). Of the {T['JBI Cross-Sectional']} JBI cross-sectional studies, {F['jbi_high_concern']} were rated 'high concern', largely reflecting sparse extraction rather than demonstrated weakness. "
         f"ROBINS-I ratings: {', '.join(f'{k} {v}' for k, v in F['robins_i_ratings'].items())}. RoB 2 ratings: {', '.join(f'{k.strip()} {v}' for k, v in F['rob2_ratings'].items())}; two of the randomised-trial studies (S294 and S366) report the same trial. "
         f"A numeric mechanism-certainty code of 3 or 4 (quasi-experimental or experimental) was recorded for {mcn['3'] + mcn['4']} studies, but only some of these are ROBINS-I or RoB 2 studies, a coding inconsistency reported in `DATA_QUALITY_AUDIT_2026-09-29.md` §5.", "",
         pick(sub, '3.4 Unresolved classifications').split('**Do the randomised')[0].strip(), "",
         "### 3.5 Quantitative evidence: three structured syntheses", "",
         pick(sub, '2A.3').split('Examples as extracted')[0].strip(), "",
         "Per-study results (exposure, outcome, direction, appraisal rating) are tabulated in the three family documents (`06_outputs/supplementary/family_*_swim_synthesis_2026-09-28.md`).", "",
         "**Sensitivity analyses.** " + re.search(r'\*\*Sensitivity of these counts\*\*(.*?)(?=\n\n|$)', pick(sub, '2A.3'), re.S).group(1).strip(), "",
         "**Reporting bias and certainty.** No publication-bias assessment was possible: although Families A and C each contain 20 studies, no common effect metric exists, so no funnel-plot or small-study analysis is defined (`ANALYSIS_PLAN.md` §9 requires about ten studies on a common scale). "
         "Certainty of evidence was **not** graded with GRADE; the direction-of-association syntheses carry no certainty rating and the overall confidence statement in Section 5.1 is qualitative.", "",
         "### 3.6 Qualitative, doctrinal and mixed-methods evidence", "",
         pick(sub, '2A.4'), "",
         "### 3.7 Gaps in the evidence base", "",
         pick(sub, '2A.5'), "",
         "## 4. Discussion", "",
         "*This section is interpretation. Each point rests on the numbers cited in Section 3 and could be wrong.*", "",
         pick(top, '2B.').strip(), "",
         "## 5. Limitations", "",
         pick(man, '3. Limitations'), "",
         "### 5.1 Confidence in the evidence and in the review's own process", "",
         pick(sub, '3.1 Overall confidence'), "",
         "### 5.2 Incomplete screening", "",
         pick(sub, '3.2 Incomplete screening'), "",
         "### 5.3 Missing or thin data", "",
         pick(sub, '3.3 Missing or thin data'), "",
         "## 6. Conclusion", "",
         f"The evidence assembled here shows that legal and administrative conditions are studied in association with water and sanitation access across a wide range of settings, most often descriptively and rarely with designs able to support causal claims ({F['causal_capable_designs']} of {n:,} studies). "
         "Where quantitative estimates exist they are too heterogeneous to pool, and their direction is most consistent for legal recognition and eligibility and for administrative assistance, least consistent for administrative barriers and ownership. "
         "These statements are provisional: extraction and appraisal were AI-conducted and only partly verified, screening of the full-text pool is incomplete, and the protocol was not registered in advance. "
         "The review does not establish the *legal last mile* as a general mechanism; it describes where evidence exists, where it is thin, and what a human-verified update would need to check first. [Author to revise.]", "",
         "### 6.1 Implications for research and practice", "",
         "*Conditional on human verification.* (1) Policy readers should not take this review as evidence that any single legal or administrative reform causes better access; the designs that could show that are few. "
         "(2) The next research step the repository supports is verification, not expansion: complete the human second pass of screening and a second extraction, fetch the full texts of the shallow extractions and the unassessed older records, and finish the check of overlap between the AMSTAR 2 reviews and the primary studies. "
         "(3) If the comparative frame of the underlying doctoral project (Netherlands, Canada, Brazil) is to be tested, targeted searches for Dutch and Canadian evidence are needed, because the corpus holds very few single-country studies for the first two (Section 3.7).", "",
         "## 7. Declarations", "",
         "- **Funding and competing interests:** [author to complete — prompts in `00_admin/disclosures/FUNDING_AND_COMPETING_INTERESTS_TEMPLATE.md`; PRISMA items 25 and 26].",
         "- **AI use:** Claude (Anthropic) performed most screening, extraction, appraisal and synthesis drafting; see `AI_USE_STATEMENT.md` for the stage-by-stage table. [Model versions and dates: add per journal policy.]",
         "- **Author contributions:** [author to complete; AI is not an author].",
         "- **Data and code availability:** repository (`README.md`); source PDFs are not redistributed.",
         "- **Ethics:** secondary analysis of published literature; [author to confirm no approval required].", "",
         "## References", "", "[Author: references to be added where marked [ref]. The repository's `SOURCES.md` lists the methodological sources already used (PRISMA 2020, SWiM, RoB 2, ROBINS-I, JBI, CASP, MMAT, AMSTAR 2).]", ""]
    text = "\n".join(x for x in L if x is not None).replace('\n\n\n', '\n\n')
    # the lifted paragraphs were written for the preliminary report: re-point its section numbers and voice at the manuscript's
    for old, new in (('§2A.1', 'Section 3.2'), ('§2A.2', 'Section 3.3'), ('§2A.3', 'Section 3.5'), ('§2A.5', 'Section 3.7'), ('see 2A.2', 'see Section 3.3'), ('§3.4', 'Section 3.4'),
                     ("this report's own observation, not a project ruling", "an observation of this draft, not a project ruling"), ('supplied by you', 'supplied by the researcher')):
        text = text.replace(old, new)
    return text + "\n"


if __name__ == '__main__':
    OUT.write_text(build(), encoding='utf-8')
    print('wrote', OUT.relative_to(ROOT))
