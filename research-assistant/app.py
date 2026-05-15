import os
from pathlib import Path
import streamlit as st
from dotenv import load_dotenv
import anthropic

load_dotenv(Path(__file__).parent / ".env")

from data_loader import (
    load_dataset,
    compute_stats,
    detect_country,
    build_country_contexts,
    get_case_links,
    get_year_trend,
    GOVERNANCE_LABELS,
)
from agents import run_pipeline
from charts import governance_chart, outcomes_chart, year_trend_chart, hr_chart
from export_memo import generate_html_memo

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

COMPARATIVE_KEYWORDS = {
    "compare", "vs", "versus", "difference", "differently", "contrast",
    "both countries", "all three", "across countries", "each country",
}
TREND_KEYWORDS = {
    "trend", "over time", "since", "changed", "change", "year", "history",
    "evolution", "grown", "increased", "decreased", "annual",
}


def _is_comparative(question: str) -> bool:
    q = question.lower()
    return any(k in q for k in COMPARATIVE_KEYWORDS) or len(detect_country(question)) >= 2


def _is_trend(question: str) -> bool:
    q = question.lower()
    return any(k in q for k in TREND_KEYWORDS)


def render_sidebar(stats: dict):
    st.sidebar.title("Dataset Overview")
    st.sidebar.markdown("**83,596 decisions · 3 countries · 1997–2026**")
    st.sidebar.markdown("---")
    for country, s in stats.items():
        with st.sidebar.expander(f"{country} ({s['total']:,} cases)"):
            top = sorted(s["governance_counts"].items(), key=lambda x: -x[1])[:6]
            for cat, n in top:
                pct = n / s["total"] * 100
                st.write(f"**{GOVERNANCE_LABELS.get(cat, cat)}**: {n:,} ({pct:.1f}%)")
            st.write(f"User wins: {s['user_wins']} | Utility wins: {s['utility_wins']}")
            st.write(f"HR-language: {s['hr_language']} cases")
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Pipeline**")
    st.sidebar.caption(
        "1. Country specialist agents\n"
        "2. Legal Last Mile theory agent\n"
        "3. Synthesis agent"
    )
    st.sidebar.markdown("---")
    st.sidebar.caption(
        "**AI Disclosure** — Claude (Anthropic) · Global Water Law Dataset "
        "(jrklaus8/water-law-dataset) · Not legal advice."
    )


def run_research(question: str, df, stats: dict):
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    country_contexts = build_country_contexts(df, question, stats)
    countries = list(country_contexts.keys())
    case_links = get_case_links(df, question, countries)

    with st.status("Running multi-agent pipeline…", expanded=True) as status:
        steps = []

        def progress(msg: str):
            steps.append(msg)
            status.update(label=steps[-1])

        result = run_pipeline(client, question, country_contexts, progress_callback=progress)
        status.update(label=f"Done — {len(countries)} jurisdiction(s) analysed", state="complete", expanded=False)

    return result, countries, country_contexts, case_links


def render_result(result: dict, countries: list, country_contexts: dict, case_links: list,
                  question: str, df, stats: dict):
    # Final answer
    st.markdown(result["final_answer"])

    # Case citations
    if case_links:
        st.markdown("---")
        st.markdown("**Key cases from dataset:**")
        for c in case_links:
            badge = f"`{c['country']}` `{c['year']}` `{c['category']}` `{c['win_loss']}`"
            if c["url"]:
                st.markdown(f"- [{c['title'][:90]}]({c['url']})  \n  {badge}")
            else:
                st.markdown(f"- {c['title'][:90]}  \n  {badge}")

    # Year-trend chart (inline when question is trend-related)
    if _is_trend(question):
        detected = detect_country(question)
        trend_df = get_year_trend(df, detected)
        if not trend_df.empty:
            st.markdown("---")
            st.plotly_chart(year_trend_chart(trend_df, detected), use_container_width=True)

    # Comparative side-by-side country analyses
    if _is_comparative(question) and len(countries) >= 2:
        st.markdown("---")
        st.markdown("**Jurisdiction analyses:**")
        cols = st.columns(len(countries))
        for col, country in zip(cols, countries):
            with col:
                st.markdown(f"**{country}**")
                st.caption(result["country_summaries"][country])

    # Export memo
    memo_html = generate_html_memo(question, result, case_links, countries)
    st.download_button(
        label="Download research memo (.html)",
        data=memo_html,
        file_name="legal_last_mile_memo.html",
        mime="text/html",
        use_container_width=False,
    )

    # Pipeline trace
    with st.expander("Full agent pipeline trace"):
        for country in countries:
            st.markdown(f"#### {country} specialist")
            st.markdown(result["country_summaries"][country])
        st.markdown("#### Legal Last Mile theory agent")
        st.markdown(result["theory_note"])
        st.markdown("---")
        st.markdown("**Raw data fed to country agents:**")
        for country, ctx in country_contexts.items():
            with st.expander(f"{country} data context"):
                st.text(ctx[:1500] + ("…" if len(ctx) > 1500 else ""))


