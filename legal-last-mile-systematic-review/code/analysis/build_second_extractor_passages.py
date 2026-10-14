#!/usr/bin/env python3
"""Build a blind reading packet for the second-extractor sample (03_extraction/second_extractor/): the passages of each sampled paper that a human needs to extract the nine sheet fields, WITHOUT the AI's extracted codes.

Outputs
  03_extraction/second_extractor/SECOND_EXTRACTOR_SOURCE_PASSAGES.md        the packet (abstract, stated aim, methods excerpt, results excerpt, table and figure captions, with PDF pages). It reproduces longer
                                                                             stretches of copyrighted papers, so it is for the author's own use and is listed in .gitignore, not committed.
  03_extraction/second_extractor/second_extractor_sheet_BLIND_VALUES_2026-10-14.csv   the sheet with NO ai_value, no where_the_AI_looked and no stratum (the stratum names the appraisal tool the AI chose), to be filled blind.
  --merge FILLED.csv  writes second_extractor_sheet_BLIND_MERGED_2026-10-14.csv: a copy of the BLANK sheet with your blind values copied into second_extractor_value (rows matched on study_id and field),
                      `agrees` left empty, so that you compare against ai_value only after you have extracted, then run score_second_extractor_sheet.py on the merged file.

Nothing here uses the AI's values to choose passages: sections are found by heading, the aim by the authors' own purpose sentences, tables by caption. No confirmation of any kind is recorded.
The PDFs are not in the repository; give their directory with --pdf-dir (files named `<study_id>.pdf`).
Run from legal-last-mile-systematic-review/:  python3 code/analysis/build_second_extractor_passages.py --pdf-dir DIR
"""
import argparse
import csv
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402
import source_text_tools as T  # noqa: E402

csv.field_size_limit(sys.maxsize)
ROOT = cf.ROOT
SE = ROOT / '03_extraction/second_extractor'
BLANK = SE / 'second_extractor_sheet_BLANK_2026-10-04.csv'
OUT_MD = SE / 'SECOND_EXTRACTOR_SOURCE_PASSAGES.md'
OUT_BLIND = SE / 'second_extractor_sheet_BLIND_VALUES_2026-10-14.csv'
OUT_MERGED = SE / 'second_extractor_sheet_BLIND_MERGED_2026-10-14.csv'


# The sheet words three fields as a check of the AI's value ("does the AI value match", "the AI coded TRUE"). For a blind pass they are re-asked as independent questions; the other six keep the sheet's wording.
BLIND_WHAT = {
    'effect_estimate': "Headline result of the study (numbers, if any), in your own words, without looking at the AI's value",
    'risk_of_bias_tool': "Which appraisal tool fits this study's design: RoB 2, ROBINS-I, JBI Cross-Sectional, CASP Qualitative, MMAT, AMSTAR 2 or the Legal Institutional Evidence Appraisal Framework (see RISK_OF_BIAS.md)",
    'outcome_flags': "Which outcome fields apply to this study (for example water_access, sanitation_access, affordability, service_quality; the list is in CODEBOOK.md)",
    'mechanism_flags': "Which mechanism fields apply to this study (for example eligibility, fees, enforcement, participation, institutional_fragmentation; the list is in CODEBOOK.md)",
}


