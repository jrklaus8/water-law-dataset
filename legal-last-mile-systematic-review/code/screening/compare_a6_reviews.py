#!/usr/bin/env python3
"""Deterministic three-way comparison for the A6 tier-3 check: original AI, a second AI (e.g. Gemini) and the human reviewer (CK).

Pre-specified in 00_admin/A6_COMPARISON_PREREGISTRATION_2026-11-18.md. No model judgement is used here: it reads three CSV files and counts.
Inputs: the human fill-in sheet, the second AI's screening CSV (record_id, decision, exclusion_code, confidence, paper_read, rationale) and the reviewer queue (for the original AI decision).
Output: a Markdown report and a CSV with one row per record. The human sheet's own columns are never modified.
Run from legal-last-mile-systematic-review/."""
import argparse, csv
from collections import Counter

HUMAN_DEC = 'reviewer_decision (include/exclude/cannot_tell)'
VALID = ('include', 'exclude', 'cannot_tell')


def rd(p):
    with open(p, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def norm(v):
    v = (v or '').strip().lower()
    return v if v in VALID else ''


def compare(human, second, queue):
    ai = {r['record_id']: norm(r['ai_decision']) for r in queue}
    h = {r['record_id']: r for r in human}
    g = {r['record_id']: r for r in second}
    out = []
    for rid in h:
        hd, gd, od = norm(h[rid][HUMAN_DEC]), norm(g.get(rid, {}).get('decision')), ai.get(rid, '')
        decided = [d for d in (hd, gd, od) if d in ('include', 'exclude')]
        pattern = '/'.join(d or 'none' for d in (od, gd, hd))
        if hd == '':
            status = 'human not yet decided'
        elif gd == '':
            status = 'second AI missing'
        elif 'cannot_tell' in (hd, gd, od):
            status = 'cannot_tell involved'
        elif len(set(decided)) == 1:
            status = 'all three agree'
        else:
            status = 'DISAGREEMENT: look at this record'
        out.append({'record_id': rid, 'study_id': h[rid].get('study_id', ''), 'original_AI': od, 'second_AI': gd,
                    'human': hd, 'pattern_AI_second_human': pattern, 'status': status,
                    'second_AI_confidence': g.get(rid, {}).get('confidence', ''),
                    'second_AI_paper_read': g.get(rid, {}).get('paper_read', ''),
                    'human_paper_read': h[rid].get('paper_read (full/partial/abstract_only/not_read)', ''),
                    'human_saw_AI_reasoning_first': h[rid].get('saw_AI_reasoning_before_deciding (Y/N)', ''),
                    'human_saw_second_AI_first': h[rid].get('saw_Gemini_output_before_deciding (Y/N)', '')})
    return out


def report(rows):
    n = len(rows)
    st = Counter(r['status'] for r in rows)
    both = [r for r in rows if r['human'] in ('include', 'exclude') and r['second_AI'] in ('include', 'exclude')]
    pairs = {
        'original AI vs human': [(r['original_AI'], r['human']) for r in rows if r['human'] in ('include', 'exclude') and r['original_AI'] in ('include', 'exclude')],
        'second AI vs human': [(r['second_AI'], r['human']) for r in both],
        'original AI vs second AI': [(r['original_AI'], r['second_AI']) for r in rows if r['second_AI'] in ('include', 'exclude') and r['original_AI'] in ('include', 'exclude')],
    }
    md = ['# A6 tier-3 three-way comparison', '', f'{n} records. Counts only; no thresholds were pre-set (see the pre-registration file).', '', '## Status of each record', '']
    md += [f'- {k}: {v}' for k, v in sorted(st.items())]
    md += ['', '## Pairwise raw agreement (cannot_tell and undecided excluded; no kappa because every original-AI decision in tier 3 is "include")', '']
    for k, v in pairs.items():
        a = sum(x == y for x, y in v)
        md.append(f'- {k}: {a} of {len(v)} agree' + (f' ({100*a/len(v):.1f}%)' if v else ''))
    md += ['', '## Records to look at first (any disagreement)', '']
    for r in rows:
        if r['status'].startswith('DISAGREEMENT'):
            md.append(f"- {r['study_id'] or r['record_id']} ({r['record_id']}): original AI {r['original_AI']}, second AI {r['second_AI']} ({r['second_AI_confidence'] or 'no confidence'}), human {r['human']}")
    flags = [r for r in rows if r['human_saw_AI_reasoning_first'].strip().upper() == 'Y' or r['human_saw_second_AI_first'].strip().upper() == 'Y']
    md += ['', f'## Anchoring flags: {len(flags)} records where the human reports seeing AI output before deciding', '']
    md += [f"- {r['record_id']}" for r in flags]
    return '\n'.join(md) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--human', required=True); ap.add_argument('--second-ai', required=True)
    ap.add_argument('--queue', default='02_screening/full_text/full_text_reviewer_2_priority_queue_2026-09-28.csv')
    ap.add_argument('--out-csv', required=True); ap.add_argument('--out-md', required=True)
    a = ap.parse_args()
    rows = compare(rd(a.human), rd(a.second_ai), rd(a.queue))
    with open(a.out_csv, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    open(a.out_md, 'w', encoding='utf-8').write(report(rows))
    print(len(rows), 'records compared')


if __name__ == '__main__':
    main()
