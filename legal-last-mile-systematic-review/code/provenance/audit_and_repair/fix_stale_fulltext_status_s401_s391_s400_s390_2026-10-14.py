"""2026-10-14: stale full-text status on four included studies. S401 (R653729F562BE), S391 (R0EED09DB6147), S400 (RE6A43701E1CD) and S390 (RA7E07382F0E4) carry full-text decisions (include)
and extraction rows that cite specific sections of the paper, but their full_text_status still said oa_pdf_candidate / oa_page_candidate ('OA PDF located via Unpaywall, not yet downloaded'). S391 and S390 also have a
blind full-text review by a second model (_reviewer2_codex/results/). Following the 2026-10-04 precedent (twelve decided rows with a stale not_retrievable status), the PI ruled that the status be set to
'retrieved' with a dated note. Nothing else in the rows changes. The PDFs themselves are still on the retrieval list (PDF_RETRIEVAL_STATUS_2026-10-09.md). Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
P = '02_screening/full_text/full_text_screening_database.csv'
IDS = {'R653729F562BE': ('S401', 'its extraction cites sections of the paper'), 'R0EED09DB6147': ('S391', 'its extraction cites sections of the paper and the second-model full-text review (Codex, 2026-10-03) read the text'),
       'RE6A43701E1CD': ('S400', 'its extraction cites sections of the paper'), 'RA7E07382F0E4': ('S390', 'its extraction cites sections of the paper and the second-model full-text review (Codex, 2026-10-03) read the text')}
MARK = 'status corrected 2026-10-14'
raw = open(P, newline='', encoding='utf-8').read(); eol = '\r\n' if '\r\n' in raw[:5000] else '\n'
with open(P, newline='', encoding='utf-8') as f:
    rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
n = 0
for r in rows:
    if r['record_id'] in IDS and MARK not in r['notes']:
        sid, why = IDS[r['record_id']]
        assert r['final_decision'] == 'include' and r['full_text_status'] in ('oa_pdf_candidate', 'oa_page_candidate'), (sid, r['full_text_status'])
        r['notes'] = (r['notes'] + ' | ' if r['notes'] else '') + f"[{MARK} by CK: full_text_status {r['full_text_status']} -> retrieved, because {why} ({sid}); the PDF is still on the retrieval list]"
        r['full_text_status'] = 'retrieved'
        n += 1
fd, tmp = tempfile.mkstemp(dir=os.path.dirname(P), suffix='.tmp')
with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator=eol); w.writeheader(); w.writerows(rows)
os.replace(tmp, P); print(n, 'rows updated')
