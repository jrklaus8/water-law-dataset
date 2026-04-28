"""
TJSC (Tribunal de Justiça de Santa Catarina) water law case scraper.
Searches https://busca.tjsc.jus.br/jurisprudencia/ year-by-year 2016-2026.
"""
import os
import urllib.request, http.cookiejar, urllib.parse, re, json, time, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = 'https://busca.tjsc.jus.br/jurisprudencia/'
AJAX = BASE + 'buscaajax.do?categoria=acordaos'
OUT = os.path.join(os.getenv('OUTPUT_DIR', '.'), 'tjsc_cases_2016_2026.json')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'pt-BR,pt;q=0.9',
    'Referer': BASE,
    'Accept': 'text/html, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
}

def make_opener():
    cj = http.cookiejar.CookieJar()
    op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    # Load main page to get session cookies
    req = urllib.request.Request(BASE, headers={k: v for k, v in HEADERS.items() if k != 'X-Requested-With'})
    with op.open(req, timeout=20) as r:
        pass
    return op

def extract_cases(html, tag):
    """Extract case data from result HTML block."""
    cases = []
    seen = set()
    blocks = re.split(r'<div class="resultados">', html)
    for block in blocks[1:]:
        # Process number
        m_num = re.search(r"openLinkAcompanhamento\('[^']+','([0-9\-\.]+)'\)", block)
        if not m_num:
            continue
        num = m_num.group(1)
        if num in seen:
            continue
        seen.add(num)

        # Clean block for text extraction
        clean = re.sub(r'<[^>]+>', ' ', block)
        clean = re.sub(r'\s+', ' ', clean).strip()

        # Fields from HTML
        relator = (re.search(r'Relator:\s*([^\n<]+?)(?:\s*<|\s*Origem:)', block, re.IGNORECASE) or
                   re.search(r'Relator.*?</strong>\s*([^<\n]+)', block, re.IGNORECASE))
        relator = relator.group(1).strip() if relator else ''

        orgao = re.search(r'Org[^:]+:\s*</strong>\s*([^<\n]+)', block, re.IGNORECASE)
        orgao = orgao.group(1).strip() if orgao else ''

        julgado = re.search(r'Julgado em:\s*</strong>\s*(\d{2}/\d{2}/\d{4})', block, re.IGNORECASE)
        julgado = julgado.group(1).strip() if julgado else ''

        classe = re.search(r'Classe:\s*</strong>\s*([^<\n]+)', block, re.IGNORECASE)
        classe = classe.group(1).strip() if classe else ''

        # Ementa from textarea (most complete)
        ementa = re.search(r'<textarea[^>]*>([^<]{10,})</textarea>', block, re.DOTALL | re.IGNORECASE)
        if ementa:
            em_text = ementa.group(1).strip()[:800]
        else:
            # Fall back to plain text excerpt
            em_text = clean[:500]

        # Relator from plain text fallback
        if not relator:
            m_r = re.search(r'Relator:\s+([A-ZÀ-Ü][a-zà-ü\s]+?)(?=\s+Origem:|\s+Org)', clean)
            relator = m_r.group(1).strip() if m_r else ''

        # Orgão from plain text fallback
        if not orgao:
            m_o = re.search(r'Org[ã|a]o Julgador:\s+([^\n]+?)(?=\s+Julgado|\s+Classe)', clean)
            orgao = m_o.group(1).strip() if m_o else ''

        cases.append({
            'num': num,
            'processDate': julgado,
            'publicDate': '',
            'classe': classe,
            'relator': relator,
            'camara': orgao,
            'comarca': '',
            'ementa': em_text,
            'tag': tag,
            'court': 'TJSC',
            'state': 'SC',
        })
    return cases

