"""2026-10-14: open item A19. R803988411D3E (van Vliet, van Buuren & Mgana eds., Urban Waste and Sanitation Services for Sustainable Development, Routledge, a 176-page edited volume) was excluded E12 on
2026-09-15 from a book record and a landing-page abstract; no chapter text was retrieved or screened before Phase 6 closed on 2026-09-28. The PI ruled that it be treated like the other records
the closure left unassessed: full_text_status 'not_retrievable', every decision field blank, no exclusion-log row. The earlier AI decision and its reason are kept in the row's notes, not deleted.
Effects: assessed records 2,277 to 2,276, never assessed 1,382 to 1,383, full-text excludes 1,174 to 1,173 (E12 47 to 46). Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
RID = 'R803988411D3E'
MARK = 'A19 ruling 2026-10-14'


def rw(p, fn):
    raw = open(p, newline='', encoding='utf-8').read(); eol = '\r\n' if '\r\n' in raw[:5000] else '\n'
    with open(p, newline='', encoding='utf-8') as f:
        rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
    rows, msg = fn(rows)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(p), suffix='.tmp')
    with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator=eol); w.writeheader(); w.writerows(rows)
    os.replace(tmp, p); print(p, msg)


def ft_fn(rows):
    r = next(x for x in rows if x['record_id'] == RID)
    if MARK in r['notes']:
        return rows, 'already done'
    prior = (f"prior AI full-text decision {r['full_text_decision']} {r['exclusion_reason']} by {r['reviewer_1']} on a landing-page abstract and book record (2026-09-15), withdrawn: {r['exclusion_reason_detail']}")
    r['notes'] = (r['notes'] + ' | ' if r['notes'] else '') + (f"[{MARK} by CK: the exclusion was made without any chapter text and is withdrawn; the record is normalised to not_retrievable with no decision, "
                                                              f"like the other records the Phase 6 closure left unassessed. {prior}]")
    r.update(full_text_status='not_retrievable', full_text_decision='', exclusion_reason='', exclusion_reason_detail='', reviewer_1='', reviewer_2='', conflict='', final_decision='')
    return rows, 'normalised'


def el_fn(rows):
    n = len(rows)
    rows = [x for x in rows if x['record_id'] != RID]
    return rows, f'exclusion-log row removed ({n} -> {len(rows)})' if len(rows) != n else 'already done'


rw('02_screening/full_text/full_text_screening_database.csv', ft_fn)
rw('02_screening/exclusion_log/exclusion_log.csv', el_fn)
