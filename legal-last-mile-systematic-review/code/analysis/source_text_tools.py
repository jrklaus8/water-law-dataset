"""Helpers for locating verbatim passages in the source PDFs. Used by build_swim_source_dossier.py and build_second_extractor_passages.py.

The PDFs themselves are never committed (copyright); these helpers read a directory of `<study_id>.pdf` files (poppler's `pdftotext` is required) and return text that is verbatim apart from three
mechanical clean-ups, stated wherever a quote is shown: ligature glyphs are expanded (ﬁ to fi), a hyphen at a line break inside a word is joined, and runs of whitespace become one space.
Page numbers are PDF page indexes (the first page of the file is page 1), which can differ from the page numbers printed in the journal.

Nothing here judges whether a passage supports a stored value: a passage is returned because it contains the stored numbers or terms, and says which ones. A person decides.
"""
import hashlib
import math
import re
import subprocess
from collections import Counter
from pathlib import Path

LIGATURES = {'\ufb00': 'ff', '\ufb01': 'fi', '\ufb02': 'fl', '\ufb03': 'ffi', '\ufb04': 'ffl', '\ufb05': 'st', '\ufb06': 'st', '\u00a0': ' ', '\u00ad': '', '\u2009': ' ', '\u200b': ''}
ABBREV = ('et al.', 'e.g.', 'i.e.', 'vs.', 'cf.', 'Fig.', 'Figs.', 'Eq.', 'No.', 'Nos.', 'approx.', 'pp.', 'p.', 'Dr.', 'Mr.', 'Ms.', 'Prof.', 'Inc.', 'Ltd.', 'Co.', 'viz.', 'ca.', 'resp.', 'St.', 'U.S.', 'U.K.')
STOP = set('about above after again against also among another around because before being below between both cannot could does doing during each either every from have having here however into more most much must only other over same should since some such than that their them then there these they this those through under until upon very were what when where which while whom with within without would your'.split())
WEAK_NUMBERS = {'0.05', '0.01', '0.001', '0.10', '0.1', '0.0', '0.00', '1.0', '1.00', '95', '99', '90', '100', '0.5', '5.0'}
HEAD = re.compile(r'^\s*(?:(?:\d+|[IVX]+)(?:\.\d+)*\.?\s+)?(abstract|introduction|background|literature(?: review)?|theor\w+(?: \w+)?|conceptual framework|data(?: and (?:methods?|methodology|sources?|variables?))?|methods?(?: and (?:data|materials))?|methodology|'
                  r'materials and methods|study (?:area|design|setting|sites?|context)|research (?:design|methods?|methodology)|empirical (?:strategy|approach|analysis|framework|specification|results|methodology)|econometric (?:approach|strategy|model|specification)|'
                  r'identification strategy|estimation (?:strategy|results)|results?(?: and discussion)?|findings|analysis|discussion|conclusions?(?: and (?:policy )?implications)?|robustness(?: checks)?|descriptive statistics|variables|sample|study population)\s*[:.]?\s*$', re.I)
TABLE_CAPTION = re.compile(r'^\s*(Table|TABLE)\s+([A-Z]?\d+[A-Za-z]?|[IVXL]+)\b')
METHOD_WORDS = re.compile(r'\b(defin|measur|variable|treatment|intervention|indicator|dummy|coded|code[sd]?|operationali[sz]|dependent|outcome|independent|explanatory|group|compar|control|sampl|survey|respondent|household|observation|N\s*=|n\s*=)', re.I)
SIGNIF_WORDS = re.compile(r'(signific|coefficient|odds|marginal|effect|percentage point|p\s*[<=>]|SE|standard error|confidence|ATT|IRR|increase|decrease|probabilit)', re.I)
DESIGN_WORDS = re.compile(r'(randomi[sz]|cluster|difference-in-difference|diff-in-diff|propensity|matching|regression|logit|probit|cross-sectional|panel|fixed effects|instrumental variable|quasi-experiment|case stud|interview|survey|multilevel|hierarchical|OLS|event history|hazard|qualitative|mixed method)', re.I)
RESULT_PAGE_HINT = re.compile(r'\b(result|finding|estimat|table)\w*', re.I)


