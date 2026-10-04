#!/usr/bin/env python3
"""Which full-text-stage exclusions rest on a landing-page abstract or a metadata record rather than on a read full text?

The full-text database holds 1,117 excludes. Most were decided on a read full text, but the reason text of some says the decision used only a landing-page
abstract, a paywalled abstract or a bibliographic metadata record. E10 (inaccessible) and E08 (duplicate) are expected to say so; for the other codes it
means a substantive exclusion (wrong topic, wrong design, no empirical evidence, insufficient information) was made without the full text. This lists them
so the researcher can retrieve the texts. Detection is a phrase match on exclusion_reason_detail, so it finds records whose reason SAYS the basis was thin;
it cannot find ones that do not say so. Writes 05_analysis/descriptive/EXCLUSION_BASIS_AUDIT_2026-10-04.{csv,md}. Run from the project root."""
import csv
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402

OUT_CSV = cf.ROOT / '05_analysis/descriptive/EXCLUSION_BASIS_AUDIT_2026-10-04.csv'
OUT_MD = cf.ROOT / '05_analysis/descriptive/EXCLUSION_BASIS_AUDIT_2026-10-04.md'
A16 = cf.ROOT / '02_screening/full_text/A16_ADJUDICATION_SHEET_2026-10-04.csv'
PAT = re.compile(r'abstract[- ]only|landing[- ]page|metadata (record|only)|bibliographic metadata|paywall|no abstract|abstract text|only (the )?abstract|abstract (was|is) (available|retrieved)', re.I)
FIELDS = ['group', 'record_id', 'year', 'exclusion_code', 'title', 'basis_phrase', 'in_A16_sheet', 'reason_excerpt']
STATUS_CONTRADICTS = ('not_retrievable', 'oa_pdf_candidate', 'oa_page_candidate')  # a decided record whose recorded status says no full text was obtained (or only located, not downloaded)
GROUPS = {'substantive': 'substantive exclusion (E01-E07, E09, E12) decided without a read full text', 'E10': 'E10 inaccessible (expected to say so)', 'E08': 'E08 duplicate (expected to say so)'}
CODE_NAMES = {'E01': 'wrong topic', 'E02': 'wrong population', 'E03': 'wrong exposure', 'E04': 'wrong outcome', 'E05': 'no empirical evidence', 'E06': 'engineering only',
              'E07': 'wrong service', 'E09': 'insufficient information', 'E12': 'wrong study design'}


