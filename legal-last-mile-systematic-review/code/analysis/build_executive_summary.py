#!/usr/bin/env python3
"""Generate 06_outputs/EXECUTIVE_SUMMARY_2026-10-14.docx: a short, partial report of the analysis and the preliminary findings.

Every number is computed from the databases (current_figures.py, sensitivity_analysis.py, the SWiM direction-coding and CK-check files,
build_a16_adjudication_sheet.py), so the summary cannot drift from the data; interpretive sentences are written here and say what they
rest on. Nothing in it is a pooled effect, a GRADE judgment or a final finding. The long version is
06_outputs/PRELIMINARY_RESULTS_REPORT_2026-09-29.md.

Uses python-docx and matplotlib (no Node dependency). The output is made byte-stable (fixed document timestamps and zip entry dates),
so regenerating it does not dirty the repository unless a figure changed.

Run from the project root:  python3 code/analysis/build_executive_summary.py
"""
import csv, io, statistics, sys, zipfile
from collections import Counter
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402
import sensitivity_analysis as sa  # noqa: E402
import build_manuscript_pieces as bmp  # noqa: E402

import matplotlib  # noqa: E402
matplotlib.use('Agg')
import matplotlib.ticker  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from docx import Document  # noqa: E402
from docx.enum.table import WD_TABLE_ALIGNMENT  # noqa: E402
from docx.enum.text import WD_ALIGN_PARAGRAPH  # noqa: E402
from docx.oxml import OxmlElement  # noqa: E402
from docx.oxml.ns import qn  # noqa: E402
from docx.shared import Inches, Pt, RGBColor  # noqa: E402

csv.field_size_limit(sys.maxsize)
ROOT = cf.ROOT
OUT = ROOT / '06_outputs/EXECUTIVE_SUMMARY_2026-10-14.docx'
REPORT_DATE = '14 October 2026'
RELEASE = '0.2.0-interim'
PIN = datetime(2026, 10, 14, 12, 0, 0)
BLUE, ORANGE, VIOLET, GREY, INK, MUTED, SURF = '#2a78d6', '#eb6834', '#4a3aa7', '#8a8984', '#0b0b0b', '#52514e', '#fcfcfb'  # the figures' palette
NAVY = RGBColor(0x1F, 0x3A, 0x5F)
T = lambda v: str(v).strip().upper() == 'TRUE'
MECH = ['institutional_fragmentation', 'discretion_accommodation', 'fees', 'service_area', 'political_coordination', 'enforcement', 'participation',
        'eligibility', 'burden', 'documentation', 'bureaucratic_assistance', 'administrative_review', 'complaint', 'judicial_review', 'disconnection', 'reconnection']


# ---------------------------------------------------------------- data
def gather():
    F = cf.compute()
    ed = cf.read('ed')
    em = cf.read('em')
    n = len(ed)
    code = {r['study_id']: r for r in csv.DictReader(open(ROOT / '05_analysis/effect_sizes/SWIM_DIRECTION_CODING_2026-10-14.csv', encoding='utf-8'))}
    ck = {r['study_id']: r for r in csv.DictReader(open(ROOT / '05_analysis/effect_sizes/SWIM_CK_CHECKS_2026-10-14.csv', encoding='utf-8'))}
    rows, *_ = sa.scenarios()
    base = rows[0]
    D = {'F': F, 'n': n, 'rows': rows, 'base': base, 'A16': bmp._a16_outcome(), 'code': code}
    # families, with the author's check status per study
    def status(s):
        c = ck.get(s)
        if c and c['scope_outcome_check'] == 'flagged':
            return 'flagged'
        if c and c['ck_raw_sign_agrees (Y/N)'] == 'Y' and c['ck_substantive_direction_agrees (Y/N)'] == 'Y':
            return 'confirmed'
        return 'unchecked'
    st = {s: status(s) for s in code}
    D['status'] = st
    cnt = Counter(st.values())
    assert cnt['confirmed'] == F['swim_core_direction_ck_confirmed'] and cnt['flagged'] == F['swim_core_flagged_for_author'] and len(code) == F['swim_core_studies']
    fam = {f: [s for s, r in code.items() if r['family'] == f] for f in 'ABC'}
    D['fam'] = fam
    for f in 'ABC':
        assert len(fam[f]) == base[f'{f}_k'], f
        raw = Counter(code[s]['raw_coefficient_sign'] for s in fam[f])
        assert (raw['+'], raw['-'], raw['null'], raw['mixed']) == tuple(base[f'{f}_{k}'] for k in ('positive', 'negative', 'null', 'mixed')), f
    # illustrative scenario: every flagged study excluded (the ruling is the author's; sensitivity_analysis.py is not changed by it)
    def tally(ids, f):
        c = Counter(code[s]['substantive_direction'] for s in ids)
        return c['Favourable'], c['Unfavourable'], c['Null'], c['Mixed']
    ill = {}
    for f in 'ABC':
        keep = [s for s in fam[f] if st[s] != 'flagged']
        ill[f] = {'k': len(keep), 'sub': tally(keep, f)}
    D['illustrative'] = ill
    D['flagged_by_family'] = {f: sum(st[s] == 'flagged' for s in fam[f]) for f in 'ABC'}
    D['diverge'] = len([x for x in next(r for r in rows if r['scenario'].startswith('S4d'))['dropped_studies_in_families'].split(';') if x])
    # descriptive numbers
    dc = Counter(r['study_design_class'] for r in em)
    D['dc'] = dc
    yrs = [int(r['publication_year']) for r in ed if r['publication_year'].strip().isdigit()]
    D['since2010'] = sum(y >= 2010 for y in yrs)
    D['median_year'] = int(statistics.median(yrs))
    D['mech'] = Counter({m: sum(T(r.get(m, '')) for r in ed) for m in MECH})
    am = [r['risk_of_bias_rating'] for r in ed if cf.tool_of(r['risk_of_bias_tool']) == 'AMSTAR 2']
    D['amstar_critically_low'] = sum(x.startswith('Critically Low') for x in am)
    D['amstar_low'] = sum(x.startswith('Low') for x in am)
    D['water_access'] = sum(T(r.get('water_access', '')) for r in ed)
    D['sanitation_access'] = sum(T(r.get('sanitation_access', '')) for r in ed)
    D['country'] = lambda name: sum(1 for r in ed if r['country'].strip() == name)
    return D


