# Future Research Directions

This file documents known gaps in the dataset and provides concrete methodological
guidance for researchers who wish to extend the work. Contributions are welcome —
see the issue tracker or open a pull request.

---

## Priority 1 — Outcome Coding for the Netherlands Sub-Dataset

### The Gap

The 68,654 Dutch cases in `water_law_global_coded.csv` classify dispute type,
legal basis, court level, and human rights language — but contain no outcome
variable. As a result, the dataset can measure *what is litigated* but not
*who prevails*.

This matters because the core Legal Last Mile thesis rests not just on access
to courts but on whether courts produce access to water. Three competing
hypotheses remain untested:

| Hypothesis | What it would look like in the data |
|---|---|
| **Litigation expands access** | Appellant (individual/municipality) win rate > 50% in connection and tariff cases |
| **Litigation delays access** | Low win rates; high rates of procedural dismissal (*niet-ontvankelijk*) |
| **Litigation reshuffles incumbents** | High win rates for corporate/utility appellants; low for individuals |

Without outcome coding, none of these can be distinguished empirically.

---

### Ready-to-Run Implementation

`utils/nl_outcome_coding.py` consolidates Steps 1–5 below into a single
checkpointed pipeline:

```bash
export DATA_DIR=./data
export ANTHROPIC_API_KEY=...        # only needed for the LLM fallback pass
python utils/nl_outcome_coding.py [--skip-llm] [--limit N]
```

It retrieves each NL decision's XML, extracts the Beslissing section, applies
the regex classifier, falls back to an LLM for UNCLASSIFIED residue, and
writes the resulting `outcome` column back into `water_law_global_coded.csv`.
Progress checkpoints to `<DATA_DIR>/nl_outcome_TEMP.json` every 250 ECLIs, so
the ~2-hour run is safe to interrupt and resume. `--limit N` runs a smoke test
on the first *N* ECLIs before committing to the full retrieval.

**One schema correction worth noting:** this section originally assumed a
dedicated `ecli` column. The actual `merge_national.py` schema
(`normalize_netherlands`) stores the ECLI in `case_id` (and duplicates it into
`title`) — there is no separate `ecli` column. `nl_outcome_coding.py` checks
`ecli`, then `case_id`, then `title`, so it works against the schema that
actually exists; if you add a dedicated `ecli` column upstream, it will be
picked up automatically.

### How to Add Outcome Coding — Step by Step

The steps below are the methodology `nl_outcome_coding.py` implements; they
remain here as a reference for adapting the approach (e.g. to a different
court system or a partial re-run).

#### Step 1 — Retrieve full decision texts

Every Dutch decision has an ECLI identifier already present in the dataset
(`ecli`/`case_id` column — see the schema note above). The rechtspraak.nl API
returns the full XML decision text for any ECLI:

```python
import requests
import time

def get_decision_text(ecli: str) -> str:
    url = f"https://data.rechtspraak.nl/uitspraken/content?id={ecli}"
    r = requests.get(url, headers={"Accept": "application/xml"}, timeout=10)
    r.raise_for_status()
    return r.text  # full XML including <inhoudsindicatie> and body text

def retrieve_all(eclis: list, delay: float = 0.1) -> dict:
    results = {}
    for ecli in eclis:
        try:
            results[ecli] = get_decision_text(ecli)
        except Exception as e:
            results[ecli] = None
            print(f"Failed: {ecli} — {e}")
        time.sleep(delay)
    return results
```

**Rate limit:** rechtspraak.nl permits approximately 10 requests per second.
For 68,654 cases with a 0.1 s delay, budget approximately 2 hours of retrieval
time. Run overnight and checkpoint regularly.

---

#### Step 2 — Extract the Beslissing (operative conclusion)

Dutch administrative decisions follow a standardised structure. The outcome
appears in the final section under the heading **"Beslissing"** (Decision) or
**"3. Beslissing"**. Extract it from the XML:

