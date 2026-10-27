#!/usr/bin/env python3
"""AI-use ledger: for every stage of the review, which AI tool or model did what, how many decisions or rows carry its label, over which dates, and how much of it a human checked.

Writes 00_admin/AI_USE_LEDGER.csv (one row per stage and actor) and 00_admin/AI_USE_LEDGER.md (the same, plus the instruction files that ARE archived and a frank list of what is NOT).
Counts come from the reviewer and researcher labels in the CSV databases (the same labels `current_figures.py` classifies), so the ledger cannot claim more or less than the databases record.

Run from legal-last-mile-systematic-review/:  python3 code/analysis/build_ai_use_ledger.py
"""
import csv
import io
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import current_figures as cf  # noqa: E402

ROOT = cf.ROOT
OUT_CSV = ROOT / '00_admin/AI_USE_LEDGER.csv'
OUT_MD = ROOT / '00_admin/AI_USE_LEDGER.md'
DATE = re.compile(r'\d{4}-\d{2}-\d{2}')
COLUMNS = ['stage', 'activity', 'actor', 'label_pattern_in_databases', 'units', 'unit_type', 'first_date', 'last_date', 'human_checked', 'human_check_note']

# files that give the AI its instructions, or record them; each must exist (checked by code/tests/test_ai_use_ledger.py)
ARCHIVED = [
    ('INCLUSION_EXCLUSION.md', 'The eligibility criteria and exclusion codes the AI screened against (also given verbatim to Codex and Gemini in the second-reviewer pass)'),
    ('CODEBOOK.md', 'The 92-field extraction codebook the AI extracted against'),
    ('RISK_OF_BIAS.md', 'Which appraisal instrument for which design, and how the batch ratings were assigned'),
    ('ANALYSIS_PLAN.md', 'The pre-stated synthesis decision rules'),
    ('02_screening/title_abstract/ai_first_pass_rationale.csv', 'The AI\'s written reason for every title/abstract decision'),
    ('02_screening/exclusion_log/exclusion_log.csv', 'The coded reason and detail for every full-text exclusion'),
    ('01_search/cowork_instructions_2026-09-11_followup.md', 'Instructions given to the AI browser assistant that relayed some database searches (six dated files, `01_search/cowork_instructions_*`)'),
    ('02_screening/full_text/COWORK_RETRIEVAL_INSTRUCTIONS.md', 'Instructions for AI-assisted full-text retrieval'),
    ('00_admin/PDF_RETRIEVAL_AGENT_BRIEF_2026-10-09.md', 'The brief given to the retrieval agent'),
    ('_reviewer2_codex/AI_USE_AND_TOOLS_DISCLOSURE.md', 'Tools, versions, blinding and the verbatim protocol of the Codex and Gemini second-reviewer pass'),
    ('_reviewer2_codex/run_codex_reviewer2.py', 'The script (with its prompt) that called Codex and Gemini for blind full-text re-screening'),
    ('_reviewer2_codex/run_second_extractor.py', 'The script (with its prompt) for AI second-extraction checks'),
    ('_reviewer2_codex/run_debate.py', 'The script (with its prompts) for the AI-versus-AI debate on disputed records'),
    ('code/provenance/README.md', 'What the one-off scripts under `code/provenance/` are: the AI-written scripts that wrote decisions and extracted data into the databases'),
]

NOT_ARCHIVED = [
    'The conversation prompts for the main work. Title/abstract screening, full-text screening, extraction and risk-of-bias appraisal were done by Claude in interactive sessions with the researcher. What survives is the instructions it was given in files (above), the decisions with a written reason per record, and the scripts that wrote them (`code/provenance/`, from record batch 64 onward). The earliest scripts existed only in an ephemeral session scratchpad and are not recoverable (audit finding 11).',
    'The exact model version behind most decisions. Labels record the tool and a date (`Claude-AI-fulltext-2026-09-16`), not a model identifier, so the model that produced a given row can only be bracketed by date. Only 60 early full-text rows carry a model name (`claude_sonnet_5`). The Codex (`gpt-5.6-sol`) and Gemini (`gemini-3.1-flash-lite`) passes record the model in the label.',
    'Sampling settings and seeds. No temperature, seed or reasoning-effort setting is recorded for the Claude work. AI decisions are not deterministic: re-running the same prompt would not be expected to reproduce the same 26,222 title/abstract decisions or the same extractions.',
    'An independent re-run. No second AI model repeated the whole first pass, and no human extracted any study. The second-model pass covers a sample of full-text decisions only.',
    'A validated accuracy figure for the AI\'s extraction or risk-of-bias rating. The only measured error rates are for screening (the A16 audit of excludes) and, informally, the 2026-09-28 audit. A blind 60-study second-extraction sample is prepared and has not been done.',
]


def label_dates(values):
    ds = sorted({d for v in values for d in DATE.findall(v)})
    return (ds[0], ds[-1]) if ds else ('', '')