def read(p):
    with open(p, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def passages(doc):
    out = []
    p, t = T.abstract_excerpt(doc)
    out.append(('Abstract or opening text', f'PDF p. {p}', t))
    aims = T.aim_sentences(doc)
    out.append(('Stated aim (the authors\' own purpose sentences)', ', '.join(sorted({f'PDF p. {a}' for a, _ in aims})) or 'none found', ' '.join(s for _, s in aims) or 'No purpose sentence was found automatically; read the introduction.'))
    meth = T.section_excerpt(doc, ('method', 'data', 'design', 'sample', 'study area', 'study setting'), 1800, stop_words=('result', 'finding', 'discussion', 'conclusion'))
    out.append(('Methods or data excerpt', f'PDF pp. {meth[0]} to {meth[1]}' if meth else 'not found', meth[2] if meth else 'No methods or data heading was found automatically; read the methods section of the paper.'))
    res = T.section_excerpt(doc, ('result', 'finding', 'analysis'), 1800, stop_words=('discussion', 'conclusion'))
    out.append(('Results excerpt', f'PDF pp. {res[0]} to {res[1]}' if res else 'not found', res[2] if res else 'No results heading was found automatically; read the results section of the paper.'))
    caps = T.table_captions(doc)
    out.append(('Lines that begin with Table or Figure', 'PDF pages as listed', '; '.join(f'p. {p}: {c}' for p, c in caps) if caps else 'none found'))
    return out


def build(pdf_dir):
    sheet = read(BLANK)
    studies = list(dict.fromkeys(r['study_id'] for r in sheet))
    es = {r['study_id']: r for r in cf.read('es')}
    ed = {r['study_id']: r for r in cf.read('ed')}
    swim = sorted((s for s in studies if es.get(s, {}).get('synthesis_family') in ('A', 'B', 'C')), key=lambda x: int(x[1:]))
    cite = {r['study_id']: r['citation'] for r in sheet}
    docs = {s: T.Doc(Path(pdf_dir) / f'{s}.pdf') for s in studies if pdf_dir and (Path(pdf_dir) / f'{s}.pdf').exists()}
    have = [s for s in studies if s in docs]
    miss = [s for s in studies if s not in docs]
    what = {r['field']: BLIND_WHAT.get(r['field'], r['what_to_check']) for r in sheet if r['study_id'] == studies[0]}
    L = ['# Second-extractor source passages (blind packet, generated 2026-10-14)', '',
         "*Generated by `code/analysis/build_second_extractor_passages.py`. For your own use only: it reproduces stretches of copyrighted papers, so it is in `.gitignore` and is not committed. "
         "It contains no AI-extracted value, no `where_the_AI_looked` and no stratum label.*", '',
         '## How to run a genuinely blind pass', '',
         "1. Fill `second_extractor_sheet_BLIND_VALUES_2026-10-14.csv` (no AI values in it) from the passages below, or from the paper itself. Do not open the `ai_value` column of the BLANK sheet until you have finished.",
         "2. Merge: `python3 code/analysis/build_second_extractor_passages.py --merge path/to/your_filled_blind_sheet.csv` writes `second_extractor_sheet_BLIND_MERGED_2026-10-14.csv` (the BLANK sheet with your values in `second_extractor_value`, `agrees` empty).",
         "3. Open the merged sheet, compare each of your values with `ai_value`, and set `agrees (Y/N/cannot_tell)` yourself.",
         "4. Score it: `python3 code/analysis/score_second_extractor_sheet.py path/to/merged_and_judged.csv`. It reports the disagreement rate per field with Wilson 95% intervals and prints its own caveat about what the sample can speak for.", '',
         "The passages are located by section heading, by the authors' purpose sentences and by table caption; they may miss the sentence you need, so use the PDF when a field is not answered here. Page numbers are PDF page indexes. "
         "Quotes are verbatim apart from ligature expansion, joining of line-break hyphens and collapsed whitespace; `[...]` marks cut text.", '',
         '## The sample and the SWiM studies', '',
         f"- The sheet covers **{len(studies)} studies** (9 fields each, {len(sheet)} rows), drawn only from S001 to S200.",
         f"- **{len(swim)} of the 37 SWiM studies are in the sample:** {', '.join(swim)}. For these, the `effect_estimate` field is an independent human check of the extracted headline result.",
         f"- PDFs available to this build: **{len(have)} of {len(studies)}**. Not available (not found on disk or in the Drive folders searched; use your own copy): {', '.join(miss) if miss else 'none'}.", '',
         '## What each field asks (blind wording; three fields are re-asked as independent questions)', '']
    for f_, w in what.items():
        L.append(f"- `{f_}`: {w}")
    L += ['', '## Papers', '']
    for s in studies:
        L += [f"### {s}  ·  {cite[s]}", '']
        if s not in docs:
            L += ['*No PDF was available to this build, so no passages are given. Use your own copy of the paper.*', '']
            continue
        d = docs[s]
        L.append(f"*PDF: {d.n} pages, text layer {'ok' if d.chars / max(d.n, 1) >= 1200 else 'sparse or none (scan); passages may be missing'}.*")
        L.append('')
        for lab, where, text in passages(d):
            L += [f"**{lab}** ({where}):", '', f"> {text}", '']
    return studies, sheet, docs, '\n'.join(L).rstrip() + '\n'


def write_blind(sheet):
    cols = ['study_id', 'citation', 'doi', 'field', 'what_to_check', 'second_extractor_value', 'comment']
    with open(OUT_BLIND, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator='\n')
        w.writeheader()
        for r in sheet:
            w.writerow({'study_id': r['study_id'], 'citation': r['citation'], 'doi': r['doi'], 'field': r['field'], 'what_to_check': BLIND_WHAT.get(r['field'], r['what_to_check']), 'second_extractor_value': '', 'comment': ''})


def merge(path):
    blank = read(BLANK)
    filled = {(r['study_id'], r['field']): r['second_extractor_value'] for r in read(path)}
    n = 0
    for r in blank:
        v = filled.get((r['study_id'], r['field']), '')
        r['second_extractor_value'] = v
        r['agrees (Y/N/cannot_tell)'] = ''
        n += bool(v.strip())
    with open(OUT_MERGED, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(blank[0]), lineterminator='\n')
        w.writeheader()
        w.writerows(blank)
    print(f'merged {n} of {len(blank)} values into {OUT_MERGED.name}; now set `agrees` yourself against ai_value, then run score_second_extractor_sheet.py')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pdf-dir', default=os.environ.get('SWIM_PDF_DIR'))
    ap.add_argument('--merge')
    a = ap.parse_args()
    if a.merge:
        merge(a.merge)
        return
    studies, sheet, docs, md = build(a.pdf_dir)
    OUT_MD.write_text(md, encoding='utf-8')
    write_blind(sheet)
    print(f'wrote {OUT_MD.name} ({len(docs)} of {len(studies)} papers with passages) and {OUT_BLIND.name}')


if __name__ == '__main__':
    main()