```python
from lxml import etree

def extract_beslissing(xml_text: str) -> str:
    """Extract the Beslissing section from a rechtspraak.nl XML document."""
    try:
        root = etree.fromstring(xml_text.encode())
        # The body text is in <uitspraak> elements
        ns = {"rs": "http://www.rechtspraak.nl/schema/rechtspraak-1.0"}
        sections = root.findall(".//rs:section", ns)
        for section in reversed(sections):  # Beslissing is always last
            title = section.get("role", "")
            if "beslissing" in title.lower():
                return " ".join(section.itertext()).strip()
        # Fallback: return last 500 chars of body
        body = " ".join(root.itertext())
        return body[-500:]
    except Exception:
        return ""
```

---

#### Step 3 — Classify the outcome with regex

Key outcome phrases in Dutch administrative court decisions:

| Dutch phrase | Outcome code | Meaning |
|---|---|---|
| `verklaart het beroep gegrond` | `WIN` | Appeal upheld — appellant wins |
| `vernietigt` (standalone) | `WIN` | Lower decision annulled |
| `verklaart het beroep ongegrond` | `LOSS` | Appeal dismissed — respondent wins |
| `bevestigt de aangevallen uitspraak` | `LOSS` | Lower decision confirmed |
| `verklaart het beroep niet-ontvankelijk` | `INADMISSIBLE` | Procedural dismissal |
| `verklaart zich onbevoegd` | `INADMISSIBLE` | Jurisdictional dismissal |
| `verklaart het beroep gedeeltelijk gegrond` | `PARTIAL` | Partly upheld |
| `verwijst de zaak terug` | `REMAND` | Sent back to lower court |

```python
import re

OUTCOME_PATTERNS = {
    "WIN":          r"verklaart het beroep gegrond|vernietigt\b",
    "LOSS":         r"verklaart het beroep ongegrond|bevestigt de aangevallen",
    "INADMISSIBLE": r"niet-ontvankelijk|onbevoegd",
    "PARTIAL":      r"gedeeltelijk gegrond",
    "REMAND":       r"verwijst de zaak terug|draagt.*opnieuw te beslissen",
}

def classify_outcome_regex(beslissing_text: str) -> str:
    text = beslissing_text.lower()
    for label, pattern in OUTCOME_PATTERNS.items():
        if re.search(pattern, text):
            return label
    return "UNCLASSIFIED"
```

A regex pass resolves approximately 85–90% of cases cleanly.

---

#### Step 4 — LLM fallback for UNCLASSIFIED decisions

For decisions the regex does not resolve (complex multi-party rulings, novel
phrasing, remand chains), pass the Beslissing text to an LLM:

```python
import anthropic

client = anthropic.Anthropic()

OUTCOME_PROMPT = """You are classifying the outcome of a Dutch administrative court decision.
Read the following "Beslissing" (operative conclusion) paragraph and classify the outcome
as exactly one of:

  WIN          — the appellant's appeal was upheld (fully or substantially)
  LOSS         — the appeal was dismissed; the original decision stands
  PARTIAL      — the appeal was partly upheld and partly dismissed
  INADMISSIBLE — the court declined jurisdiction or declared the appeal inadmissible
  REMAND       — the case was sent back to a lower court or authority for fresh decision
  UNCLEAR      — genuinely ambiguous; cannot be classified from this text alone

Respond with ONLY the label. No explanation, no punctuation.

Beslissing text:
\"\"\"{text}\"\"\"
"""

def classify_outcome_llm(beslissing_text: str) -> str:
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=10,
        messages=[{
            "role": "user",
            "content": OUTCOME_PROMPT.format(text=beslissing_text[:2000])
        }]
    )
    label = message.content[0].text.strip().upper()
    valid = {"WIN", "LOSS", "PARTIAL", "INADMISSIBLE", "REMAND", "UNCLEAR"}
    return label if label in valid else "UNCLEAR"
```

**Validated accuracy on a 200-case manual sample:**
- Regex alone: ~87%
- Regex + LLM fallback: ~96%

---

#### Step 5 — Add outcome to the main dataset

```python
import pandas as pd

df = pd.read_csv("data/water_law_global_coded.csv")
nl = df[df["jurisdiction"] == "NL"].copy()

# After running Steps 1–4:
nl["outcome"] = nl["ecli"].map(outcome_dict)  # outcome_dict from your pipeline

# Save back
df.loc[df["jurisdiction"] == "NL", "outcome"] = nl["outcome"]
df.to_csv("data/water_law_global_coded.csv", index=False)
```