# ---------------------------------------------------------------- chart
def chart(D):
    code, fam = D['code'], D['fam']
    names = {'A': 'A  Legal status, tenure, recognition', 'B': 'B  Assistance, participation, trust', 'C': 'C  Ownership, regulation, institutions'}
    panels = [('raw_coefficient_sign', [('+', BLUE, 'Positive (+)'), ('-', ORANGE, 'Negative (-)'), ('mixed', VIOLET, 'Mixed'), ('null', GREY, 'Null')], 'Raw sign of the reported estimate'),
              ('substantive_direction', [('Favourable', BLUE, 'Favourable'), ('Unfavourable', ORANGE, 'Unfavourable'), ('Mixed', VIOLET, 'Mixed'), ('Null', GREY, 'Null')],
               'Substantive direction for households')]
    plt.rcParams.update({'font.family': 'sans-serif', 'font.size': 9, 'axes.edgecolor': '#c8c7c1', 'axes.labelcolor': MUTED, 'xtick.color': MUTED, 'ytick.color': INK,
                         'figure.facecolor': SURF, 'axes.facecolor': SURF, 'text.color': INK})
    fig, axes = plt.subplots(2, 1, figsize=(6.6, 4.3), sharex=True)
    for ax, (key, cols, ttl) in zip(axes, panels):
        for i, f in enumerate('ABC'):
            c = Counter(code[s][key] for s in fam[f])
            left = 0
            for val, col, _ in cols:
                v = c.get(val, 0)
                if v:
                    ax.barh(i, v, left=left, color=col, height=0.55, edgecolor=SURF, linewidth=2)
                    ax.text(left + v / 2, i, str(v), ha='center', va='center', color='white', fontsize=9, fontweight='bold')
                    left += v
            ax.text(left + 0.4, i, f'k = {left}', va='center', fontsize=8.5, color=MUTED)
        ax.set_yticks(range(3)); ax.set_yticklabels([names[f] for f in 'ABC']); ax.invert_yaxis(); ax.set_xlim(0, 21); ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(5))
        ax.set_title(ttl, loc='left', fontsize=9, color=INK, pad=22)
        ax.legend([plt.Rectangle((0, 0), 1, 1, color=col) for _, col, _ in cols], [lab for _, _, lab in cols], ncol=4, frameon=False, loc='lower left',
                  bbox_to_anchor=(0.0, 1.0), fontsize=8, handlelength=1.0, columnspacing=1.2)
        for sp in ('top', 'right'):
            ax.spines[sp].set_visible(False)
        ax.tick_params(length=0)
    axes[1].set_xlabel('Number of studies (nothing is pooled; no effect size is shown)')
    fig.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=200, metadata={'Software': None})
    plt.close(fig)
    buf.seek(0)
    return buf


# ---------------------------------------------------------------- docx helpers
TBLPR_ORDER = ['tblStyle', 'tblpPr', 'tblOverlap', 'bidiVisual', 'tblStyleRowBandSize', 'tblStyleColBandSize', 'tblW', 'jc', 'tblCellSpacing', 'tblInd', 'tblBorders', 'shd',
               'tblLayout', 'tblCellMar', 'tblLook']


def tblpr_put(tblPr, el):
    """Insert el into tblPr at its place in the schema sequence (Word rejects out-of-order children), replacing any element of the same name."""
    name = el.tag.split('}')[1]
    for old in tblPr.findall(qn(f'w:{name}')):
        tblPr.remove(old)
    later = TBLPR_ORDER[TBLPR_ORDER.index(name) + 1:]
    for child in tblPr:
        if child.tag.split('}')[1] in later:
            child.addprevious(el)
            return
    tblPr.append(el)


def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), fill)
    tcPr.append(shd)