def search_year(opener, year, query_frase, max_pages=20):
    """Search for all cases in a given year."""
    d1 = f'01/01/{year}'
    d2 = f'31/12/{year}'
    tag = f'{year}-sc'
    all_cases = []
    seen = set()

    # Page 1: POST
    post_data = urllib.parse.urlencode([
        ('q', ''), ('frase', query_frase), ('qualquer', ''), ('excluir', ''),
        ('prox1', ''), ('prox2', ''), ('proxc', ''),
        ('busca', 'avancada'), ('radio_campo', 'ementa'),
        ('datainicial', d1), ('datafinal', d2),
        ('resultado', '2'),
    ]).encode('utf-8')

    req = urllib.request.Request(AJAX, data=post_data, headers=HEADERS)
    try:
        with opener.open(req, timeout=30) as r:
            html = r.read().decode('iso-8859-1')
    except Exception as e:
        print(f'  Error page 1: {e}')
        return []

    # Get total pages from pagination
    # Count may use '.' as thousands sep: "<b>2.251</b> resultados"
    total_m = re.search(r'<b>([\d\.]+)</b>\s*resultados', html)
    total = int(total_m.group(1).replace('.', '')) if total_m else 0
    # "Página X de Y" — á becomes replacement char \ufffd when Latin-1 decoded as UTF-8
    pages_m = re.search(r'P.gina\s+\d+\s+de\s+(\d+)', html)
    total_pages = int(pages_m.group(1)) if pages_m else 1
    print(f'  {year}: {total} results, {total_pages} pages')

    # Extract page 1
    m = re.search(r'###inicio_resultado###(.+?)###fim_resultado###', html, re.DOTALL)
    if m:
        cases = extract_cases(m.group(1), tag)
        for c in cases:
            if c['num'] not in seen:
                seen.add(c['num'])
                all_cases.append(c)

    # Pages 2..N via GET (pagination links use GET format)
    pages_to_fetch = min(total_pages, max_pages)
    for pg in range(2, pages_to_fetch + 1):
        time.sleep(2)  # polite delay
        get_params = urllib.parse.urlencode([
            ('q', ''), ('only_ementa', ''), ('frase', query_frase), ('excluir', ''),
            ('qualquer', ''), ('prox1', ''), ('prox2', ''), ('proxc', ''),
            ('sort', 'dtJulgamento desc'), ('ps', '20'),
            ('busca', 'avancada'), ('pg', str(pg)),
            ('categoria', 'acordaos'), ('flapto', '1'),
            ('datainicial', d1), ('datafinal', d2),
            ('radio_campo', 'ementa'),
        ])
        url = BASE + 'buscaajax.do?' + get_params
        req = urllib.request.Request(url, headers=HEADERS)
        try:
            with opener.open(req, timeout=30) as r:
                page_html = r.read().decode('iso-8859-1')
        except Exception as e:
            print(f'  Error page {pg}: {e}')
            break

        m2 = re.search(r'###inicio_resultado###(.+?)###fim_resultado###', page_html, re.DOTALL)
        if m2:
            cases = extract_cases(m2.group(1), tag)
            new = 0
            for c in cases:
                if c['num'] not in seen:
                    seen.add(c['num'])
                    all_cases.append(c)
                    new += 1
            print(f'    Page {pg}: {new} new cases (total {len(all_cases)})')
        else:
            print(f'    Page {pg}: no result section found')

        if len(all_cases) >= total:
            break

    return all_cases


def main():
    # Main water law query for TJSC using frase (exact phrase match in ementa)
    # CASAN = Companhia Catarinense de Águas e Saneamento (SC state water utility)
    QUERY = 'CASAN'

    print('Starting TJSC scraper...')
    print(f'Query (frase/ementa): {QUERY}')

    opener = make_opener()
    all_cases = []
    seen_global = set()

    for year in range(2016, 2027):
        print(f'\nYear {year}:')
        try:
            cases = search_year(opener, year, QUERY)
        except Exception as e:
            print(f'  FAILED: {e}')
            cases = []

        new = 0
        for c in cases:
            if c['num'] not in seen_global:
                seen_global.add(c['num'])
                all_cases.append(c)
                new += 1
        print(f'  -> {new} unique new cases added (total: {len(all_cases)})')

        # Save incrementally after each year
        with open(OUT, 'w', encoding='utf-8') as f:
            json.dump(all_cases, f, ensure_ascii=False, indent=2)

        time.sleep(5)  # pause between years

    print(f'\n=== DONE: {len(all_cases)} total unique TJSC cases ===')
    print(f'Saved to: {OUT}')

if __name__ == '__main__':
    main()