def clean(text):
    for k, v in LIGATURES.items():
        text = text.replace(k, v)
    text = re.sub(r'(?<=[A-Za-z])-\s*\n\s*(?=[a-z])', '', text)
    return re.sub(r'\s+', ' ', text).strip()


def _ws(text):
    for k, v in LIGATURES.items():
        text = text.replace(k, v)
    return re.sub(r'\s+', ' ', text).strip()


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def _pdftotext(path, layout=False):
    cmd = ['pdftotext'] + (['-layout'] if layout else []) + [str(path), '-']
    out = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    pages = out.split('\f')
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    return pages


class Doc:
    """One source PDF: per-page raw and cleaned text, per-page layout lines (for table rows), section headings per page."""

    def __init__(self, path):
        self.path = Path(path)
        self.raw = _pdftotext(path)
        self.layout_raw = _pdftotext(path, layout=True)
        self.pages = [clean(p) for p in self.raw]
        self.n = len(self.pages)
        self.chars = sum(len(p) for p in self.pages)
        self.headings = [self._headings(p) for p in self.raw]
        self.sections = self._carry()

    @staticmethod
    def _headings(raw):
        out = []
        for line in raw.splitlines():
            s = line.strip()
            if 3 <= len(s) <= 70 and HEAD.match(s):
                out.append(re.sub(r'^\s*(?:\d+|[IVX]+)(?:\.\d+)*\.?\s+', '', s).strip(' :.').title())
        return out

    def _carry(self):
        """For each page: (section carried in from earlier pages, headings that appear on this page)."""
        cur, out = '', []
        for hs in self.headings:
            out.append((cur, hs))
            if hs:
                cur = hs[-1]
        return out

    def section_label(self, page):
        carried, here = self.sections[page - 1]
        parts = []
        if carried:
            parts.append(f'carried in: {carried}')
        if here:
            parts.append('headings on this page: ' + ', '.join(here))
        return '; '.join(parts) or 'no section heading detected'

    def tables_on(self, page):
        caps = []
        for line in self.layout_raw[page - 1].splitlines():
            m = TABLE_CAPTION.match(line)
            if m:
                caps.append(f'Table {m.group(2)}')
        return caps

    def caption_above(self, page, line_text):
        """Nearest table caption above a layout line on the same page (None when there is none)."""
        lines = self.layout_raw[page - 1].splitlines()
        want = clean(line_text)
        for i, line in enumerate(lines):
            if clean(line) == want:
                for j in range(i, -1, -1):
                    m = TABLE_CAPTION.match(lines[j])
                    if m:
                        return f'Table {m.group(2)}'
                return None
        return None

    def sentences(self, page):
        t = self.pages[page - 1]
        for a in ABBREV:
            t = t.replace(a, a.replace('.', '\u2024'))
        t = re.sub(r'(\d)\.(\d)', '\\1\u2024\\2', t)
        parts = re.split(r'(?<=[.!?])\s+(?=[A-Z0-9(\[\u2018\u201c"\'])', t)
        return [p.replace('\u2024', '.').strip() for p in parts if len(p.strip()) > 25]

    def layout_lines(self, page):
        return [clean(l) for l in self.layout_raw[page - 1].splitlines() if l.strip()]

    def contains(self, page, quote):
        """True when every segment of `quote` (split at the [...] cut marks) occurs on that PDF page, in the plain or the layout text. Used to prove that trimmed passages are still verbatim."""
        plain = self.pages[page - 1].lower()
        lay = clean(self.layout_raw[page - 1]).lower()
        lay_ws = _ws(self.layout_raw[page - 1]).lower()       # whitespace collapsed only, so a layout line that ends in a hyphen is still found
        for seg in re.split(r'\s*\[\.\.\.\]\s*', quote):
            seg = clean(seg).lower()
            if seg and seg not in plain and seg not in lay and seg not in lay_ws:
                return False
        return True

    def find(self, snippet):
        """Page numbers on which the cleaned snippet occurs (case-insensitive), used to validate curated quotes."""
        s = clean(snippet).lower()
        return [i + 1 for i, p in enumerate(self.pages) if s in p.lower()] + [i + 1 for i, p in enumerate(self.layout_raw) if s in clean(p).lower() and s not in self.pages[i].lower()]