def build():
    ta, ft, ed, em = cf.read('ta'), cf.read('ft'), cf.read('ed'), cf.read('em')
    dec = [r for r in ft if r['final_decision'] in ('include', 'exclude')]
    F = cf.compute()
    rows = []

    def add(stage, activity, actor, pattern, units, unit_type, dates, human, note):
        rows.append({'stage': stage, 'activity': activity, 'actor': actor, 'label_pattern_in_databases': pattern, 'units': units, 'unit_type': unit_type,
                     'first_date': dates[0], 'last_date': dates[1], 'human_checked': human, 'human_check_note': note})

    # --- search: no AI decisions, one AI relay
    cow = len(list((ROOT / '01_search').glob('cowork_instructions_*.md')))
    add('Search', 'Database searches run by the researcher through institutional access; some exports relayed by an AI browser assistant', 'researcher; AI browser assistant (Cowork)', 'n/a (raw exports in 01_search/raw_exports/)', cow, 'instruction files for the assistant', ('2026-09-11', '2026-09-11'), 'n/a', 'Exports are untouched; the researcher ran every search')
    # --- title/abstract
    t1 = [r for r in ta if r['reviewer_1']]
    t2 = [r for r in ta if r['reviewer_2'].startswith('Human-')]
    ai_ex_only = sum(r['title_abstract_decision'] == 'exclude' and not r['reviewer_2'] for r in ta)
    add('Title/abstract screening', 'First-pass include / exclude / unsure with a written reason', 'AI (Claude)', 'Claude-AI-1stpass-<date>', len(t1), 'records', label_dates([r['reviewer_1'] for r in t1]), len(t2), f"A human second reviewer covered the include-or-unsure records only; {ai_ex_only:,} AI exclusions were not human-checked (a 120-record random spot-check of exclusions was reviewed on 2026-09-12, 119 of 120 correct; the changelog does not say whether the researcher or the AI reviewed it)")
    add('Title/abstract screening', 'Second pass on the include-or-unsure records', 'human second reviewer', 'Human-reviewer2-<date>', len(t2), 'records', label_dates([r['reviewer_2'] for r in t2]), len(t2), '99.8% agreement with the AI; flagged as unusually high in the README and confirmed by the researcher before merging')
    # --- full text, first decision
    groups = Counter(re.sub(r'\d{4}-\d{2}-\d{2}', '<date>', r['reviewer_1']) for r in dec)
    for lab, n in cf.ranked(groups):
        rr = [r for r in dec if re.sub(r'\d{4}-\d{2}-\d{2}', '<date>', r['reviewer_1']) == lab]
        add('Full-text screening', 'First decision with coded reason (include / exclude)', 'AI (Claude)', lab, n, 'decided records', label_dates([r['reviewer_1'] for r in rr]),
            sum(1 for r in rr if r['reviewer_2'].startswith('Human-') or r['reviewer_2'] == 'CK' or any(m in r['notes'] for m in cf.HUMAN_RULING_MARKS)),
            'Decisions in this group that a human later confirmed or ruled on' + ('; label inferred when backfilled on 2026-10-14 (A2) for rows that had none' if lab.startswith('Claude-AI-fulltext') else ''))
    # --- full text, second review
    for pat, actor, unit in (('Human-', 'human second reviewer', 'Human-reviewer2-fulltext-<date>'), ('Codex-', 'AI (Codex, gpt-5.6-sol), blind second model', 'Codex-gpt-5.6-sol-reviewer2-fulltext-<date>'), ('Gemini-', 'AI (Gemini, gemini-3.1-flash-lite), blind second model', 'Gemini-gemini-3.1-flash-lite-reviewer2-fulltext-<date>')):
        rr = [r for r in dec if r['reviewer_2'].startswith(pat)]
        add('Full-text screening', 'Independent second review', actor, unit, len(rr), 'decided records', label_dates([r['reviewer_2'] for r in rr]), len(rr) if pat == 'Human-' else 0,
            'Human' if pat == 'Human-' else 'An AI-versus-AI check; not counted as human verification')
    add('Full-text screening', 'Adjudication of contested and sampled decisions', 'principal investigator (CK)', 'reviewer_2 = CK, or a dated ruling note', F['human_adjudicated_rows'], 'decided records', ('2026-10-13', '2026-10-14'), F['human_adjudicated_rows'],
        f"{F['human_adjudicated_excludes']} exclusions and {F['human_adjudicated_includes']} inclusions; recorded only where the researcher reviewed the evidence and instructed the entry")
    # --- extraction
    grp = Counter(re.sub(r'\s*\(.*', '', re.sub(r'\d{4}-\d{2}-\d{2}', '<date>', r['researcher'])) for r in ed)
    re_ex = sum('re-extraction' in r['researcher'] for r in ed)
    add('Data extraction (92 fields)', 'Extraction of every included study, with source location', 'AI (Claude)', '; '.join(f'{k} ({v})' for k, v in cf.ranked(grp)), len(ed), 'extraction rows',
        (min(r['date_extracted'] for r in ed if r['date_extracted']), max(r['date_extracted'] for r in ed if r['date_extracted'])), 0, f"No second extractor. {re_ex} rows were re-extracted from full texts after an audit found shallow extraction; {F['abstract_only_extractions']} remain abstract- or metadata-only")
    # --- risk of bias
    forms = len({p.name.split('_')[0] for p in (ROOT / '04_quality/appraisal_forms').glob('S*.md')} & {r['study_id'] for r in ed})
    add('Risk-of-bias appraisal', 'Instrument assignment and rating', 'AI (Claude)', 'risk_of_bias_tool / risk_of_bias_rating columns', len(ed), 'extraction rows', ('', ''), 0,
        f"{forms} included studies have a per-study signalling-question form; the rest are rule-based batch ratings. One instrument (Legal Framework) is the project's own and not validated")
    add('Evidence classification', 'Design class, mechanism family, outcome family, certainty', 'AI (Claude), with controlled vocabularies the researcher approved', 'evidence_map.csv', len(em), 'evidence-map rows', ('', ''), 0, 'The researcher ruled on the vocabularies (items A5, A10) and on individual overrides')
    add('Synthesis', 'Effect-size table, direction coding, SWiM drafts, sensitivity analysis', 'AI (Claude)', 'effect_sizes.csv; SWiM family documents', F['swim_core_studies'], 'synthesis studies', ('', ''), F['swim_core_inclusion_human_verified'],
        f"Inclusion human-verified for {F['swim_core_inclusion_human_verified']}; {F['swim_core_ai_checked_not_human']} AI-checked only; the author has confirmed the direction coding of {F['swim_core_direction_ck_confirmed']}")
    n_py = len([p for p in (ROOT / 'code').rglob('*.py') if '__pycache__' not in p.parts])
    add('Code and documentation', 'Every script in code/ and every document in this repository was drafted by the AI', 'AI (Claude)', 'git history', n_py, 'Python scripts under code/', ('', ''), 'no independent review recorded', 'The verifier and unit tests (code/tests/) check the numbers and some of the code; the researcher approved merges and rulings, and no line-by-line human code review is recorded')
    return rows


