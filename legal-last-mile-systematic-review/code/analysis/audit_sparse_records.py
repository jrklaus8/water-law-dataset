#!/usr/bin/env python3
"""Read-only audit of how thinly each extraction row is evidenced, written because the original "abstract-only" count (62 when this was written; fewer remain after the 2026-10-04 re-extractions) is computed from one note prefix
and that prefix missed S327 (a citation-level row) and S214 ("extracted from openly-readable abstract ... full text not accessible").

For every extraction row it records, from the CSV alone (no source papers), five signals:
  S1 prefix      extraction_note starts with the abstract-only prefix (the 62 already on the request list)
  S2 note        the note says the abstract/citation/metadata was all that was read ("full text not accessible", "abstract/citation-level only", ...)
  S3 location    the recorded location cites the abstract alone (section is only Abstract/Resumen/Resumo, or exact_location begins "Abstract" with no deeper section) and no table or figure
  S4 first-pages the recorded section is the abstract plus the introduction/background/highlights only
  S5 sparse      9 or fewer of 14 descriptive content fields are populated
Rows already re-extracted from full text (note says it supersedes an abstract-only entry, or a full-text appraisal) are excluded.
Strength: strong = S1 or S2; moderate = S3; weak = S4 or S5 only. The signals are heuristics read from the AI's own recorded fields, not the papers: a row can cite
"Abstract" because that is where a quotation came from. Use the list to decide which full texts to fetch next, not as a finding about any paper.
Nothing here changes a flag, a rating or a decision. Writes 05_analysis/descriptive/sparse_record_audit_2026-10-04.csv and SPARSE_RECORD_AUDIT_2026-10-04.md. Run from the project root.
"""
import csv, re, sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402

ROOT = cf.ROOT
OUT_CSV = ROOT / '05_analysis/descriptive/sparse_record_audit_2026-10-04.csv'
OUT_MD = ROOT / '05_analysis/descriptive/SPARSE_RECORD_AUDIT_2026-10-04.md'
CONTENT = ['country', 'legal_system', 'urban_rural', 'service_provider', 'regulatory_model', 'population', 'sample_size', 'effect_measure', 'effect_estimate',
           'extraction_sample_size', 'model_type', 'study_design', 'section', 'exact_location']
ABS = r'(abstract|resumen|resumo)'
SEC_ONLY = re.compile(rf'^\s*{ABS}(\s*[/;,&]\s*{ABS})*\s*\.?\s*$', re.I)
SEC_INTRO = re.compile(rf'^\s*{ABS}\s*[;,/&]\s*(introduction|background|highlights|introducci[oó]n|introdu[cç][aã]o|literature review)\s*$', re.I)
LOC_ABS = re.compile(r'^\s*(p\.?\s*\d+(-\d+)?\s*\(?)?\(?\s*(abstract|resumen|resumo)', re.I)
NOTE_THIN = re.compile(r'full[- ]text (is |was )?(not|un)(available|accessible)|only the abstract|abstract[/ -]*(and )?citation[- ]level|citation[- ]level|summary[- ]level|'
                       r'abstract/repository metadata|not yet retrieved|extracted from (the )?(openly[- ]readable )?abstract|extraction depth', re.I)
REEXTRACTED = re.compile(r'supersedes the abstract|upgrading the original|full-text appraisal|full-text re-extraction|re-extracted from (the )?full text|corrects the earlier abstract', re.I)


def audit():
    ed = cf.read('ed')
    em = {r['study_id']: r for r in cf.read('em')}
    es = Counter(r['study_id'] for r in cf.read('es'))
    ft = {r['record_id']: r for r in cf.read('ft')}
    out = []
    for r in ed:
        s = r['study_id']
        note = r['extraction_note']
        re_ext = bool(REEXTRACTED.search(note)) or 're-extraction' in r['researcher'] or 'full-text appraisal' in r['researcher']
        if re_ext:
            continue
        n_content = sum(1 for k in CONTENT if r[k].strip())
        s1 = note.startswith(cf.ABSTRACT_ONLY_PREFIXES)
        s2 = (not s1) and bool(NOTE_THIN.search(note))
        deeper = bool(r['table'].strip() or r['figure'].strip())
        sec = r['section']
        s3 = (not deeper) and (bool(SEC_ONLY.match(sec)) or ((not sec.strip() or bool(SEC_ONLY.match(sec))) and bool(LOC_ABS.match(r['exact_location']))))
        s4 = bool(SEC_INTRO.match(sec)) and not deeper
        s5 = n_content <= 9
        if not (s1 or s2 or s3 or s4 or s5):
            continue
        strength = 'strong' if (s1 or s2) else 'moderate' if s3 else 'weak'
        tool = cf.tool_of(r['risk_of_bias_tool'])
        f = ft.get(r['record_id'], {})
        weight = []
        if es[s]:
            weight.append('effect-size row')
        if em[s]['quantitative_synthesis_eligible'] == 'TRUE':
            weight.append('quantitative-eligible')
        if tool in ('RoB 2', 'ROBINS-I'):
            weight.append(tool)
        if tool == 'AMSTAR 2':
            weight.append('AMSTAR 2')
        if r['mechanism_certainty'].strip() in ('3', '4'):
            weight.append('certainty 3-4')
        out.append({'study_id': s, 'record_id': r['record_id'], 'strength': strength, 'S1_prefix': s1, 'S2_note': s2, 'S3_location_abstract_only': s3, 'S4_abstract_plus_intro': s4,
                    'S5_sparse_9_or_fewer': s5, 'content_fields_of_14': n_content, 'in_current_request_list': s1, 'risk_of_bias_tool': tool, 'weight': '; '.join(weight),
                    'weight_score': len(weight), 'year': f.get('year', ''), 'authors': f.get('authors', '')[:80], 'title': f.get('title', '')[:140], 'doi': f.get('doi', ''),
                    'section': sec[:60], 'extraction_note_start': note[:120]})
    rank = {'strong': 0, 'moderate': 1, 'weak': 2}
    return sorted(out, key=lambda x: (rank[x['strength']], -x['weight_score'], int(x['study_id'][1:])))