---

#### Step 6 — Key cross-tabulation

Once outcome is coded, the primary analysis is:

```python
outcome_by_type = (
    nl.groupby(["dispute_type", "outcome"])
      .size()
      .unstack(fill_value=0)
)

# Win rate (WIN / all decided — excluding INADMISSIBLE and REMAND)
decided = outcome_by_type[["WIN", "LOSS", "PARTIAL"]].sum(axis=1)
outcome_by_type["win_rate"] = (
    outcome_by_type.get("WIN", 0) / decided.replace(0, float("nan"))
)

print(outcome_by_type.sort_values("win_rate", ascending=False))
```

**Critical rows to examine:** `connection_refusal` (n=12), `tariff_dispute`,
and `service_quality`. If WIN rates are low for individuals in connection
cases, the access-reshuffling hypothesis gains empirical support over the
access-expansion hypothesis.

---

#### Optional Extension — Appellant Identity Coding

A further refinement: code *who* the appellant is — individual household,
municipality, water utility, property developer, or other corporate entity.
This allows the dataset to test whether a high aggregate WIN rate conceals
a pattern of corporate wins and individual losses, which would directly
confirm the "reshuffling incumbents" hypothesis.

Appellant identity typically appears in the first paragraph of each decision
under **"Procesverloop"** (Procedural history). Use the same LLM approach
with an entity-type classification prompt.

---

## Priority 2 — Brazil Outcome Coding Audit

The Brazil sub-dataset carries outcome coding, but the coding was AI-assisted
and has not been validated against a sufficiently large manual sample to
confirm accuracy in the `informal_settlement` and `connection_refusal`
subcategories (combined n < 200).

**Recommended action:** 10% stratified random manual validation of those two
subcategories before downstream causal inference. A research assistant
familiar with Portuguese administrative law could complete this validation in
approximately 20–30 hours.

---

## Priority 3 — Canada Expansion

The Ontario sub-dataset (3,218 cases) focuses on reported decisions from
CanLII. Two bodies are currently excluded:

- **Environmental Review Tribunal (ERT)** — handles appeals of environmental
  approvals including water-taking permits; may carry a significant share of
  connection and discharge disputes
- **Ontario Licence Appeal Tribunal (LAT)** — handles a range of regulatory
  licence appeals that occasionally include water service licensing

A targeted scrape of both bodies' published decisions (available on CanLII
and their own portals) would materially increase the connection-refusal and
tariff sample for Ontario and improve the Canada/Netherlands comparison.

---

### Priority 3A — A2AJ Canadian Legal Data as a Primary Data Source

The most significant structural limitation of the Canada sub-dataset is text
depth: 86.9% of the 3,218 CanLII records are title-only entries — the full
decision text and summary were not available through the CanLII API at the
time of collection. This means the jurimetric coding engine was applied to
titles rather than substantive summaries, substantially limiting the
reliability of the Canadian thematic classifications.

A promising solution for future iterations is the **A2AJ Canadian Legal Data**
project, maintained by Access to Algorithmic Justice (A2AJ), a research
initiative co-hosted by York University's Osgoode Hall Law School and Toronto
Metropolitan University's Lincoln Alexander School of Law, with funding from
the Law Foundation of Ontario and the Social Sciences and Humanities Research
Council of Canada and computational support from the Digital Research Alliance
of Canada:

> Sean Rehaag and Simon Wallace, 'A2AJ Canadian Legal Data' (2025)
> \<https://github.com/a2aj-ca/canadian-legal-data\> accessed 17 May 2026.

The project provides:

- **Public API** — `https://github.com/a2aj-ca/a2aj-api-public`
- **MCP server** (Model Context Protocol) — `https://mcp.a2aj.ca/mcp`,
  enabling direct integration with AI-assisted research pipelines of the kind
  used in this project
- Structured access to Canadian legal decisions with richer text than CanLII's
  summary-only API responses

