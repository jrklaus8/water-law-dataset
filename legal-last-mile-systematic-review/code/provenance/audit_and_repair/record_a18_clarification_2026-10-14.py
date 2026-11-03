"""2026-10-14: open item A18. The full-text exclusion of R0B87CA1C5270 (Fonta, Gordon & Toumpakari 2025) was written with a sentence that cited the null water estimate (RR = 1.00) next to the real ground,
which read as a results-based exclusion. The PI confirmed the exclusion on scope grounds alone (a macro Francophone versus Anglophone colonial-legacy comparison across 22 countries, not a legal or administrative
access rule, as for S969) and re-coded it E01 to E03 (apply_a16_adjudications.py, 2026-10-14). This script appends a dated clarification to the exclusion detail in full_text_screening_database.csv and
exclusion_log.csv so the row says, in its own text, that the estimate played no part. Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
RID = 'R0B87CA1C5270'
MARK = '[A18 clarification 2026-10-14'
TEXT = (MARK + ': excluded on scope grounds alone (a macro Francophone versus Anglophone colonial-legacy comparison across 22 countries, not a legal or administrative water or sanitation access rule, as for S969). '
        'The null water-dimension estimate (RR = 1.00) quoted above played no part in the decision; eligibility never depends on the significance, magnitude or direction of a reported estimate.]')
for p in ('02_screening/full_text/full_text_screening_database.csv', '02_screening/exclusion_log/exclusion_log.csv'):
    raw = open(p, newline='', encoding='utf-8').read(); eol = '\r\n' if '\r\n' in raw[:5000] else '\n'
    with open(p, newline='', encoding='utf-8') as f:
        rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
    col = 'exclusion_reason_detail'
    hit = [r for r in rows if r['record_id'] == RID]
    assert len(hit) == 1, (p, len(hit))
    if MARK in hit[0][col]:
        print(p, 'already done'); continue
    hit[0][col] = hit[0][col].rstrip() + ' ' + TEXT
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(p), suffix='.tmp')
    with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator=eol); w.writeheader(); w.writerows(rows)
    os.replace(tmp, p); print(p, 'clarified')