def build():
    a16 = {r['record_id']: r['priority'] for r in csv.DictReader(open(A16, encoding='utf-8', newline=''))} if A16.exists() else {}
    rows = []
    for r in cf.read('ft'):
        if r['final_decision'] != 'exclude':
            continue
        m = PAT.search(r['exclusion_reason_detail'])
        if not m or 'full text read' in r['exclusion_reason_detail'].lower():  # a reason that says the full text WAS read is not a thin-basis exclusion (e.g. S356's retired abstract-only extraction)
            continue
        code = r['exclusion_reason']
        group = code if code in ('E10', 'E08') else 'substantive'
        rows.append({'group': group, 'record_id': r['record_id'], 'year': r['year'], 'exclusion_code': code, 'title': r['title'][:110], 'basis_phrase': m.group(0).lower(),
                     'in_A16_sheet': ('priority ' + a16[r['record_id']]) if r['record_id'] in a16 else 'no', 'reason_excerpt': r['exclusion_reason_detail'][:240].replace('\n', ' ')})
    ed = {r['record_id']: r for r in cf.read('ed')}
    ed_notes = {k: v['extraction_note'] for k, v in ed.items()}
    have = {r['record_id'] for r in rows}
    for r in cf.read('ft'):
        code = r['exclusion_reason']
        if r['final_decision'] not in ('include', 'exclude') or r['full_text_status'] not in STATUS_CONTRADICTS or code in ('E10', 'E08') or r['record_id'] in have:
            continue
        e = ed.get(r['record_id'])
        basis = ('extraction note: ' + e['extraction_note'][:70].replace('\n', ' ')) if e else r['notes'][:120].replace('\n', ' ')
        rows.append({'group': 'status_include' if r['final_decision'] == 'include' else 'status_exclude', 'record_id': r['record_id'], 'year': r['year'], 'exclusion_code': code or 'include', 'title': r['title'][:110],
                     'basis_phrase': 'status ' + r['full_text_status'], 'in_A16_sheet': ('priority ' + a16[r['record_id']]) if r['record_id'] in a16 else 'no', 'reason_excerpt': basis})
    order = {'substantive': 0, 'status_exclude': 1, 'status_include': 2, 'E10': 3, 'E08': 4}
    rows.sort(key=lambda x: (order[x['group']], x['exclusion_code'], x['record_id']))
    n_ex = sum(1 for r in cf.read('ft') if r['final_decision'] == 'exclude')
    sub = [r for r in rows if r['group'] == 'substantive']
    st_ex = [r for r in rows if r['group'] == 'status_exclude']
    st_in = [r for r in rows if r['group'] == 'status_include']
    st_in_full = sum(1 for r in st_in if not ed_notes.get(r['record_id'], '').startswith(cf.ABSTRACT_ONLY_PREFIXES))  # extraction not marked abstract-only
    by = {}
    for r in sub:
        by[r['exclusion_code']] = by.get(r['exclusion_code'], 0) + 1
    L = ['# Decisions that rest on a landing page, abstract or metadata record rather than a read full text', '',
         f"Generated by `code/analysis/audit_exclusion_basis.py` from `full_text_screening_database.csv`. Of {n_ex:,} full-text-stage excludes, {sum(1 for r in rows if r['group'] in ('substantive', 'E10', 'E08'))} have a reason text that mentions a landing-page abstract, a paywalled abstract or a metadata record.", '',
         f"- **{len(sub)} are substantive exclusions** ({', '.join(f'{k} {CODE_NAMES[k]} {v}' for k, v in sorted(by.items()))}) made at the full-text stage without a read full text. They are the ones that matter: a topic, design or evidence judgement rests on an abstract the reviewer itself called incomplete.",
         f"- {sum(1 for r in rows if r['group'] == 'E10')} are E10 (inaccessible full text) and {sum(1 for r in rows if r['group'] == 'E08')} E08 (duplicate); a thin basis is expected for both and is listed only for completeness.", '',
         f"A second check uses the recorded `full_text_status` instead of the reason text: {len(st_ex)} further substantive excludes and {len(st_in)} includes are decided although their status says `not_retrievable` or only `oa_pdf_candidate` / `oa_page_candidate` (a PDF or landing page located, not downloaded). "
         f"For the includes the likely explanation is a stale status (the PDF arrived later through Drive: {st_in_full} of {len(st_in)} have an extraction that is not marked abstract-only); for the excludes no such trail exists, so they too are exclusions without a read full text, missed by the phrase match. Blank statuses are not counted: {sum(1 for r in cf.read('ft') if r['final_decision'] in ('include', 'exclude') and not r['full_text_status'])} decided records have none, which looks like unfilled bookkeeping rather than evidence either way.", '',
         "The phrase match finds exclusions whose reason *says* the basis was thin and the status check finds contradictions in the bookkeeping; other cases may exist that show neither. Nothing here changes a decision.", '',
         "**What would resolve it:** retrieve the full texts of the substantive and status-contradicting excludes (about 30 records) and re-screen them against `INCLUSION_EXCLUSION.md`; or relabel them as excluded at the title/abstract stage and state in the PRISMA flow that they were never read in full (`DECISIONS_AND_OPEN_ITEMS.md` A19).", '',
         "| Group | Record | Year | Code | Title | In A16 sheet |", "|---|---|---|---|---|---|"]
    for r in rows:
        L.append(f"| {r['group']} | {r['record_id']} | {r['year']} | {r['exclusion_code']} | {r['title']} | {r['in_A16_sheet']} |")
    return rows, '\n'.join(L) + '\n'


if __name__ == '__main__':
    rows, md = build()
    with open(OUT_CSV, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator='\n'); w.writeheader(); w.writerows(rows)
    OUT_MD.write_text(md, encoding='utf-8')
    print(f'wrote {OUT_CSV.relative_to(cf.ROOT)} ({len(rows)} rows) and {OUT_MD.name}')