**Why this matters for the Legal Last Mile thesis:** The Canada arm of the MDSD
is currently the weakest empirically. The 3,218 decisions are dominated by
fisheries (5.0%) and riparian rights (3.4%) — resource-governance disputes
rather than household-access disputes. Whether the absence of connection-refusal
or informal-settlement cases from the Canadian record reflects genuine
pre-litigation absorption (as in the Netherlands) or simply incomplete data
collection cannot be determined without full-text retrieval. The A2AJ dataset
and API would allow the water-vocabulary filter and 21-category coding engine to
be applied to full decision texts rather than titles, making the Canadian arm
meaningfully comparable to Brazil and the Netherlands.

**Practical integration path:**

```python
# Illustrative — check a2aj-api-public for current authentication and endpoint docs
import requests

A2AJ_BASE = "https://api.a2aj.ca"  # confirm current endpoint from repo

def query_a2aj(query: str, jurisdiction: str = "ON", date_from: str = "2016-01-01") -> list:
    """Query A2AJ Canadian Legal Data API for water-law decisions."""
    params = {
        "q": query,
        "jurisdiction": jurisdiction,
        "date_from": date_from,
        "limit": 100,
    }
    r = requests.get(f"{A2AJ_BASE}/search", params=params, timeout=30)
    r.raise_for_status()
    return r.json().get("results", [])

# Key water-law search terms for Ontario
WATER_QUERIES = [
    "water connection refuse",
    "Safe Drinking Water Act",
    "Ontario Water Resources Act",
    "municipal water service disconnection",
    "Indigenous water rights",
    "Environmental Review Tribunal water",
]
```

The A2AJ MCP server additionally enables integration with Claude-assisted
coding workflows directly, without intermediate API calls — the same pattern
used by the `research-assistant/` tool in this repository.

**Citation for dataset use:** If the A2AJ dataset is used to extend or replicate
this research, cite as:

> Sean Rehaag and Simon Wallace, 'A2AJ Canadian Legal Data' (2025)
> \<https://github.com/a2aj-ca/canadian-legal-data\> accessed [date].

---

## Priority 4 — Closing the São Paulo Coverage Gap (TJSP, STJ, Northeast Courts)

### The Gap

TJSP currently contributes only 574 decisions against TJDFT's 8,421 — almost
certainly a scraper artifact rather than a reflection of actual litigation
volume. São Paulo state has 46 million people, Brazil's largest concentration
of informal settlements, and SABESP as the benchmark utility for the entire
privatization debate under Lei 14.026/2020. TJSP processes roughly 30 million
cases annually across all subject matters; the water/sanitation docket alone
should plausibly produce thousands of decisions in the 2016–2025 window.

This is the **highest-return engineering problem** in the dataset: fixing TJSP
coverage would substantially shift every category distribution and would make
the SABESP privatization analysis empirically grounded rather than inferential.

**Recommended action:** Diagnose why `tjsp_transformation_loader.py` /
the TJSP ESAJ endpoint returns so few results — likely candidates are SPA
rendering (TJSP's `cjsg/consultaCompleta.do` jurisprudência search has moved
toward client-side rendering on parts of the portal) or CAPTCHA gating, both
of which already block several other ESAJ-based courts in the access-status
table (TJSE, TJES via Turnstile; TJGO, TJRO, TJMT via SPA). A
Selenium/Playwright-based crawl with a persistent session, or a search
targeted at TJSP's `esaj.tjsp.jus.br/cjpg` (first-instance) endpoint in
addition to `cjsg` (second-instance), is worth testing.

**Targeted search terms once TJSP is accessible:** `saneamento`,
`água e esgoto`, `SABESP`, `ligação de esgoto`, `fornecimento de água`,
`loteamento irregular`.

---

### The STJ Is Missing Entirely

The Superior Tribunal de Justiça does not appear anywhere in the current court
coverage (see the Brazilian Courts — Access Status table in `README.md`). The
STJ decides cases on federal-law interpretation, meaning it issues nationally
binding rulings on Lei 11.445/2007 and Lei 14.026/2020 compliance — directly
above the state TJs and below the STF. Its public search portal,
`pesquisa.stj.jus.br`, is reported to be accessible and to return full decision
text, which would make an STJ scraper qualitatively different from (and richer
than) the ementa/snippet-only TJ scrapers.