def main():
    st.set_page_config(
        page_title="Legal Last Mile Research Assistant",
        page_icon="💧",
        layout="wide",
    )

    if not ANTHROPIC_API_KEY:
        st.error("ANTHROPIC_API_KEY not set. Add it to a .env file or set it as an environment variable.")
        st.stop()

    with st.spinner("Loading dataset (83,596 cases)…"):
        df = load_dataset()
        stats = compute_stats(df)

    render_sidebar(stats)

    st.title("💧 Legal Last Mile Research Assistant")
    st.markdown(
        "Natural-language research across **83,596 water law decisions** from "
        "Brazil, Netherlands, and Canada — analysed by a multi-agent pipeline."
    )
    st.info(
        "**AI Disclosure** — Uses Claude (Anthropic) to analyse the Global Water Law Dataset. "
        "Responses reflect dataset patterns. Not legal advice.",
        icon="ℹ️",
    )

    tab_research, tab_analytics = st.tabs(["Research", "Analytics"])

    # ── Research tab ────────────────────────────────────────────────────────
    with tab_research:
        st.markdown("**Try a question:**")
        examples = [
            "Why does Brazil have so many tariff disputes compared to the Netherlands?",
            "What happens to residents of informal settlements who seek water connections in Brazil?",
            "How do Dutch courts handle connection refusal cases differently from Brazilian courts?",
            "Does using human rights language in water disputes improve outcomes for users?",
            "What does the data reveal about the Legal Last Mile theory across all three countries?",
        ]
        cols = st.columns(len(examples))
        selected = None
        for col, ex in zip(cols, examples):
            if col.button(ex, use_container_width=True):
                selected = ex

        st.markdown("---")

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                if msg["role"] == "user":
                    st.markdown(msg["content"])
                else:
                    p = msg.get("pipeline")
                    if p:
                        render_result(
                            p["result"], p["countries"], p["country_contexts"],
                            p["case_links"], p["question"], df, stats,
                        )
                    else:
                        st.markdown(msg["content"])

        question = selected or st.chat_input("Ask a research question about water law…")

        if question:
            st.session_state.messages.append({"role": "user", "content": question})
            with st.chat_message("user"):
                st.markdown(question)

            with st.chat_message("assistant"):
                result, countries, country_contexts, case_links = run_research(question, df, stats)
                render_result(result, countries, country_contexts, case_links, question, df, stats)

            st.session_state.messages.append({
                "role": "assistant",
                "content": result["final_answer"],
                "pipeline": {
                    "result": result,
                    "countries": countries,
                    "country_contexts": country_contexts,
                    "case_links": case_links,
                    "question": question,
                },
            })

        if st.session_state.messages:
            if st.button("Clear conversation"):
                st.session_state.messages = []
                st.rerun()

    # ── Analytics tab ───────────────────────────────────────────────────────
    with tab_analytics:
        st.markdown("### Dataset Analytics — 83,596 cases · Brazil · Netherlands · Canada")

        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(governance_chart(stats), use_container_width=True)
            st.plotly_chart(hr_chart(stats), use_container_width=True)
        with col2:
            st.plotly_chart(outcomes_chart(stats), use_container_width=True)
            trend_df = get_year_trend(df, ["Brazil", "Netherlands", "Canada"])
            st.plotly_chart(year_trend_chart(trend_df, ["Brazil", "Netherlands", "Canada"]),
                            use_container_width=True)

        st.markdown("---")
        st.caption(
            "Data: Global Water Law Dataset · "
            "[github.com/jrklaus8/water-law-dataset](https://github.com/jrklaus8/water-law-dataset) · "
            "DOI [10.5281/zenodo.19836413](https://doi.org/10.5281/zenodo.19836413)"
        )


if __name__ == "__main__":
    main()
