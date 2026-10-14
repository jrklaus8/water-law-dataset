"""2026-10-14 (open item A6, tier 1, next batches): the 55 tier-1 rows of the reviewer-2 queue that are NOT among the 18 rows of A6_TIER1_SECOND_MODEL_CK_SHEET_2026-10-14.csv, in queue (priority_rank) order, cut into batches of 20
(batch 2 = the next 20, batch 3 the 20 after, batch 4 the last 14). One row already carries a CK ruling (an A16 reversal) and is listed as batch 0. READ-ONLY on every database; writes
02_screening/full_text/A6_TIER1_BATCHES_2_TO_4_CK_SHEET_2026-10-14.{csv,md} with empty ck_* columns.
For includes the sheet shows the rule-type mechanism flags TRUE in the extraction row (the A24 recheck sheet listed an include only when it had none, so a flag here means the study never went through that recheck) and marks
`only discretion_accommodation` where that is the sole rule-type flag, the weakest case (S391 and S395 passed the A24 selection on that flag alone). For excludes it shows the Pass-1 written rationale.
Refuses to overwrite a sheet that holds CK rulings. Run from legal-last-mile-systematic-review/."""
import csv, os, re, sys
csv.field_size_limit(sys.maxsize)
Q = '02_screening/full_text/full_text_reviewer_2_priority_queue_2026-09-28.csv'
DONE = '02_screening/full_text/A6_TIER1_SECOND_MODEL_CK_SHEET_2026-10-14.csv'
FT = '02_screening/full_text/full_text_screening_database.csv'
ED = '03_extraction/extracted_data/extraction_database.csv'
EM = '05_analysis/descriptive/evidence_map.csv'
OUT = '02_screening/full_text/A6_TIER1_BATCHES_2_TO_4_CK_SHEET_2026-10-14'
RULE = ['eligibility', 'burden', 'discretion_accommodation', 'enforcement', 'documentation', 'tenure', 'property', 'planning', 'zoning', 'building_permit', 'service_area', 'fees', 'procedural_steps', 'delay',
        'discretion', 'hardship_exception', 'administrative_review', 'complaint', 'judicial_review', 'disconnection', 'reconnection', 'sanction']
GOV = ['participation', 'institutional_fragmentation', 'political_coordination', 'bureaucratic_assistance']
if os.path.exists(OUT + '.csv') and any(r['ck_decision (include/exclude)'].strip() for r in csv.DictReader(open(OUT + '.csv', encoding='utf-8'))) and '--force' not in sys.argv:
    sys.exit('Refusing to overwrite a sheet that already holds CK rulings (pass --force to rebuild it).')
q = [r for r in csv.DictReader(open(Q, encoding='utf-8')) if r['priority_tier'] == '1']
done = {r['record_id'] for r in csv.DictReader(open(DONE, encoding='utf-8'))}
ft = {r['record_id']: r for r in csv.DictReader(open(FT, encoding='utf-8'))}
ed = {r['record_id']: r for r in csv.DictReader(open(ED, encoding='utf-8'))}
em = {r['study_id']: r for r in csv.DictReader(open(EM, encoding='utf-8'))}
TAG = re.compile(r'^[^.]{0,90}\b(19|20)\d\d[a-z]?\.\s*')


def short(t, n):
    t = ' '.join((t or '').split())
    return t if len(t) <= n else t[:n].rstrip() + '…'


def sentence(t, n=330):
    t = ' '.join((t or '').split())
    m = re.search(r'(?<!\bp)(?<!\bpp)(?<!\bal)(?<!\bet)(?<!\bvs)\.\s+(?=[A-Z“"(])', t)
    return t[:m.start() + 1] if m and m.start() < n else short(t, n)


rows, k = [], 0
for r in q:
    rid = r['record_id']
    if rid in done:
        continue
    f = ft[rid]
    ruled = f['reviewer_2'] == 'CK' or 'A16 adjudication' in f['notes']
    if ruled:
        batch = 0
    else:
        k += 1
        batch = 2 if k <= 20 else 3 if k <= 40 else 4
    inc = r['ai_decision'] == 'include'
    e = ed.get(rid)
    rule = [x for x in RULE if e and e[x] == 'TRUE']
    gov = [x for x in GOV if e and e[x] == 'TRUE']
    if inc and e:
        summ = sentence(em[r['study_id']]['evidence_level']) if r['study_id'] in em else ''
        exposure = short(e['regulatory_model'], 230)
        design = short(e['study_design'], 70)
        country = short(e['country'], 30)
        mech = em[r['study_id']]['mechanism_family'] if r['study_id'] in em else ''
    else:
        summ, exposure, design, country, mech = sentence(TAG.sub('', f['exclusion_reason_detail'])), '', '', '', ''
    rows.append({'batch': batch, 'rank': r['priority_rank'], 'record_id': rid, 'study_id': r['study_id'], 'citation': short(f"{r['authors']} ({r['year']}). {r['title']}", 190), 'ai_decision': r['ai_decision'], 'ai_code': r['ai_exclusion_code'],
                 'full_text_status': f['full_text_status'], 'rule_type_flags_true': ', '.join(rule), 'weak_rule_flag': 'only discretion_accommodation' if inc and rule == ['discretion_accommodation'] else ('NO rule-type flag' if inc and not rule else ''),
                 'governance_flags_true': ', '.join(gov), 'mechanism_family': mech, 'country': country, 'design': design, 'regulatory_model_or_exposure': exposure, 'summary_1line': summ,
                 'prior_ck_ruling': next((p.strip() for p in f['notes'].split(' | ') if 'adjudication' in p and 'by CK' in p), ''),
                 'ck_decision (include/exclude)': '', 'ck_exclusion_code (E01-E12)': '', 'ck_comment': ''})
assert len(rows) == 55, len(rows)
with open(OUT + '.csv', 'w', newline='', encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0]), lineterminator='\r\n'); w.writeheader(); w.writerows(rows)
L = ['# A6 tier 1: the remaining 55 rows, in batches (for human `CK` rulings)', '',
     '*Generated by `code/provenance/audit_and_repair/build_a6_tier1_batches_2026-10-14.py`; read-only. Queue order puts the 36 includes before the 19 excludes, so batches 2 and 3 start with includes. '
     'Fill `ck_*` in the CSV. A rule-type flag is an AI extraction, not a ruling.*', '']
for b, name in ((2, 'Batch 2 (next 20)'), (3, 'Batch 3'), (4, 'Batch 4'), (0, 'Already ruled by CK')):
    sub = [x for x in rows if x['batch'] == b]
    if not sub:
        continue
    L += [f'## {name}: {len(sub)} rows', '', '| rank | record / study | citation | Pass-1 | rule-type flags | summary |', '|---|---|---|---|---|---|']
    for x in sub:
        fl = x['rule_type_flags_true'] + ((' — **' + x['weak_rule_flag'] + '**') if x['weak_rule_flag'] else '')
        L.append(f"| {x['rank']} | `{x['record_id']}` {x['study_id']} | {x['citation']} | {x['ai_decision']} {x['ai_code']} | {fl} | {x['summary_1line']} |")
    L.append('')
open(OUT + '.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
import collections
print('wrote', OUT + '.csv/.md;', dict(collections.Counter((x['batch'], x['ai_decision']) for x in rows)))