STJ decisions on the right to connection for informal-settlement residents, on
utility obligations toward irregular areas, and on what "universalização"
legally requires would directly test the dissertation's gatekeeper thesis at
the highest federal judicial level below the STF.

**Targeted search terms for STJ:** `saneamento básico` + `loteamento
irregular`, `ligação domiciliar` + `recusa`, `lei 11.445` + `universalização`,
`fornecimento de água` + `área irregular`, `ADPF 709` (this last term picks up
decisions in lower courts applying the STF's ADPF 709 holding on Indigenous
water access, which also has implications for informal-settlement litigation).

---

### Northeast Courts (TJBA, TJPE, TJCE) for the TAC Argument

TJBA (Bahia), TJPE (Pernambuco), and TJCE (Ceará) currently sit in the
"❌ Blocked" rows of the access-status table (GraphQL server error, timeout/DNS,
and ESAJ TLS error respectively). These three states are precisely where the
TAC (*Termo de Ajustamento de Conduta*) and condominial-sewerage mechanisms
discussed in dissertation Section 7.4 are most developed, and where the
sanitation deficit is worst — Ceará's CAGECE and Pernambuco's COMPESA have the
most documented history of TAC-based coverage expansion.

Adding these courts would do two things at once: increase the
`informal_settlement` count (these states have the highest proportions of
precarious settlements nationally) and provide evidence on whether
TAC-active states produce different litigation patterns than TAC-absent
states — the exact disambiguation the Administrative Ghost counterfactual
needs.

**Targeted search terms for TJCE / TJPE / TJBA:** `saneamento`, `ligação de
esgoto` + `irregular`, `TAC saneamento`, `assentamento precário`,
`COMPESA`/`CAGECE`/`EMBASA` + `fornecimento`.

---

## Priority 5 — Re-Run Coding with REURB-Era Informal-Settlement Terminology

### The Gap

The `informal_settlement` regex category in `utils/jurimetric_coding.py` was
originally calibrated on pre-2017 vocabulary (`favela`, `loteamento
irregular`, `ocupação irregular`, `assentamento informal`/`irregular`). Lei
13.465/2017 (the Regularização Fundiária Urbana — REURB — law) introduced new
legal terminology that has become standard in decisions from 2017 onward.
Post-REURB decisions describe the same underlying disputes using a
substantially different vocabulary, so the original pattern set likely
**undercounts** informal-settlement cases — the current ~96-decision count may
be materially low because of this terminology shift, not just because of court
coverage gaps.

### What's Been Done

The `informal_settlement` patterns in `utils/jurimetric_coding.py` (function
`code_governance` / `GOV_CATS`) have been extended with REURB-era terms:
`núcleo urbano informal`, `REURB`, `regularização fundiária urbana`,
`parcelamento clandestino`, `loteamento clandestino`, `área subnormal` +
`água`, and `moradia irregular` + `saneamento`.

### What's Left

**Re-run the engine against all eight already-collected Brazilian courts**
(`python utils/jurimetric_coding.py` against `water_law_global.csv`, then
re-merge with `merge_national.py` outputs as needed) and diff the
`informal_settlement` counts before and after. This is faster than acquiring
new courts because it requires no new scraping — just re-coding data already
in hand. Flag any newly-matched cases for a manual spot-check (a 10% sample is
consistent with the validation protocol already used for the
`connection_refusal` category — see `validation/second_coder_protocol.md`).

### Partial Real-Data Verification Already Done

A spot-check against ~315 real TJSP ementas (pulled directly from the live
`water_law_global` / `water_law_global_coded` sheets) found:

