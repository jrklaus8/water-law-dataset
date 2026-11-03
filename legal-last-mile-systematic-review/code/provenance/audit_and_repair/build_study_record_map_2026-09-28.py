import csv, sys, re, unicodedata
from collections import defaultdict, Counter
csv.field_size_limit(sys.maxsize)
ft={r['record_id']:r for r in csv.DictReader(open('02_screening/full_text/full_text_screening_database.csv',newline=''))}
ed=list(csv.DictReader(open('03_extraction/extracted_data/extraction_database.csv',newline='')))
inc={r for r,v in ft.items() if v['final_decision']=='include'}
def norm(t): return re.sub(r'[^a-z0-9]+',' ',''.join(c for c in unicodedata.normalize('NFKD',t) if not unicodedata.combining(c)).lower()).strip()
mp={}      # study_id -> (record_id, method)
# 1. record id in the extraction note (prefer 'record_id RXXX' pattern; else any include id, last mention)
for x in ed:
    n=x['extraction_note']
    cands=[m for m in re.findall(r'record_id (R[0-9A-F]{12})',n) if m in inc]
    if not cands: cands=[m for m in re.findall(r'R[0-9A-F]{12}',n) if m in inc]
    if cands: mp[x['study_id']]=(cands[-1] if len(set(cands))>1 else cands[0],'extraction_note')
# resolve duplicates: record claimed by >1 study
byrec=defaultdict(list)
for s,(r,m) in mp.items(): byrec[r].append(s)
multi={r:v for r,v in byrec.items() if len(v)>1}
print('records claimed by >1 study via note:',multi)
used={r for r,_ in mp.values()}
doi_of={re.sub(r'^https?://(dx\.)?doi\.org/','',x['doi'].strip().lower()):x['study_id'] for x in ed if x['doi'].strip()}
cit={x['study_id']:norm(x['citation']) for x in ed}
MANUAL={'RB26ACD9EDC54':'S1008','R58C7B8CDD09C':'S1067','R4298BDB00D8D':'S1047','R33F5730F8C31':'S1035','R5EDAB88CC052':'S1161'}
unlinked=[r for r in inc if r not in used]
for rid in sorted(unlinked):
    r=ft[rid]; doi=re.sub(r'^https?://(dx\.)?doi\.org/','',r['doi'].strip().lower())
    if rid in MANUAL: sid=MANUAL[rid]; meth='manual (accent/spelling variant of title; verified by hand)'
    elif doi and doi in doi_of: sid=doi_of[doi]; meth='doi'
    else:
        nt=norm(r['title'])[:60]; hit=[s for s,c in cit.items() if nt and nt in c]
        if len(hit)==1: sid=hit[0]; meth='title in citation'
        else: print('UNLINKED',rid,r['title'][:70],hit); continue
    if sid in mp: print('CONFLICT',rid,sid,mp[sid]); continue
    mp[sid]=(rid,meth)
print('study rows mapped',len(mp),'of',len(ed),'| unmapped studies:',[x['study_id'] for x in ed if x['study_id'] not in mp])
recs=Counter(r for r,_ in mp.values()); print('records used twice:',[r for r,c in recs.items() if c>1],'| includes without a study:',len(inc-set(recs)))
print(Counter(m.split(' ')[0] for _,m in mp.values()))
rows=[]
for x in ed:
    r,m=mp[x['study_id']]; rows.append({'study_id':x['study_id'],'record_id':r,'link_method':m,'status':'active','note':''})
def sk(s): return int(s[1:])
rows.sort(key=lambda d: sk(d['study_id']))
rows+= [{'study_id':'S233','record_id':'RFEFB1427701B','link_method':'extraction_note (retired row)','status':'retired_duplicate','note':'merged into S1008 on 2026-09-28 (same paper as record RB26ACD9EDC54)'},
        {'study_id':'S299','record_id':'R7896D097B364','link_method':'extraction_note (retired row)','status':'retired_duplicate','note':'merged into S392 on 2026-09-28 (same paper as record R56D409CF27A6)'}]
import io
with open('/tmp/claude-0/-home-user-water-law-dataset/13a4d716-bf67-5f8e-b123-127698a45259/scratchpad/study_record_map.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['study_id','record_id','link_method','status','note'],lineterminator='\r\n'); w.writeheader(); w.writerows(rows)
print('wrote',len(rows))