def render(rows):
    n_all = len(cf.read('ed'))
    by = Counter(r['strength'] for r in rows)
    s1 = sum(r['S1_prefix'] for r in rows)
    new = [r for r in rows if not r['S1_prefix']]
    new_s = [r for r in new if r['strength'] == 'strong']
    new_m = [r for r in new if r['strength'] == 'moderate']
    L = ["# Sparse-record audit — which extractions are thinly evidenced?", "",
         "*Generated by `code/analysis/audit_sparse_records.py`. Read-only; changes no flag, rating or decision. The signals are read from the AI's own recorded fields, not from the papers, "
         "so they are a way to choose which full texts to fetch next, not a finding about any paper. Rows already re-extracted from full text are excluded.*", "",
         "## Why this exists", "",
         f"The \"{cf.compute()['abstract_only_extractions']} abstract-only extractions\" figure counts one note prefix. That prefix missed S327 (a citation-level row) and S214 (\"extracted from openly-readable abstract … full text not accessible\"), "
         "so the figure is a **floor**, not the full count of shallow extractions. This audit looks for four further signals.", "",
         "## Signals", "",
         "| Signal | Meaning | Rows |", "|---|---|---|",
         f"| S1 prefix | note starts with the abstract-only prefix (already on the request list) | {s1} |",
         f"| S2 note | note says only the abstract, citation or metadata was read | {sum(r['S2_note'] for r in rows)} |",
         f"| S3 location | recorded location cites the abstract alone, no table or figure | {sum(r['S3_location_abstract_only'] for r in rows)} |",
         f"| S4 first pages | section is the abstract plus introduction, background or highlights only | {sum(r['S4_abstract_plus_intro'] for r in rows)} |",
         f"| S5 sparse | 9 or fewer of 14 descriptive content fields populated | {sum(r['S5_sparse_9_or_fewer'] for r in rows)} |", "",
         "## Result", "",
         f"- **{len(rows)} of {n_all:,} extraction rows** show at least one signal and have not been re-extracted from full text: **{by['strong']} strong** (S1 or S2), **{by['moderate']} moderate** (location cites the abstract alone), **{by['weak']} weak** (abstract plus introduction, or sparse fields).",
         f"- **{len(new)} of them are not on the current abstract-only request list**: {len(new_s)} strong and {len(new_m)} moderate. These are the rows the prefix check missed.",
         "- A \"moderate\" row is not proven abstract-only: an extractor may cite \"Abstract\" because that is where a quotation sits while having read more. Treat the moderate tier as a **verification queue**, not a count of failures.", "",
         "### By risk-of-bias tool (rows not already on the request list)", "", "| Tool | strong | moderate | weak |", "|---|---|---|---|"]
    tools = Counter((r['risk_of_bias_tool'], r['strength']) for r in new)
    for t in sorted({r['risk_of_bias_tool'] for r in new}):
        L.append(f"| {t} | {tools[(t, 'strong')]} | {tools[(t, 'moderate')]} | {tools[(t, 'weak')]} |")
    L += ["", "### Strong and moderate rows with analytic weight (effect-size row, quantitative-eligible, RoB 2/ROBINS-I, AMSTAR 2, certainty 3–4) — not on the current list", "",
          "| Study | Strength | Signals | Weight | Tool | Section recorded |", "|---|---|---|---|---|---|"]
    heavy = [r for r in new if r['strength'] in ('strong', 'moderate') and r['weight_score'] >= 2]
    for r in heavy[:60]:
        sig = ','.join(k for k, v in (('S2', r['S2_note']), ('S3', r['S3_location_abstract_only']), ('S5', r['S5_sparse_9_or_fewer'])) if v)
        L.append(f"| {r['study_id']} | {r['strength']} | {sig} | {r['weight']} | {r['risk_of_bias_tool']} | {r['section'] or '(blank)'} |")
    if len(heavy) > 60:
        L.append(f"| … | | | {len(heavy) - 60} more in the CSV | | |")
    L += ["", "## What to do with it (researcher decisions, not applied)", "",
          "1. Obtain full texts for the strong rows first, then the moderate rows that carry effect-size rows or RoB 2/ROBINS-I ratings, and re-extract them as was done for S366, S326 and S277.",
          "2. Decide whether the headline \"abstract-only\" count in the report should be replaced by this broader definition. It has **not** been changed: the report still quotes the prefix-based figure and adds this audit as a caveat.",
          "3. The full per-row table is `sparse_record_audit_2026-10-04.csv` (title, DOI and authors included, so it can double as a request list).", ""]
    return "\n".join(L)


if __name__ == '__main__':
    rs = audit()
    with open(OUT_CSV, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rs[0]), lineterminator='\r\n'); w.writeheader(); w.writerows(rs)
    OUT_MD.write_text(render(rs), encoding='utf-8')
    print('wrote', OUT_CSV.name, len(rs), 'rows;', OUT_MD.name)