def borders(table, color='C8C7C1', sz=4, inside=True, only_h=False):
    tblPr = table._tbl.tblPr
    b = OxmlElement('w:tblBorders')
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        e = OxmlElement(f'w:{edge}')
        off = (edge in ('left', 'right', 'insideV') and only_h) or (edge.startswith('inside') and not inside)
        e.set(qn('w:val'), 'nil' if off else 'single'); e.set(qn('w:sz'), str(sz)); e.set(qn('w:space'), '0'); e.set(qn('w:color'), color)
        b.append(e)
    tblpr_put(tblPr, b)


def cell_margins(table, top=50, bottom=50, left=90, right=90):
    tblPr = table._tbl.tblPr
    m = OxmlElement('w:tblCellMar')
    for k, v in (('top', top), ('left', left), ('bottom', bottom), ('right', right)):
        e = OxmlElement(f'w:{k}'); e.set(qn('w:w'), str(v)); e.set(qn('w:type'), 'dxa'); m.append(e)
    tblpr_put(tblPr, m)


def fix_widths(table, widths):
    table.autofit = False
    tblPr = table._tbl.tblPr
    lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); tblpr_put(tblPr, lay)
    tw = OxmlElement('w:tblW'); tw.set(qn('w:w'), str(int(sum(widths) * 1440))); tw.set(qn('w:type'), 'dxa'); tblpr_put(tblPr, tw)
    for i, w in enumerate(widths):
        table.columns[i].width = Inches(w)
        for c in table.columns[i].cells:
            c.width = Inches(w)


def runs(p, text, size=None, color=None, italic=False, bold=False):
    """Add text to paragraph p; **x** marks bold spans."""
    for i, part in enumerate(text.split('**')):
        if not part:
            continue
        r = p.add_run(part)
        r.bold = bold or (i % 2 == 1)
        r.italic = italic
        if size:
            r.font.size = Pt(size)
        if color:
            r.font.color.rgb = color
    return p


def para(doc, text, size=None, after=5, before=0, italic=False, color=None, align=None, keep=False, style=None):
    p = doc.add_paragraph(style=style)
    p.paragraph_format.space_after = Pt(after); p.paragraph_format.space_before = Pt(before)
    if align:
        p.alignment = align
    if keep:
        p.paragraph_format.keep_with_next = True
    return runs(p, text, size=size, color=color, italic=italic)


def bullet(doc, text, style='List Bullet', after=3):
    p = doc.add_paragraph(style=style)
    p.paragraph_format.space_after = Pt(after)
    return runs(p, text)


def table(doc, headers, rows, widths, align=None, size=8.5, header_fill='E8EEF5', bold_first=False, fills=None):
    t = doc.add_table(rows=1 + len(rows), cols=len(headers))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    borders(t); cell_margins(t); fix_widths(t, widths)
    align = align or ['l'] * len(headers)
    amap = {'l': WD_ALIGN_PARAGRAPH.LEFT, 'c': WD_ALIGN_PARAGRAPH.CENTER, 'r': WD_ALIGN_PARAGRAPH.RIGHT}
    for ri, row in enumerate([headers] + rows):
        for ci, val in enumerate(row):
            c = t.cell(ri, ci)
            p = c.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.alignment = amap[align[ci]] if ri else (WD_ALIGN_PARAGRAPH.LEFT if align[ci] == 'l' else WD_ALIGN_PARAGRAPH.CENTER)
            runs(p, str(val), size=size, bold=(ri == 0) or (bold_first and ci == 0))
            if ri == 0:
                shade(c, header_fill)
            elif fills and fills.get(ri - 1):
                shade(c, fills[ri - 1])
    # keep rows whole and repeat the header row (cantSplit precedes tblHeader in the schema)
    for r in t.rows:
        cs = OxmlElement('w:cantSplit'); cs.set(qn('w:val'), 'true'); r._tr.get_or_add_trPr().append(cs)
    h = OxmlElement('w:tblHeader'); h.set(qn('w:val'), 'true'); t.rows[0]._tr.get_or_add_trPr().append(h)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t


def field(run, instr):
    for kind, txt in (('begin', None), (None, instr), ('end', None)):
        if kind:
            e = OxmlElement('w:fldChar'); e.set(qn('w:fldCharType'), kind)
        else:
            e = OxmlElement('w:instrText'); e.set(qn('xml:space'), 'preserve'); e.text = txt
        run._r.append(e)


