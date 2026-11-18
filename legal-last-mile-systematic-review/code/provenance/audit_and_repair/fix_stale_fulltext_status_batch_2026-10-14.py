"""2026-10-14 (PI ruling, reviewer CK): batch-correct stale full_text_status bookkeeping listed in EXCLUSION_BASIS_AUDIT_2026-10-04.md.
17 decided EXCLUDES and 16 decided INCLUDES carry a full_text_status of oa_pdf_candidate / oa_page_candidate ('located, not downloaded'), although the researcher's Drive holds a real PDF that was read on 2026-10-04 or 2026-10-09
(the audit's `drive_check` column says 'status field stale' for each exclude, and each include has an extraction that is not marked abstract-only). Following the 2026-10-04 and 2026-10-14 precedents (S401, S391, S400, S390), the status
becomes 'retrieved' with a dated note. Decisions, exclusion codes and reasons do not change. For the excludes the note says plainly that the Drive copy was read after the decision. RCB78D4EF3652 (no Drive text) is NOT touched.
Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
P = '02_screening/full_text/full_text_screening_database.csv'
EXCLUDES = ['R0B462A3EF2D7', 'R54D4AEC2087E', 'RAA8D967AD545', 'R1A33C22EDA73', 'R600CF4CBBFE7', 'RD1829FC2C94A', 'R00E98F4E387F', 'R64A7E6073EF0', 'R057F7388EEF4', 'R4266AA2DF8F3', 'R804A6CFFD1D7', 'REA305644CBB3', 'RF22EFFAD48CC', 'RF8AB3815D963', 'R0532032FE3BB', 'R9167527BC9AE', 'RDEA162168676']
INCLUDES = ['R0206140E81E4', 'R03824D388779', 'R28001B16ADA4', 'R2B5A92453E91', 'R56D409CF27A6', 'R7170047A72DF', 'R79E038D49B1A', 'R86610BDFBD5E', 'R897B0E5CB3C7', 'RA0005AC70700', 'RA1109B58A443', 'RBEBE095D118E', 'RC4C6E385D8B9', 'RC72A82468618', 'REA101C40B5BB', 'RF20B9AADA984']
MARK = 'status corrected 2026-10-14'
STALE = ('oa_pdf_candidate', 'oa_page_candidate')
raw = open(P, newline='', encoding='utf-8').read(); eol = '\r\n' if '\r\n' in raw[:5000] else '\n'
with open(P, newline='', encoding='utf-8') as f:
    rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
n = {'exclude': 0, 'include': 0}
for r in rows:
    if r['record_id'] in EXCLUDES + INCLUDES and MARK not in r['notes']:
        want = 'exclude' if r['record_id'] in EXCLUDES else 'include'
        assert r['final_decision'] == want and r['full_text_status'] in STALE, (r['record_id'], r['final_decision'], r['full_text_status'])
        why = ("a PDF is in the researcher's Drive and was read on 2026-10-04 or 2026-10-09, after this decision was made; the exclusion and its code are unchanged" if want == 'exclude'
               else "a PDF is in the researcher's Drive and was read on 2026-10-04 or 2026-10-09, and the extraction is consistent with it")
        r['notes'] = (r['notes'] + ' | ' if r['notes'] else '') + f"[{MARK} by CK: full_text_status {r['full_text_status']} -> retrieved, because {why}; see EXCLUSION_BASIS_AUDIT_2026-10-04.md]"
        r['full_text_status'] = 'retrieved'
        n[want] += 1
if n['exclude'] or n['include']:
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(P), suffix='.tmp')
    with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator=eol); w.writeheader(); w.writerows(rows)
    os.replace(tmp, P)
print(n['exclude'], 'excludes and', n['include'], 'includes updated')
