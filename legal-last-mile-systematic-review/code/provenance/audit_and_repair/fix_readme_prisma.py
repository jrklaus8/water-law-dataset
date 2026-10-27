def edit(path, pairs):
    s=open(path,encoding='utf-8').read()
    for old,new in pairs:
        assert s.count(old)==1,(path,s.count(old),old[:80])
        s=s.replace(old,new)
    open(path,'w',encoding='utf-8').write(s)

DIST_OLD="(5 RoB 2, 63 ROBINS-I, 166 JBI, 207\n    MMAT, 245 CASP, 22 AMSTAR 2, 425 Legal Framework, 12 NONE)"
DIST_NEW="(5 RoB 2, 63 ROBINS-I, 140 JBI, 206\n    MMAT, 263 CASP, 24 AMSTAR 2, 449 Legal Framework, 12 NONE — live counts;\n    an earlier draft of this list showed pre-reassignment figures)"
edit('README.md',[
 ("`risk_of_bias_tool` (including 8 correctly flagged `NONE` where no\nvalidated instrument applies), and all 1,154 studies to which a tool\napplies carry a `risk_of_bias_rating`",
  "`risk_of_bias_tool` (including 12 correctly flagged `NONE` where no\nvalidated instrument applies), and all 1,150 studies to which a tool\napplies carry a `risk_of_bias_rating`"),
 ("`risk_of_bias_tool` (1,154 with an applicable validated or project-specific\n   instrument, 8 correctly flagged `NONE`), and all 1,154 carry a\n   `risk_of_bias_rating`.",
  "`risk_of_bias_tool` (1,150 with an applicable validated or project-specific\n   instrument, 12 correctly flagged `NONE`), and all 1,150 carry a\n   `risk_of_bias_rating` (of the 12 `NONE` studies, 4 carry an explicit\n   NOT APPLICABLE note and 8 are blank by design)."),
 ("roughly 1,050 studies rated via CASP, MMAT, or the project's own Legal\n   Institutional Evidence Appraisal Framework",
  "918 studies rated via CASP (263), MMAT (206), or the project's own Legal\n   Institutional Evidence Appraisal Framework (449)"),
 (DIST_OLD, DIST_NEW),
 ("    1,154 to which a tool applies carry a `risk_of_bias_rating`. See",
  "    1,150 to which a tool applies carry a `risk_of_bias_rating`. See"),
 ("(5 RoB 2, 63 ROBINS-I, 166 JBI Cross-Sectional, 207 MMAT, 245 CASP Qualitative, 22 AMSTAR 2, 425 Legal Institutional Evidence Appraisal Framework, 12 correctly-flagged `NONE`)",
  "(5 RoB 2, 63 ROBINS-I, 140 JBI Cross-Sectional, 206 MMAT, 263 CASP Qualitative, 24 AMSTAR 2, 449 Legal Institutional Evidence Appraisal Framework, 12 correctly-flagged `NONE` — live counts as recomputed by the 2026-09-28 audit)"),
 ("All 1,154 studies to which a tool applies carry a `risk_of_bias_rating`",
  "All 1,150 studies to which a tool applies carry a `risk_of_bias_rating`"),
 ("For the roughly 1,050 studies rated via\nCASP, MMAT, or the Legal Framework,","For the 918 studies rated via\nCASP, MMAT, or the Legal Framework,"),
 ("Every one of the 1,154 studies to which a\ntool applies (the other 8 are correctly flagged `NONE`)","Every one of the 1,150 studies to which a\ntool applies (the other 12 are correctly flagged `NONE`)"),
 ("resulting 1,154 ratings (see **Current project","resulting 1,150 ratings (see **Current project"),
 ("- All 1,154 risk-of-bias ratings produced by","- All 1,150 risk-of-bias ratings produced by"),
 ("for the ~1,050 studies rated via CASP, MMAT, or the Legal Framework,","for the ~918 studies rated via CASP, MMAT, or the Legal Framework,"),
])
edit('PRISMA_WORKFLOW.md',[
 ("(5 RoB 2, 63 ROBINS-I, 166 JBI, 207 MMAT, 245 CASP, 22 AMSTAR 2, 425 Legal Framework, 12 correctly-flagged `NONE`)",
  "(5 RoB 2, 63 ROBINS-I, 140 JBI, 206 MMAT, 263 CASP, 24 AMSTAR 2, 449 Legal Framework, 12 correctly-flagged `NONE` — live counts as recomputed by the 2026-09-28 audit; this cell originally listed pre-reassignment figures)"),
 ("all 1,154 to which a tool applies carry a `risk_of_bias_rating`","all 1,150 to which a tool applies carry a `risk_of_bias_rating`"),
])
print('ok')
