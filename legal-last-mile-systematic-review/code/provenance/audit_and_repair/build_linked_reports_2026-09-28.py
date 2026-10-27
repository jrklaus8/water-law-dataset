"""2026-09-28 audit follow-up: write 03_extraction/extracted_data/linked_reports_2026-09-28.csv and append
cross-reference notes (REPRODUCIBILITY.md section 6 requires linked reports of one study to be cross-referenced by
study_id) to the extraction rows of the documented pairs. Additive only: no row removed, no decision or count changed.

Two sources of links, kept distinct in the CSV: 'extractor_note' (the original extractor already stated the
relationship in extraction_note / effect_measure / mechanism_certainty) and 'audit_inferred' (this audit's own
inference from extracted fields; NOT verified against the source papers, and NOT written into the extraction rows)."""
import csv, sys, os, tempfile
csv.field_size_limit(sys.maxsize)
ED='03_extraction/extracted_data/extraction_database.csv'
OUT='03_extraction/extracted_data/linked_reports_2026-09-28.csv'
es={r['study_id'] for r in csv.DictReader(open('05_analysis/effect_sizes/effect_sizes.csv',newline=''))}
F=['link_id','study_id_a','study_id_b','relationship','same_underlying_data','basis','source_of_link','in_effect_sizes','confidence','status']
L=[
('LR01','S294','S366','two reports of the same cluster-randomised trial (VEA community-driven WASH intervention, rural DRC, 332 villages): S294 reports health/child-growth/institutional outcomes, S366 reports infrastructure/access/behaviour/governance outcomes','yes',"S366's own extraction: 'companion outcomes paper to the same VEA trial reported for health/institutional outcomes in Quattrochi et al.'; S366 RoB 2 form: 'same underlying trial as S294'",'extractor_note','high'),
('LR02','S097','S098','two papers from the same fieldwork/stakeholder sample (George Compound, Lusaka), different analytic lens','yes',"both extraction notes: 'Companion paper ... same underlying fieldwork/stakeholder sample ... flagged to avoid double-counting the same underlying interviews'",'extractor_note','high'),
('LR03','S681','S682','two papers drawing on overlapping ethnographic fieldwork (Madhya Pradesh / West Bengal), different analytic focus','partial',"both extraction notes: 'Companion paper ... drawing on overlapping fieldwork'",'extractor_note','medium'),
('LR04','S357','S369','earlier/foundational and later reports of the same VAPAR participatory-action-research programme in the Agincourt HDSS area','partial',"S369 extraction note: 'Companion paper to S357 ... the earlier/foundational participatory action research process in the same VAPAR programme and Agincourt HDSS study area that S357's later paper builds on'",'extractor_note','medium'),
('LR05','S008','S009','same author group, same country and topic (Kenyan small-scale service providers)','no',"S009 extraction note: 'Companion paper to S008 (same author group, distinct dataset/framework)'",'extractor_note','high'),
('LR06','S541','S542','same Water Policy special issue (22 S1), different countries and data tables','no',"S542 extraction note: 'Companion paper to S541 in the same Water Policy special issue ... own quantitative supply-demand data table'",'extractor_note','high'),
('LR07','S761','S763','same author, same delegated-management arrangement in Kisumu, Kenya; different designs','possible',"S763 extraction: 'companion study to Nzengya 2018 (S761)'; S761 = 294-respondent quasi-experimental survey, S763 = interviews with master/kiosk operators; overlap of fieldwork not stated",'extractor_note','low'),
('LR08','S794','S803','same author, same country (Guatemala), household survey (2015) vs official interviews (2011)','no',"S803 extraction note: 'companion study to the already-included S794 Vasquez 2015'; different respondents",'extractor_note','medium'),
('LR09','S526','S539','two US cross-sectional studies of large water utilities (S526: 1,183-1,189 utilities serving 40,000+; S539: the 500 largest community systems); samples probably overlap','probable',"extracted sample descriptions only; not verified against the source papers' data appendices; matters for any future pooling of the ownership/price cluster because both rows are in effect_sizes.csv",'audit_inferred','low'),
('LR10','S175','S891','same author, same Kenya/Ghana research programme: agent-based model (Ecology and Society 2017) vs empirical paper (Water Policy 2018)','possible','same first author and country pair; different DOIs and journals; underlying data not compared','audit_inferred','low'),
('LR11','S734','S1001','Kooy & Bakker (2008): S734 (Int. J. Urban and Regional Research) and S1001 (Geoforum), both on colonial and contemporary Jakarta water infrastructure','possible','same authors, year and city; different titles/journals; underlying material not compared','audit_inferred','low'),
('LR12','S1000','S1001','Bakker, Kooy, Shofiani & Martijn (2008, World Development) and Kooy & Bakker (2008, Geoforum), both on Jakarta urban water supply and governance','possible','overlapping authors, year and city; different titles/journals; underlying material not compared','audit_inferred','low'),
]
rows=[dict(zip(F[:6]+['source_of_link'],(l[0],l[1],l[2],l[3],l[4],l[5],l[6]))) | {'in_effect_sizes':'both' if l[1] in es and l[2] in es else 'first only' if l[1] in es else 'second only' if l[2] in es else 'neither','confidence':l[7],'status':'proposed - not applied to any count; awaiting researcher decision'} for l in L]
with open(OUT,'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=F,lineterminator='\r\n'); w.writeheader(); w.writerows(rows)

# cross-reference notes on the extractor-documented pairs only
with open(ED,newline='') as f: raw=f.read()
crlf='\r\n' in raw[:5000]
with open(ED,newline='') as f:
    rd=csv.DictReader(f); fields=rd.fieldnames; data=list(rd)
by={r['study_id']:r for r in data}; touched=0
for l in L:
    if l[6]!='extractor_note': continue
    for me,other in ((l[1],l[2]),(l[2],l[1])):
        r=by[me]
        if other in r['extraction_note']: continue     # already cross-referenced by the extractor
        r['extraction_note']=r['extraction_note'].rstrip()+f" | LINKED REPORT (audit 2026-09-28, {l[0]}): related to {other} - {l[4]} underlying data; see 03_extraction/extracted_data/linked_reports_2026-09-28.csv."
        touched+=1
fd,tmp=tempfile.mkstemp(dir=os.path.dirname(ED),suffix='.tmp')
with os.fdopen(fd,'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,lineterminator='\r\n' if crlf else '\n'); w.writeheader(); w.writerows(data)
os.replace(tmp,ED)
print('linked rows',len(rows),'| extraction notes appended',touched)
