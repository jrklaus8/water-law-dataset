#!/usr/bin/env python3
"""Turn the researcher's queued A16 reversals (02_screening/full_text/A16_PENDING_REVERSALS.csv, written by apply_a16_adjudications.py)
into real inclusions and exclusions, so every count follows. DRY RUN BY DEFAULT; pass --apply to write.

Per pending row (the whole batch is validated first; any problem stops the run before anything is written):
- exclude -> include (new inclusion). Needs a prepared extraction: 02_screening/full_text/a16_new_includes/<record_id>.json with two objects,
  "extraction" (every extraction_database.csv column except study_id and record_id, filled from the FULL TEXT with the same rules as any extraction,
  including the risk-of-bias tool and rating) and "evidence_map" (every evidence_map.csv column except study_id). The script assigns the next study
  ID (retired IDs are never reused), appends the extraction and evidence-map rows, adds a study_record_map row (link_method a16_reversal),
  flips the full-text database row to include and removes its exclusion-log row. If the new include has a quantitative effect, add its
  effect_sizes.csv row with a separate dated script (one prespecified effect per study, CODEBOOK section 12).
- include -> exclude (new exclusion). Retires the study ID (map status retired_excluded, never reused), removes its extraction and evidence-map
  rows (and its row in the abstract-only sensitivity list, as the S356 precedent did), flips the full-text row to exclude with the researcher's code and comment, and appends an exclusion-log row. A study that has an
  effect_sizes.csv row or a linked_reports entry is refused: handle those by hand first, because removing them changes the synthesis.
Resolved rows move from A16_PENDING_REVERSALS.csv to A16_RESOLVED_REVERSALS.csv (with the study ID and date); re-running is safe.
Precedent for the exclude direction: code/provenance/audit_and_repair/resolve_s356_exclude_2026-09-28.py.

Usage (from legal-last-mile-systematic-review/):
  python3 code/screening/resolve_a16_pending_reversals.py --reviewer "Initials"           # dry run
  python3 code/screening/resolve_a16_pending_reversals.py --reviewer "Initials" --apply   # write
Then: bash code/analysis/regenerate_all.sh (the verifier must pass; counts in README/PRISMA/manuscript are computed or flagged by it) and add a
dated CHANGELOG entry. After a real reversal the verifier and two tests WILL fail on hand-written figures (rehearsed end to end on a scratch copy with two mock new
includes: 36 verifier failures); run `python3 code/analysis/fix_documented_counts.py` (dry run, then --apply; it fixed 24 of 42 in the rehearsal and lists the rest as MANUAL) and update the remainder from the numbers the verifier names, in this order of files: README.md and the repository-root README.md (include/exclude
totals, extraction rows, tool counts, quantitative/qualitative split, exclusion total and per-code breakdown, reviewer-2 coverage), 06_outputs/prisma/prisma_flow.md
and PRISMA_WORKFLOW.md (included and excluded totals), 04_quality/risk_of_bias/2026-09-28_evidence_limitations.md (tool table, causal-capable, abstract-only,
mechanism-certainty, legal-system and country counts), the dated-correction sentence in RISK_OF_BIAS.md, the A16 figures (README, DECISIONS_AND_OPEN_ITEMS A16, decision
brief 13, session handoff), and the _KNOWN_YEAR list in verify_repository.py if a new study's year differs from its screening record; then rebuild the HTML report
(regenerate_all.sh does). test_search_reconciliation also asserts the flow-text figures, so it fails until prisma_flow.md is updated. The linkage checks (study_record_map
bijection with includes, exclusion log one-to-one, retired IDs) pass without edits.
"""
from __future__ import annotations

import argparse
import csv
import datetime
import json
import os
import re
import sys
import tempfile
from pathlib import Path

csv.field_size_limit(sys.maxsize)
CODES = {f'E{i:02d}' for i in range(1, 13)}
REL = dict(FT='02_screening/full_text/full_text_screening_database.csv', EL='02_screening/exclusion_log/exclusion_log.csv',
           ED='03_extraction/extracted_data/extraction_database.csv', EM='05_analysis/descriptive/evidence_map.csv',
           MAP='03_extraction/extracted_data/study_record_map.csv', ES='05_analysis/effect_sizes/effect_sizes.csv',
           LINKS='03_extraction/extracted_data/linked_reports_2026-09-28.csv', AB='05_analysis/sensitivity/abstract_only_extractions_2026-09-28.csv',
           PEND='02_screening/full_text/A16_PENDING_REVERSALS.csv', DONE='02_screening/full_text/A16_RESOLVED_REVERSALS.csv',
           INC='02_screening/full_text/a16_new_includes')


