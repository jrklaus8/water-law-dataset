#!/usr/bin/env python3
"""Keep repository jargon out of the manuscript prose (author's instruction, 2026-10-14).

The generated manuscript text quotes file paths, a commit hash and open-item codes ('open item A16') that mean something to someone inside the repository and nothing to a reader of the paper.
`strip_repository_jargon(text)` replaces every backticked file path with a numbered 'Supplementary File Sn' reference, drops the open-item codes and the commit hash from the prose, and returns the list
of files it cited; `appendix(used)` writes the single Data and code availability table that keeps the exact paths. A path or code that is not recognised raises an error, so a new citation cannot reach the
manuscript without an entry in SUPP. Deterministic; no data are read. Used by build_manuscript_draft.py."""
import re

# (key = file name as it appears in the prose, repository path, what the file holds). Order = order of the Supplementary File numbers.
SUPP = [
    ('PROTOCOL.md', 'PROTOCOL.md', 'Written protocol (PRISMA-P style), fixed in writing on 2026-08-22 before any database was searched'),
    ('SEARCH_PROTOCOL.md', 'SEARCH_PROTOCOL.md', 'Search protocol: sources, strings and dates'),
    ('PROJECT_SPEC.md', 'PROJECT_SPEC.md', 'Project specification: research questions, outcome definitions and the planned synthesis families, with dated notes on later changes'),
    ('ANALYSIS_PLAN.md', 'ANALYSIS_PLAN.md', 'Analysis plan: decision tree for pooling versus structured synthesis'),
    ('INCLUSION_EXCLUSION.md', 'INCLUSION_EXCLUSION.md', 'Eligibility criteria, standardised exclusion codes and the dated narrow reading of criterion 2'),
    ('CODEBOOK.md', 'CODEBOOK.md', 'Extraction codebook, including the design-driven mechanism-certainty scale'),
    ('RISK_OF_BIAS.md', 'RISK_OF_BIAS.md', 'Appraisal tools by study design and the rule-based rating procedure'),
    ('osf_preregistration_draft.md', '00_admin/preregistration/osf_preregistration_draft.md', 'Text of the retrospective OSF registration, frozen at release 0.2.0-interim'),
    ('SOURCES.md', 'SOURCES.md', 'Methodological sources (RoB 2, ROBINS-I, JBI, CASP, MMAT, AMSTAR 2, PRISMA 2020, SWiM)'),
    ('sources.bib', 'sources.bib', 'Bibliography file of the methodological and cited sources'),
    ('DECISIONS_AND_OPEN_ITEMS.md', '00_admin/DECISIONS_AND_OPEN_ITEMS.md', 'Repository Audit Trail: the dated ledger of every decision and open item, with the author\'s rulings'),
    ('CHANGELOG.md', 'CHANGELOG.md', 'Dated change log of the data, rules and documents'),
    ('README.md', 'README.md', 'Repository overview, workflow, known limitations and release history'),
    ('AUDITING_GUIDE.md', 'AUDITING_GUIDE.md', 'Guide for an external auditor of the repository'),
    ('AI_USE_STATEMENT.md', 'AI_USE_STATEMENT.md', 'AI-use statement: stage-by-stage division of labour, models and tools, with provenance taken from the logged labels'),
    ('AI_USE_AND_TOOLS_DISCLOSURE.md', '_reviewer2_codex/AI_USE_AND_TOOLS_DISCLOSURE.md', 'Disclosure of the Codex and Gemini blind-reviewer runs'),
    ('CURRENT_FIGURES.md', '00_admin/CURRENT_FIGURES.md', 'Every quoted figure with its source, regenerated from the databases'),
    ('verify_repository.py', 'code/analysis/verify_repository.py', 'Verification script that re-derives every quoted figure and checks that generated files are current'),
    ('exclusion_log.csv', '02_screening/exclusion_log/exclusion_log.csv', 'Exclusion log: standardised code and rationale for every full-text exclusion'),
    ('A16_ADJUDICATION_SHEET_2026-10-04.md', '02_screening/full_text/A16_ADJUDICATION_SHEET_2026-10-04.md', 'Reading list for the records on which two blind AI reviewers disagreed with the original AI decision (the author\'s rulings are in the filled sheet beside it)'),
    ('REVIEWER_2_PRIORITY_QUEUE_README.md', '02_screening/full_text/REVIEWER_2_PRIORITY_QUEUE_README.md', 'Priority queue and instructions for the human second pass of the full-text decisions'),
    ('second_extractor/', '03_extraction/second_extractor/', 'Second-extractor sample (an AI check of the AI extraction) and its worksheets'),
    ('linked_reports_2026-09-28.csv', '03_extraction/extracted_data/linked_reports_2026-09-28.csv', 'Reports that share underlying data or overlap'),
    ('extraction_mechanism_certainty_original_2026-10-14.csv', '03_extraction/extracted_data/extraction_mechanism_certainty_original_2026-10-14.csv', 'Original mechanism-certainty values (including the narrative sentences) before the 2026-10-14 normalisation'),
    ('CAMPAIGN_NOTES.md', 'code/provenance/audit_and_repair/reextract_2026-10-04/CAMPAIGN_NOTES.md', 'Notes on the full-text re-extraction campaign'),
    ('evidence_map_original_labels_2026-10-14.csv', '05_analysis/descriptive/evidence_map_original_labels_2026-10-14.csv', 'Original free-text design, mechanism and outcome labels before they were mapped to the controlled vocabularies'),
    ('DATA_QUALITY_AUDIT_2026-09-29.md', '05_analysis/descriptive/DATA_QUALITY_AUDIT_2026-09-29.md', 'Data-quality audit of the extraction database'),
    ('SPARSE_RECORD_AUDIT_2026-10-04.md', '05_analysis/descriptive/SPARSE_RECORD_AUDIT_2026-10-04.md', 'Audit of extraction rows that show signs of shallow (abstract-level) extraction'),
    ('AMSTAR2_OVERLAP_CHECK_2026-10-04.md', '05_analysis/descriptive/AMSTAR2_OVERLAP_CHECK_2026-10-04.md', 'Overlap between the AMSTAR 2-appraised reviews and the primary studies in the corpus'),
    ('FAMILY_VOCABULARY_PROPOSAL_2026-09-28.md', '05_analysis/descriptive/FAMILY_VOCABULARY_PROPOSAL_2026-09-28.md', 'Controlled vocabularies for mechanism and outcome families (mechanical, unvalidated)'),
    ('FAMILY_FIT_AUDIT_2026-10-04.md', '05_analysis/effect_sizes/FAMILY_FIT_AUDIT_2026-10-04.md', 'Audit of whether each effect-size row fits the wording of its synthesis family'),
    ('SWIM_CORE_VERIFICATION_TABLE_2026-10-14.csv', '05_analysis/effect_sizes/SWIM_CORE_VERIFICATION_TABLE_2026-10-14.csv', 'The 44 family-assigned effect rows: exposure, comparator, outcome, estimate, raw sign, substantive direction, appraisal, and the worksheet for the human check'),
    ('SWIM_DIRECTION_CODING_2026-10-14.csv', '05_analysis/effect_sizes/SWIM_DIRECTION_CODING_2026-10-14.csv', 'Coding of the raw sign and the substantive direction of the 44 family-assigned effect rows, with the outcome polarity and the exposure pole'),
    ('SENSITIVITY_ANALYSIS_2026-09-28.md', '05_analysis/sensitivity/SENSITIVITY_ANALYSIS_2026-09-28.md', 'Sensitivity analysis of the three structured syntheses'),
    ('family_*_swim_synthesis_2026-09-28.md', '06_outputs/supplementary/family_{A,B,C}_swim_synthesis_2026-09-28.md', 'Structured (SWiM) syntheses of Families A, B and C: studies, tables, robustness and certainty'),
    ('phase11_blank_family_resolution_2026-09-28.md', '06_outputs/supplementary/phase11_blank_family_resolution_2026-09-28.md', 'Resolution of the effect-size rows that had no synthesis family'),
    ('phase11_quantitative_feasibility_judgment.md', '06_outputs/supplementary/phase11_quantitative_feasibility_judgment.md', 'Judgment on the feasibility of pooling'),
    ('fig1_design_mix.svg', '06_outputs/figures/fig1_design_mix.svg', 'Figure 1: design mix'),
    ('fig2_publication_years.svg', '06_outputs/figures/fig2_publication_years.svg', 'Figure 2: publication years'),
    ('fig3_countries.svg', '06_outputs/figures/fig3_countries.svg', 'Figure 3: countries'),
    ('fig4_direction_by_family.svg', '06_outputs/figures/fig4_direction_by_family.svg', 'Figure 4: raw sign and substantive direction by family'),
    ('fig5_appraisal_tools.svg', '06_outputs/figures/fig5_appraisal_tools.svg', 'Figure 5: appraisal instruments'),
    ('build_figures.py', 'code/analysis/build_figures.py', 'Script that draws Figures 1 to 5 from the databases'),
    ('build_manuscript_draft.py', 'code/analysis/build_manuscript_draft.py', 'Script that generates this manuscript from the verified figures'),
]
KEYS = {k: i for i, (k, _, _) in enumerate(SUPP)}
for _f in 'ABC':   # a single family document is cited under its own name; it is indexed with the three
    KEYS[f'family_{_f}_swim_synthesis_2026-09-28.md'] = KEYS['family_*_swim_synthesis_2026-09-28.md']