def render():
    rows = build()
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=COLUMNS, lineterminator='\n')
    w.writeheader()
    w.writerows(rows)
    md = ['# AI-use ledger', '',
          '*Generated by `code/analysis/build_ai_use_ledger.py` from the reviewer and researcher labels in the CSV databases; do not edit by hand. The data are in `AI_USE_LEDGER.csv`. The narrative statement is `../AI_USE_STATEMENT.md`; the per-study view is `STUDY_AUDIT_TRAIL.csv`.*', '',
          'This ledger says, stage by stage, which AI tool or model did what, how many records or rows carry its label, over which dates, and how many a human checked. It is meant to let a reader judge how much of the review rests on an AI\'s unverified judgment, and to let a critic target the weakest stage.', '',
          '## Stage by stage', '', '| Stage | Activity | Actor | Label in the databases | Units | First - last date | Human-checked |', '|---|---|---|---|---|---|---|']
    for r in rows:
        dates = f"{r['first_date']} to {r['last_date']}" if r['first_date'] else ''
        hc = r['human_checked']
        hc = f'{hc:,}' if isinstance(hc, int) else hc
        md.append(f"| {r['stage']} | {r['activity']} | {r['actor']} | `{r['label_pattern_in_databases']}` | {int(r['units']):,} {r['unit_type']} | {dates} | {hc} — {r['human_check_note']} |")
    md += ['', '## What is archived: the instructions the AI worked from', '', '| File | What it is |', '|---|---|']
    md += [f'| `{p}` | {d} |' for p, d in ARCHIVED]
    md += ['', '## What is NOT archived (read this before trying to reproduce or critique the AI work)', '']
    md += [f'{i}. {t}' for i, t in enumerate(NOT_ARCHIVED, 1)]
    md += ['', '## How to use this to find the weak points', '',
           '- The largest AI-only stages are the title/abstract exclusions, the full-text exclusions that were not adjudicated, every extraction, and every risk-of-bias rating. Pick a stage and test it: `AUDITING_GUIDE.md` §5 lists ways to challenge each.',
           '- To re-screen or re-extract a sample, `../03_extraction/second_extractor/README.md` and `../02_screening/full_text/REVIEWER_2_PRIORITY_QUEUE_README.md` are ready-made.',
           '- For one study, filter `STUDY_AUDIT_TRAIL.csv` on its `study_id`.', '']
    return buf.getvalue(), '\n'.join(md)


def main():
    csv_text, md_text = render()
    OUT_CSV.write_text(csv_text, encoding='utf-8', newline='')
    OUT_MD.write_text(md_text, encoding='utf-8')
    print(f'wrote {OUT_CSV.name} ({csv_text.count(chr(10)) - 1} rows) and {OUT_MD.name}')


if __name__ == '__main__':
    main()
