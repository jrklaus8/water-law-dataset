"""2026-09-28: S356 (record R1827C03DA45A, Tremolet & Smith 2026, OECD Environment Working Paper No. 275) resolved on the
full text supplied by the researcher. It states no search strategy or method; it is a seminar-derived policy overview built on
illustrative case boxes drawn from secondary sources and stakeholder feedback, with no primary data or analysis. Under the
project's own precedent (e.g. R0186AD905238, R67ED91FDC3BF) that is E05 (no empirical evidence; inclusion criterion 3 requires
empirical evidence or a *systematic* empirical synthesis). S356 is retired (permanent ID gap) and the record becomes an E05 exclusion.
Researcher-approved. Run from legal-last-mile-systematic-review/."""
import csv, sys, os, tempfile
csv.field_size_limit(sys.maxsize)
P=dict(ED='03_extraction/extracted_data/extraction_database.csv',EM='05_analysis/descriptive/evidence_map.csv',
       FT='02_screening/full_text/full_text_screening_database.csv',EL='02_screening/exclusion_log/exclusion_log.csv',
       MAP='03_extraction/extracted_data/study_record_map.csv',AB='05_analysis/sensitivity/abstract_only_extractions_2026-09-28.csv')
WHO='Claude-AI-fulltext-2026-09-28'; DATE='2026-09-28'; RID='R1827C03DA45A'
DETAIL=("Tremolet & Smith (2026), 'Economic regulation of water supply and sanitation services: key trends and approaches', OECD Environment Working Paper No. 275 "
 "(DOI 10.1787/14514522-en, CC BY 4.0). Full text read 2026-09-28 (researcher-supplied PDF). A seminar-derived policy overview of regulatory models (regulation by contract, "
 "agency, self-regulation) and pro-poor and environmental regulatory instruments, illustrated with case boxes (Senegal, Paris, Portugal, England, Manila, Burkina Faso, "
 "Djibouti, Jamaica, Wallonia, Benin, Italy) compiled from secondary sources and stakeholder feedback. It states no search strategy or synthesis method, collects and analyses no primary data, "
 "and itself notes that no robust comparative evidence exists ('in the absence of robust comparative studies ... it is necessary to draw on a series of case studies'). "
 "A non-systematic narrative policy overview, not an empirical study or systematic empirical synthesis (inclusion criterion 3) -- excluded on the same basis as R0186AD905238 and R67ED91FDC3BF. "
 "Previously included at full-text stage on an abstract-level reading with no reviewer recorded and extracted as S356 (abstract only); S356 retired 2026-09-28.")
def rw(path,fn,before=None,after=None):
    raw=open(path,newline='').read(); crlf='\r\n' in raw[:5000]
    with open(path,newline='') as f:
        rd=csv.DictReader(f); fields=rd.fieldnames; rows=list(rd)
    if before is not None: assert len(rows)==before,(path,len(rows))
    rows=fn(rows)
    if after is not None: assert len(rows)==after,(path,len(rows))
    fd,tmp=tempfile.mkstemp(dir=os.path.dirname(path),suffix='.tmp')
    with os.fdopen(fd,'w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,lineterminator='\r\n' if crlf else '\n'); w.writeheader(); w.writerows(rows)
    os.replace(tmp,path)
log=[]
def m_ft(rows):
    r=[x for x in rows if x['record_id']==RID][0]; assert r['final_decision']=='include'
    r.update(full_text_decision='exclude',final_decision='exclude',exclusion_reason='E05',exclusion_reason_detail=DETAIL,reviewer_1=WHO,
             full_text_status='retrieved',full_text_location='researcher-supplied PDF, 2026-09-28 (session upload; open access CC BY 4.0 at https://doi.org/10.1787/14514522-en)',
             notes='Previously an include with no reviewer (abstract-level); resolved on full text 2026-09-28 -> E05 exclusion. Extraction row S356 retired.')
    log.append({'record_id':RID,'title':r['title'],'authors':r['authors'],'year':r['year'],'stage':'full_text','exclusion_code':'E05','exclusion_reason_detail':DETAIL,'reviewer':WHO,'date':DATE})
    return rows
rw(P['FT'],m_ft)
rw(P['EL'],lambda rows: rows+log,1116,1117)
rw(P['ED'],lambda rows:[x for x in rows if x['study_id']!='S356'],1160,1159)
rw(P['EM'],lambda rows:[x for x in rows if x['study_id']!='S356'],1160,1159)
def m_map(rows):
    for x in rows:
        if x['study_id']=='S356':
            x.update(status='retired_excluded',note='record R1827C03DA45A excluded E05 on full-text reading 2026-09-28; S356 retired'); return rows
    raise SystemExit('S356 not in map')
rw(P['MAP'],m_map)
rw(P['AB'],lambda rows:[x for x in rows if x['study_id']!='S356'],70,69)
print('S356 resolved: exclude E05')