def style_doc(doc):
    base = doc.styles['Normal']
    base.font.name = 'Calibri'; base.font.size = Pt(10)
    base.element.rPr.rFonts.set(qn('w:eastAsia'), 'Calibri')
    base.paragraph_format.line_spacing = 1.08
    for name, size, before, after in (('Heading 1', 13.5, 12, 4), ('Heading 2', 11, 8, 3), ('Title', 22, 0, 2)):
        s = doc.styles[name]
        s.font.name = 'Calibri'; s.font.size = Pt(size); s.font.bold = True; s.font.color.rgb = NAVY
        rpr = s.element.get_or_add_rPr()
        rf = rpr.find(qn('w:rFonts'))
        if rf is None:
            rf = OxmlElement('w:rFonts'); rpr.append(rf)
        for a in ('w:ascii', 'w:hAnsi', 'w:eastAsia', 'w:cs'):
            rf.set(qn(a), 'Calibri')
        for a in ('w:asciiTheme', 'w:hAnsiTheme', 'w:eastAsiaTheme', 'w:cstheme'):
            if rf.get(qn(a)) is not None:
                del rf.attrib[qn(a)]
        s.paragraph_format.space_before = Pt(before); s.paragraph_format.space_after = Pt(after)
        s.paragraph_format.keep_with_next = True
    # the default Title style carries a bottom border and heavy spacing; remove the border
    ppr = doc.styles['Title'].element.get_or_add_pPr()
    for b in ppr.findall(qn('w:pBdr')):
        ppr.remove(b)
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Inches(8.5), Inches(11)
    sec.left_margin = sec.right_margin = Inches(0.9)
    sec.top_margin, sec.bottom_margin = Inches(0.85), Inches(0.8)
    hp = sec.header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.LEFT
    runs(hp, f'The Legal Last Mile: executive summary of preliminary findings   |   release {RELEASE}   |   PRELIMINARY', size=8, color=RGBColor(0x52, 0x51, 0x4E))
    fp = sec.footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = fp.add_run('Page '); r.font.size = Pt(8)
    r = fp.add_run(); r.font.size = Pt(8); field(r, 'PAGE')
    r = fp.add_run(' of '); r.font.size = Pt(8)
    r = fp.add_run(); r.font.size = Pt(8); field(r, 'NUMPAGES')


def banner(doc, text, fill='FFF4D6', edge='E0A100', width=6.7):
    t = doc.add_table(rows=1, cols=1)
    fix_widths(t, [width]); cell_margins(t, 90, 90, 140, 120)
    tblPr = t._tbl.tblPr
    b = OxmlElement('w:tblBorders')
    for edge_name in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        e = OxmlElement(f'w:{edge_name}')
        if edge_name == 'left':
            e.set(qn('w:val'), 'single'); e.set(qn('w:sz'), '24'); e.set(qn('w:space'), '0'); e.set(qn('w:color'), edge)
        else:
            e.set(qn('w:val'), 'nil')
        b.append(e)
    tblpr_put(tblPr, b)
    c = t.cell(0, 0); shade(c, fill)
    p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
    runs(p, text, size=9.5)
    doc.add_paragraph().paragraph_format.space_after = Pt(0)


