#!/usr/bin/env python3
"""Build the PRIORITISED human reviewer_2 queue for full-text decisions (2026-09-28).

Tiers (rationale in 02_screening/full_text/REVIEWER_2_PRIORITY_QUEUE_README.md):
  1  every decided row with NO reviewer label (provenance unknown)                       -- all of them
  2  seeded, stratified random sample of substantive EXCLUDES (E08 duplicates and E10 'inaccessible' excluded from sampling)
  3  seeded random sample of INCLUDES beyond the 100 already human-confirmed (S001-S100)  -- optional

Deterministic: fixed seed, stratified allocation stated below. Regenerate:  python3 code/screening/build_reviewer2_priority_queue.py
Run from the project root. Writes 02_screening/full_text/full_text_reviewer_2_priority_queue_2026-09-28.csv
"""
import csv, random, sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'analysis'))
import current_figures as cf  # noqa: E402

ROOT = cf.ROOT
OUT = ROOT / '02_screening/full_text/full_text_reviewer_2_priority_queue_2026-09-28.csv'
SEED = 20260928
EXCLUDE_SAMPLE_TARGET = 100     # proportional across codes, minimum MIN_PER_CODE per code
MIN_PER_CODE = 3
INCLUDE_SAMPLE = 50
SKIP_EXCLUDE_CODES = {'E08', 'E10'}     # duplicates and inaccessible-text are not content judgments a second reader can re-make from the paper


def build():
    ft = cf.read('ft')
    ext = {r['record_id']: r for r in cf.read('ed')}
    m = {r['record_id']: r['study_id'] for r in cf.read('map') if r['status'] == 'active'}
    confirmed = {r['record_id'] for r in ft if r['reviewer_2']}
    dec = [r for r in ft if r['final_decision']]
    rng = random.Random(SEED)
    tier1 = sorted([r for r in dec if not r['reviewer_1']], key=lambda r: (r['final_decision'] != 'include', r['record_id']))
    chosen = {r['record_id'] for r in tier1}
    pool = defaultdict(list)
    for r in sorted(dec, key=lambda r: r['record_id']):
        if r['final_decision'] == 'exclude' and r['exclusion_reason'] not in SKIP_EXCLUDE_CODES and r['record_id'] not in chosen and not r['reviewer_2']:
            pool[r['exclusion_reason']].append(r)
    total = sum(len(v) for v in pool.values())
    tier2 = []
    for code in sorted(pool):
        k = min(len(pool[code]), max(MIN_PER_CODE, round(EXCLUDE_SAMPLE_TARGET * len(pool[code]) / total)))
        tier2 += rng.sample(pool[code], k)
    tier2.sort(key=lambda r: (r['exclusion_reason'], r['record_id']))
    chosen |= {r['record_id'] for r in tier2}
    inc_pool = sorted([r for r in dec if r['final_decision'] == 'include' and r['record_id'] not in chosen and r['record_id'] not in confirmed], key=lambda r: r['record_id'])
    tier3 = sorted(rng.sample(inc_pool, INCLUDE_SAMPLE), key=lambda r: r['record_id'])
    rows = []
    why = {1: 'no reviewer_1 label recorded: provenance of the decision unknown',
           2: 'random check that AI excludes are correct (stratified by exclusion code)',
           3: 'random check that AI includes (and their extraction) are correct; optional'}
    for tier, group in ((1, tier1), (2, tier2), (3, tier3)):
        for r in group:
            inc = r['final_decision'] == 'include'
            rows.append({'priority_tier': tier, 'priority_rank': len(rows) + 1, 'record_id': r['record_id'], 'study_id': m.get(r['record_id'], ''),
                         'year': r['year'], 'authors': r['authors'], 'title': r['title'], 'doi': r['doi'], 'url': r['url'],
                         'full_text_status': r['full_text_status'], 'ai_decision': r['final_decision'],
                         'ai_exclusion_code': r['exclusion_reason'], 'ai_reviewer_label': r['reviewer_1'] or '(none recorded)',
                         'why_prioritised': why[tier],
                         'reviewer_2_decision (include/exclude/cannot_tell)': '', 'reviewer_2_exclusion_code (E01-E12)': '', 'reviewer_2_agrees_with_AI (Y/N)': '', 'reviewer_2_comment': '',
                         'ai_reasoning_READ_AFTER_YOUR_OWN_JUDGMENT': (r['exclusion_reason_detail'] if not inc else '') or r['notes'][:1200]
                             or (ext[r['record_id']]['extraction_note'][:600] if r['record_id'] in ext and ext[r['record_id']]['extraction_note'] else '')
                             or 'NO WRITTEN RATIONALE is recorded for this decision (a provenance gap; treat as unreviewed)'})
    return rows


if __name__ == '__main__':
    rows = build()
    with open(OUT, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\r\n'); w.writeheader(); w.writerows(rows)
    from collections import Counter
    print(f'wrote {OUT.name}: {len(rows)} rows; tiers', dict(Counter(r["priority_tier"] for r in rows)))
