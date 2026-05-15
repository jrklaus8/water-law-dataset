import os
import pandas as pd
import streamlit as st
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

_env_path = os.getenv("DATASET_PATH")
DATASET_PATH = (
    Path(_env_path)
    if _env_path
    else Path(r"C:\Users\junio\OneDrive\Área de Trabalho\Legal Last Mile - Water Law Dataset\Dataset\water_law_global_coded.csv")
)

GOVERNANCE_LABELS = {
    "tariff_dispute": "Tariff Disputes",
    "connection_refusal": "Connection Refusal",
    "informal_settlement": "Informal Settlements",
    "flood_protection": "Flood Protection",
    "environmental_protection": "Environmental Protection",
    "sanitation_sewage": "Sanitation & Sewage",
    "riparian_waterway": "Riparian/Waterway",
    "water_infrastructure_contract": "Infrastructure Contracts",
    "fisheries_water": "Fisheries",
    "flooding": "Flooding",
    "regulatory_permit": "Regulatory Permits",
    "spatial_planning_water": "Spatial Planning",
    "hydroelectric_dam": "Hydroelectric Dams",
    "waterboard_governance": "Waterboard Governance",
    "water_quality": "Water Quality",
    "groundwater": "Groundwater",
    "water_theft_fraud": "Water Theft/Fraud",
    "irrigation_agricultural": "Irrigation/Agriculture",
    "pipe_leak_damage": "Pipe Leak Damage",
    "other_water": "Other Water",
    "not_water_related": "Not Water-Related",
}

COUNTRY_KEYWORDS = {
    "Brazil": ["brazil", "brasil", "brazilian", "stj", "tjsp", "tjrj", "tjmg", "tjrs", "tjpr"],
    "Netherlands": ["netherlands", "dutch", "holland", "dutch", "rechtbank", "raad van state", "afdeling"],
    "Canada": ["canada", "canadian", "ontario", "british columbia", "quebec", "alberta", "federal court"],
}


@st.cache_data(show_spinner=False)
def load_dataset():
    df = pd.read_csv(DATASET_PATH, low_memory=False)
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df["hr_language"] = pd.to_numeric(df["hr_language"], errors="coerce").fillna(0).astype(int)
    df["sust_language"] = pd.to_numeric(df["sust_language"], errors="coerce").fillna(0).astype(int)
    return df


@st.cache_data(show_spinner=False)
def compute_stats(df):
    stats = {}
    for country in ["Brazil", "Netherlands", "Canada"]:
        sub = df[df["country"] == country]
        total = len(sub)
        gov_counts = sub["governance_cat"].value_counts().to_dict()
        coded = sub[sub["win_loss"].isin(["user_wins", "utility_wins", "mixed", "unclear"])]
        user_wins = len(sub[sub["win_loss"] == "user_wins"])
        util_wins = len(sub[sub["win_loss"] == "utility_wins"])
        hr_count = int(sub["hr_language"].sum())
        year_min = int(sub["year"].min()) if not sub["year"].isna().all() else None
        year_max = int(sub["year"].max()) if not sub["year"].isna().all() else None
        stats[country] = {
            "total": total,
            "governance_counts": gov_counts,
            "coded_outcomes": len(coded),
            "user_wins": user_wins,
            "utility_wins": util_wins,
            "hr_language": hr_count,
            "year_range": (year_min, year_max),
        }
    return stats


def detect_country(question: str) -> list[str]:
    q = question.lower()
    detected = []
    for country, keywords in COUNTRY_KEYWORDS.items():
        if any(k in q for k in keywords):
            detected.append(country)
    return detected if detected else ["Brazil", "Netherlands", "Canada"]


