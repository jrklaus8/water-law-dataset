"""2026-10-14 (author's instruction, Round 10): make `mechanism_certainty` in extraction_database.csv follow CODEBOOK.md section 9 for all 1,080 included studies.

Before: 513 rows held an integer 0-4 and 567 held a narrative sentence that begins with a label ('High:', 'Moderate-high:', 'Moderate:', 'Low-moderate:'); 24 numeric 3s and 3 of the 8 numeric 4s sat on designs that cannot
support them (the codebook scale is design-driven: 3 = quasi-experimental evidence, 4 = experimental evidence). The data-quality audit flagged both problems.

The rule, deterministic and applied in this order (the parameters are the constants below, so an alternative mapping can be re-run from the provenance file):
  ceiling  4 for a RoB 2 study (a randomised trial); 3 for a ROBINS-I study whose overall rating is Low or Moderate ('credible identification' is read as no worse than Moderate confounding risk); 2 for everything else,
           including a ROBINS-I study rated Serious or Critical, every observational, mixed-methods, qualitative, doctrinal or jurimetric study, and every secondary review.
  numeric  new = min(old, ceiling). A numeric value is lowered to its ceiling, never raised.
  narrative  label High -> the ceiling; Moderate-high -> min(ceiling, 2); Moderate and Low-moderate -> 1.  (The narrative sentences say whether the paper documents the mechanism directly, 'High' and 'Moderate-high',
           or documents a real but qualitative or partial link, 'Moderate'; level 2 of the codebook is 'mechanism directly observed' and level 1 'documented association'. This label-to-level step is the AI's reading, not a validated
           mapping: a study that was High under a quasi-experimental ROBINS-I rating becomes 3, a High one under any other design becomes 2.)
The narrative sentence is not lost: the original value (full text) goes to 03_extraction/extracted_data/extraction_mechanism_certainty_original_2026-10-14.csv and is appended to the study's extraction_note; the evidence map
already keeps the label as its narrative `evidence_level` tier. A numeric value that is lowered is noted the same way.

Dry run by default; --apply rewrites extraction_database.csv (in place, line endings kept) and writes the provenance CSV. Idempotent (refuses to run twice). Run from legal-last-mile-systematic-review/."""
import csv, os, re, sys, tempfile
from collections import Counter

sys.path.insert(0, 'code/analysis')
csv.field_size_limit(sys.maxsize)
import current_figures as cf

ED = '03_extraction/extracted_data/extraction_database.csv'
PROV = '03_extraction/extracted_data/extraction_mechanism_certainty_original_2026-10-14.csv'
MARK = 'mechanism_certainty normalised 2026-10-14'
LABEL_LEVEL = {'high': 'ceiling', 'moderate-high': 2, 'moderate': 1, 'low-moderate': 1}   # 'ceiling' = the design ceiling below; a number is a cap applied with min(..., ceiling)
CREDIBLE = ('Low', 'Moderate')                                                             # ROBINS-I overall ratings that count as credible identification


def ceiling(tool, rating):
    first = re.split(r'[ (,:;]', rating.strip())[0]
    if tool == 'RoB 2':
        return 4
    if tool == 'ROBINS-I' and first in CREDIBLE:
        return 3
    return 2


def label_of(v):
    m = re.match(r'^\s*([A-Za-z]+(?:-[A-Za-z]+)?)', v)
    lab = m.group(1).lower() if m else ''
    assert lab in LABEL_LEVEL, f'unrecognised narrative label: {v[:60]}'
    return lab


def decide(r):
    v = r['mechanism_certainty'].strip()
    cap = ceiling(cf.tool_of(r['risk_of_bias_tool']), r['risk_of_bias_rating'])
    if v in ('0', '1', '2', '3', '4'):
        new = min(int(v), cap)
        return 'numeric', '', cap, new, ('kept' if new == int(v) else f'lowered from {v} to the design ceiling {cap}')
    lab = label_of(v)
    rule = LABEL_LEVEL[lab]
    new = cap if rule == 'ceiling' else min(rule, cap)
    return 'narrative', lab, cap, new, f"label '{lab}' mapped to {new} (ceiling {cap})"


def load(p):
    raw = open(p, newline='', encoding='utf-8').read()
    crlf = '\r\n' in raw[:20000]
    with open(p, newline='', encoding='utf-8') as f:
        rd = csv.DictReader(f)
        return rd.fieldnames, list(rd), crlf


def main(apply):
    fields, rows, crlf = load(ED)
    if any(MARK in r['extraction_note'] for r in rows) or os.path.exists(PROV):
        sys.exit('Already applied (the marker is in extraction_note or the provenance file exists); nothing to do.')
    prov, kinds = [], Counter()
    before, after = Counter(), Counter()
    for r in rows:
        kind, lab, cap, new, why = decide(r)
        old = r['mechanism_certainty']
        before[old.strip() if kind == 'numeric' else 'narrative'] += 1
        after[str(new)] += 1
        kinds[(kind, why.split(' ')[0] if kind == 'numeric' else 'mapped')] += 1
        prov.append({'study_id': r['study_id'], 'record_id': r['record_id'], 'original_value': old, 'original_type': kind, 'narrative_label': lab,
                     'risk_of_bias_tool': cf.tool_of(r['risk_of_bias_tool']), 'risk_of_bias_rating_first_word': re.split(r'[ (,:;]', r['risk_of_bias_rating'].strip())[0],
                     'design_ceiling': cap, 'new_value': new, 'rule': why})
        if apply:
            changed = kind == 'narrative' or str(new) != old.strip()
            r['mechanism_certainty'] = str(new)
            if changed:
                note = f"{MARK} (CODEBOOK section 9; original in extraction_mechanism_certainty_original_2026-10-14.csv): "
                note += f"original narrative text: {old.strip()} -> {new}." if kind == 'narrative' else f"{old.strip()} lowered to {new} because the design ceiling is {cap}."
                r['extraction_note'] = (r['extraction_note'].rstrip() + ' ' + note).strip()
    print('before:', dict(before))
    print('after: ', dict(sorted(after.items())))
    print('decisions:', dict(kinds))
    hi = [(p['study_id'], p['original_value'][:12], p['new_value']) for p in prov if p['original_type'] == 'numeric' and str(p['new_value']) != p['original_value'].strip()]
    print('numeric values lowered:', len(hi), Counter((o, n) for _, o, n in hi))
    if not apply:
        print('dry run; pass --apply to write')
        return
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(ED), suffix='.tmp')
    with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n' if crlf else '\n')
        w.writeheader(); w.writerows(rows)
    os.replace(tmp, ED)
    with open(PROV, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(prov[0]), lineterminator='\r\n'); w.writeheader(); w.writerows(prov)
    print('applied; wrote', ED, 'and', PROV)


if __name__ == '__main__':
    main('--apply' in sys.argv)
