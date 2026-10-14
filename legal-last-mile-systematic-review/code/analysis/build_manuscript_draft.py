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
import build_manuscript_pieces as bmp
import manuscript_supplement as msup  # noqa: E402
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


# references of the Introduction: (key in the text, study_id of the included record); the reference lines are built from the extraction rows so they match the database
INTRO_REFS = [('Abdulhadi', 'S350'), ('Alam', 'S537'), ('Bakker', 'S1000'), ('Criqui', 'S1165'), ('Hackenbroch', 'S652'), ('Hendraputra', 'S344'), ('Nelson', 'S372'), ('Olmstead', 'S1169')]
METHOD_REFS = ["Campbell, M., McKenzie, J. E., Sowden, A., Katikireddi, S. V., Brennan, S. E., Ellis, S., et al. (2020). Synthesis without meta-analysis (SWiM) in systematic reviews: reporting guideline. *BMJ*, 368, l6890. https://doi.org/10.1136/bmj.l6890",
               "Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., et al. (2021). The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. *BMJ*, 372, n71. https://doi.org/10.1136/bmj.n71"]


def _reference_lines():
    ed = {r['study_id']: r for r in cf.read('ed')}
    lines = []
    for key, sid in INTRO_REFS:
        r = ed[sid]
        assert key.lower() in r['citation'].lower(), (key, sid)
        cit = r['citation'].rstrip('.').replace('"Behaviour', 'Behaviour').replace('scoping review."', 'scoping review.') if key == 'Alam' else r['citation'].rstrip('.')
        lines.append((key, f"{cit}." + (f" https://doi.org/{r['doi']}" if r['doi'].strip() else '')))
    lines += [(m.split(',')[0], m) for m in METHOD_REFS]
    out = []
    for _, line in sorted(lines, key=lambda x: x[0].lower()):
        out += [line, ""]
    return out