# ---------------------------------------------------------------- content
def build():
    D = gather()
    F, n, base, rows, A16, fam, ill, st = D['F'], D['n'], D['base'], D['rows'], D['A16'], D['fam'], D['illustrative'], D['status']
    dc = D['dc']
    pct = lambda k, d: f'{100 * k / d:.0f}%'
    dec = F['full_text_decided']
    hv = F['human_verified_rows']
    hv_inc = F['reviewer_2_confirmed_includes'] + F['human_adjudicated_includes']
    hv_exc = F['human_adjudicated_excludes']
    descriptive = dc['qualitative'] + dc['mixed_methods'] + dc['doctrinal']
    causal = F['causal_capable_designs']
    all_hold = all('FAILS' not in (r['A_test_majority_concordant'], r['B_test_none_negative_or_null'], r['C_test_no_dominant_sign'], r['C_test_no_dominant_direction']) for r in rows)
    shares = [r['A_concordant_pct'] for r in rows if r['A_concordant_pct'] != '']
    fl = D['flagged_by_family']
    b_k, b_rest = base['B_k'], ill['B']['k']
    top3 = D['mech'].most_common(3)
    country = D['country']
    geo = bmp.geography_framing(F)
    doc = Document()
    z = doc.settings.element.find(qn('w:zoom'))
    if z is not None and z.get(qn('w:percent')) is None:
        z.set(qn('w:percent'), '100')   # the python-docx template omits the required attribute
    style_doc(doc)
    cp = doc.core_properties
    cp.title = 'The Legal Last Mile: executive summary of preliminary findings'
    cp.subject = 'AI-assisted systematic review of legal and administrative conditions and household water and sanitation access'
    cp.author = 'The Legal Last Mile review project'; cp.last_modified_by = cp.author
    cp.created = cp.modified = PIN
    cp.keywords = 'systematic review; SWiM; water; sanitation; administrative law; preliminary'

    # ---- title block
    doc.add_paragraph('The Legal Last Mile', style='Title')
    para(doc, '**Executive summary of preliminary findings (partial report)**', size=13, after=2, color=NAVY)
    para(doc, f'AI-assisted systematic review of legal and administrative conditions and household access to water and sanitation  ·  interim release {RELEASE}  ·  {REPORT_DATE}', size=9, color=RGBColor(0x52, 0x51, 0x4E), after=8)
    banner(doc, f"**Preliminary and partial.** Screening, data extraction, quality appraisal and the direction coding of each estimate were done by an AI under the author's rulings. "
                f"Only {hv:,} of {dec:,} full-text decisions ({hv / dec * 100:.1f}%) have a recorded human check. Of the {F['swim_core_studies']} studies in the quantitative syntheses, the author's own earlier checks cover the inclusion decisions of {F['swim_core_inclusion_human_verified'] - F['swim_core_direction_ck_confirmed']}; "
                f"for {F['swim_core_direction_ck_confirmed']} more a confirmation was recorded after the AI's own scope check and has not yet been checked by the author against the papers. "
                f"No effect size is pooled. Read every number as AI-produced and unverified against the source papers unless this summary says otherwise.")

    # ---- 1. bottom line
    doc.add_heading('1. The bottom line', level=1)
    msgs = [
        f"**A large evidence base that is mostly descriptive.** {n:,} studies met the full-text criteria ({pct(D['since2010'], n)} published since 2010). {descriptive:,} ({pct(descriptive, n)}) are qualitative, mixed-methods or doctrinal designs, "
        f"and only {causal} ({pct(causal, n)}) were appraised with a causal-design instrument (ROBINS-I or RoB 2); the 5 randomised trials are 4 distinct trials.",
        f"**Legal recognition and formal status tend to go with better access (Family A).** {base['A_favourable']} of {base['A_k']} quantitative studies ({base['A_concordant_pct']:.0f}%) point in the favourable direction; "
        f"{base['A_unfavourable']} point the other way and {base['A_subst_null']} are null.",
        f"**Assistance, participation and trust look uniformly favourable (Family B), but this is the least secure result.** All {b_k} studies are favourable ({base['B_favourable']}) or mixed ({base['B_subst_mixed']}), "
        f"yet {fl['B']} of the {b_k} are among the ten studies flagged on a scope check and awaiting the author's ruling. If all {fl['B']} were excluded, {b_rest} {'study' if b_rest == 1 else 'studies'} would remain.",
        f"**Ownership, regulation and institutional structure show no consistent direction (Family C).** {base['C_favourable']} favourable, {base['C_unfavourable']} unfavourable and {base['C_subst_mixed']} mixed across {base['C_k']} studies with "
        f"heterogeneous exposures and outcomes. The one coherent sub-pattern, private ownership going with worse affordability, rests on three studies that probably draw on two independent samples.",
        f"**The counts survive every test tried, but nothing is pooled and confidence is low.** " + (f"The pre-stated conclusions hold in all {len(rows) - 1} alternative scenarios" if all_hold else "Some pre-stated conclusions fail in some scenarios (section 5)") +
        f" (Family A's favourable share ranges {min(shares):.1f}% to {max(shares):.1f}%). No family has enough comparable studies for meta-analysis, and confidence in any causal or comparative claim is low to very low.",
        f"**The evidence is concentrated where networks are incomplete.** India, Brazil, South Africa, Ghana and the United States dominate, while high-coverage welfare states are sparsely represented ({geo['canada']} single-country studies in Canada, {geo['canada_fn']} on the drinking water of First Nations and other Indigenous communities, and {geo['netherlands']} in the Netherlands). "
        "Administrative exclusion inside universal-network systems (tariff hardship exemptions, tenant billing rules, administrative redress) is therefore comparatively under-examined in this evidence base.",
    ]
    for m in msgs:
        bullet(doc, m, style='List Number', after=4)

    # ---- 2. where the review stands
    doc.add_heading('2. What was done and where the review stands', level=1)
    funnel = [
        ['Search', f"{bmp.RAW:,} records, {bmp.UNIQUE:,} after de-duplication", f"Closed {bmp.SEARCH_CLOSED}. SSRN and Westlaw/Lexis were never searched."],
        ['Title and abstract', f"{F['title_abstract_include']:,} included", f"{bmp.TA_SCREENED:,} screened by the AI; a human second pass covered the {bmp.TA_HUMAN_PASS:,} include-or-unsure records, not the AI's excludes."],
        ['Full text', f"{dec:,} of {F['full_text_records']:,} assessed ({100 * dec / F['full_text_records']:.1f}%): {F['full_text_include']:,} included, {F['full_text_exclude']:,} excluded",
         f"Retrieval closed by decision; {F['full_text_undecided']:,} records were never assessed. {hv:,} decisions ({100 * hv / dec:.1f}%) carry a human check."],
        ['Extraction and appraisal', f"{F['extraction_rows']:,} studies, 92 fields; all rated with a design-matched tool", 'By the AI, with no second extractor; the appraisal ratings are rule-based, and 40% use the project\'s own non-validated framework.'],
        ['Synthesis', f"{F['effect_size_rows']} effect-size rows: {sum(len(v) for v in fam.values())} in three families, {F['effect_size_by_family']['(none: reasoned non-fit)']} reasoned non-fits", 'Structured vote counting of direction (SWiM). None is pooled.'],
    ]
    table(doc, ['Stage', 'Result', 'Note'], funnel, [1.25, 2.55, 2.9], size=8.5, bold_first=True)
    para(doc, f"**Why no meta-analysis.** A phase-11 feasibility judgment found no family with enough studies sharing an exposure, comparator, outcome and effect measure. The {F['effect_size_rows']} extractable estimates were instead grouped into three thematic families "
              f"and synthesised by vote counting (Synthesis Without Meta-analysis, Campbell et al. 2020). Each estimate is coded twice: its **raw sign** (the sign of the reported coefficient) and its **substantive direction** "
              f"(whether the result is favourable or unfavourable for household access, affordability or equity). The two differ because a higher tariff is worse for households while a higher coverage rate is better.", after=4)

    # ---- 3. the evidence base
    doc.add_heading('3. What the evidence base looks like', level=1)
    tools = F['tools']
    for b in (
        f"**Designs.** Qualitative {dc['qualitative']}, mixed-methods {dc['mixed_methods']}, observational {dc['observational']}, quasi-experimental {dc['quasi_experimental']}, doctrinal {dc['doctrinal']}, jurimetric {dc['jurimetric']}, "
        f"secondary systematic reviews {dc['systematic_review_secondary']}, experimental {dc['experimental']}, other {dc['other']}.",
        f"**Appraisal.** Tools used: CASP qualitative {tools['CASP Qualitative']}, MMAT {tools['MMAT']}, JBI cross-sectional {tools['JBI Cross-Sectional']}, ROBINS-I {tools['ROBINS-I']}, AMSTAR 2 {tools['AMSTAR 2']}, RoB 2 {tools['RoB 2']}, and "
        f"{tools['Legal Framework']} ({pct(tools['Legal Framework'], n)}) under the project's own non-validated framework. Of the {tools['AMSTAR 2']} systematic reviews, {D['amstar_critically_low']} rate critically low and {D['amstar_low']} low on AMSTAR 2. "
        f"Only {F['mechanism_certainty_numeric']['3'] + F['mechanism_certainty_numeric']['4']} studies reach the two highest mechanism-certainty levels (quasi-experimental or experimental evidence).",
        f"**Where.** " + ', '.join(f'{c} {v}' for c, v in F['country_top10_single_name'][:5]) + f" are the most frequent single countries ({F['country_multi_or_regional_studies']} studies name several countries or a region).",
        f"**What is studied.** The most coded mechanisms are " + ', '.join(f"{m.replace('_', ' ')} ({v})" for m, v in top3) + f". Water access is coded in {D['water_access']} studies and sanitation access in {D['sanitation_access']}, about half as often. "
        f"Redress mechanisms are thin: administrative review {D['mech']['administrative_review']} studies, judicial review {D['mech']['judicial_review']}.",
    ):
        bullet(doc, b)

    # ---- 4. the quantitative syntheses
    doc.add_heading('4. What the quantitative studies show', level=1)
    names = {'A': 'A. Legal status, tenure, recognition and governance arrangements', 'B': 'B. Assistance, participation, trust and external support', 'C': 'C. Ownership, regulation, institutional capacity and structure'}
    trs = []
    for f in 'ABC':
        c = Counter(st[s] for s in fam[f])
        trs.append([names[f], base[f'{f}_k'], f"{base[f'{f}_positive']} / {base[f'{f}_negative']} / {base[f'{f}_null']} / {base[f'{f}_mixed']}",
                    f"{base[f'{f}_favourable']} / {base[f'{f}_unfavourable']} / {base[f'{f}_subst_null']} / {base[f'{f}_subst_mixed']}", f"{c['confirmed']} / {c['flagged']} / {c['unchecked']}"])
    table(doc, ['Family', 'Studies', 'Raw sign\n+ / − / null / mixed', 'Substantive direction\nfav. / unfav. / null / mixed', "Direction-coding check\npassed AI check* / flagged / not yet"], trs, [2.45, 0.6, 1.15, 1.4, 1.1],
          align=['l', 'c', 'c', 'c', 'c'], size=8.5)
    para(doc, "*Passed the AI's own narrow-scope and outcome check; a confirmation was recorded on that basis and the author has not yet checked these papers against their source passages. 'Not yet' means the inclusion was confirmed earlier and the direction coding has not been checked.", size=8, color=RGBColor(0x52, 0x51, 0x4E), after=4)
    pic = doc.add_paragraph()
    pic.alignment = WD_ALIGN_PARAGRAPH.CENTER; pic.paragraph_format.space_after = Pt(2); pic.paragraph_format.keep_with_next = True
    shape = pic.add_run().add_picture(chart(D), width=Inches(5.9))
    shape._inline.docPr.set('descr', 'Two stacked bar panels for Families A, B and C. The first shows the raw sign of each study\'s estimate; the second shows its substantive direction for households. '
                                      f"Family A: {base['A_favourable']} favourable, {base['A_unfavourable']} unfavourable, {base['A_subst_null']} null. Family B: {base['B_favourable']} favourable, {base['B_subst_mixed']} mixed. "
                                      f"Family C: {base['C_favourable']} favourable, {base['C_unfavourable']} unfavourable, {base['C_subst_mixed']} mixed.")
    shape._inline.docPr.set('name', 'Direction of association by family')
    para(doc, '**Figure 1.** Direction of association in the three structured syntheses, read two ways.', size=8.5, color=RGBColor(0x52, 0x51, 0x4E), after=6, align=WD_ALIGN_PARAGRAPH.CENTER)
    for b in (
        f"**Family A (recognition and status).** Where a legal status, tenure right or formal recognition is the exposure, the association with access is favourable in {base['A_concordant_pct']:.0f}% of studies. "
        f"Two point the other way (S104, a tenure study in which owners had more service interruptions, and S1020, a watershed programme after which collection time rose; the second is among the flagged studies) and two are null.",
        f"**Family B (assistance, participation, trust).** {base['B_favourable']} studies are favourable and {base['B_subst_mixed']} is mixed (S294, a cluster trial with null health outcomes). The {b_k} study different mechanisms, and {fl['B']} of them are flagged (see below), so this should not be read as a pattern.",
        f"**Family C (ownership, regulation, structure).** Raw signs split {base['C_positive']} positive, {base['C_negative']} negative and {base['C_mixed']} mixed; substantive directions split {base['C_favourable']}, {base['C_unfavourable']} and {base['C_subst_mixed']}. "
        f"The exposures are too different (private versus public ownership, the level of regulation, new local governments, contract enforcement, cost-recovery policy, governance quality) to expect agreement.",
        f"**Two readings, deliberately.** Raw sign and substantive direction come apart for {D['diverge']} of the {F['swim_core_studies']} studies, so each is reported separately.",
        f"**Verification status.** {F['swim_core_inclusion_human_verified']} of the {F['swim_core_studies']} studies carry a recorded human verification of the inclusion decision, but for {F['swim_core_direction_ck_confirmed']} of them (and for their two direction codings) the record was entered after the AI's own scope check, and the author has not yet checked those papers; "
        f"the author's own earlier confirmations cover {F['swim_core_inclusion_human_verified'] - F['swim_core_direction_ck_confirmed']}. "
        f"The other {F['swim_core_flagged_for_author']} were flagged on a narrow-scope check (an exposure that is community management, participation, programme delivery, an attitude or macro-governance, or an outcome that is not household access) and are not counted as confirmed. "
        f"The effect estimates were extracted and checked against the full texts by the AI, not by a human.",
    ):
        bullet(doc, b)

    # ---- 5. robustness
    doc.add_heading('5. How robust are the counts?', level=1)
    pick = [('S0', 'Baseline'), ('S4 ', 'Drop S404, the one Family A coding judgment call'), ('S4c', 'Recode S471 as null (fully adjusted estimate)'),
            ('S4e', 'Recode S879 as null (household water access alone)'), ('S5', 'All of the above, plus the data-quality drops, applied together'), ('S4d', 'Keep only studies where raw sign and direction agree')]
    rr = []
    for key, label in pick:
        r = next(x for x in rows if x['scenario'].startswith(key))
        tests = 'all hold' if 'FAILS' not in (r['A_test_majority_concordant'], r['B_test_none_negative_or_null'], r['C_test_no_dominant_sign'], r['C_test_no_dominant_direction']) else 'one fails'
        rr.append([label, f"{r['A_k']}; {r['A_favourable']}/{r['A_unfavourable']}/{r['A_subst_null']} ({r['A_concordant_pct']:.0f}%)", f"{r['B_k']}; {r['B_favourable']}/{r['B_subst_mixed']}",
                   f"{r['C_k']}; {r['C_favourable']}/{r['C_unfavourable']}/{r['C_subst_mixed']}", tests])
    a, bb, cc = ill['A'], ill['B'], ill['C']
    a_ok = a['sub'][0] * 2 > a['k']
    b_ok = bb['sub'][1] == 0 and bb['sub'][2] == 0
    c_ok = max(cc['sub']) * 2 <= cc['k']
    rr.append(['**Illustrative:** all ten flagged studies excluded (the ruling is the author\'s)', f"{a['k']}; {a['sub'][0]}/{a['sub'][1]}/{a['sub'][2]} ({100 * a['sub'][0] / a['k']:.0f}%)", f"{bb['k']}; {bb['sub'][0]}/{bb['sub'][3]}",
               f"{cc['k']}; {cc['sub'][0]}/{cc['sub'][1]}/{cc['sub'][3]}", 'all hold' if (a_ok and b_ok and c_ok) else 'one fails'])
    table(doc, ['Scenario', 'Family A: k; fav./unfav./null', 'Family B: k; fav./mixed', 'Family C: k; fav./unfav./mixed', 'Pre-stated tests'], rr, [2.35, 1.35, 0.95, 1.2, 0.85],
          align=['l', 'c', 'c', 'c', 'c'], size=8)
    para(doc, f"The pre-stated conclusions were: more than half of Family A favourable; no Family B study unfavourable or null; no single direction holding a majority in Family C. They were fixed before the numbers were computed. "
              f"The scenarios do not test the direction coding itself, studies that were never extracted, or overlap between reports that were not flagged as linked. "
              f"The illustrative row shows the cost of the open scope question: Family B would shrink to {bb['k']} {'study' if bb['k'] == 1 else 'studies'}, though its direction would not change.", size=9.5, after=4)

    # ---- 6. confidence and limits
    doc.add_heading('6. How far to trust this', level=1)
    para(doc, "The author's tentative characterisation is **low to very low confidence for any causal or comparative claim** (no GRADE judgment has been made). The main reasons:", after=3)
    for b in (
        f"**Screening is incomplete.** {F['full_text_undecided']:,} of {F['full_text_records']:,} candidate records were never assessed at full text, and they are older on average, so earlier literature is under-represented. {F['exclusion_by_code']['E10']} of the {F['full_text_exclude']:,} excludes were never judged on content because the text was inaccessible.",
        f"**Most decisions are the AI's.** {dec - hv:,} of {dec:,} full-text decisions have no human check ({hv_inc} includes and {hv_exc} excludes do). A blind re-read of {A16['reread_excludes']} exclusions by two other AI models, adjudicated by the author, found "
        f"{A16['reversed_in_sample']} false exclusions among the {A16['sample']} randomly sampled ({100 * A16['rate']:.1f}%, 95% interval {100 * A16['rate_lo']:.1f} to {100 * A16['rate_hi']:.1f}%), roughly {A16['scaled']} studies across the {A16['pool']:,} content-based exclusions (interval {A16['scaled_lo']} to {A16['scaled_hi']}).",
        f"**Eligibility was narrowed after the fact.** After seeing the models' disagreement the author adopted a narrow reading of the second criterion (a legal or administrative access rule or mechanism, not programme delivery, participation or macro-governance). "
        f"Together with the four inclusions the models questioned, that moved {A16['moved_to_exclusion']} included reports to the exclusions, and it is also why ten core studies are flagged. The protocol was fixed before searching but registered on OSF retrospectively.",
        f"**Extraction and appraisal are unchecked.** There is no second extractor, {F['abstract_only_extractions']} studies were extracted from abstracts only (a floor), and appraisal ratings are rule-based. {F['jbi_high_concern']} of {tools['JBI Cross-Sectional']} JBI ratings are \"High concern\", which here means sparse extraction rather than a poor study.",
        "**The families are thematic groupings, not homogeneous pairs.** Vote counting weights every study equally, ignores size and precision, and is not certainty-graded.",
    ):
        bullet(doc, b)

    # ---- 7. decisions and next steps
    doc.add_heading('7. Decisions and next steps', level=1)
    steps = [
        ['1', f"Rule on the {F['swim_core_flagged_for_author']} flagged core studies (open item A28)", f"Include or exclude, with a reason code. Family B is most affected ({fl['B']} of {b_k}), then A ({fl['A']} of {base['A_k']}) and C ({fl['C']} of {base['C_k']}). The sheet is `02_screening/full_text/A28_SWIM_FLAGGED_CK_SHEET_2026-10-14.csv`."],
        ['2', 'Finish the human check of screening (A6, tiers 2 and 3)', '152 further rows (102 excludes, 50 includes) would bound the risk of wrongly excluded or included studies.'],
        ['3', 'Second-extract the prepared sample', '60 studies from S001 to S200, checked against the source papers, to estimate extraction error. A second sample from later studies is needed before any corpus-wide claim.'],
        ['4', 'Reduce the retrieval bias', "Prioritise the older, unassessed records, and consider targeted searches for evidence from high-coverage welfare states (for example the Netherlands and other European systems) to examine administrative exclusion inside universal-network systems."],
        ['5', 'Register and freeze', f"Upload the preregistration draft to OSF (A7) and push the release tag `v{RELEASE}` from your own clone."],
        ['6', 'Revise the manuscript draft by hand', 'The draft in `07_manuscript/draft/` is generated from the same figures and is marked as not reviewed by a human author.'],
    ]
    table(doc, ['#', 'Item', 'What it needs'], [[a, b.replace('`', ''), c.replace('`', '')] for a, b, c in steps], [0.3, 2.3, 4.1], align=['c', 'l', 'l'], size=8.5)

    para(doc, 'Provenance. Every figure is computed by code/analysis/build_executive_summary.py from the project databases (00_admin/CURRENT_FIGURES.md, 05_analysis/sensitivity/SENSITIVITY_ANALYSIS_2026-09-28.md, '
              '05_analysis/effect_sizes/SWIM_DIRECTION_CODING_2026-10-14.csv and SWIM_CK_CHECKS_2026-10-14.csv). The full report is 06_outputs/PRELIMINARY_RESULTS_REPORT_2026-09-29.docx; '
              'AI use is described in AI_USE_STATEMENT.md.', size=8.5, color=RGBColor(0x52, 0x51, 0x4E), before=4, after=0)
    doc.save(OUT)
    pin_zip(OUT)
    return D


def pin_zip(path, when=(2026, 10, 14, 12, 0, 0)):
    """Rewrite the zip with fixed entry dates so the file is byte-stable between runs."""
    with zipfile.ZipFile(path) as z:
        items = [(i.filename, z.read(i.filename)) for i in z.infolist()]
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as z:
        for name, data in items:
            zi = zipfile.ZipInfo(name, date_time=when)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o600 << 16
            z.writestr(zi, data)


if __name__ == '__main__':
    D = build()
    print('wrote', OUT.relative_to(ROOT), f"({D['n']:,} studies; families {[len(v) for v in D['fam'].values()]})")