def read(path: Path):
    raw = path.read_bytes().decode('utf-8')
    with open(path, encoding='utf-8', newline='') as f:
        rd = csv.DictReader(f)
        return rd.fieldnames, list(rd), ('\r\n' if raw.split('\n', 1)[0].endswith('\r') else '\n')


def write(path: Path, fields, rows, eol):
    fd, tmp = tempfile.mkstemp(dir=path.parent, suffix='.tmp')
    with os.fdopen(fd, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator=eol); w.writeheader(); w.writerows(rows)
    os.replace(tmp, path)


def next_study_id(map_rows):
    n = max(int(re.sub(r'\D', '', r['study_id'])) for r in map_rows) + 1
    return f'S{n:03d}'


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--reviewer', required=True)
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2], help='project root (for testing on a copy)')
    a = ap.parse_args(argv)
    P = {k: a.root / v for k, v in REL.items()}
    today = datetime.date.today().isoformat()
    if not P['PEND'].exists():
        print('No A16_PENDING_REVERSALS.csv: nothing to do.'); return 0
    pend_fields, pend, pend_eol = read(P['PEND'])
    if not pend:
        print('No pending reversals.'); return 0
    ft_f, ft, ft_e = read(P['FT']); el_f, el, el_e = read(P['EL']); ed_f, ed, ed_e = read(P['ED'])
    em_f, em, em_e = read(P['EM']); map_f, mp, map_e = read(P['MAP'])
    es = read(P['ES'])[1]; links = read(P['LINKS'])[1] if P['LINKS'].exists() else []
    ft_by = {r['record_id']: r for r in ft}
    active_by_rec = {r['record_id']: r for r in mp if r['status'] == 'active'}
    errors, plan, new_id = [], [], next_study_id(mp)
    for p in pend:
        rid, dec, code = p['record_id'], p['researcher_decision'], p['researcher_exclusion_code']
        r = ft_by.get(rid)
        if r is None:
            errors.append(f'{rid}: not in the full-text database'); continue
        if dec == 'include':
            if r['final_decision'] != 'exclude':
                errors.append(f'{rid}: queued as exclude -> include but the database says {r["final_decision"]!r}'); continue
            f = P['INC'] / f'{rid}.json'
            if not f.exists():
                errors.append(f'{rid}: no prepared extraction at {f.relative_to(a.root)} (see the docstring for its format)'); continue
            spec = json.loads(f.read_text(encoding='utf-8'))
            miss = (set(ed_f) - {'study_id', 'record_id'}) - set(spec.get('extraction', {}))
            extra = set(spec.get('extraction', {})) - set(ed_f)
            em_miss = (set(em_f) - {'study_id'}) - set(spec.get('evidence_map', {}))
            em_extra = set(spec.get('evidence_map', {})) - set(em_f)
            if miss or extra or em_miss or em_extra:
                errors.append(f'{rid}: extraction JSON columns differ (missing {sorted(miss)}, unknown {sorted(extra)}; evidence_map missing {sorted(em_miss)}, unknown {sorted(em_extra)})'); continue
            plan.append(('include', p, spec, new_id)); new_id = f"S{int(new_id[1:]) + 1:03d}"
        elif dec == 'exclude':
            if r['final_decision'] != 'include' or rid not in active_by_rec:
                errors.append(f'{rid}: queued as include -> exclude but it is not an active include'); continue
            sid = active_by_rec[rid]['study_id']
            if code not in CODES:
                errors.append(f'{rid}: exclusion code {code!r} is not E01-E12'); continue
            if any(x['study_id'] == sid for x in es):
                errors.append(f'{rid} ({sid}): has an effect_sizes.csv row; remove it by a dated script first (changes the synthesis)'); continue
            if any(sid in (x.get('study_id_a'), x.get('study_id_b')) for x in links):
                errors.append(f'{rid} ({sid}): appears in linked_reports_2026-09-28.csv; resolve the link first'); continue
            plan.append(('exclude', p, sid, None))
        else:
            errors.append(f'{rid}: researcher_decision must be include or exclude, got {dec!r}')
    if errors:
        print('Nothing written; fix these first:'); [print('  ' + e) for e in errors]; return 2
    done = []
    for kind, p, extra, sid_new in plan:
        rid = p['record_id']; r = ft_by[rid]
        who = f"{p['adjudicated_by']} (A16, {p['date']}); resolved by {a.reviewer} {today}"
        if kind == 'include':
            print(f'INCLUDE  {rid} -> {sid_new}: new study, extraction and evidence-map rows added, exclusion-log row removed')
            r.update(full_text_decision='include', final_decision='include', exclusion_reason='', exclusion_reason_detail='', reviewer_2=p['adjudicated_by'])
            r['notes'] = (r['notes'] + ' | ' if r['notes'] else '') + f'A16 reversal exclude -> include, {who}; study {sid_new}'
            el = [x for x in el if x['record_id'] != rid]
            ed.append({'study_id': sid_new, 'record_id': rid, **extra['extraction']})
            em.append({'study_id': sid_new, **extra['evidence_map']})
            mp.append({'study_id': sid_new, 'record_id': rid, 'link_method': 'a16_reversal', 'status': 'active', 'note': f'new include from A16 reversal {today}'})
            done.append({**p, 'study_id': sid_new, 'resolved_on': today, 'resolved_by': a.reviewer})
        else:
            sid = extra
            print(f'EXCLUDE  {rid} ({sid}): study retired, extraction and evidence-map rows removed, exclusion-log row added ({p["researcher_exclusion_code"]})')
            detail = f"A16 adjudication {p['date']} by {p['adjudicated_by']}: " + (p['researcher_comment'] or 'excluded on the researcher\'s reading') + f"; study {sid} retired {today}"
            r.update(full_text_decision='exclude', final_decision='exclude', exclusion_reason=p['researcher_exclusion_code'], exclusion_reason_detail=detail, reviewer_2=p['adjudicated_by'])
            r['notes'] = (r['notes'] + ' | ' if r['notes'] else '') + f'A16 reversal include -> exclude, {who}; {sid} retired'
            el.append({'record_id': rid, 'title': r['title'], 'authors': r['authors'], 'year': r['year'], 'stage': 'full_text',
                       'exclusion_code': p['researcher_exclusion_code'], 'exclusion_reason_detail': detail, 'reviewer': p['adjudicated_by'], 'date': today})
            ed = [x for x in ed if x['study_id'] != sid]; em = [x for x in em if x['study_id'] != sid]
            for m in mp:
                if m['study_id'] == sid:
                    m.update(status='retired_excluded', note=f'record {rid} excluded {p["researcher_exclusion_code"]} on A16 adjudication {today}; {sid} retired')
            done.append({**p, 'study_id': sid, 'resolved_on': today, 'resolved_by': a.reviewer})
    print(f'\n{len(plan)} reversal(s) resolved: {sum(1 for k, *_ in plan if k == "include")} new inclusion(s), {sum(1 for k, *_ in plan if k == "exclude")} new exclusion(s).')
    if not a.apply:
        print('DRY RUN: nothing written. Re-run with --apply to write.'); return 0
    write(P['FT'], ft_f, ft, ft_e); write(P['EL'], el_f, el, el_e); write(P['ED'], ed_f, ed, ed_e)
    write(P['EM'], em_f, em, em_e); write(P['MAP'], map_f, mp, map_e)
    retired = {sid for kind, _, sid, _ in plan if kind == 'exclude'}
    if retired and P['AB'].exists():  # the abstract-only sensitivity list must not keep a retired study (the verifier compares it with the extraction notes)
        ab_f, ab_rows, ab_e = read(P['AB'])
        write(P['AB'], ab_f, [r for r in ab_rows if r['study_id'] not in retired], ab_e)
    if P['DONE'].exists():
        d_f, d_rows, _ = read(P['DONE'])
    else:
        d_f, d_rows = list(pend_fields) + ['study_id', 'resolved_on', 'resolved_by'], []
    write(P['DONE'], d_f, d_rows + done, '\n')
    write(P['PEND'], pend_fields, [], pend_eol)
    print('Written. Now run: bash code/analysis/regenerate_all.sh, add effect_sizes rows by a dated script if needed, and add a dated CHANGELOG entry.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
