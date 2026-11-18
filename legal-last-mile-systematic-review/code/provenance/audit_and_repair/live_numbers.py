import csv, sys, re
from collections import Counter
csv.field_size_limit(sys.maxsize)
ed=list(csv.DictReader(open('03_extraction/extracted_data/extraction_database.csv')))
KEYS=[('RoB 2','RoB2'),('ROBINS-I','ROBINS-I'),('JBI','JBI'),('MMAT','MMAT'),('CASP','CASP'),('AMSTAR','AMSTAR2'),('Legal Institutional','LegalFramework'),('NONE','NONE')]
def tool(s):
    best=None
    for k,name in KEYS:
        i=s.find(k)
        if i>=0 and (best is None or i<best[0]): best=(i,name)
    return best[1] if best else 'UNCLASSIFIED'
t=Counter(tool(x['risk_of_bias_tool']) for x in ed)
n=len(ed); print('N',n)
for k,v in t.most_common(): print(f'{k:15s}{v:5d} {100*v/n:5.1f}%')
print('CASP+MMAT',t['CASP']+t['MMAT'], round(100*(t['CASP']+t['MMAT'])/n,1),'| CASP+MMAT+LF',t['CASP']+t['MMAT']+t['LegalFramework'])
lf=[x for x in ed if tool(x['risk_of_bias_tool'])=='LegalFramework']
print('LF legal_measurement_quality populated:',sum(1 for x in lf if x['legal_measurement_quality'].strip()),'of',len(lf))
jbi=[x for x in ed if tool(x['risk_of_bias_tool'])=='JBI']
print('JBI High concern:',sum(1 for x in jbi if x['risk_of_bias_rating'].startswith('High concern')),'of',len(jbi))
ab=[x for x in ed if re.search(r'abstract/(repository )?(metadata|introduction)',x['extraction_note'][:200])]
print('abstract/metadata-only extractions:',len(ab),Counter(tool(x['risk_of_bias_tool']) for x in ab))
print('total High concern rating (any tool):',sum(1 for x in ed if x['risk_of_bias_rating'].startswith('High concern')))
print('Not ratable:',sum(1 for x in ed if x['risk_of_bias_rating'].startswith('Not ratable')),'| blank rating:',sum(1 for x in ed if not x['risk_of_bias_rating'].strip()))