def section_excerpt(doc, name_words, maxchars=1800, stop_words=()):
    """Text that follows the first real heading whose name contains one of `name_words` (for example ('method', 'data')), up to maxchars, crossing pages. Table-of-contents lines (dot leaders) are skipped.
    Returns (first_page, last_page, text) or None. Headings are found by the same rule as Doc.headings (a short line that is only a section name)."""
    want = tuple(w.lower() for w in name_words)
    for p in range(1, doc.n + 1):
        lines = doc.raw[p - 1].splitlines()
        for i, line in enumerate(lines):
            st = line.strip()
            if not (3 <= len(st) <= 70):
                continue
            m = HEAD.match(st)
            if not m or not any(w in m.group(1).lower() for w in want):
                continue
            body, page, last = [], p, p
            rest = lines[i + 1:]
            pages_iter = [rest] + [doc.raw[q - 1].splitlines() for q in range(p + 1, min(doc.n, p + 4) + 1)]
            for pi, chunk in enumerate(pages_iter):
                for ln in chunk:
                    st2 = ln.strip()
                    if stop_words and 3 <= len(st2) <= 70 and HEAD.match(st2) and any(w in HEAD.match(st2).group(1).lower() for w in stop_words):
                        text = clean(' '.join(body))
                        if len(text) >= 300:
                            return page, last, text[:maxchars]
                    body.append(ln)
                    last = p + pi
                    if len(clean(' '.join(body))) >= maxchars * 1.3:
                        break
                if len(clean(' '.join(body))) >= maxchars * 1.3:
                    break
            text = clean(' '.join(body))
            if len(text) >= 300 and text.count('. . .') + text.count('....') < 3:
                return page, last, text[:maxchars].rsplit(' ', 1)[0] + (' [...]' if len(text) > maxchars else '')
    return None


def table_captions(doc, limit=14):
    """(page, caption text) for lines that begin a table or figure caption."""
    out = []
    for p in range(1, doc.n + 1):
        for line in doc.layout_raw[p - 1].splitlines():
            if re.match(r'^\s*(Table|TABLE|Figure|FIGURE|Fig\.)\s+([A-Z]?\d+[A-Za-z]?|[IVXL]+)\b', line):
                cap = clean(line)
                if len(cap) > 25 and cap.count('....') == 0:
                    out.append((p, cap[:150]))
    seen, uniq = set(), []
    for p, c in out:
        if c[:40] not in seen:
            seen.add(c[:40])
            uniq.append((p, c))
    return uniq[:limit]


def aim_sentences(doc, limit=3):
    """Sentences, mostly from the first pages, in which the authors state their aim or question."""
    pat = re.compile(r'\b(this|the present|our)\s+(paper|study|article|research|work|review|chapter|thesis|analysis)\b.{0,60}\b(aim|examin|investigat|analy[sz]|evaluat|explor|assess|argue|seek|test|estimat|compar|map|document|describ|identif|review|understand)', re.I)
    out = []
    for p in range(1, min(doc.n, 6) + 1):
        for sent in doc.sentences(p):
            if pat.search(sent) and len(sent) < 600 and not _garbled(sent):
                out.append((p, sent))
    return out[:limit]


def abstract_excerpt(doc, maxchars=1800):
    """The abstract or summary when it can be found on the first two pages, else the start of page 1."""
    for p in (1, 2):
        if p > doc.n:
            break
        t = doc.pages[p - 1]
        m = re.search(r'\b(abstract|summary|resumen|resumo|r\u00e9sum\u00e9)\b[\s.:\u2014-]*', t, re.I)
        if m and len(t) - m.end() > 300:
            return p, t[m.end(): m.end() + maxchars].rsplit(' ', 1)[0] + (' [...]' if len(t) - m.end() > maxchars else '')
    return 1, doc.pages[0][:maxchars].rsplit(' ', 1)[0] + (' [...]' if len(doc.pages[0]) > maxchars else '')


