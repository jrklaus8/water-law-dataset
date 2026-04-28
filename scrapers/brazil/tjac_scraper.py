"""
TJAC (Tribunal de Justiça do Acre) — ESAJ system.
Portal: https://esaj.tjac.jus.br/cjsg/consultaCompleta.do
Key insight: results are in <tr class="fundocinza1"> rows within 273KB response.
Metadata is in <div id="dadosSemFormatacao_ID"> divs (structured text with all fields).
"""
import os
import urllib.request, http.cookiejar, urllib.parse, re, json, time, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = 'https://esaj.tjac.jus.br/'
AJAX = BASE + 'cjsg/resultadoCompleta.do'
OUT = os.path.join(os.getenv('OUTPUT_DIR', '.'), 'tjac_cases_2016_2026.json')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept-Language': 'pt-BR,pt;q=0.9',
    'Referer': 'https://esaj.tjac.jus.br/cjsg/consultaCompleta.do',
    'Accept': 'text/html, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
}

def make_opener():
    cj = http.cookiejar.CookieJar()
    op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    req = urllib.request.Request(BASE + 'cjsg/consultaCompleta.do',
                                  headers={k:v for k,v in HEADERS.items() if k != 'X-Requested-With'})
    with op.open(req, timeout=20) as r:
        pass
    return op


def extract_cases(html, tag):
    cases = []
    seen = set()

    # Split on fundocinza rows (result rows) directly on full HTML
    rows = re.split(r'(?=<tr[^>]*class="[^"]*fundocinza[^"]*")', html, flags=re.IGNORECASE)

    for row in rows:
        if 'fundocinza' not in row.lower():
            continue
        m = re.search(r'(\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4})', row)
        if not m:
            continue
        num = m.group(1)
        if num in seen:
            continue
        seen.add(num)

        # The dadosSemFormatacao div contains structured text:
        # "(Relator (a): NAME; Comarca: NAME; Número do Processo: CNJ; Órgão julgador: NAME; Data do julgamento: DD/MM/YYYY; ...)"
        sem_m = re.search(r'class="mensagemSemFormatacao"\s*>(.*?)</div>', row, re.DOTALL | re.IGNORECASE)
        if sem_m:
            structured = re.sub(r'<[^>]+>', ' ', sem_m.group(1))
            structured = re.sub(r'&[a-zA-Z]+;', lambda x: {
                '&ccedil;': 'ç', '&atilde;': 'ã', '&otilde;': 'õ', '&oacute;': 'ó',
                '&aacute;': 'á', '&eacute;': 'é', '&iacute;': 'í', '&uacute;': 'ú',
                '&Ccedil;': 'Ç', '&Atilde;': 'Ã', '&Otilde;': 'Õ', '&Oacute;': 'Ó',
                '&Aacute;': 'Á', '&Eacute;': 'É', '&Iacute;': 'Í', '&Uacute;': 'Ú',
                '&nbsp;': ' ', '&amp;': '&', '&lt;': '<', '&gt;': '>',
            }.get(x.group(), x.group()), structured)
            structured = re.sub(r'\s+', ' ', structured).strip()
        else:
            clean = re.sub(r'<[^>]+>', ' ', row)
            structured = re.sub(r'\s+', ' ', clean).strip()

        # Extract fields from structured text
        relator_m = re.search(r'Relator[^:]*:\s*([^;]{3,60}?)(?:\s*;|\s*Comarca|\s*N[úu]mero)', structured, re.IGNORECASE)
        comarca_m = re.search(r'Comarca[^:]*:\s*([^;]{2,60}?)(?:\s*;|\s*N[úu]mero)', structured, re.IGNORECASE)
        camara_m = re.search(r'(?:Órgão julgador|Câmara)[^:]*:\s*([^;]{3,80}?)(?:\s*;|\s*Data)', structured, re.IGNORECASE)
        date_m = re.search(r'Data do julgamento[^:]*:\s*(\d{2}/\d{2}/\d{4})', structured, re.IGNORECASE)
        pub_dt_m = re.search(r'Data de registro[^:]*:\s*(\d{2}/\d{2}/\d{4})', structured, re.IGNORECASE)

        # Classe/Assunto from row HTML (separate span)
        classe_m = re.search(r'Classe/Assunto[^:]*:\s*</strong>\s*([^<]{3,80})', row, re.IGNORECASE)

        # Ementa: the large text block before the structured footer "(Relator..."
        ementa = ''
        paren_idx = structured.find('(Relator')
        if paren_idx > 80:
            ementa = structured[:paren_idx].strip()[:800]
        if not ementa:
            # Try anchor text
            for a_m in re.finditer(r'<a[^>]*>([^<]{60,})</a>', row):
                ementa = a_m.group(1).strip()[:800]
                break
        if not ementa:
            ementa = structured[:400]

        cases.append({
            'num': num,
            'processDate': date_m.group(1) if date_m else '',
            'publicDate': pub_dt_m.group(1) if pub_dt_m else '',
            'classe': classe_m.group(1).strip() if classe_m else '',
            'relator': relator_m.group(1).strip() if relator_m else '',
            'camara': camara_m.group(1).strip() if camara_m else '',
            'comarca': comarca_m.group(1).strip() if comarca_m else '',
            'ementa': ementa,
            'tag': tag,
            'court': 'TJAC',
            'state': 'AC',
        })
    return cases


