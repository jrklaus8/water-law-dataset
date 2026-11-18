"""2026-10-02: the researcher reported that they (human reviewer_2) reviewed the full-text classifications of S101-S200 (100 included studies), agreed with all of
them and had no further notes. Recorded exactly as for S001-S100 (2026-09-27): reviewer_2 = 'Human-reviewer2-fulltext-<date>', conflict = FALSE. The decision
fields are NOT changed (an agreement confirms the existing include). The researcher's statement is the only source: no per-record decision sheet exists, so
the label date is the date of the statement. Assumption: 'classifications 100 to 200' = study IDs S101-S200 (100 studies, continuing S001-S100).
Asserts: all 100 map to active records, each is an AI-decided include with blank reviewer_2 and blank conflict. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
FT = '02_screening/full_text/full_text_screening_database.csv'
MAP = '03_extraction/extracted_data/study_record_map.csv'
LABEL = 'Human-reviewer2-fulltext-2026-10-02'
ids = {f'S{i:03d}' for i in range(101, 201)}
with open(MAP, newline='') as f:
    rid = {r['study_id']: r['record_id'] for r in csv.DictReader(f) if r['status'] == 'active'}
assert ids <= set(rid), sorted(ids - set(rid))
target = {rid[s] for s in ids}
raw = open(FT, newline='').read(); crlf = '\r\n' in raw[:5000]
with open(FT, newline='') as f:
    rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
n = len(rows); done = 0
for r in rows:
    if r['record_id'] in target:
        assert r['final_decision'] == 'include' and r['full_text_decision'] == 'include', r['record_id']
        assert not r['reviewer_2'] and not r['conflict'], r['record_id']
        r['reviewer_2'] = LABEL; r['conflict'] = 'FALSE'; done += 1
assert done == 100 and len(rows) == n
fd, tmp = tempfile.mkstemp(dir=os.path.dirname(FT), suffix='.tmp')
with os.fdopen(fd, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n' if crlf else '\n'); w.writeheader(); w.writerows(rows)
os.replace(tmp, FT)
print('recorded human reviewer_2 agreement for', done, 'includes (S101-S200)')