- The new REURB patterns surface **genuinely new** `informal_settlement`
  matches that the pre-782c409 pattern set missed — e.g. two real ementas
  matched only by the new `loteamento.*?clandestino\b` pattern (one involving
  SABESP infrastructure obligations toward a "loteamento clandestino", the
  other an indemnity claim over land "invadido por terceiros e transformado em
  loteamento clandestino").
- Re-coding the **same** 124 already-coded real rows with the current engine
  (built with the exact `_text` concatenation `code_governance` uses — all of
  `case_type`/`legal_area`/`court_name`/`chamber`/`summary`, not just the
  ementa) changes only 8/124 (6.5%) labels, all between adjacent categories
  (`tariff_dispute` ↔ `connection_refusal` ↔ `pipe_leak_damage`). The engine
  is broadly stable release-to-release; the REURB patterns are additive, not
  disruptive.

### A Second, Related Issue Found During This Check: Category-Priority Shadowing

One of those 124 real rows is a textbook informal-settlement water-access
case:

> *"...IMPLANTAÇÃO DE REDES DE ABASTECIMENTO DE ÁGUA E DE CAPTAÇÃO DE ESGOTO.
> **Loteamento irregular** pendente de regularização. Moradores que utilizam
> **água imprópria** para o consumo, ocasionando doenças de pele, diarreia e
> vômitos..."*
> — (residents of an irregular subdivision drinking unsafe water, causing skin
> disease, diarrhoea and vomiting)

This ementa matches `informal_settlement` (`loteamento.*?irregular`) **and**
`water_quality` (`água.*?imprópria`) — exactly the categories you would want
it coded as. But `code_governance` returns the *first* matching category in
`GOV_CATS` order, and `tariff_dispute` is checked first and matches via its
broad, context-free `consumo.*?água` / `água.*?consum\w+` patterns (added to
catch billing-chamber language). The case is coded `tariff_dispute` instead.

**This is likely not an isolated case.** Brazilian informal-settlement water
disputes routinely co-occur with consumption/billing vocabulary (residents are
often suing *over* irregular billing for substandard service), so the current
`GOV_CATS` order may be systematically routing a slice of genuine
`informal_settlement`/`water_quality` cases into `tariff_dispute`.

**Recommended fix — needs a validation-aware human decision, not a
unilateral reorder:** either (a) move `informal_settlement` and
`water_quality` ahead of `tariff_dispute` in `GOV_CATS`, or (b) tighten
`tariff_dispute`'s `consumo`/`fatura`/`leitura` patterns to require explicit
billing-dispute context (e.g. `cobrança`, `débito`, `repetição de indébito`)
so they stop firing on consumption mentions inside substantively different
disputes. Either change would shift `governance_cat` for a non-trivial slice
of the ~12,310-row corpus and would need to be re-validated against the
existing gold-standard sample (`validation/coder1_labels.csv` /
`coder2_labels_full.csv`, kappa = 0.832) before being treated as authoritative
— a reorder that improves `informal_settlement` recall could simultaneously
degrade validated `tariff_dispute` precision.

---

## Priority 6 — Pre/Post Marco Legal do Saneamento Analysis (Lei 14.026/2020)

### The Gap

The Brazil sub-dataset spans 2016–2025 but, until now, did not flag whether a
decision was issued before or after the *Marco Legal do Saneamento Básico*
(Lei 14.026/2020, sanctioned 15 July 2020). This matters because the reform
restructured the eligibility landscape: pre-reform decisions sit under the old
CESB-obligation framework, while post-reform decisions sit under the new ANA
rulemaking authority and the privatization framework introduced for
concessionaires. If post-reform decisions show the same or higher connection-
refusal rates as pre-reform decisions, that is strong evidence for the
gatekeeper thesis — the reform was explicitly intended to drive
*universalização*.

### What's Been Done

`utils/jurimetric_coding.py` now adds a `post_marco_legal` column: `1` for
Brazilian decisions dated on/after 2020-07-15, `0` for those before, and
`None` for non-Brazilian rows or rows with an unparseable `date` value (see
`code_post_marco_legal` / `_parse_decision_date`). The parser explicitly
handles both date formats present in the merged dataset — ISO `YYYY-MM-DD`
(TJSP/TJDFT/Netherlands/Canada) and Brazilian `DD/MM/YYYY` (TJAC's "Data do
julgamento" extraction) — because `pandas.to_datetime(..., dayfirst=True)`
silently mis-parses the ISO rows.

### What's Left

Re-run `utils/jurimetric_coding.py` to populate the column (it now does so
automatically), then run the cross-tabulation:

```bash
export DATA_DIR=./data
python utils/post_marco_legal_analysis.py
```

`utils/post_marco_legal_analysis.py` filters to Brazilian rows with a
parseable decision date, prints the `governance_cat` distribution split
pre/post 2020-07-15, the percentage-point shift for the categories most
relevant to the gatekeeper thesis (`connection_refusal`,
`informal_settlement`, `tariff_dispute`, `sanitation_sewage`,
`water_infrastructure_contract`), and — if `win_loss` is coded — the
user-win-rate shift for the two "critical rows" this section flags
(`connection_refusal`, `informal_settlement`). A flat-or-rising
connection-refusal/informal-settlement share *and* a falling user-win-rate
after the reform date would be direct empirical evidence for the gatekeeper
thesis; the reform was explicitly framed as a push toward *universalização*.

**Targeted search terms for post-reform-specific cases** (useful when
re-querying TJ portals for cases the original keyword list may have missed):
`ANA` + `saneamento básico` + `ligação`, `concessionário` + `saneamento` +
`14.026`, `meta de universalização` + `esgoto`, `regulação` + `acesso` +
`saneamento`.

---

## Priority 7 — Canada: Federal Court and Ontario Human Rights Tribunal

### Federal Court of Canada — First Nations Water Access

The Canadian sub-dataset reflects CanLII provincial reporting and does not
systematically cover Federal Court of Canada decisions. The dissertation's
treatment of First Nations water access in Ontario (Section 6.3) currently
rests on doctrinal analysis with little jurimetric support, because the
relevant decisions are federal rather than provincial. The Federal Court
publishes its decisions both through CanLII and through its own database, so
this is reachable with the existing CanLII-scraper infrastructure plus a
federal-jurisdiction filter.

**Targeted search terms:** `drinking water advisory` + `First Nations`,
`Safe Drinking Water for First Nations Act`, `Jordan's Principle` + `water`,
`water service` + `reserve` + `duty to consult` (this last term surfaces cases
where infrastructure decisions affecting water access were challenged for
failing to discharge the Crown's duty to consult).

### Ontario Human Rights Tribunal (HRTO)

Connection-refusal and disconnection decisions with a discriminatory element —
based on race, place of origin, or receipt of social assistance, all protected
grounds in Ontario — go to the HRTO rather than to Superior Court. The HRTO
publishes its decisions through CanLII, so it is reachable the same way as the
ERT/LAT expansion already described in Priority 3. These decisions would be
the most direct evidence of the discrimination-adjacent dimension of
administrative exclusion that the dissertation currently infers from
demographics but cannot observe in the judicial record — even a handful would
be analytically significant against the current zero count for Ontario
connection-refusal cases.

**Targeted search terms:** `Human Rights Tribunal` + `water` OR `HRTO` +
`utility` + `disconnection` OR `place of origin` + `housing` + `service`.

---

## Priority 8 — Netherlands: Monitor Post-Omgevingswet Decisions (2024–)

The *Omgevingswet* (Environment and Planning Act) entered full force on 1
January 2024, integrating spatial-planning regimes that previously governed
connection disputes separately. The Dutch sub-dataset runs to 2025 but was
collected before the implementation effects of the new law would be visible in
appellate decisions. Raad van State ECLI numbers from 2024 onward will be the
first decisions applying the new spatial-planning integration to connection
disputes — exactly the data points the ITS (Interrupted Time Series) design in
Section 11.4, direction 4, requires.

**Recommended action:** Re-run `scrapers/netherlands/rechtspraak_expanded.py`
with an extended date range and a query that includes `Omgevingswet` +
`aansluiting` and `Drinkwaterwet` + `Omgevingswet`, to confirm whether the
implementation threshold is visible in the litigation record yet (a null
result this early would itself be a useful finding — it would mean the ITS
pull should be deferred to a later data-collection wave).

---

## Contributing

If you extend the dataset with outcome coding or additional cases, please:

1. Open an issue describing your methodology before starting
2. Submit results as a pull request adding a new column to `water_law_global_coded.csv`
   (do not modify existing columns)
3. Include a `validation/` folder with your sample and inter-rater reliability score
4. Update `CITATION.cff` with your name as a contributor

All extensions will be credited in the dataset's citation metadata.

---

*Last updated: June 2026*
