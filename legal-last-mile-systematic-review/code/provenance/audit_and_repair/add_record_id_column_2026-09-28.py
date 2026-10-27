"""2026-09-28 (researcher-approved schema change): append a `record_id` column to extraction_database.csv, filled from
03_extraction/extracted_data/study_record_map.csv (active rows). The map remains the provenance record of HOW each link was made
(link_method). Column is appended LAST so positional readers of the 92 codebook fields are unaffected. Run from the project root."""
import csv, sys, os, tempfile
csv.field_size_limit(sys.maxsize)
ED='03_extraction/extracted_data/extraction_database.csv'; MAP='03_extraction/extracted_data/study_record_map.csv'
m={r['study_id']:r['record_id'] for r in csv.DictReader(open(MAP,newline='')) if r['status']=='active'}
raw=open(ED,newline='').read(); crlf='\r\n' in raw[:5000]
with open(ED,newline='') as f:
    rd=csv.DictReader(f); fields=rd.fieldnames; rows=list(rd)
assert 'record_id' not in fields and len(fields)==92 and len(rows)==len(m)==1159, (len(fields),len(rows),len(m))
for r in rows: r['record_id']=m[r['study_id']]
fd,tmp=tempfile.mkstemp(dir=os.path.dirname(ED),suffix='.tmp')
with os.fdopen(fd,'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields+['record_id'],lineterminator='\r\n' if crlf else '\n'); w.writeheader(); w.writerows(rows)
os.replace(tmp,ED); print('record_id column added to',len(rows),'rows')