def _rob2_double_reports(F):
    """Number of RoB 2 reports that repeat another RoB 2 report of the same trial (definite same-data links between two RoB 2 studies)."""
    rob2 = {r['study_id'] for r in cf.read('ed') if cf.tool_of(r['risk_of_bias_tool']) == 'RoB 2'}
    return sum(1 for r in cf.read('links') if r['same_underlying_data'] == 'yes' and r['study_id_a'] in rob2 and r['study_id_b'] in rob2)


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
         "**Background.** Physical expansion of water and sanitation infrastructure does not automatically guarantee household connection or effective use where legal, regulatory, and administrative conditions—such as eligibility screening, tenure and documentation rules, tariffs, bureaucratic discretion, and enforcement—operate as barriers at the 'legal last mile.'", "",
         "**Objective.** To map and synthesise the empirical evidence on how legal and administrative institutions shape the translation of physical availability of water and sanitation infrastructure into effective household access, "
         "and to synthesise quantitative evidence where it is comparable.", "",
         f"**Methods.** An AI-assisted systematic review: 34,594 records from multiple databases (27,481 after deduplication) were screened at title/abstract level and {F['full_text_decided']:,} full texts assessed; {inc:,} reports (representing {F['distinct_studies_definite_links']:,} distinct studies; {F['distinct_studies_incl_partial_links']:,} counting partial sample overlaps) were included and extracted into a {n:,}-row database, and appraised with the instrument matching each design "
         "(RoB 2, ROBINS-I, JBI, MMAT, CASP, AMSTAR 2, and a project-specific non-validated framework for legal-documentary studies). Quantitative findings were synthesised without meta-analysis (SWiM). The protocol was not registered in advance; most steps were carried out by a large language model with partial human verification.", "",
         f"**Results.** {n:,} included reports ({F['distinct_studies_definite_links']:,} distinct studies; 85% since 2010) spanned many countries (India, Brazil, South Africa, the United States and Ghana the most frequent), but only {F['causal_capable_designs']} ({100 * F['causal_capable_designs'] / n:.0f}%) used designs able to support a causal claim. "
         f"{F['effect_size_rows']} studies had an extractable effect-size row; none could be pooled. In three SWiM families the direction of association was mostly favourable for legal-status, tenure and recognition mechanisms (Family A, k = {fam['A']}), uniformly favourable or mixed for assistance, participation, trust and external-support mechanisms (Family B, k = {fam['B']}), and without a dominant direction for ownership, regulation, institutional-capacity and administrative-structure mechanisms (Family C, k = {fam['C']}); the families are thematic mechanism groupings, not homogeneous exposure–outcome pairs. " +
         bmp.human_verification_clause(F) + " " + bmp.swim_core_clause(F), "",
         "**Conclusions.** The empirical literature extensively documents associations between legal and administrative conditions and household water and sanitation access across diverse institutional contexts, but rarely employs designs capable of isolating causal effects and does not support a single pooled meta-analytic estimate. Overall certainty for causal or cross-jurisdictional magnitude claims remains low to very low, underscoring the need for quasi-experimental and comparative socio-legal designs targeting specific administrative rules.", "",
         "**Registration.** Not registered before the work was done. The protocol was fixed in writing on 2026-08-22 (git commit `d591062`), before any database was searched, and was registered retrospectively on OSF, frozen at release `0.2.0-interim` (2026-10-14) [author: add the OSF identifier and submission date once submitted, and label the registration retrospective].", "",
         "## 1. Introduction", "",
                  "Access to water and sanitation is usually measured by infrastructure coverage, but a household within reach of a network may still be unable to connect, or to keep and use a connection, because of legal and administrative conditions: "
         "who is recognised as eligible, what documents or tenure the application requires, what it costs, how much discretion officials hold, and how rules are enforced or reviewed (Bakker et al., 2008; Criqui, 2015; Hackenbroch & Hossain, 2012; Olmstead, 2004). "
         "This review calls the gap between physical availability and effective access the *legal last mile*. The term organises the question; it is not assumed to be established by the evidence (`PROJECT_SPEC.md` §14).", "",
         "The relevant evidence is scattered across disciplines and designs — public administration, economics, law, geography, public health, development studies — and across mechanisms and outcome measures that are rarely comparable. Most of the systematic reviews in the corpus synthesise a single intervention type or governance model: community participation (Nelson et al., 2021), behaviour-change and legal-provision approaches to household sewer connection (Alam et al., 2025), or the privatisation of one city's water services (Hendraputra, 2026). The closest cross-cutting review in the corpus, a scoping review of access inequalities in slums, organises its 33 studies into five barrier themes, one of which is governance and policy, rather than by the legal and administrative mechanisms through which access is conditioned (Abdulhadi et al., 2024). To the authors' knowledge, no prior synthesis maps this evidence with a mechanism-based framework.", "",
         "**Objectives.** (1) Describe the empirical evidence on legal and administrative conditions and access to water and sanitation, by design, setting, mechanism and outcome. "
         "(2) Synthesise quantitative evidence where exposure, comparator, outcome and effect measure are comparable enough to do so defensibly, and otherwise report the direction of association transparently. "
         "(3) State what the evidence base does and does not allow us to conclude, including how reliable the review's own process is.", "",
         "### 1.1 Conceptual framework", "",
         "Structural conditions (legal and property status, documentation, income, geography, institutional capacity) act through an administrative architecture (eligibility screening, administrative burden, discretion, accommodation, enforcement, review, participation) "
         "and administrative navigation (understanding requirements, applying, satisfying requirements, obtaining accommodation, challenging decisions) to produce service access (formal connection, continuity, reliability, quantity, affordability, effective use) and, ultimately, inclusion or exclusion (`PROJECT_SPEC.md` §5). "
         "Administrative law is the central lens, not the only candidate cause; property, planning, municipal, utility-regulatory and political institutions are in scope.", "",
         "## 2. Methods", "",
         "### 2.1 Design, protocol and registration", "",
         "The review followed a written protocol (`PROTOCOL.md`, PRISMA-P style), the PRISMA 2020 reporting guideline (Page et al., 2021), and SWiM guidance for synthesis without meta-analysis (Campbell et al., 2020). "
         "**The protocol was not registered before the work was done.** It was fixed in writing on 2026-08-22 (git commit `d591062`), before any database was searched, and an OSF Generalized Systematic Review registration is being filed retrospectively, frozen at release `0.2.0-interim` (2026-10-14) and labelled as such (`00_admin/preregistration/osf_preregistration_draft.md`) [author: add the registration identifier and date once submitted]. "
         "Specified a priori were the research questions, the PECO frame, the eligibility criteria and exclusion codes, the sources and search strings, the selection process, the 92-field codebook, the design-matched risk-of-bias tools, and the synthesis decision tree with its commitment not to claim a pooled finding unless the tree was satisfied. "
         "Decided or clarified afterwards, each with its date in `CHANGELOG.md`: the closure of the search on 2026-09-11 (SSRN and Westlaw/Lexis never searched) and of full-text retrieval on 2026-09-28; rule-based instead of item-by-item appraisal; the narrow reading of eligibility criterion 2 adopted on 2026-10-13 (Section 2.2); the clarification that results never decide eligibility (2026-10-14); the retitling of the synthesis families as thematic groupings (2026-10-14); and the adoption of controlled vocabularies (2026-10-14). "
         "The title was amended on 2026-09-28 to state AI assistance; the research question and the wording of the eligibility criteria were not changed (`PROTOCOL.md` §12).", "",
         "### 2.2 Research questions and eligibility", "",
         "The primary question asked how legal and administrative institutions shape the translation of physical availability of water and sanitation infrastructure into effective household access, and what evidence exists on the mechanisms by which eligibility screening, administrative burden, discretion, accommodation and enforcement produce or mitigate exclusion. "
         "The secondary question asked, where evidence is sufficiently comparable, for the magnitude of association between specific legal or administrative conditions and access outcomes. "
         "Studies were eligible if they examined water or sanitation access, examined a legal, administrative, institutional, regulatory or governance factor, and contained empirical evidence or a systematic empirical synthesis with an access-relevant outcome and an identifiable design; "
         "English, Portuguese and Dutch were eligible without translation (`INCLUSION_EXCLUSION.md`). Qualitative socio-legal studies were not excluded for being unpoolable. "
         "**Scope reading of criterion 2 (post-hoc).** Criterion 2 is literally broad. After a blind re-read by two other AI models disagreed with about half of a sample of the AI's full-text exclusions, the author ruled on 2026-10-13 that it would be applied as a legal or administrative access rule or mechanism "
         "(eligibility screening, administrative burden, documentation or tenure requirements, tariff or cost-recovery rules, discretion or accommodation, enforcement, or utility ownership or regulatory structure directly governing service access) rather than as project delivery, behavioural promotion or unanalysed macro-governance background, and to included and excluded studies alike. "
         "Because this was decided after the disagreement was seen, it is a post-hoc interpretive clarification of unchanged wording, not an a priori rule. It was followed on 2026-10-13 and 14 by consistency passes over the included studies (open items A6, A16, A19, and A22 to A25) applying criterion 3 (no primary data and no systematic method, code E05), criterion 4 (the outcome is not a household access outcome, E04) and the exposure test (E03); in these passes 83 included reports were moved to the exclusions and three exclusions to the inclusions. "
         "Eligibility never depends on the significance, magnitude or direction of a study's estimate (clarification of 2026-10-14).", "",
         "### 2.3 Search and selection", "",
         f"Searches closed on {bmp.SEARCH_CLOSED}; SSRN and Westlaw/Lexis were not searched (`SEARCH_PROTOCOL.md`, README Known limitations). "
         "Selection was by an AI first pass (title/abstract and full text) with written rationales and standardised exclusion codes (E01–E12); the human reviewer (the author) covered the "
         f"{bmp.TA_HUMAN_PASS:,} title/abstract records the AI marked include or unsure, and confirmed {F['reviewer_2_confirmed_includes']} of the {inc:,} full-text includes; the author then adjudicated {F['human_adjudicated_rows']} further full-text decisions, so {F['human_verified_rows']:,} of the {F['full_text_decided']:,} decisions ({100 * F['human_verified_rows'] / F['full_text_decided']:.1f}%) carry human verification or adjudication. "
         f"Full-text retrieval was closed by the author's decision on 2026-09-28 with {F['unretrieved_not_retrievable'] + F['unretrieved_wrong_file']:,} title/abstract includes never assessed; the unassessed set is older on average (see 3.1). "
         f"The {inc:,} included items are reports, describing {F['distinct_studies_definite_links']:,} distinct studies on the definite same-data links ({F['distinct_studies_incl_partial_links']:,} counting the partial overlaps); no companion report was collapsed.", "",
         "### 2.4 Data extraction", "",
         f"A 92-field extraction form (`CODEBOOK.md`) was completed for every included study by the AI, largely from full text; {F['abstract_only_extractions']} studies were extracted from abstract or metadata only and an audit found further rows with signs of shallow extraction (Limitations). The AI later re-read {bmp.reextraction_counts()[0]} studies from full texts found in the researcher's Drive; of the {bmp.reextraction_counts()[1]} rows flagged only by the sparse-record audit, {bmp.reextraction_counts()[2]} had an abstract-level extraction that was materially wrong or incomplete (`reextract_2026-10-04/CAMPAIGN_NOTES.md`). There was no second extractor. "
         "A seeded sample for human second extraction has been prepared (`03_extraction/second_extractor/`) but not yet completed.", "",
         "### 2.5 Risk of bias and critical appraisal", "",
         f"Each study was appraised with the instrument matching its design: RoB 2 (cluster variant) for randomised trials ({T['RoB 2']} reports of {T['RoB 2'] - _rob2_double_reports(F)} distinct trials), ROBINS-I ({T['ROBINS-I']}), JBI cross-sectional ({T['JBI Cross-Sectional']}), MMAT ({T['MMAT']}), CASP qualitative ({T['CASP Qualitative']}) and AMSTAR 2 for systematic reviews ({T['AMSTAR 2']}). "
         f"For {T['Legal Framework']} legal-documentary or doctrinal studies no published instrument fits, and this project's own **non-validated** Legal Institutional Evidence Appraisal Framework was used; {('no study was judged not appraisable' if not T.get('NONE', 0) else str(T.get('NONE', 0)) + ' studies were judged not appraisable')}. "
         "Ratings were assigned by rule from the extracted fields, not by signalling-question reading of each paper, except for the studies re-appraised from full text (listed in `CHANGELOG.md`). Ratings therefore describe the extraction as much as the paper.", "",
         "### 2.6 Synthesis", "",
         "Each study was coded to one of nine mechanism families (eligibility, status and documentation; procedural burden; fees, tariffs and subsidies; discretion and accommodation; enforcement and sanctions; review and redress; institutional structure and coordination; participation and assistance; regulatory model and ownership) or to `multiple`, and to one of four outcome families (primary connection, effective access, economic access, administrative outcome) or `multiple`; the families are not pooled with each other. "
         "The labels were mapped from the free-text labels of the extraction by keyword rules, with the rows the rules could not place resolved by the AI under the author's review (four studies the mapping could not place were excluded), and the original labels are preserved; the mapping is mechanical and unvalidated, and the author has not checked it. Free-text study-design labels were mapped to the design list (eight values plus `other`) in the same way. "
         f"A feasibility judgment (`phase11_quantitative_feasibility_judgment.md`) concluded that no family reaches the bar for meta-analysis, so {F['effect_size_rows']} effect-size rows were compiled, {F['swim_core_studies']} of them into three structured syntheses reporting direction and significance of each study's own estimate (SWiM) and the rest recorded as reasoned non-fits with their reasons. "
         "For each family-assigned study the raw coefficient sign of the estimate and its substantive direction for household access, affordability or equity (Favourable, Unfavourable, Null or Mixed) were coded separately, because the two readings differ when the outcome is adverse (a tariff, an interruption, a collection time) or the exposure is a non-recognised status; both codings are the AI's. "
         + bmp.family_fit_clause() + " "
         "No effect was converted to a common scale. " + bmp.swim_core_clause(F) + " "
         "Sensitivity analyses removed abstract-only and shallow extractions, linked reports, the remaining Family A coding judgment call and the two kept studies with no household access outcome, recoded the direction of two studies (the fully adjusted estimate of S471; the household-access reading of S879) and kept only the studies where the two readings agree, and would remove the rows of studies not flagged eligible (none remain since S589's row was taken out on 2026-10-14); they are reported as a supplementary table (`05_analysis/sensitivity/SENSITIVITY_ANALYSIS_2026-09-28.md`), a standing pre-publication requirement.", "",
         "### 2.7 Secondary reviews", "",
         "Systematic reviews in the corpus are treated as secondary evidence and never pooled as if primary; their primary studies may also be in the corpus (a double-counting risk assessed only in part, Limitations).", "",
         "### 2.8 Data and code", "",
         "All databases, scripts and generated figures are in the project repository; a verification script (`code/analysis/verify_repository.py`) re-derives every quoted figure and checks that generated files are current. Every dated decision, rule change and adjudication, including the author's rulings on the screening decisions, is recorded in the Repository Audit Trail (`00_admin/DECISIONS_AND_OPEN_ITEMS.md`), and the files cited in the text are indexed in the Appendix.", "",
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
         f"The mechanism-certainty code was normalised to the codebook's design-driven scale (Section 3.2): all {mcn['3'] + mcn['4']} studies at level 3 or 4 (quasi-experimental or experimental evidence) are ROBINS-I or RoB 2 studies, so the earlier mismatch between the certainty code and the study design no longer exists.", "",
         pick(sub, '3.4 Unresolved classifications').split('**Do the randomised')[0].strip(), "",
         "### 3.5 Quantitative evidence: three structured syntheses", "",
         pick(sub, '2A.3').split('Examples as extracted')[0].strip(), "",
         "Per-study results (exposure, outcome, direction, appraisal rating) are tabulated in the three family documents (`06_outputs/supplementary/family_*_swim_synthesis_2026-09-28.md`).", "",
         "**Sensitivity analyses.** " + re.search(r'\*\*Sensitivity of these counts\*\*(.*?)(?=\n\n|$)', pick(sub, '2A.3'), re.S).group(1).strip(), "",
         f"**Reporting bias and certainty.** No publication-bias assessment was possible: although Family A contains {fam['A']} studies and Family C {fam['C']}, no common effect metric exists, so no funnel-plot or small-study analysis is defined (`ANALYSIS_PLAN.md` §9 requires about ten studies on a common scale). "
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
         "Where quantitative estimates exist they are too heterogeneous to pool, and their direction is most consistent for legal-status, tenure and recognition mechanisms and for assistance and participation mechanisms, least consistent for ownership, regulation and administrative-structure mechanisms. "
         "These statements are provisional: extraction and appraisal were AI-conducted and only partly verified, screening of the full-text pool is incomplete, and the protocol was not registered in advance. "
         "The review does not establish the *legal last mile* as a general mechanism; it describes where evidence exists, where it is thin, and what a human-verified update would need to check first. [Author to revise.]", "",
         "### 6.1 Implications for research and practice", "",
         "*Conditional on human verification.* (1) Policy readers should not take this review as evidence that any single legal or administrative reform causes better access; the designs that could show that are few. "
         "(2) The next research step the repository supports is verification, not expansion: complete the human second pass of screening and a second extraction, fetch the full texts of the shallow extractions and the unassessed older records, and finish the check of overlap between the AMSTAR 2 reviews and the primary studies. "
         "(3) If the comparative frame of the underlying doctoral project (Netherlands, Canada, Brazil) is to be tested, targeted searches for Dutch and Canadian evidence are needed, because the corpus holds very few single-country studies for the first two (Section 3.7).", "",
         "## 7. Declarations", "",
         "- **Author and affiliation:** Claudio Klaus, External Doctoral Candidate, Erasmus School of Law, Erasmus University Rotterdam, Rotterdam, The Netherlands. This is the companion systematic review to the PhD dissertation *The Legal Last Mile: Administrative Law as a Mechanism of Connectivity and Exclusion in Sanitation Governance: A Comparative Study of the Netherlands, Canada (Ontario), and Brazil*.",
         "- **Funding (PRISMA item 25):** This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors. Database access was provided through institutional subscriptions at Erasmus University Rotterdam. API and subscription costs for Anthropic Claude and OpenAI Codex were paid personally by the author, and Google Gemini runs (`gemini-3.1-flash-lite`) used the author's free-tier API key; no external, institutional, or vendor funding was received.",
         "- **Competing interests (PRISMA item 26):** The author declares no competing financial or non-financial interests. The author has no employment, consulting, equity or other financial or non-financial relationship with Anthropic, OpenAI, Google or any other AI vendor whose models were used in this project.",
         "- **Registration (PRISMA item 24):** retrospective, frozen at release `0.2.0-interim` (2026-10-14); see Section 2.1 [author: add the identifier once submitted].",
         "- **AI use:** Claude (Anthropic) performed most screening, extraction, appraisal and synthesis drafting; see `AI_USE_STATEMENT.md` for the stage-by-stage table. " + bmp.ai_provenance_clause(),
         "- **Author contributions (CRediT):** Claudio Klaus: Conceptualization, Data curation, Formal analysis, Funding acquisition (self-funded), Investigation, Methodology, Project administration, Resources, Software, Supervision, Validation, Visualization, Writing – original draft (direction and revision of AI-assisted synthesis; see AI_USE_STATEMENT.md), Writing – review & editing. The AI tools used (Anthropic Claude, OpenAI Codex, Google Gemini) are not authors; the AI-assisted stages are described in `AI_USE_STATEMENT.md`.",
         "- **Data and code availability:** all databases, scripts and generated files are in the project repository (release 0.2.0-interim, tag v0.2.0-interim); the Supplementary Files cited in the text are indexed, with their exact repository paths, in the Appendix. Source PDFs are not redistributed.",
         "- **Ethics:** Ethics approval was not required for this study as it is a systematic review of published and grey literature involving no primary data collection from human participants.", "",
         "## References", "", *_reference_lines(), "[Author: the Introduction cites included studies and reviews as examples of each point; check each against the paper before submission, and add a general reference on administrative burden if wanted. `SOURCES.md` and `sources.bib` list the methodological sources (RoB 2, ROBINS-I, JBI, CASP, MMAT and AMSTAR 2).]", ""]
    text = "\n".join(x for x in L if x is not None).replace('\n\n\n', '\n\n')
    # the lifted paragraphs were written for the preliminary report: re-point its section numbers and voice at the manuscript's
    for old, new in (('§2A.1', 'Section 3.2'), ('§2A.2', 'Section 3.3'), ('§2A.3', 'Section 3.5'), ('§2A.5', 'Section 3.7'), ('see 2A.2', 'see Section 3.3'), ('§3.4', 'Section 3.4'),
                     ("this report's own observation, not a project ruling", "an observation of this draft, not a project ruling"), ('supplied by you', 'supplied by the author'), ('the human researcher', 'the author'), ("the researcher's", "the author's"), ('The researcher', 'The author'), ('the researcher', 'the author')):
        text = text.replace(old, new)
    a16 = bmp._a16_outcome()
    n_ex_, n_inc_, _ = bmp.reviewer2_ai_counts()
    for old_, new_ in (("After a blind re-read by two other AI models disagreed with about half of a sample of the AI's full-text exclusions, the author ruled",
                        f"After a blind re-read by two other AI models disagreed with the AI on about half of the full-text exclusions they re-read ({n_inc_} of {n_ex_} for the primary model; the author's own adjudication of the {a16['flagged']} exclusions flagged by either model then confirmed {a16['upheld']} and reversed {a16['reversed']}, Section 5.2), the author ruled"),
                       ("in these passes 83 included reports were moved to the exclusions and three exclusions to the inclusions",
                        f"in these passes {a16['moved_to_exclusion']} included reports were moved to the exclusions and {a16['moved_to_inclusion']} exclusions to the inclusions")):
        assert old_ in text, old_[:60]
        text = text.replace(old_, new_)
    text, used = msup.strip_repository_jargon(text)   # file paths, the commit hash and open-item codes leave the prose; the Appendix keeps the exact paths
    return text.rstrip("\n") + "\n\n" + msup.appendix(used)


if __name__ == '__main__':
    OUT.write_text(build(), encoding='utf-8')
    print('wrote', OUT.relative_to(ROOT))