def number_tokens(text, kind):
    """Numbers from a stored field, as they would be printed in a paper. kind 'estimate': decimals (and integers next to %, pp or 'percentage point'); kind 'n': integers of 30 or more that are not years."""
    toks = []
    text = text.replace('\u2212', '-')
    if kind == 'estimate':
        for m in re.finditer(r'(?<![\w.])(?<!\d,)-?\d{1,3}(?:,\d{3})+\.\d+|(?<![\w.])(?<!\d,)-?\d+\.\d+', text):
            t = m.group(0).lstrip('-').replace(',', '')
            if t not in WEAK_NUMBERS:
                toks.append(t)
        if len(set(toks)) < 2:
            for m in re.finditer(r'(?<![\w.])(\d{2,3})(?=\s*(?:%|pp\b|percentage point))', text):
                toks.append(m.group(1))
    else:
        for m in re.finditer(r'(?<![\w.])\d{1,3}(?:,\d{3})+(?![\d])|(?<![\w.,])\d{2,6}(?![\d,]*\.\d)', text):
            raw = m.group(0)
            v = int(raw.replace(',', ''))
            if v >= 30 and not (1900 <= v <= 2035 and ',' not in raw):
                toks.append(raw.replace(',', ''))
    seen = []
    for t in toks:
        if t not in seen:
            seen.append(t)
    return seen


def token_regex(tok):
    """Regex for a number as printed: 3283 also matches 3,283; the match must not sit inside a longer number."""
    variants = [re.escape(tok)]
    if '.' not in tok and len(tok) >= 4:
        variants.append(re.escape(f'{int(tok):,}'))
    if '.' in tok:
        ip, dp = tok.split('.', 1)
        if len(ip) >= 4:
            variants.append(re.escape(f'{int(ip):,}.{dp}'))     # 41810.91 as printed 41,810.91
        variants.append(re.escape(tok.replace('.', ',')))      # decimal comma (Portuguese, Spanish, French papers)
        if tok.startswith('0.'):
            variants.append(re.escape(tok[1:]))                 # .55 for 0.55, as printed in many tables
    return re.compile(r'(?<![\d.,])(?:' + '|'.join(variants) + r')(?![\d]|\.\d|,\d)')


def present(tokens, text):
    return [t for t in tokens if token_regex(t).search(text)]


def present_rounded(tokens, text):
    """Stored decimals that appear in the text only as a more precisely printed number that rounds to them (stored 0.14 or 19.21, printed 0.140 or 19.2078; a decimal comma counts)."""
    from decimal import Decimal, ROUND_HALF_UP
    printed = [m.replace(',', '.') for m in re.findall(r'(?<![\w.,])\d+[.,]\d{3,}(?!\d)', text)]
    out = []
    for t in tokens:
        if '.' not in t or token_regex(t).search(text):
            continue
        d = len(t.split('.')[1])
        q = Decimal(1).scaleb(-d)
        for n in printed:
            try:
                if len(n.split('.')[1]) > d and Decimal(n).quantize(q, rounding=ROUND_HALF_UP) == Decimal(t):
                    out.append(t)
                    break
            except Exception:
                continue
    return out


def content_terms(text, minlen=5):
    ws = re.findall(r"[A-Za-z\u00c0-\u00ff]{%d,}" % minlen, text.lower())
    return [w for w in dict.fromkeys(ws) if w not in STOP]


def term_weights(doc, terms):
    """Rarer terms in the paper weigh more (inverse document frequency within the paper)."""
    alltext = ' '.join(doc.pages).lower()
    return {t: 1.0 + 1.0 / (1.0 + math.log(1 + alltext.count(t))) for t in terms}


