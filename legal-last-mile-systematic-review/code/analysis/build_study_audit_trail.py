#!/usr/bin/env python3
"""Per-study audit trail: for every included study, who made each decision about it, how deep each step went, and which checks it has had.

Writes 00_admin/STUDY_AUDIT_TRAIL.csv (one row per included study) and 00_admin/STUDY_AUDIT_TRAIL.md (what the columns mean and how the rows add up). Everything is derived from the
CSV databases and the dated verification files, using the same definitions as current_figures.py, so the file can be filtered, joined and challenged: it is the answer to
"for this study, what exactly has a human looked at?". A study's row never says more than the databases say; where nothing records a human check the cell says so.

Run from legal-last-mile-systematic-review/:  python3 code/analysis/build_study_audit_trail.py
"""
import csv
import io
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import current_figures as cf  # noqa: E402
import build_evidence_atlas as bea  # noqa: E402

ROOT = cf.ROOT
OUT_CSV = ROOT / '00_admin/STUDY_AUDIT_TRAIL.csv'
OUT_MD = ROOT / '00_admin/STUDY_AUDIT_TRAIL.md'
SPARSE = ROOT / '05_analysis/descriptive/sparse_record_audit_2026-10-04.csv'
SECOND_EXTRACTOR = ROOT / '03_extraction/second_extractor/second_extractor_sheet_BLANK_2026-10-04.csv'
SWIM_CHECKS = ROOT / '05_analysis/effect_sizes/SWIM_AI_SCOPE_CHECKS_2026-10-14.csv'
SWIM_CODING = ROOT / '05_analysis/effect_sizes/SWIM_DIRECTION_CODING_2026-10-14.csv'
FORMS = ROOT / '04_quality/appraisal_forms'

COLUMNS = [
    'study_id', 'record_id', 'citation_short', 'doi', 'publication_year', 'country', 'study_design_class',
    'ta_ai_decision', 'ta_second_pass',
    'ft_reviewer_1', 'inclusion_verified_by', 'second_ai_model', 'second_ai_model_conflict', 'borderline_include',
    'extracted_by', 'date_extracted', 'extraction_depth', 'source_location_recorded', 'in_sparse_audit', 'in_second_extractor_sample', 'second_extractor_checked',
    'rob_tool', 'rob_rating', 'rob_depth', 'rob_human_checked',
    'mechanism_family', 'outcome_family', 'mechanism_certainty',
    'effect_rows', 'synthesis_family', 'swim_inclusion_status', 'direction_coding_confirmed_by_author', 'scenarios_dropping_or_recoding',
    'linked_report_of', 'record_map_status',
]


def actor(label):
    if label.startswith(('Claude', 'claude')):
        return 'AI (Claude)'
    if label.startswith('Human-'):
        return 'human second reviewer'
    if label == 'CK':
        return 'principal investigator (CK)'
    if label.startswith('Codex-'):
        return 'AI (Codex, second model)'
    if label.startswith('Gemini-'):
        return 'AI (Gemini, second model)'
    return 'none recorded' if not label else label


def short(citation, n=110):
    c = ' '.join(citation.split())
    return c if len(c) <= n else c[:n - 1].rstrip() + '…'


