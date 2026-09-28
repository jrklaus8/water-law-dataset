"""2026-09-28 repository audit: annotate (NOT merge, NOT delete) two live double-counted papers.

S233 / S1008  = Morales & Zambrano 2018, Poblacion y Salud en Mesoamerica 16(1), DOI 10.15517/psm.v1i1.32031
                (records RFEFB1427701B and RB26ACD9EDC54: English vs Spanish title, one with a blank DOI,
                so the DOI-variant and title-similarity audits both missed the pair)
S299 / S392   = Minaverry 2017, Tecnologia y Ciencias del Agua 8(1):5-20, DOI 10.24850/j-tyca-2017-01-01
                (records R7896D097B364 and R56D409CF27A6: the second title carries a bilingual suffix and a
                blank DOI field, which pushes token-Jaccard similarity below the audit's threshold)

Only the free-text note fields are touched; no decision, count, or classification changes. The merge itself
is left to the researcher (see 00_admin/audits/2026-09-28_repository_audit.md, finding 13)."""
import csv, sys, os, tempfile
csv.field_size_limit(sys.maxsize)
ED='03_extraction/extracted_data/extraction_database.csv'
FT='02_screening/full_text/full_text_screening_database.csv'
TAG=" | AUDIT 2026-09-28: PROBABLE LIVE DUPLICATE of {other} ({ref}). Same paper under two record_ids (English vs Spanish/bilingual title, one DOI blank), so the DOI-variant and title-similarity audits missed it. NOT merged; awaiting researcher decision -- see 00_admin/audits/2026-09-28_repository_audit.md, finding 13."
PAIRS={'S233':('S1008','Morales & Zambrano 2018, Poblacion y Salud en Mesoamerica 16(1), DOI 10.15517/psm.v1i1.32031'),
       'S1008':('S233','Morales & Zambrano 2018, Poblacion y Salud en Mesoamerica 16(1), DOI 10.15517/psm.v1i1.32031'),
       'S299':('S392','Minaverry 2017, Tecnologia y Ciencias del Agua 8(1):5-20, DOI 10.24850/j-tyca-2017-01-01'),
       'S392':('S299','Minaverry 2017, Tecnologia y Ciencias del Agua 8(1):5-20, DOI 10.24850/j-tyca-2017-01-01')}
REC={'RFEFB1427701B':'S233','RB26ACD9EDC54':'S1008','R7896D097B364':'S299','R56D409CF27A6':'S392'}

def rewrite(path, mutate, expect):
    with open(path,newline='') as f:
        raw=f.read()
    crlf='\r\n' in raw[:5000]
    with open(path,newline='') as f:
        rd=csv.DictReader(f); fields=rd.fieldnames; rows=list(rd)
    n=mutate(rows)
    assert n==expect,(path,n)
    fd,tmp=tempfile.mkstemp(dir=os.path.dirname(path),suffix='.tmp')
    with os.fdopen(fd,'w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,lineterminator='\r\n' if crlf else '\n'); w.writeheader(); w.writerows(rows)
    os.replace(tmp,path)

def m_ed(rows):
    n=0
    for r in rows:
        if r['study_id'] in PAIRS:
            other,ref=PAIRS[r['study_id']]; assert 'PROBABLE LIVE DUPLICATE' not in r['extraction_note']
            r['extraction_note']=r['extraction_note'].rstrip()+TAG.format(other=other,ref=ref); n+=1
    return n
def m_ft(rows):
    n=0
    for r in rows:
        if r['record_id'] in REC:
            sid=REC[r['record_id']]; other,ref=PAIRS[sid]; assert 'PROBABLE LIVE DUPLICATE' not in r['notes']
            r['notes']=(r['notes'].rstrip()+TAG.format(other=other,ref=ref)) if r['notes'].strip() else TAG.format(other=other,ref=ref).lstrip(' |').lstrip(); n+=1
    return n
rewrite(ED,m_ed,4); rewrite(FT,m_ft,4)
print('annotated 4 extraction rows + 4 screening rows')