AUDIT_TRAIL = 'DECISIONS_AND_OPEN_ITEMS.md'
PATHLIKE = re.compile(r'/|\.(?:md|csv|py|json|svg|cff|bib|R|sh|xlsx|txt)$')
CODES = r'A\d{1,2}(?:(?:,\s*(?:and\s+)?|\s+and\s+|\s+to\s+|–)A?\d{1,2})*'      # A16, A19, A22 to A25 and A6 / A22–A25


def _key(span):
    s = re.sub(r'^python3\s+', '', span.strip())
    base = s.rstrip('/').rsplit('/', 1)[-1] if not s.endswith('/') else s.rstrip('/').rsplit('/', 1)[-1] + '/'
    if base not in KEYS:
        raise KeyError(f'manuscript_supplement.SUPP has no entry for {span!r} (key {base!r}); add it so the file is indexed in the Data and code availability table')
    return KEYS[base]


def _runs(text, used):
    """Turn [[SF:n]] markers into 'Supplementary File Sn' / 'Supplementary Files Sn, Sm and Sk'; numbers are assigned in order of first use."""
    number = {}
    def num(i):
        if i not in number:
            number[i] = len(number) + 1
            used.append(i)
        return number[i]
    # order of first appearance in the text
    for m in re.finditer(r'\[\[SF:(\d+)\]\]', text):
        num(int(m.group(1)))
    run = re.compile(r'\[\[SF:(\d+)\]\](?:(?:, and | and |, |; |/)\[\[SF:(\d+)\]\])+')
    def fix_run(m):
        ids = [int(x) for x in re.findall(r'\[\[SF:(\d+)\]\]', m.group(0))]
        labels = [f'S{number[i]}' for i in ids]
        return 'Supplementary Files ' + (', '.join(labels[:-1]) + ' and ' + labels[-1])
    text = run.sub(fix_run, text)
    return re.sub(r'\[\[SF:(\d+)\]\]', lambda m: f'Supplementary File S{number[int(m.group(1))]}', text), number


