#!/usr/bin/env python3
"""One list of every article whose full text the project is missing or has not been able to read, with the DOI, a DOI link and the reason it matters.

The researcher asks for "a CSV of all the articles that are missing and you need the full text of". The need comes from several different open items, so this joins them,
one row per article, with the most urgent reason as `priority` (1 = most urgent) and every reason listed in `needed_for`:
  1  A19 nine: substantive full-text-stage excludes decided on a landing page or metadata record, to be re-screened (EXCLUSION_BASIS_AUDIT_2026-10-04.csv, group substantive)
  2  A22: includes that may fail criterion 3 and whose Drive copy is only a portal page or is missing (INCLUDES_CRITERION3_SCREEN_2026-10-04.csv)
  3  effect-size rows never compared with the paper (FULLTEXT_VERIFICATION_2026-10-04.csv, verdict not_checked)
  4  AMSTAR 2 reviews still unrated (risk_of_bias_rating starts 'Not ratable')
  5  includes extracted from the abstract or metadata only, or with a strong sparse-extraction signal (SPARSE_RECORD_AUDIT_2026-10-04.csv strength strong; the abstract-only prefix)
  6  other full-text-stage decisions whose recorded status says no full text was read (A19 status groups, 'not checked')
  7  the 60 studies of the human second-extraction sample (the human needs the PDF; most are already in Drive for the AI)
  9  records never assessed because no full text could be retrieved (full-text screening closed by researcher decision, 2026-09-28)
Output: 02_screening/full_text/MISSING_FULLTEXTS_REQUEST_LIST_2026-10-04.csv (all) and A19_NINE_FULLTEXTS_TO_RETRIEVE_2026-10-04.csv (priority 1 only, with what to check).
Name a retrieved PDF `S<id>_...pdf` (an included study) or `R<record_id>__...pdf` (any other record) and put it in the Drive inbox folder; the AI reads it and moves it to `Processed`.
Run from the project root.
"""
import csv, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402
import audit_sparse_records as asr  # noqa: E402

csv.field_size_limit(sys.maxsize)
ROOT = cf.ROOT
OUT = ROOT / '02_screening/full_text/MISSING_FULLTEXTS_REQUEST_LIST_2026-10-04.csv'
OUT_A19 = ROOT / '02_screening/full_text/A19_NINE_FULLTEXTS_TO_RETRIEVE_2026-10-04.csv'
FIELDS = ['priority', 'needed_for', 'study_id', 'record_id', 'year', 'authors', 'title', 'doi', 'doi_link', 'other_link', 'what_we_have', 'file_name_to_use']
A19_FIELDS = ['record_id', 'year', 'authors', 'title', 'doi', 'doi_link', 'other_link', 'ai_decision_and_code', 'why_it_must_be_re_screened', 'what_to_check_in_the_full_text', 'file_name_to_use']
WHAT = {'E01': 'INCLUSION_EXCLUSION.md criterion 2: does the paper study how legal or administrative institutions (rules, rights, eligibility, procedures, regulators, tenure, tariffs, enforcement) shape access to drinking water or sanitation, with an empirical design? The AI excluded it as wrong topic on the abstract alone.',
        'E09': 'whether the paper is a full report with empirical evidence on water or sanitation access, or only a conference-abstract supplement (the AI excluded it as a conference abstract on the metadata record alone)',
        'E12': 'whether the volume contains a chapter or study that meets the inclusion criteria (the AI excluded the edited volume on the book record alone); if so, name the chapter'}
BY_YEAR = lambda r: (r['priority'], int(r['year']) if str(r['year']).isdigit() else 0, r['record_id'])


def clean_doi(d):
    d = (d or '').strip()
    d = re.sub(r'^https?://(dx\.)?doi\.org/', '', d, flags=re.I)
    return d if re.match(r'^10\.\d{4,9}/\S+$', d) else ''