def get_relevant_cases(df, question: str, countries: list[str], n: int = 12) -> pd.DataFrame:
    q = question.lower()
    sub = df[df["country"].isin(countries)].copy()

    # governance category keyword matching
    gov_matches = []
    for cat, label in GOVERNANCE_LABELS.items():
        if cat.replace("_", " ") in q or label.lower() in q:
            gov_matches.append(cat)

    if gov_matches:
        sub = sub[sub["governance_cat"].isin(gov_matches)]

    # keyword search in summary/title
    keywords = [w for w in q.split() if len(w) > 4 and w not in {
        "what", "which", "where", "there", "their", "about", "cases", "legal", "court", "water",
        "rights", "does", "have", "that", "with", "from", "this", "into", "been", "more",
    }]
    if keywords and len(sub) > n:
        mask = sub["summary"].fillna("").str.lower().apply(
            lambda s: any(k in s for k in keywords)
        ) | sub["title"].fillna("").str.lower().apply(
            lambda s: any(k in s for k in keywords)
        )
        filtered = sub[mask]
        if len(filtered) >= 3:
            sub = filtered

    # prefer cases with outcome coded
    coded = sub[sub["win_loss"].isin(["user_wins", "utility_wins", "mixed"])]
    not_coded = sub[~sub["win_loss"].isin(["user_wins", "utility_wins", "mixed"])]
    combined = pd.concat([coded, not_coded]).head(n)
    return combined


def build_country_context(df, question: str, country: str, stats: dict, n_cases: int = 8) -> str:
    """Build a focused context block for a single country — used by per-country agents."""
    s = stats[country]
    top_cats = sorted(s["governance_counts"].items(), key=lambda x: -x[1])[:8]
    top_str = "\n".join(
        f"  {GOVERNANCE_LABELS.get(k, k)}: {v} ({v/s['total']*100:.1f}%)"
        for k, v in top_cats
    )
    stats_block = (
        f"Total cases: {s['total']:,} ({s['year_range'][0]}–{s['year_range'][1]})\n"
        f"Outcome coding: user_wins={s['user_wins']}, utility_wins={s['utility_wins']}, "
        f"coded_total={s['coded_outcomes']} ({s['coded_outcomes']/s['total']*100:.1f}% coded)\n"
        f"HR-language cases: {s['hr_language']}\n\n"
        f"Governance categories:\n{top_str}"
    )

    cases = get_relevant_cases(df, question, [country], n=n_cases)
    case_lines = []
    for _, row in cases.iterrows():
        case_lines.append(
            f"[{row.get('year', '?')} | {GOVERNANCE_LABELS.get(row.get('governance_cat', ''), row.get('governance_cat', ''))} | "
            f"win_loss: {row.get('win_loss', 'not_coded')}] "
            f"{row.get('title', 'Untitled')}\n"
            f"  {str(row.get('summary', ''))[:250]}"
        )

    cases_block = "\n\n".join(case_lines) if case_lines else "No closely matching cases found."
    return f"Statistics:\n{stats_block}\n\nRepresentative cases:\n\n{cases_block}"


def build_country_contexts(df, question: str, stats: dict) -> dict[str, str]:
    """Return a per-country context dict for the multi-agent pipeline."""
    countries = detect_country(question)
    return {c: build_country_context(df, question, c, stats) for c in countries}


def build_context(df, question: str, stats: dict) -> str:
    """Legacy single-context builder — kept for the sidebar evidence expander."""
    countries = detect_country(question)
    cases = get_relevant_cases(df, question, countries)

    country_stats_block = []
    for c in countries:
        s = stats[c]
        top_cats = sorted(s["governance_counts"].items(), key=lambda x: -x[1])[:5]
        top_str = "; ".join(f"{GOVERNANCE_LABELS.get(k, k)}: {v}" for k, v in top_cats)
        country_stats_block.append(
            f"**{c}** — {s['total']:,} cases ({s['year_range'][0]}–{s['year_range'][1]})\n"
            f"  Top categories: {top_str}\n"
            f"  User wins: {s['user_wins']} | Utility wins: {s['utility_wins']} "
            f"| HR-language cases: {s['hr_language']}"
        )

    case_block = []
    for _, row in cases.iterrows():
        case_block.append(
            f"[{row['country']} | {row.get('year', '?')} | {GOVERNANCE_LABELS.get(row.get('governance_cat', ''), row.get('governance_cat', ''))}] "
            f"{row.get('title', 'Untitled')} — win_loss: {row.get('win_loss', 'not_coded')}\n"
            f"Summary: {str(row.get('summary', ''))[:300]}"
        )

    return "\n\n".join(country_stats_block) + "\n\n---\n\nRelevant cases:\n\n" + "\n\n".join(case_block)