def search_year(opener, year, query, max_pages=20):
    d1 = f'01/01/{year}'
    d2 = f'31/12/{year}'
    tag = f'{year}-ac'
    all_cases = []
    seen = set()

    # Page 1 — POST
    post_data = urllib.parse.urlencode([
        ('dados.buscaInteiroTeor', query),
        ('dados.dtJulgamentoInicio', d1),
        ('dados.dtJulgamentoFim', d2),
        ('dados.pesquisarComSinonimos', 'S'),
        ('dados.origensSelecionadas', 'T'),
        ('dados.origensSelecionadas', 'R'),
        ('tipoDecisaoSelecionados', 'A'),
        ('tipoDecisaoSelecionados', 'D'),
        ('pbEnviar', 'Pesquisar'),
    ]).encode('utf-8')

    req = urllib.request.Request(AJAX, data=post_data, headers=HEADERS)
    try:
        with opener.open(req, timeout=30) as r:
            html = r.read().decode('utf-8', errors='replace')
    except Exception as e:
        print(f'  Error page 1: {e}')
        return []

    # Count results: "Acórdãos(N)" or hidden input totalResultadoAba-A
    total_m = (re.search(r'Acórd[^(]*\((\d+)\)', html, re.IGNORECASE) or
               re.search(r'id="totalResultadoAba-A"[^>]*value="(\d+)"', html) or
               re.search(r'value="(\d+)"[^>]*/>\s*</li>', html))
    total = int(total_m.group(1)) if total_m else 0

    # Pagination: look for pagina=N or pg=N or paginacao links
    page_nums = [int(x) for x in re.findall(r'[?&]pagina=(\d+)', html)]
    if not page_nums:
        page_nums = [int(x) for x in re.findall(r'paginacaoSuperior.*?pagina.*?(\d+)', html, re.DOTALL)]
    total_pages = max(page_nums) if page_nums else max(1, (total + 19) // 20)
    print(f'  {year}: {total} results, ~{total_pages} pages')

    cases = extract_cases(html, tag)
    for c in cases:
        if c['num'] not in seen:
            seen.add(c['num'])
            all_cases.append(c)

    # Paginate — ESAJ uses GET with pagina=N
    pages_to_fetch = min(total_pages, max_pages)
    for pg in range(2, pages_to_fetch + 1):
        time.sleep(2)
        get_url = (AJAX + '?' +
                   urllib.parse.urlencode([
                       ('dados.buscaInteiroTeor', query),
                       ('dados.dtJulgamentoInicio', d1),
                       ('dados.dtJulgamentoFim', d2),
                       ('dados.pesquisarComSinonimos', 'S'),
                       ('dados.origensSelecionadas', 'T'),
                       ('dados.origensSelecionadas', 'R'),
                       ('tipoDecisaoSelecionados', 'A'),
                       ('tipoDecisaoSelecionados', 'D'),
                       ('paginaAnterior', str(pg - 1)),
                       ('pagina', str(pg)),
                   ]))
        req2 = urllib.request.Request(get_url, headers=HEADERS)
        try:
            with opener.open(req2, timeout=30) as r2:
                page_html = r2.read().decode('utf-8', errors='replace')
        except Exception as e:
            print(f'  Error page {pg}: {e}')
            break
        new = 0
        for c in extract_cases(page_html, tag):
            if c['num'] not in seen:
                seen.add(c['num'])
                all_cases.append(c)
                new += 1
        print(f'    Page {pg}: {new} new (total {len(all_cases)})')
        if new == 0:
            break
    return all_cases


def main():
    QUERY = 'água abastecimento fornecimento saneamento'
    print('Starting TJAC scraper...')
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
        print(f'  -> {new} new (total: {len(all_cases)})')
        with open(OUT, 'w', encoding='utf-8') as f:
            json.dump(all_cases, f, ensure_ascii=False, indent=2)
        time.sleep(5)

    print(f'\n=== DONE: {len(all_cases)} TJAC cases ===')


if __name__ == '__main__':
    main()
