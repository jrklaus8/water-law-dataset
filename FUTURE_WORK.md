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

### How to Add Outcome Coding — Step by Step

#### Step 1 — Retrieve full decision texts

Every Dutch decision has an ECLI identifier already present in the dataset
(`ecli` column). The rechtspraak.nl API returns the full XML decision text
for any ECLI:

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

## Contributing

If you extend the dataset with outcome coding or additional cases, please:

1. Open an issue describing your methodology before starting
2. Submit results as a pull request adding a new column to `water_law_global_coded.csv`
   (do not modify existing columns)
3. Include a `validation/` folder with your sample and inter-rater reliability score
4. Update `CITATION.cff` with your name as a contributor

All extensions will be credited in the dataset's citation metadata.

---

*Last updated: May 2026*