def strip_repository_jargon(text, audit_trail_pointer=True):
    """Return (text without paths, commit hashes and open-item codes, list of SUPP indices in the order of the Supplementary File numbers)."""
    def span(m):
        s = m.group(1)
        if PATHLIKE.search(s) and not re.fullmatch(r'[0-9a-f]{7,40}', s):
            return f'[[SF:{_key(s)}]]'
        return m.group(0)
    text = re.sub(r'`([^`\n]+)`', span, text)
    # commit hash of the protocol commit: the hash itself goes to the appendix
    text = re.sub(r'\s*\(git commit `?[0-9a-f]{7,40}`?\)', ' (see the Repository Audit Trail, [[SF:%d]])' % KEYS[AUDIT_TRAIL], text)
    text = re.sub(r'`[0-9a-f]{7,40}`', 'the protocol commit', text)
    # open-item codes: drop the parentheticals and clauses that consist of them
    text = re.sub(r'\s*\((?:open items? )?' + CODES + r'\)', '', text)
    text = re.sub(r'[;,]\s*open items? ' + CODES + r'(?=\))', '', text)
    text = re.sub(r'[;,]\s*open items? ' + CODES + r'(?=[.;])', '', text)
    text = re.sub(r'\s+under open items? ' + CODES, '', text)
    left = re.findall(r'.{0,80}\b(?:open items? )?A\d{1,2}\b.{0,60}', text)
    if left:
        raise ValueError('open-item codes left in the manuscript prose:\n' + '\n'.join(left))
    text, number = _runs(text, [])
    used = [i for i, _ in sorted(number.items(), key=lambda kv: kv[1])]
    return text, used


def appendix(used, hash_note='d591062'):
    """The single table that keeps the exact paths (and the one commit hash), for the Supplementary Files cited in the text."""
    L = ['## Appendix. Data and code availability: Supplementary Files', '',
         'All databases, scripts and generated files behind this manuscript are in the project repository (release 0.2.0-interim, tag v0.2.0-interim); the written protocol was fixed at commit '
         f'{hash_note} on 2026-08-22, before any database was searched. The files cited in the text are indexed below with their exact paths, relative to the repository root. Source PDFs are not redistributed. '
         'The open items cited in earlier drafts of this manuscript (the dated decisions and adjudication passes, numbered A1 to A25) are documented in the Repository Audit Trail.', '',
         '| Supplementary File | Path in the repository | Content |', '|---|---|---|']
    for n, i in enumerate(used, 1):
        _, path, desc = SUPP[i]
        L.append(f'| S{n} | `{path}` | {desc} |')
    return '\n'.join(L) + '\n'


if __name__ == '__main__':
    demo, used = strip_repository_jargon('The protocol (`PROTOCOL.md`, `CODEBOOK.md`) was fixed (git commit `d591062`); see open item A16 (`06_outputs/figures/fig1_design_mix.svg`).')
    print(demo); print(appendix(used))
