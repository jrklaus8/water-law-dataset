#!/usr/bin/env python3
"""Advisory screen of the INCLUDED studies against inclusion criterion 3 ("contains empirical evidence or a systematic empirical synthesis").

Flags included studies whose own extracted design text says essay, theoretical, conceptual, simulation or modelling AND whose sample-size field names no primary
sample (blank, 'not stated', 'no primary...', 'none'). The 13 narrative or non-systematic reviews already listed in DECISIONS_AND_OPEN_ITEMS.md (reviews are handled
by the AMSTAR 2 eligibility question) and studies with an effect-size row are left out, so this is the residue: possible conceptual or theory-only includes, the same
kind of record the S356 exclusion (E05, narrative policy overview) removed. Cue-word match on extracted text, not a validated judgement; a flagged study may well be
empirical (a modelling study fed with real data). Nothing changes. Writes 05_analysis/descriptive/INCLUDES_CRITERION3_SCREEN_2026-10-04.{csv,md}. Run from the project root."""
import csv
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402

OUT_CSV = cf.ROOT / '05_analysis/descriptive/INCLUDES_CRITERION3_SCREEN_2026-10-04.csv'
OUT_MD = cf.ROOT / '05_analysis/descriptive/INCLUDES_CRITERION3_SCREEN_2026-10-04.md'
CUE = re.compile(r'essay|theoretical|game-theoretic|conceptual|simulation|model(l)?ing study|decision-analytic|normative|ex-ante|perspective article|framework (demonstration|development)', re.I)
NO_SAMPLE = re.compile(r'^\s*$|not stated|not reported|no primary|none\b|^n/?a\b|no (stated|sample)', re.I)
REVIEWS_ALREADY_LISTED = {'S079', 'S320', 'S321', 'S322', 'S326', 'S429', 'S430', 'S436', 'S440', 'S466', 'S479', 'S480', 'S482'}  # DECISIONS_AND_OPEN_ITEMS.md, narrative/non-systematic reviews
# What reading the Drive copy of each flagged study showed (2026-10-04; an AI reading, same model family as the extraction, not independent). Hand-entered, so it is listed
# here rather than derived; studies not in the dict have no Drive text.
DRIVE_CHECK = {
    'S219': 'Drive PDF is the full article (Aquino & Ledo 2023): a stylised theoretical model, then tested on municipal panel data with an econometric model; empirical, so it meets criterion 3 and the cue was a false positive',
    'S264': 'Drive file is only a Wageningen research-portal abstract page (Joy et al. 2014): a conceptual argument illustrated with evidence from India; no full text to judge how much is empirical',
    'S297': 'Drive file is the journal page with the full introduction (Jones 2015): case-study research on WaterAid in Mali (collaborative fieldwork 2010-11); empirical case study, so it likely meets criterion 3',
    'S314': 'Drive file is only a Wageningen research-portal abstract page (Mehta & Karpouzoglou 2015): states it shows that peri-urban waterscapes fall outside planning models for Ghaziabad; empirical basis cannot be judged from the abstract',
    'S462': 'full article in Drive under an author-title file name, not the record id (Araujo et al. 2024): multiobjective optimisation and scenario modelling of water-supply investment pathways for two service areas of the Federal District of Brazil, with equity disaggregation; model-based on local data, with little legal or institutional exposure. Compare R0532032FE3BB (Kathmandu scenario modelling), excluded E06: the two are alike, so one of the two decisions is inconsistent',
    'S340': 'searched by title as well as record id: no Drive copy found',
    'S513': 'full article in Drive (McGranahan 2015, read 2026-10-09): a conceptual and policy argument on the right to sanitation; two community-driven initiatives (Orangi Pilot Project, Karachi; the Mahila Milan/SPARC/NSDF Alliance, Pune and Mumbai) are summarised from published documentation, with no stated data, sample or method -- fails criterion 3 on the full text (proposal only; see A22_VERDICTS_2026-10-04.csv)',
}
FIELDS = ['study_id', 'record_id', 'tool', 'cue', 'study_design', 'sample_size', 'extraction_note_start', 'drive_check']


def build():
    es = {r['study_id'] for r in cf.read('es')}
    em = {r['study_id']: r for r in cf.read('em')}
    rows = []
    for r in cf.read('ed'):
        s = r['study_id']
        if s in es or s in REVIEWS_ALREADY_LISTED or em[s]['study_design_class'] == 'systematic_review_secondary':
            continue
        txt = ' | '.join([em[s]['study_design_class'], r['study_design']])
        m = CUE.search(txt)
        if m and NO_SAMPLE.search(r['sample_size'] or ''):
            rows.append({'study_id': s, 'record_id': r['record_id'], 'tool': cf.tool_of(r['risk_of_bias_tool']), 'cue': m.group(0).lower(), 'study_design': r['study_design'][:120].replace('\n', ' '),
                         'sample_size': (r['sample_size'] or '')[:60], 'extraction_note_start': r['extraction_note'][:90].replace('\n', ' '), 'drive_check': DRIVE_CHECK.get(s, 'no Drive text found')})
    return sorted(rows, key=lambda x: int(x['study_id'][1:]))


def render(rows):
    L = ['# Included studies that may fail criterion 3 (conceptual or theory-only)', '',
         f"Generated by `code/analysis/audit_includes_criterion3.py`. {len(rows)} of {len(cf.read('ed')):,} included studies have a design text with an essay, theoretical, conceptual, simulation or modelling cue and no primary sample named in the sample-size field. "
         "Excluded from the screen: studies with an effect-size row, systematic-review-class rows, and the 13 narrative reviews already listed in `DECISIONS_AND_OPEN_ITEMS.md`. Advisory only: cue words in extracted text, not a validated judgement; some of these are empirical (a model fed with real data) and may stay. "
         "The precedent is S356 (a narrative policy overview, excluded E05 on its full text, 2026-09-28).", '',
         "**What would resolve it:** read the flagged studies against `INCLUSION_EXCLUSION.md` criterion 3 (`DECISIONS_AND_OPEN_ITEMS.md` A22); any that are conceptual or theory-only would be excluded E05 by a dated script like `resolve_s356_exclude_2026-09-28.py` (or `resolve_a16_pending_reversals.py` once queued).", '',
         "| Study | Tool | Cue | Design (extracted) | Sample size field |", "|---|---|---|---|---|"]
    L += [f"| {r['study_id']} | {r['tool']} | {r['cue']} | {r['study_design'][:90]} | {r['sample_size'] or '(blank)'} |" for r in rows]
    L += ['', '## What the Drive copies showed', '', 'An AI reading (same model family as the extraction, so not independent) of the copy of each flagged study held in the researcher\'s Drive:', '']
    L += [f"- **{r['study_id']}** — {r['drive_check']}" for r in rows]
    return '\n'.join(L) + '\n'


if __name__ == '__main__':
    rows = build()
    with open(OUT_CSV, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator='\n'); w.writeheader(); w.writerows(rows)
    OUT_MD.write_text(render(rows), encoding='utf-8')
    print(f'wrote {OUT_CSV.relative_to(cf.ROOT)} ({len(rows)} rows) and {OUT_MD.name}')
