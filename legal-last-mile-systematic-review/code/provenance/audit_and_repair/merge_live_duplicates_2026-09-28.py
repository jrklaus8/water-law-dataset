"""2026-09-28: researcher-approved merge of the two live double-counted papers found by the repository
audit (00_admin/audits/2026-09-28_repository_audit.md, finding 13). Follows the S399 -> S102 precedent:
retire one extraction/evidence-map row (leaving a permanent gap in the study_id sequence) and record the
retired screening record as an E08 duplicate exclusion.

  KEEP S1008 (record RB26ACD9EDC54, full-text-based extraction, DOI, sample size)  | RETIRE S233 (record RFEFB1427701B)
  KEEP S392  (record R56D409CF27A6, fuller full-text-based extraction)              | RETIRE S299 (record R7896D097B364)

Effects: included 1,162 -> 1,160; excluded 1,114 -> 1,116; exclusion_log 1,114 -> 1,116 rows;
extraction_database and evidence_map 1,162 -> 1,160 rows. effect_sizes.csv untouched (no row for any of the four).
Only S392's blank DOI is filled from the retired S299 row; no judgement codings are carried across."""
import csv, sys, os, tempfile
csv.field_size_limit(sys.maxsize)
ED='03_extraction/extracted_data/extraction_database.csv'
EM='05_analysis/descriptive/evidence_map.csv'
FT='02_screening/full_text/full_text_screening_database.csv'
EL='02_screening/exclusion_log/exclusion_log.csv'
CUT=" | AUDIT 2026-09-28: PROBABLE LIVE DUPLICATE"
WHO='Claude-AI-audit-2026-09-28'; DATE='2026-09-28'

def rewrite(path, mutate, expect_before, expect_after):
    raw=open(path,newline='').read(); crlf='\r\n' in raw[:5000]
    with open(path,newline='') as f:
        rd=csv.DictReader(f); fields=rd.fieldnames; rows=list(rd)
    assert len(rows)==expect_before,(path,len(rows))
    rows=mutate(rows)
    assert len(rows)==expect_after,(path,len(rows))
    fd,tmp=tempfile.mkstemp(dir=os.path.dirname(path),suffix='.tmp')
    with os.fdopen(fd,'w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,lineterminator='\r\n' if crlf else '\n'); w.writeheader(); w.writerows(rows)
    os.replace(tmp,path)

def strip_annotation(text):
    i=text.find(CUT); assert i>=0; return text[:i].rstrip()

S233_EFFECT=None
def m_ed(rows):
    global S233_EFFECT
    by={r['study_id']:r for r in rows}
    S233_EFFECT=by['S233']['effect_estimate']
    assert S233_EFFECT.startswith('Poor wastewater management is identified by 82%')
    assert by['S299']['doi']=='10.24850/j-tyca-2017-01-01' and by['S392']['doi']==''
    k=by['S1008']
    k['extraction_note']=strip_annotation(k['extraction_note'])+(
      " | MERGED 2026-09-28 (researcher-approved, repository audit finding 13): this row is the kept row for Morales & Zambrano 2018; "
      "the duplicate abstract-level row S233 (record RFEFB1427701B, extracted 2026-09-15) was retired and its study_id left as a permanent gap. "
      "Nothing was overwritten. For reference, S233's abstract-level effect_estimate read: \""+S233_EFFECT+"\" "
      "(S233 also coded discretion_accommodation=TRUE and flagged the paper quantitative_synthesis_eligible from that abstract; this row's full-text coding, "
      "which does not, is retained.)")
    k=by['S392']
    k['doi']=by['S299']['doi']
    k['extraction_note']=strip_annotation(k['extraction_note'])+(
      " | MERGED 2026-09-28 (researcher-approved, repository audit finding 13): this row is the kept row for Minaverry 2017; the duplicate "
      "abstract/metadata-only row S299 (record R7896D097B364, extracted 2026-09-15) was retired and its study_id left as a permanent gap. "
      "Only the DOI (10.24850/j-tyca-2017-01-01) was carried over from S299; S299's other codings (administrative_review, complaint, community_level) were not.")
    return [r for r in rows if r['study_id'] not in ('S233','S299')]

def m_em(rows): return [r for r in rows if r['study_id'] not in ('S233','S299')]

DETAIL={
 'RFEFB1427701B':("Duplicate of RB26ACD9EDC54 (same paper: Morales & Zambrano 2018, Poblacion y Salud en Mesoamerica 16(1), DOI 10.15517/psm.v1i1.32031; "
    "this record carries the English-language title, the kept record the Spanish-language one, so neither the DOI-variant nor the title-similarity duplicate audit matched them). "
    "Originally included by Claude-AI-fulltext-2026-09-15 and extracted as S233 from the abstract; retired 2026-09-28 with researcher approval after the repository audit "
    "(00_admin/audits/2026-09-28_repository_audit.md, finding 13). Kept as S1008.", 'RB26ACD9EDC54','S233','S1008'),
 'R7896D097B364':("Duplicate of R56D409CF27A6 (same paper: Minaverry 2017, Tecnologia y Ciencias del Agua 8(1):5-20, DOI 10.24850/j-tyca-2017-01-01; "
    "the kept record's title carries a bilingual [translation] suffix and its DOI field is blank, which defeated both the DOI-variant and title-similarity duplicate audits). "
    "Originally included by Claude-AI-fulltext-2026-09-15 and extracted as S299 from abstract/repository metadata only; retired 2026-09-28 with researcher approval after the repository audit "
    "(00_admin/audits/2026-09-28_repository_audit.md, finding 13). Kept as S392.", 'R56D409CF27A6','S299','S392'),
}
KEPT={'RB26ACD9EDC54':('RFEFB1427701B','S233','S1008'),'R56D409CF27A6':('R7896D097B364','S299','S392')}
LOGROWS=[]
def m_ft(rows):
    by={r['record_id']:r for r in rows}
    for rid,(detail,kept,sold,snew) in DETAIL.items():
        r=by[rid]; assert r['final_decision']=='include'
        r['full_text_decision']='exclude'; r['final_decision']='exclude'; r['exclusion_reason']='E08'
        r['exclusion_reason_detail']=detail; r['reviewer_1']=WHO
        r['notes']='Retired duplicate; merged into '+kept+' ('+snew+'). Original decision by '+'Claude-AI-fulltext-2026-09-15'+' (include) superseded by the researcher-approved merge of '+DATE+'.'
        LOGROWS.append({'record_id':rid,'title':r['title'],'authors':r['authors'],'year':r['year'],'stage':'full_text',
                        'exclusion_code':'E08','exclusion_reason_detail':detail,'reviewer':WHO,'date':DATE})
    for rid,(retired,sold,snew) in KEPT.items():
        r=by[rid]; assert r['final_decision']=='include'
        r['notes']=strip_annotation(r['notes'])+' | MERGED '+DATE+': kept record of a duplicate pair; retired record '+retired+' ('+sold+') is now an E08 exclusion. This record\'s extraction is '+snew+'.'
    return rows
def m_el(rows): return rows+LOGROWS

rewrite(ED,m_ed,1162,1160); rewrite(EM,m_em,1162,1160); rewrite(FT,m_ft,None if False else len(list(csv.DictReader(open(FT,newline='')))),len(list(csv.DictReader(open(FT,newline='')))))
rewrite(EL,m_el,1114,1116)
print('merge applied')