def rows():
    ta = {r['record_id']: r for r in cf.read('ta')}
    ft = {r['record_id']: r for r in cf.read('ft')}
    ed, em = cf.read('ed'), {r['study_id']: r for r in cf.read('em')}
    es = cf.read('es')
    rmap = {r['study_id']: r for r in cf.read('map')}
    links = cf.read('links')
    sparse = {r['study_id'] for r in csv.DictReader(open(SPARSE, encoding='utf-8', newline=''))}
    sample = {r['study_id'] for r in csv.DictReader(open(SECOND_EXTRACTOR, encoding='utf-8', newline=''))}
    checks = {r['study_id']: r for r in csv.DictReader(open(SWIM_CHECKS, encoding='utf-8', newline=''))}
    coding = {r['study_id']: r for r in csv.DictReader(open(SWIM_CODING, encoding='utf-8', newline=''))}
    fam = {r['study_id']: r['synthesis_family'] for r in es if r['synthesis_family'] in ('A', 'B', 'C')}
    n_eff = Counter(r['study_id'] for r in es)
    scen = bea.gather()['scen']
    link_of = {}
    for r in links:
        link_of.setdefault(r['study_id_a'], []).append(r['study_id_b'])
        link_of.setdefault(r['study_id_b'], []).append(r['study_id_a'])
    forms = {p.name.split('_')[0] for p in FORMS.glob('S*.md')}
    out = []
    for e in sorted(ed, key=lambda r: int(r['study_id'][1:])):
        sid = e['study_id']
        f, t, m = ft[e['record_id']], ta.get(e['record_id'], {}), em[sid]
        r2 = f['reviewer_2']
        human_conf = r2.startswith('Human-')
        pi_ruling = (r2 == 'CK' or any(k in f['notes'] for k in cf.HUMAN_RULING_MARKS)) and not human_conf
        verified = 'human second reviewer' if human_conf else ('principal investigator ruling' if pi_ruling else 'none (AI only)')
        second = 'Codex' if r2.startswith('Codex-') else ('Gemini' if r2.startswith('Gemini-') else '')
        note = e['extraction_note']
        depth = 'abstract or metadata only' if note.startswith(cf.ABSTRACT_ONLY_PREFIXES) else ('full text (flagged sparse in the 2026-10-04 audit)' if sid in sparse else 'full text')
        tool = cf.tool_of(e['risk_of_bias_tool'])
        in_swim = sid in fam
        if in_swim:
            hv = human_conf or pi_ruling
            status = 'human-verified inclusion' if hv else ('AI-checked only' if checks.get(sid, {}).get('ai_scope_check') == 'passed' else 'AI only')
            confirmed = 'yes' if (checks.get(sid, {}).get('ck_raw_sign_agrees (Y/N)') == 'Y' and checks[sid].get('ck_substantive_direction_agrees (Y/N)') == 'Y') else 'no'
        else:
            status, confirmed = '', ''
        affected = ';'.join(s['name'].split(' ')[0] for s in scen if sid in s['dropped'] or sid in s['recoded'])
        out.append({
            'study_id': sid, 'record_id': e['record_id'], 'citation_short': short(e['citation']), 'doi': e['doi'], 'publication_year': e['publication_year'],
            'country': e['country'], 'study_design_class': m['study_design_class'],
            'ta_ai_decision': t.get('title_abstract_decision', ''), 'ta_second_pass': 'human second reviewer' if t.get('reviewer_2', '').startswith('Human-') else 'none',
            'ft_reviewer_1': actor(f['reviewer_1']), 'inclusion_verified_by': verified, 'second_ai_model': second,
            'second_ai_model_conflict': ('yes' if f['conflict'].lower() == 'true' else 'no') if second else '',
            'borderline_include': 'yes' if 'BORDERLINE INCLUDE' in f['notes'] else 'no',
            'extracted_by': 'AI (Claude)' if e['researcher'].startswith('Claude') else e['researcher'], 'date_extracted': e['date_extracted'], 'extraction_depth': depth,
            'source_location_recorded': 'yes' if (e['exact_location'] or e['page'] or e['table']) else 'no',
            'in_sparse_audit': 'yes' if sid in sparse else 'no', 'in_second_extractor_sample': 'yes' if sid in sample else 'no', 'second_extractor_checked': 'no',
            'rob_tool': tool, 'rob_rating': short(e['risk_of_bias_rating'], 90), 'rob_depth': 'signalling-question form on file' if sid in forms else 'rule-based batch rating', 'rob_human_checked': 'no',
            'mechanism_family': m['mechanism_family'], 'outcome_family': m['outcome_family'], 'mechanism_certainty': e['mechanism_certainty'],
            'effect_rows': n_eff.get(sid, 0), 'synthesis_family': fam.get(sid, ''), 'swim_inclusion_status': status,
            'direction_coding_confirmed_by_author': confirmed, 'scenarios_dropping_or_recoding': affected,
            'linked_report_of': ';'.join(sorted(link_of.get(sid, []))), 'record_map_status': rmap.get(sid, {}).get('status', ''),
        })
    return out