def trim(text, centre=None, width=650):
    if len(text) <= width:
        return text
    if centre is None:
        return text[:width].rstrip() + ' [...]'
    a = max(0, centre - width // 2)
    b = min(len(text), a + width)
    return ('[...] ' if a else '') + text[a:b].strip() + (' [...]' if b < len(text) else '')


def estimate_passages(doc, tokens, limit=3):
    """Table rows (layout lines) and sentences that contain stored estimate numbers, best first (most stored numbers, then pages that read as results)."""
    cands = []
    for p in range(1, doc.n + 1):
        for line in doc.layout_lines(p):
            hit, rnd = present(tokens, line), present_rounded(tokens, line)
            if (hit or rnd) and len(line) < 400:
                cands.append((len(hit) * 3 + len(rnd) * 1.5 + 1, p, 'table or layout line', line, hit + [t + ' (printed more precisely)' for t in rnd]))
        for sent in doc.sentences(p):
            hit, rnd = present(tokens, sent), present_rounded(tokens, sent)
            if (hit or rnd) and len(sent) <= 700:
                bonus = 1 if SIGNIF_WORDS.search(sent) else 0
                cands.append((len(hit) * 3 + len(rnd) * 1.5 + bonus, p, 'sentence', sent, hit + [t + ' (printed more precisely)' for t in rnd]))
    return _pick(cands, limit)


def n_passages(doc, tokens, limit=2):
    cands = []
    word = re.compile(r'\b(household|respondent|observation|village|municipalit|communit|participant|individual|cluster|school|countr|utilit|firm|sample|N\s*=|n\s*=|people|persons|cases|studies|colonias|states|counties|towns|districts|wards)', re.I)
    for p in range(1, doc.n + 1):
        for sent in doc.sentences(p):
            hit = present(tokens, sent)
            if hit and word.search(sent) and len(sent) <= 600:
                cands.append((len(hit) * 3 + (1 if p <= max(3, doc.n // 2) else 0), p, 'sentence', sent, hit))
    return _pick(cands, limit)


def term_passages(doc, terms, limit=2, need=2, first_share=0.75, extra=None):
    """Sentences, mostly from the first part of the paper (where methods sit), that share the most distinctive terms with a stored definition."""
    w = term_weights(doc, terms)
    cands = []
    last = max(3, int(doc.n * first_share))
    for p in range(1, min(doc.n, last) + 1):
        for sent in doc.sentences(p):
            low = sent.lower()
            hit = [t for t in terms if t in low]
            if len(hit) >= need:
                score = sum(w[t] for t in hit) + (1.5 if METHOD_WORDS.search(sent) else 0) + (1.0 if extra and extra.search(sent) else 0)
                cands.append((score, p, 'sentence', sent, hit))
    return _pick(cands, limit)


def design_passages(doc, limit=2):
    cands = []
    for p in range(1, min(doc.n, max(4, doc.n // 2)) + 1):
        for sent in doc.sentences(p):
            hits = DESIGN_WORDS.findall(sent)
            if hits and re.search(r'\b(we|this (study|paper|article)|our|I)\b|\b(estimate|use[sd]?|employ|adopt|conduct|collect)', sent, re.I):
                cands.append((len(set(h.lower() for h in hits)) + (1 if p <= 4 else 0), p, 'sentence', sent, sorted(set(h.lower() for h in hits))))
    return _pick(cands, limit)


def _garbled(text):
    """Equation or symbol-font debris (for example 'y it \u00bc a \u00fe b1 D:x'): characters that stand in for operators in math fonts (thorn, eth, vulgar fractions, private-use glyphs), or too few ordinary characters."""
    debris = sum(ch in '\u00fe\u00de\u00f0\u00d0\u00bc\u00bd\u00be' or 0xE000 <= ord(ch) <= 0xF8FF for ch in text)
    ok = sum(ch.isalnum() or ch in ' .,;:()[]%/-\'"\u201c\u201d\u2018\u2019\u2013\u2014+=<>*$#&' for ch in text)
    return debris >= 2 or ok / max(len(text), 1) < 0.93


def _pick(cands, limit):
    cands.sort(key=lambda c: (-c[0], c[1]))
    out, seen_text, pages = [], set(), Counter()
    for score, p, kind, text, hit in cands:
        if _garbled(text):
            continue
        key = text[:80]
        if key in seen_text or pages[p] >= 2:
            continue
        seen_text.add(key)
        pages[p] += 1
        out.append({'page': p, 'kind': kind, 'text': text, 'matched': hit, 'score': score})
        if len(out) >= limit:
            break
    return out


def identity_check(doc, citation):
    """Does the PDF look like the cited paper? Share of the citation's title words found on its first two pages, and whether the first author's surname is there."""
    m = re.search(r'\((\d{4})[a-z]?\)\.?\s*(.*)', citation)
    title = (m.group(2) if m else citation)
    title = re.split(r'\.\s+[A-Z][^.]{2,80}\s*\d', title)[0]
    words = [w for w in content_terms(title, 5)][:14]
    first = re.sub(r'\W', '', re.split(r'[ ,]', citation.strip())[0]).lower()
    head = ' '.join(doc.pages[:2]).lower()
    share = (sum(w in head for w in words) / len(words)) if words else 0.0
    return {'title_word_share': share, 'first_author_found': first in head, 'n_words': len(words)}