def build():
    ed = {r['study_id']: r for r in cf.read('ed')}
    ft = {r['record_id']: r for r in cf.read('ft')}
    sid_of = {r['record_id']: s for s, r in ed.items()}
    items = {}  # record_id -> dict

    def add(rid, prio, why, have):
        f = ft[rid]
        it = items.setdefault(rid, {'priority': prio, 'reasons': [], 'have': have, 'record_id': rid})
        it['priority'] = min(it['priority'], prio)
        if why not in it['reasons']:
            it['reasons'].append(why)
        if prio <= it['priority']:
            it['have'] = have

    def csvrows(rel):
        with open(ROOT / rel, encoding='utf-8', newline='') as fh:
            return list(csv.DictReader(fh))

    # 1: A19 nine
    audit = csvrows('05_analysis/descriptive/EXCLUSION_BASIS_AUDIT_2026-10-04.csv')
    nine = [r for r in audit if r['group'] == 'substantive' and not r['drive_check'].startswith(('full PDF in Drive', 'PDF in Drive', 'settled without a full text'))]  # a full text that has since arrived through Drive is no longer missing
    for r in nine:
        add(r['record_id'], 1, f"A19: excluded {r['exclusion_code']} on a thin basis; re-screen on the full text", r['drive_check'])
    # 6: other A19 status groups still not checked
    for r in audit:
        if r['group'] in ('status_include', 'status_exclude') and r['drive_check'].startswith('not checked'):
            add(r['record_id'], 6, f"A19: decided ({r['group']}) although the recorded full-text status says no full text was read", r['drive_check'])
    # 2: A22
    for r in csvrows('05_analysis/descriptive/INCLUDES_CRITERION3_SCREEN_2026-10-04.csv'):
        d = r['drive_check']
        if 'no Drive copy' in d or d.startswith('Drive file is only') or d.startswith('Drive file is the journal page'):
            add(r['record_id'], 2, f"A22: {r['study_id']} may fail criterion 3 (cue: {r['cue']}); Drive copy missing or only a portal page", d)
    # 3: effect-size rows
    for r in csvrows('05_analysis/effect_sizes/FULLTEXT_VERIFICATION_2026-10-04.csv'):
        if r['verdict'] == 'not_checked':
            add(ed[r['study_id']]['record_id'], 3, f"effect-size row of {r['study_id']} never compared with the paper", 'extraction from the abstract/record; no full text in Drive')
    # 4: unrated AMSTAR 2 reviews
    for s, r in ed.items():
        if cf.tool_of(r['risk_of_bias_tool']) == 'AMSTAR 2' and r['risk_of_bias_rating'].startswith('Not ratable'):
            add(r['record_id'], 4, f'{s} is a systematic review whose AMSTAR 2 appraisal is still "not ratable"', 'abstract-level extraction; partial pilot appraisal only')
    # 5: abstract-only and strong sparse
    for r in asr.audit():
        if r['strength'] == 'strong':
            add(r['record_id'], 5, f"{r['study_id']} extracted from the abstract/record only (strong sparse-extraction signal)", 'abstract-level extraction')
    # 7: second-extractor sample
    for r in csvrows('03_extraction/second_extractor/second_extractor_sheet_BLANK_2026-10-04.csv'):
        if r['field'] == 'publication_year':
            add(ed[r['study_id']]['record_id'], 7, f"{r['study_id']} is in the human second-extraction sample", 'AI full-text or abstract extraction; the human needs the PDF')
    # 9: never assessed
    for rid, f in ft.items():
        if not f['final_decision']:
            add(rid, 9, 'never assessed: no full text could be retrieved; full-text screening closed by researcher decision 2026-09-28', f"status {f['full_text_status'] or 'blank'}")

    rows = []
    for rid, it in items.items():
        f = ft[rid]
        s = sid_of.get(rid, '')
        doi = clean_doi(f['doi'])
        first = re.split(r'[,;]| and ', f['authors'])[0].strip() if f['authors'] else ''
        stem = re.sub(r'[^A-Za-z0-9]+', '_', first)[:20].strip('_')
        name = (f'{s}_{stem}_{f["year"]}_<short title>.pdf' if s else f'{rid}__<short title>.pdf')
        rows.append({'priority': it['priority'], 'needed_for': ' | '.join(it['reasons']), 'study_id': s, 'record_id': rid, 'year': f['year'], 'authors': f['authors'][:120],
                     'title': f['title'][:200], 'doi': doi, 'doi_link': f'https://doi.org/{doi}' if doi else '', 'other_link': f['url'],
                     'what_we_have': it['have'][:160], 'file_name_to_use': name})
    rows.sort(key=BY_YEAR)
    a19 = []
    for r in sorted(nine, key=lambda x: x['record_id']):
        f = ft[r['record_id']]
        doi = clean_doi(f['doi'])
        a19.append({'record_id': r['record_id'], 'year': f['year'], 'authors': f['authors'][:120], 'title': f['title'][:200], 'doi': doi, 'doi_link': f'https://doi.org/{doi}' if doi else '',
                    'other_link': f['url'], 'ai_decision_and_code': f"exclude {r['exclusion_code']}", 'why_it_must_be_re_screened': f['exclusion_reason_detail'][:300].replace('\n', ' '),
                    'what_to_check_in_the_full_text': WHAT.get(r['exclusion_code'], ''), 'file_name_to_use': f'{r["record_id"]}__<short title>.pdf'})
    return rows, a19


def write(path, fields, rows):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n'); w.writeheader(); w.writerows(rows)


if __name__ == '__main__':
    rows, a19 = build()
    write(OUT, FIELDS, rows); write(OUT_A19, A19_FIELDS, a19)
    from collections import Counter
    c = Counter(r['priority'] for r in rows)
    print(f'wrote {OUT.name} ({len(rows)} articles; by priority {dict(sorted(c.items()))}) and {OUT_A19.name} ({len(a19)} articles)')