def render():
    data = rows()
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=COLUMNS, lineterminator='\n')
    w.writeheader()
    w.writerows(data)
    n = len(data)
    c = lambda key: Counter(r[key] for r in data)
    ver, depth, rob = c('inclusion_verified_by'), c('extraction_depth'), c('rob_depth')
    st = Counter(r['swim_inclusion_status'] for r in data if r['synthesis_family'])
    md = [
        '# Study audit trail', '',
        '*Generated by `code/analysis/build_study_audit_trail.py` from the CSV databases (same definitions as `current_figures.py`); do not edit by hand. The data are in `STUDY_AUDIT_TRAIL.csv`.*', '',
        f'One row per included study ({n:,} rows). For any study ID it answers: who decided the inclusion, who extracted the data and how deeply, how the risk of bias was rated, whether the study is in a synthesis and how far that has been checked. '
        'A cell says "none" or "no" wherever the databases record no human check; nothing here is inferred upward.', '',
        '## How the rows add up', '',
        '| Question | Answer |', '|---|---|',
        f"| Inclusion decided by the AI and verified by no human | {ver['none (AI only)']:,} |",
        f"| Inclusion confirmed by a human second reviewer | {ver['human second reviewer']:,} |",
        f"| Inclusion ruled on by the principal investigator (`CK`) | {ver['principal investigator ruling']:,} |",
        f"| Extracted from a full text (of which {depth['full text (flagged sparse in the 2026-10-04 audit)']:,} flagged sparse in the 2026-10-04 audit) | {depth['full text'] + depth['full text (flagged sparse in the 2026-10-04 audit)']:,} |",
        f"| Extracted from an abstract or metadata only | {depth['abstract or metadata only']:,} |",
        '| Extraction checked by a second extractor | 0 (a blind 60-study sample is prepared, not done) |',
        f"| Risk of bias rated from a signalling-question form on file / by a rule applied to the extracted fields | {rob['signalling-question form on file']:,} / {rob['rule-based batch rating']:,} |",
        '| Risk-of-bias rating checked by a human | 0 |',
        f"| In a structured synthesis (families A, B, C) | {sum(st.values())} (human-verified inclusion {st['human-verified inclusion']}, AI-checked only {st['AI-checked only']}) |",
        f"| Direction coding confirmed by the author | {sum(r['direction_coding_confirmed_by_author'] == 'yes' for r in data)} |", '',
        '## Columns', '',
        '| Column | Meaning |', '|---|---|',
        '| `study_id`, `record_id` | The study and the screening record it came from (`R…`); see `GLOSSARY.md` |',
        '| `citation_short`, `doi`, `publication_year`, `country`, `study_design_class` | Identification, as extracted |',
        '| `ta_ai_decision`, `ta_second_pass` | The AI\'s title/abstract decision; whether a human second reviewer also saw the record (the include-or-unsure records only) |',
        '| `ft_reviewer_1` | Who made the first full-text decision. `AI (Claude)` for every row, including rows whose label was inferred when it was backfilled (see item A2) |',
        '| `inclusion_verified_by` | `human second reviewer` (a `Human-` confirmation), `principal investigator ruling` (reviewer `CK` or a dated ruling note), or `none (AI only)`. A second AI model\'s agreement is **not** a human verification |',
        '| `second_ai_model`, `second_ai_model_conflict` | Whether Codex or Gemini blind re-screened the record and disagreed. Only recorded while `reviewer_2` still holds the model label; a later ruling by the principal investigator replaces it |',
        '| `borderline_include` | Kept but flagged because the link to the rule-type mechanism is thin |',
        '| `extracted_by`, `date_extracted` | Extraction is always by the AI; there is no second extractor |',
        '| `extraction_depth` | `abstract or metadata only`, `full text`, or `full text (flagged sparse in the 2026-10-04 audit)` |',
        '| `source_location_recorded` | Whether the row records a page, table or location an auditor can go to |',
        '| `in_sparse_audit` | Listed in `05_analysis/descriptive/sparse_record_audit_2026-10-04.csv` as a likely shallow extraction |',
        '| `in_second_extractor_sample`, `second_extractor_checked` | In the prepared blind 60-study sample; whether anyone has checked it (always `no` so far) |',
        '| `rob_tool`, `rob_rating`, `rob_depth`, `rob_human_checked` | The instrument and the start of the rating text (the full text is in the extraction database; most non-causal instruments give domain-level answers, not one overall rating); whether a signalling-question form exists in `04_quality/appraisal_forms/` or the rating is a rule applied to extracted fields; whether a human checked it (always `no`) |',
        '| `mechanism_family`, `outcome_family`, `mechanism_certainty` | Evidence-map labels (AI-assigned, with the researcher\'s vocabulary rulings); certainty 0 to 4 per `CODEBOOK.md` §9 |',
        '| `effect_rows`, `synthesis_family` | Rows in `effect_sizes.csv`; the family (A, B or C) if the study is in a synthesis |',
        '| `swim_inclusion_status`, `direction_coding_confirmed_by_author` | For synthesis studies: `human-verified inclusion` or `AI-checked only`; whether the author confirmed both direction codings |',
        '| `scenarios_dropping_or_recoding` | Sensitivity scenarios (`S4`, `S4c`, `S4e`, `S5`, `S4d`) that drop or recode the study. Scenario names are not study IDs |',
        '| `linked_report_of`, `record_map_status` | Companion reports of the same underlying study; the study-to-record link status |', '',
        '## Using it', '',
        '```python',
        'import pandas as pd',
        "t = pd.read_csv('00_admin/STUDY_AUDIT_TRAIL.csv')",
        "t[(t.inclusion_verified_by == 'none (AI only)') & (t.extraction_depth != 'full text')]   # AI-only inclusions with a thin extraction",
        "t[t.synthesis_family.notna() & (t.swim_inclusion_status == 'AI-checked only')]           # synthesis studies nobody has verified",
        '```', '',
        'To trace a row to the evidence, follow `AUDITING_GUIDE.md` §3 with the `study_id` and `record_id`.',
    ]
    return buf.getvalue(), '\n'.join(md) + '\n'


def main():
    csv_text, md_text = render()
    OUT_CSV.write_text(csv_text, encoding='utf-8', newline='')
    OUT_MD.write_text(md_text, encoding='utf-8')
    print(f'wrote {OUT_CSV.name} ({csv_text.count(chr(10)) - 1:,} studies) and {OUT_MD.name}')


if __name__ == '__main__':
    main()
