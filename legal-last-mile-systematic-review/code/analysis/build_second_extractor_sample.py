#!/usr/bin/env python3
"""Draw a seeded, stratified sample of extracted studies for an independent (human) second extraction, and write a blank comparison sheet.

Purpose: estimate how often the AI's extraction disagrees with the source paper. Nothing about the AI extraction is verified until a human fills this in.
Population: all extracted studies except those still extracted from abstract/metadata only (a second extractor cannot check those against a full text the
project does not hold). Strata are drawn in order without overlap (seed 20260929):
  effect-size rows 15 | RoB 2 / ROBINS-I 8 | JBI Cross-Sectional 8 | MMAT 8 | CASP Qualitative 8 | Legal Framework 8 | AMSTAR 2 + NONE 5   (total 60)
Output (long format, one row per study x field): 03_extraction/second_extractor/second_extractor_sheet_BLANK_2026-09-29.csv
The human copies the file, fills `second_extractor_value` / `agrees` / `comment`, and scores it with code/analysis/score_second_extractor_sheet.py.
Regenerating overwrites only the BLANK file. Run from the project root.
"""
import csv, random, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402

ROOT = cf.ROOT
OUT = ROOT / '03_extraction/second_extractor/second_extractor_sheet_BLANK_2026-09-29.csv'
SEED = 20260929
STRATA = [('effect-size row', 15), ('RoB 2 / ROBINS-I', 8), ('JBI Cross-Sectional', 8), ('MMAT', 8), ('CASP Qualitative', 8), ('Legal Framework', 8), ('AMSTAR 2 / NONE', 5)]
FIELDS = [
    ('publication_year', 'Year of publication'),
    ('country', 'Country / countries studied'),
    ('sample_size', 'Sample size / number of units'),
    ('study_design', 'Study design as the authors describe it'),
    ('effect_estimate', 'Headline result (numbers, if any) — does the AI value match the paper?'),
    ('risk_of_bias_tool', 'Is this the right appraisal tool for the design?'),
    ('mechanism_certainty', '0 inferred, 1 documented association, 2 mechanism directly observed, 3 quasi-experimental, 4 experimental'),
    ('outcome_flags', 'Outcome fields the AI coded TRUE (water_access, sanitation_access, affordability, ...): right and complete?'),
    ('mechanism_flags', 'Mechanism fields the AI coded TRUE (eligibility, fees, enforcement, ...): right and complete?'),
]
OUTCOME = ['water_access', 'sanitation_access', 'service_coverage', 'service_reliability', 'service_quantity', 'service_quality', 'affordability', 'service_continuity', 'formal_connection', 'application_success', 'refusal', 'delay_outcome']
MECH = ['eligibility', 'burden', 'discretion_accommodation', 'enforcement', 'documentation', 'tenure', 'property', 'planning', 'zoning', 'building_permit', 'service_area', 'fees', 'procedural_steps', 'delay',
        'discretion', 'hardship_exception', 'administrative_review', 'complaint', 'judicial_review', 'disconnection', 'reconnection', 'sanction', 'participation', 'institutional_fragmentation', 'political_coordination', 'bureaucratic_assistance']


def draw():
    ed = {r['study_id']: r for r in cf.read('ed')}
    es = {r['study_id']: r for r in cf.read('es')}
    ft = {r['record_id']: r for r in cf.read('ft')}
    pool = sorted((s for s, r in ed.items() if not r['extraction_note'].startswith(cf.ABSTRACT_ONLY_PREFIXES)), key=lambda x: int(x[1:]))
    rng = random.Random(SEED)
    chosen, used = [], set()
    for name, k in STRATA:
        if name == 'effect-size row':
            cand = [s for s in pool if s in es]
        elif name == 'RoB 2 / ROBINS-I':
            cand = [s for s in pool if cf.tool_of(ed[s]['risk_of_bias_tool']) in ('RoB 2', 'ROBINS-I')]
        elif name == 'AMSTAR 2 / NONE':
            cand = [s for s in pool if cf.tool_of(ed[s]['risk_of_bias_tool']) in ('AMSTAR 2', 'NONE')]
        else:
            cand = [s for s in pool if cf.tool_of(ed[s]['risk_of_bias_tool']) == name]
        cand = [s for s in cand if s not in used]
        pick = sorted(rng.sample(cand, k), key=lambda x: int(x[1:]))
        used.update(pick)
        chosen += [(s, name) for s in pick]
    rows = []
    for s, stratum in chosen:
        r = ed[s]
        f = ft[r['record_id']]
        loc = '; '.join(x for x in (('page ' + r['page']) if r['page'] else '', ('table ' + r['table']) if r['table'] else '', ('figure ' + r['figure']) if r['figure'] else '', r['exact_location'][:100]) if x)
        for key, prompt in FIELDS:
            if key == 'outcome_flags':
                val = ', '.join(o for o in OUTCOME if r[o] == 'TRUE') or '(none coded)'
            elif key == 'mechanism_flags':
                val = ', '.join(m for m in MECH if r[m] == 'TRUE') or '(none coded)'
            elif key == 'risk_of_bias_tool':
                val = cf.tool_of(r['risk_of_bias_tool'])
            elif key == 'effect_estimate' and s in es:
                val = es[s]['effect_estimate'][:400]
            elif key == 'effect_estimate':
                val = r['effect_estimate'][:400]
            else:
                val = r[key][:300]
            rows.append({'study_id': s, 'stratum': stratum, 'citation': r['citation'][:200], 'doi': r['doi'], 'url': f['url'], 'where_the_AI_looked': loc,
                         'field': key, 'what_to_check': prompt, 'ai_value': val, 'second_extractor_value': '', 'agrees (Y/N/cannot_tell)': '', 'comment': ''})
    return rows


if __name__ == '__main__':
    rows = draw()
    with open(OUT, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\r\n'); w.writeheader(); w.writerows(rows)
    print('wrote', OUT.name, len({r['study_id'] for r in rows}), 'studies,', len(rows), 'rows')
