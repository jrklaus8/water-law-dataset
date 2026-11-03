"""2026-09-28 audit: re-sync evidence_map.csv study_design_class to risk_of_bias_tool for
studies whose tool was reassigned AFTER the earlier normalization pass. Same mapping as
05_analysis/descriptive/study_design_class_normalization_2026-09-28.md."""
import csv, sys, os, tempfile
csv.field_size_limit(sys.maxsize)
ED='03_extraction/extracted_data/extraction_database.csv'
EM='05_analysis/descriptive/evidence_map.csv'
KEYS=[('RoB 2','RoB2'),('ROBINS-I','ROBINS-I'),('JBI','JBI'),('MMAT','MMAT'),('CASP','CASP'),('AMSTAR','AMSTAR2'),('Legal Institutional','LegalFramework'),('NONE','NONE')]
CANON={'RoB2':'experimental','ROBINS-I':'quasi_experimental','JBI':'observational','MMAT':'mixed_methods','CASP':'qualitative','AMSTAR2':'systematic_review_secondary'}
def tool(s):
    best=None
    for k,n in KEYS:
        i=s.find(k)
        if i>=0 and (best is None or i<best[0]): best=(i,n)
    return best[1] if best else None
ed={r['study_id']:r for r in csv.DictReader(open(ED))}
with open(EM,newline='') as f:
    rd=csv.DictReader(f); fields=rd.fieldnames; rows=list(rd)
assert len(rows)==1162
touched=[]
for r in rows:
    t=tool(ed[r['study_id']]['risk_of_bias_tool'])
    if t in CANON and r['study_design_class']!=CANON[t]:
        touched.append((r['study_id'],r['study_design_class'],CANON[t])); r['study_design_class']=CANON[t]
assert len(touched)==22, len(touched)
fd,tmp=tempfile.mkstemp(dir=os.path.dirname(EM),suffix='.tmp')
with os.fdopen(fd,'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,lineterminator='\r\n'); w.writeheader(); w.writerows(rows)
os.replace(tmp,EM)
for t in touched: print(*t)
