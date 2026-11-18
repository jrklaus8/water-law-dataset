#!/usr/bin/env python3
"""Render 06_outputs/PRELIMINARY_RESULTS_REPORT_2026-09-29.md as one self-contained, navigable HTML page.

No third-party dependencies, no network use, no external fonts/scripts: the file works when opened from disk, from GitHub Pages or from any static host.
The report text is converted by a small Markdown subset converter (headings, paragraphs, lists, tables, blockquote, rules, bold/italic/code/links) so that the
verifier can check freshness without pandoc. The headline cards are computed from current_figures.compute(), not typed.
Run from the project root:  python3 code/analysis/build_report_html.py
"""
import html as H
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402

ROOT = cf.ROOT
SRC = ROOT / '06_outputs/PRELIMINARY_RESULTS_REPORT_2026-09-29.md'
OUT = ROOT / '06_outputs/PRELIMINARY_RESULTS_REPORT_2026-09-29.html'


# ------------------------------------------------------------------ inline markdown
def slug(num):
    return 's-' + re.sub(r'[^a-z0-9]+', '-', num.lower()).strip('-')


def inline(text, ids):
    codes = []

    def keep(m):
        codes.append(m.group(1))
        return f'\x00{len(codes) - 1}\x00'

    t = re.sub(r'`([^`]+)`', keep, text)
    t = H.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\*\w])\*(?!\s)(.+?)(?<!\s)\*(?![\*\w])', r'<em>\1</em>', t)
    # only http(s), in-page or relative links become anchors; anything else (e.g. a javascript: URL inside an AI-extracted quotation) is left as plain text (2026-10-04 review)
    t = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', lambda m: f'<a href="{H.escape(m.group(2))}">{m.group(1)}</a>' if re.match(r'^(https?://|#|[\w./-]+$)', m.group(2), re.I) else m.group(0), t)

    def xref(m):
        sid = slug(m.group(1))
        return f'<a class="xref" href="#{sid}">§{m.group(1)}</a>' if sid in ids else m.group(0)

    t = re.sub(r'§(\d[A-Z]?(?:\.\d+)?)', xref, t)
    return re.sub(r'\x00(\d+)\x00', lambda m: f'<code>{H.escape(codes[int(m.group(1))], quote=False)}</code>', t)


# ------------------------------------------------------------------ block parser
def parse(md):
    lines = md.split('\n')
    blocks, i = [], 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1
        elif re.match(r'^#{1,3} ', ln):
            lvl = len(ln) - len(ln.lstrip('#'))
            blocks.append(('h', lvl, ln[lvl:].strip()))
            i += 1
        elif ln.startswith('>'):
            buf = []
            while i < len(lines) and lines[i].startswith('>'):
                buf.append(lines[i].lstrip('>').strip())
                i += 1
            blocks.append(('quote', ' '.join(buf)))
        elif re.match(r'^-{3,}\s*$', ln):
            blocks.append(('hr',))
            i += 1
        elif ln.startswith('|'):
            buf = []
            while i < len(lines) and lines[i].startswith('|'):
                buf.append(lines[i])
                i += 1
            rows = [[c.strip() for c in re.split(r'(?<!\\)\|', r.strip()[1:-1])] for r in buf]
            assert re.fullmatch(r'[\s|:\-]+', buf[1]), 'table without separator row'
            for r in rows:
                assert len(r) == len(rows[0]), f'ragged table row: {r[:3]}'
            blocks.append(('table', rows[0], rows[2:]))
        elif re.match(r'^- ', ln) or re.match(r'^\d+\. ', ln):
            ordered = bool(re.match(r'^\d+\. ', ln))
            items = []
            pat = r'^\d+\. ' if ordered else r'^- '
            while i < len(lines) and re.match(pat, lines[i]):
                items.append(re.sub(pat, '', lines[i]))
                i += 1
            blocks.append(('ol' if ordered else 'ul', items))
        else:
            buf = []
            while i < len(lines) and lines[i].strip() and not re.match(r'^(#{1,3} |>|\||- |\d+\. |-{3,}\s*$)', lines[i]):
                buf.append(lines[i].strip())
                i += 1
            blocks.append(('p', ' '.join(buf)))
    return blocks


KIND = {  # section number prefix -> (css class, label)
    '1': ('methods', 'Methods & progress'),
    '2A': ('evidence', 'Extracted evidence'),
    '2B': ('interp', 'Tentative interpretation'),
    '3': ('limits', 'Confidence & limitations'),
    '4': ('next', 'Next steps'),
}


def split_num(title):
    m = re.match(r'^(\d+[A-Z]?(?:\.\d+)?)\.?\s+(.*)$', title)
    return (m.group(1), m.group(2)) if m else ('', title)


def short(title):
    return re.split(r' \(| — ', title, 1)[0]


NUMERIC = re.compile(r'[\d,.%\s/()+\-–]+')


def render_table(head, rows):
    def td(c):
        cls = ' class="num"' if NUMERIC.fullmatch(c) and c.strip() else ''
        return '<td' + cls + '>' + c + '</td>'

    out = ['<div class="tablewrap" tabindex="0"><table><thead><tr>']
    out += ['<th scope="col">' + c + '</th>' for c in head]
    out.append('</tr></thead><tbody>')
    out += ['<tr>' + ''.join(td(c) for c in r) + '</tr>' for r in rows]
    out.append('</tbody></table></div>')
    return ''.join(out)


def build():
    F = cf.compute()
    md = SRC.read_text(encoding='utf-8')
    blocks = parse(md)
    ids = {slug(split_num(b[2])[0]) for b in blocks if b[0] == 'h' and b[1] in (2, 3) and split_num(b[2])[0]}
    title = next(b[2] for b in blocks if b[0] == 'h' and b[1] == 1)
    gen_date = re.search(r'generated (\d{4}-\d\d-\d\d)', title).group(1)
    clean_title = re.sub(r'\s*\(generated [^)]*\)', '', title)

    toc, body, banner = [], [], ''
    open_sub = open_sec = False
    kind = ('plain', '')
    n = F['extraction_rows']
    for b in blocks:
        if b[0] == 'h' and b[1] == 1:
            continue
        if b[0] == 'h' and b[1] == 2:
            if open_sub:
                body.append('</div></details>')
                open_sub = False
            if open_sec:
                body.append('</section>')
            num, name = split_num(b[2])
            kind = KIND.get(num, ('plain', ''))
            sid = slug(num) if num else slug(name)
            toc.append(('h2', sid, num, short(name), kind[0]))
            body.append(f'<section class="sec k-{kind[0]}" id="{sid}"><header class="sechead"><span class="chip">{H.escape(kind[1])}</span>'
                        f'<h2><span class="num">{H.escape(num)}</span> {inline(name, ids)}<a class="anchor" href="#{sid}" aria-label="Link to this section">#</a></h2></header>')
            open_sec = True
        elif b[0] == 'h' and b[1] == 3:
            if open_sub:
                body.append('</div></details>')
            num, name = split_num(b[2])
            sid = slug(num)
            toc.append(('h3', sid, num, short(name), kind[0]))
            body.append(f'<details class="sub" id="{sid}" open><summary><h3><span class="num">{H.escape(num)}</span> {inline(name, ids)}</h3>'
                        f'<a class="anchor" href="#{sid}" aria-label="Link to this subsection">#</a></summary><div class="subbody">')
            open_sub = True
        elif b[0] == 'p':
            body.append(f'<p>{inline(b[1], ids)}</p>')
        elif b[0] == 'quote' and not banner:
            banner = (f'<aside class="banner" role="note"><div class="bicon" aria-hidden="true">!</div><p>{inline(b[1], ids)}</p></aside>')
        elif b[0] == 'quote':
            body.append(f'<blockquote>{inline(b[1], ids)}</blockquote>')
        elif b[0] == 'hr':
            body.append('<hr>')
        elif b[0] in ('ul', 'ol'):
            body.append(f'<{b[0]}>' + ''.join(f'<li>{inline(x, ids)}</li>' for x in b[1]) + f'</{b[0]}>')
        elif b[0] == 'table':
            body.append(render_table([inline(c, ids) for c in b[1]], [[inline(c, ids) for c in r] for r in b[2]]))
    if open_sub:
        body.append('</div></details>')
    if open_sec:
        body.append('</section>')

    toc_html = []
    for kind_, sid, num, name, k in toc:
        cls = 'l2' if kind_ == 'h2' else 'l3'
        toc_html.append(f'<a class="{cls} k-{k}" href="#{sid}" data-target="{sid}"><span class="tn">{H.escape(num)}</span><span class="tt">{H.escape(name)}</span></a>')

    dec, rec = F['full_text_decided'], F['full_text_records']
    cards = [
        (f"{n:,}", 'studies extracted', 'by an AI; no human second extraction yet', 'neutral'),
        (f"{100 * dec / rec:.1f}%", 'of full texts assessed', f"{dec:,} of {rec:,}; {F['full_text_undecided']:,} never assessed", 'warn'),
        (f"{F['causal_capable_designs']}", 'causal-capable designs', f"{100 * F['causal_capable_designs'] / n:.0f}% of studies (63 quasi-experimental, 5 randomised = 4 trials)", 'warn'),
        (f"{F['effect_size_rows_pooled']}", 'pooled estimates', f"{F['effect_size_rows']} effect-size rows; direction of association only", 'neutral'),
        (f"{F['abstract_only_extractions']}", 'abstract-only extractions', 'extracted without the full text', 'warn'),
        (f"{F['reviewer_2_confirmed_includes']}", 'human-confirmed includes', 'no extracted value or rating human-checked', 'bad'),
    ]
    figs = [('fig4_direction_by_family', 'Direction of association in the three syntheses'), ('fig1_design_mix', 'Study designs'), ('fig2_publication_years', 'Publication years'),
            ('fig3_countries', 'Countries'), ('fig5_appraisal_tools', 'Appraisal instruments')]
    fdir = cf.ROOT / '06_outputs/figures'
    inner = ''.join(f'<figure class="fig"><div class="figsvg" role="img" aria-label="{H.escape(t)}">{(fdir / (f + ".svg")).read_text(encoding="utf-8").split("?>", 1)[-1]}</div></figure>' for f, t in figs if (fdir / (f + '.svg')).exists())
    figures_html = f'<details class="figs" open><summary>Figures</summary><div class="figgrid">{inner}</div></details>' if inner else ''
    cards_html = ''.join(f'<div class="card c-{c}"><div class="big">{a}</div><div class="lab">{b}</div><div class="sub">{H.escape(d)}</div></div>' for a, b, d, c in cards)

    return (TEMPLATE
            .replace('{{TITLE}}', H.escape(clean_title))
            .replace('{{DATE}}', gen_date)
            .replace('{{TOC}}', '\n'.join(toc_html))
            .replace('{{CARDS}}', cards_html)
            .replace('{{FIGURES}}', figures_html)
            .replace('{{BANNER}}', banner)
            .replace('{{BODY}}', '\n'.join(body)))


TEMPLATE = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Preliminary Results Report</title>
<meta name="description" content="Preliminary, AI-assisted results of the Legal Last Mile systematic review. Not final.">
<style>
:root{--bg:#f6f7f9;--surface:#fff;--ink:#1c2430;--muted:#5a6676;--line:#dfe4ea;--brand:#1f5f8b;--brand-ink:#fff;--soft:#eef3f8;
--evidence:#1f5f8b;--evidence-bg:#e8f1f8;--interp:#8a5a00;--interp-bg:#fff4dc;--limits:#a12b2b;--limits-bg:#fdecec;--next:#1d7a4d;--next-bg:#e6f5ec;--methods:#4b5565;--methods-bg:#edf0f4;
--code:#eef1f5;--shadow:0 1px 2px rgba(20,30,45,.06),0 4px 14px rgba(20,30,45,.05);--r:12px;--side:300px}
:root[data-theme=dark]{--bg:#0f141a;--surface:#171e27;--ink:#e6ebf1;--muted:#9aa7b7;--line:#2a3441;--brand:#6db3e6;--brand-ink:#0b1117;--soft:#1d2733;
--evidence:#7bbdee;--evidence-bg:#15283a;--interp:#f0b94d;--interp-bg:#33290f;--limits:#f08a8a;--limits-bg:#381a1a;--next:#6fd39c;--next-bg:#12301f;--methods:#a9b4c2;--methods-bg:#1f2833;--code:#222c38;--shadow:none}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#0f141a;--surface:#171e27;--ink:#e6ebf1;--muted:#9aa7b7;--line:#2a3441;--brand:#6db3e6;--brand-ink:#0b1117;--soft:#1d2733;
--evidence:#7bbdee;--evidence-bg:#15283a;--interp:#f0b94d;--interp-bg:#33290f;--limits:#f08a8a;--limits-bg:#381a1a;--next:#6fd39c;--next-bg:#12301f;--methods:#a9b4c2;--methods-bg:#1f2833;--code:#222c38;--shadow:none}}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:76px}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;-webkit-text-size-adjust:100%}
a{color:var(--brand)}
.skip{position:absolute;left:-999px;top:8px;background:var(--brand);color:var(--brand-ink);padding:8px 12px;border-radius:8px;z-index:100}
.skip:focus{left:8px}
#progress{position:fixed;top:0;left:0;height:3px;width:0;background:var(--brand);z-index:60}
.top{position:sticky;top:0;z-index:50;display:flex;align-items:center;gap:10px;padding:10px 16px;background:var(--surface);border-bottom:1px solid var(--line)}
.top .name{font-weight:650;font-size:.95rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;flex:1;min-width:0}
.pill{font-size:.72rem;font-weight:700;letter-spacing:.04em;text-transform:uppercase;padding:3px 9px;border-radius:999px;background:var(--interp-bg);color:var(--interp);border:1px solid var(--interp);white-space:nowrap}
button,.btn{white-space:nowrap;font:inherit;font-size:.85rem;border:1px solid var(--line);background:var(--surface);color:var(--ink);padding:6px 11px;border-radius:9px;cursor:pointer}
button:hover{background:var(--soft)}
:focus-visible{outline:3px solid var(--brand);outline-offset:2px}
#menu{display:none}
.layout{display:grid;grid-template-columns:var(--side) minmax(0,1fr);max-width:1280px;margin:0 auto}
nav#toc{position:sticky;top:53px;align-self:start;height:calc(100vh - 53px);overflow:auto;padding:18px 14px 28px 18px;border-right:1px solid var(--line)}
.search{position:relative;margin-bottom:14px}
.search input{width:100%;padding:9px 12px;border:1px solid var(--line);border-radius:10px;background:var(--surface);color:var(--ink);font:inherit;font-size:.9rem}
.search small{display:block;color:var(--muted);margin-top:4px;min-height:1.2em;font-size:.78rem}
.tocnav a{display:flex;gap:8px;text-decoration:none;color:var(--muted);padding:5px 8px;border-radius:8px;font-size:.88rem;line-height:1.35;border-left:3px solid transparent}
.tocnav a:hover{background:var(--soft);color:var(--ink)}
.tocnav a.l2{font-weight:650;color:var(--ink);margin-top:10px}
.tocnav a.l3{margin-left:14px}
.tocnav a .tn{flex:none;min-width:2.2em;font-variant-numeric:tabular-nums;opacity:.75}
.tocnav a.active{background:var(--soft);color:var(--ink);border-left-color:var(--brand)}
.tocnav a.k-evidence.active{border-left-color:var(--evidence)}.tocnav a.k-interp.active{border-left-color:var(--interp)}.tocnav a.k-limits.active{border-left-color:var(--limits)}.tocnav a.k-next.active{border-left-color:var(--next)}
main{padding:28px clamp(16px,4vw,48px) 80px;min-width:0}
.hero h1{font-size:clamp(1.6rem,3.4vw,2.2rem);line-height:1.2;margin:.2em 0 .3em;letter-spacing:-.01em}
.hero .meta{color:var(--muted);font-size:.9rem}
.figs{margin:14px 0}.figs summary{cursor:pointer;font-weight:650;margin-bottom:8px}.figgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr));gap:12px}.fig{margin:0;border:1px solid var(--line,#d7d6cf);border-radius:10px;overflow:hidden;background:#fcfcfb}.figsvg svg{display:block;width:100%;height:auto}
.cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:18px 0 8px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:14px 15px;box-shadow:var(--shadow);border-top:4px solid var(--methods)}
.card .big{font-size:1.9rem;font-weight:750;line-height:1.1;font-variant-numeric:tabular-nums}
.card .lab{font-weight:600;font-size:.9rem;margin-top:3px}.card .sub{color:var(--muted);font-size:.8rem;margin-top:3px;line-height:1.35}
.card.c-warn{border-top-color:var(--interp)}.card.c-bad{border-top-color:var(--limits)}.card.c-neutral{border-top-color:var(--evidence)}
.guide{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin:14px 0 6px}
.guide a{display:block;text-decoration:none;color:var(--ink);background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:12px 14px;box-shadow:var(--shadow)}
.guide a:hover{transform:translateY(-1px)}
.guide b{display:block;margin-bottom:2px}.guide span{color:var(--muted);font-size:.86rem}
.guide .g1{border-left:5px solid var(--evidence)}.guide .g2{border-left:5px solid var(--interp)}.guide .g3{border-left:5px solid var(--limits)}.guide .g4{border-left:5px solid var(--next)}
.tools{display:flex;gap:8px;flex-wrap:wrap;margin:18px 0 4px}
.banner{display:flex;gap:12px;align-items:flex-start;background:var(--interp-bg);border:1px solid var(--interp);color:var(--ink);border-radius:var(--r);padding:12px 16px;margin:16px 0}
.banner p{margin:0}.bicon{flex:none;width:26px;height:26px;border-radius:50%;background:var(--interp);color:var(--bg);font-weight:800;display:grid;place-items:center;margin-top:2px}
.sec{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:6px clamp(14px,2.6vw,26px) 18px;margin:22px 0;box-shadow:var(--shadow);border-top:5px solid var(--methods)}
.sec.k-evidence{border-top-color:var(--evidence)}.sec.k-interp{border-top-color:var(--interp)}.sec.k-limits{border-top-color:var(--limits)}.sec.k-next{border-top-color:var(--next)}
.sechead{padding-top:12px}
.chip{display:inline-block;font-size:.72rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;padding:3px 10px;border-radius:999px;background:var(--methods-bg);color:var(--methods)}
.k-evidence .chip{background:var(--evidence-bg);color:var(--evidence)}.k-interp .chip{background:var(--interp-bg);color:var(--interp)}.k-limits .chip{background:var(--limits-bg);color:var(--limits)}.k-next .chip{background:var(--next-bg);color:var(--next)}
.sec.k-plain .chip{display:none}
h2{font-size:1.4rem;line-height:1.25;margin:.45em 0 .4em}
h3{font-size:1.05rem;line-height:1.35;margin:0;display:inline}
.num{color:var(--muted);font-variant-numeric:tabular-nums;margin-right:.25em;font-weight:600}
.anchor{opacity:0;margin-left:8px;text-decoration:none;font-weight:400;color:var(--muted)}
h2:hover .anchor,summary:hover .anchor,.anchor:focus{opacity:1}
details.sub{border-top:1px solid var(--line);margin-top:10px}
details.sub>summary{cursor:pointer;list-style:none;padding:12px 0 8px;display:flex;align-items:baseline;gap:6px}
details.sub>summary::-webkit-details-marker{display:none}
details.sub>summary::before{content:"";flex:none;width:.5em;height:.5em;border-right:2px solid var(--muted);border-bottom:2px solid var(--muted);transform:rotate(-45deg);transition:transform .15s;margin-right:6px;position:relative;top:-1px}
details.sub[open]>summary::before{transform:rotate(45deg)}
.subbody{padding:0 0 4px}
p{margin:.7em 0}ul,ol{padding-left:1.3em;margin:.6em 0}li{margin:.4em 0}
code{background:var(--code);padding:.1em .38em;border-radius:5px;font:.84em ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;word-break:break-word}
hr{border:0;border-top:1px solid var(--line);margin:26px 0}
.tablewrap{overflow-x:auto;margin:14px 0;border:1px solid var(--line);border-radius:10px;-webkit-overflow-scrolling:touch}
table{border-collapse:collapse;width:100%;font-size:.88rem;line-height:1.45}
th,td{padding:8px 11px;text-align:left;vertical-align:top;border-bottom:1px solid var(--line)}
th{position:sticky;top:0;background:var(--soft);font-weight:650;white-space:nowrap}
tbody tr:nth-child(even){background:color-mix(in srgb,var(--soft) 55%,transparent)}
tbody tr:last-child td{border-bottom:0}
td.num{text-align:right;font-variant-numeric:tabular-nums}
.sec.k-interp ol{list-style:none;padding:0;counter-reset:i}
.sec.k-interp ol>li{counter-increment:i;background:var(--interp-bg);border:1px solid var(--line);border-left:5px solid var(--interp);border-radius:10px;padding:10px 14px 10px 46px;position:relative;margin:10px 0}
.sec.k-interp ol>li::before{content:counter(i);position:absolute;left:12px;top:10px;width:24px;height:24px;border-radius:50%;background:var(--interp);color:var(--bg);font-weight:700;display:grid;place-items:center;font-size:.85rem}
.sec.k-next ol{list-style:none;padding:0;counter-reset:i}
.sec.k-next ol>li{counter-increment:i;border:1px solid var(--line);border-left:5px solid var(--next);border-radius:10px;padding:10px 14px 10px 46px;position:relative;margin:10px 0;background:var(--next-bg)}
.sec.k-next ol>li::before{content:counter(i);position:absolute;left:12px;top:10px;width:24px;height:24px;border-radius:50%;background:var(--next);color:var(--bg);font-weight:700;display:grid;place-items:center;font-size:.85rem}
mark{background:#ffe27a;color:#000;border-radius:3px;padding:0 1px}mark.cur{outline:2px solid var(--brand);background:#ffc400}
footer{color:var(--muted);font-size:.84rem;margin-top:30px}
#top{position:fixed;right:18px;bottom:18px;display:none;z-index:40;box-shadow:var(--shadow)}
.scrim{display:none}
@media (max-width:1100px){.guide{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:560px){.guide{grid-template-columns:1fr}.cards{grid-template-columns:repeat(2,minmax(0,1fr))}.card .big{font-size:1.6rem}.top .name{display:none}.top{justify-content:space-between}#menu{white-space:nowrap}}
@media (max-width:900px){
 .layout{display:block}#menu{display:inline-block}
 nav#toc{position:fixed;z-index:70;top:0;left:0;bottom:0;height:100vh;height:100dvh;width:min(86vw,340px);background:var(--surface);transform:translateX(-102%);transition:transform .2s;box-shadow:var(--shadow);border-right:1px solid var(--line)}
 body.menu-open nav#toc{transform:none}body.menu-open .scrim{display:block;position:fixed;inset:0;background:rgba(0,0,0,.45);z-index:65}
}
@media print{.top,nav#toc,#top,.tools,#progress,.skip,.anchor{display:none!important}.layout{display:block}main{padding:0}body{background:#fff;color:#000;font-size:11pt}.sec,.card{box-shadow:none;break-inside:avoid-page}details.sub>summary::before{display:none}.tablewrap{overflow:visible}th{position:static}}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition:none!important}}
</style>
</head>
<body>
<a class="skip" href="#content">Skip to the report</a>
<div id="progress" aria-hidden="true"></div>
<div class="top">
  <button id="menu" aria-label="Open contents" aria-expanded="false">☰ Contents</button>
  <span class="name">{{TITLE}}</span>
  <span class="pill">Preliminary · not final</span>
  <button id="theme" aria-label="Toggle dark mode">◐</button>
</div>
<div class="scrim" id="scrim"></div>
<div class="layout">
<nav id="toc" aria-label="Report contents">
  <div class="search"><input id="q" type="search" placeholder="Search the report…" aria-label="Search the report" autocomplete="off"><small id="qinfo" aria-live="polite">Enter = next match</small></div>
  <div class="tocnav">
{{TOC}}
  </div>
</nav>
<main id="content">
  <div class="hero">
    <h1>{{TITLE}}</h1>
    <div class="meta">Generated {{DATE}} from the repository's databases · AI-assisted review, nothing independently verified against source papers</div>
  </div>
  {{BANNER}}
  <div class="cards" role="list">{{CARDS}}</div>
  {{FIGURES}}
  <div class="guide">
    <a class="g1" href="#s-2a"><b>Findings</b><span>What the extracted records contain</span></a>
    <a class="g2" href="#s-2b"><b>Tentative interpretations</b><span>Readings that could be wrong</span></a>
    <a class="g3" href="#s-3"><b>Confidence &amp; limits</b><span>Incomplete screening, thin data, open classifications</span></a>
    <a class="g4" href="#s-4"><b>Next steps</b><span>What would help most, in order</span></a>
  </div>
  <div class="tools"><button id="expand">Expand all</button><button id="collapse">Collapse subsections</button><button onclick="window.print()">Print / save as PDF</button></div>
{{BODY}}
  <footer>Source: <code>06_outputs/PRELIMINARY_RESULTS_REPORT_2026-09-29.md</code> (generated by <code>code/analysis/build_preliminary_report.py</code>); this page by <code>code/analysis/build_report_html.py</code>. Regenerate both after any data change; <code>verify_repository.py</code> checks they are current.</footer>
</main>
</div>
<button id="top" aria-label="Back to top">↑ Top</button>
<script>
(function(){
var d=document,root=d.documentElement,$=function(s,c){return(c||d).querySelector(s)},$$=function(s,c){return Array.prototype.slice.call((c||d).querySelectorAll(s))};
function store(k,v){try{if(v===undefined)return localStorage.getItem(k);localStorage.setItem(k,v)}catch(e){return null}}
var t=store('lm-theme');if(t)root.setAttribute('data-theme',t);
$('#theme').onclick=function(){var dark=root.getAttribute('data-theme')==='dark'||(!root.getAttribute('data-theme')&&matchMedia('(prefers-color-scheme:dark)').matches);var n=dark?'light':'dark';root.setAttribute('data-theme',n);store('lm-theme',n)};
function menu(o){d.body.classList.toggle('menu-open',o);$('#menu').setAttribute('aria-expanded',o)}
$('#menu').onclick=function(){menu(!d.body.classList.contains('menu-open'))};$('#scrim').onclick=function(){menu(false)};
$$('.tocnav a').forEach(function(a){a.addEventListener('click',function(){menu(false)})});
d.addEventListener('keydown',function(e){if(e.key==='Escape')menu(false);if(e.key==='/'&&d.activeElement.tagName!=='INPUT'){e.preventDefault();$('#q').focus()}});
var subs=$$('details.sub');
$('#expand').onclick=function(){subs.forEach(function(x){x.open=true})};$('#collapse').onclick=function(){subs.forEach(function(x){x.open=false})};
function openFor(id){var el=id&&d.getElementById(id);if(!el)return;var p=el.closest('details.sub');if(p)p.open=true;if(el.tagName==='DETAILS')el.open=true}
addEventListener('hashchange',function(){openFor(location.hash.slice(1))});openFor(location.hash.slice(1));
window.addEventListener('beforeprint',function(){subs.forEach(function(x){x.open=true})});
var links={};$$('.tocnav a').forEach(function(a){links[a.dataset.target]=a});
var heads=$$('section.sec, details.sub');var cur=null;
function setActive(id){if(cur===id)return;cur=id;$$('.tocnav a.active').forEach(function(a){a.classList.remove('active')});var a=links[id];if(a){a.classList.add('active');var nav=$('#toc');var r=a.getBoundingClientRect(),n=nav.getBoundingClientRect();if(r.top<n.top+60||r.bottom>n.bottom-20)nav.scrollTop+=r.top-n.top-120}}
function spy(){var y=innerHeight*0.25,best=null;heads.forEach(function(h){var r=h.getBoundingClientRect();if(r.top<=y)best=h});if(best)setActive(best.id);else setActive(null)}
var tick=false;addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(function(){tick=false;spy();var h=d.documentElement;var p=h.scrollTop/(h.scrollHeight-h.clientHeight);$('#progress').style.width=(Math.max(0,Math.min(1,p))*100)+'%';$('#top').style.display=h.scrollTop>700?'block':'none'})}},{passive:true});spy();
$('#top').onclick=function(){scrollTo({top:0})};
var q=$('#q'),info=$('#qinfo'),hits=[],idx=-1;
function clear(){$$('mark').forEach(function(m){var p=m.parentNode;p.replaceChild(d.createTextNode(m.textContent),m);p.normalize()});hits=[];idx=-1}
function run(){clear();var v=q.value.trim();if(v.length<2){info.textContent='Enter = next match';return}
 var re=new RegExp(v.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'),'gi');var w=d.createTreeWalker($('#content'),NodeFilter.SHOW_TEXT,{acceptNode:function(n){var p=n.parentNode;return(p.closest('script,style,button')||!n.nodeValue.trim())?NodeFilter.FILTER_REJECT:NodeFilter.FILTER_ACCEPT}});
 var nodes=[];while(w.nextNode())nodes.push(w.currentNode);
 nodes.forEach(function(n){var s=n.nodeValue,m,last=0,f=null;re.lastIndex=0;while((m=re.exec(s))){if(!f)f=d.createDocumentFragment();f.appendChild(d.createTextNode(s.slice(last,m.index)));var k=d.createElement('mark');k.textContent=m[0];f.appendChild(k);last=m.index+m[0].length;if(m[0].length===0)re.lastIndex++}
  if(f){f.appendChild(d.createTextNode(s.slice(last)));n.parentNode.replaceChild(f,n)}});
 hits=$$('mark',$('#content'));hits.forEach(function(m){var p=m.closest('details.sub');if(p)p.open=true});
 info.textContent=hits.length?hits.length+' match'+(hits.length>1?'es':'')+' · Enter = next':'No matches';if(hits.length)go(0)}
function go(i){if(!hits.length)return;if(hits[idx])hits[idx].classList.remove('cur');idx=(i+hits.length)%hits.length;hits[idx].classList.add('cur');hits[idx].scrollIntoView({block:'center'});info.textContent=(idx+1)+' of '+hits.length+' · Enter = next'}
var to;q.addEventListener('input',function(){clearTimeout(to);to=setTimeout(run,180)});
q.addEventListener('keydown',function(e){if(e.key==='Enter'){e.preventDefault();if(!hits.length)run();else go(idx+(e.shiftKey?-1:1))}if(e.key==='Escape'){q.value='';clear();info.textContent='Enter = next match'}});
})();
</script>
</body>
</html>
'''

if __name__ == '__main__':
    OUT.write_text(build(), encoding='utf-8')
    print('wrote', OUT.relative_to(ROOT))
