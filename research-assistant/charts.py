import plotly.graph_objects as go
import pandas as pd
from data_loader import GOVERNANCE_LABELS

COUNTRY_COLORS = {
    "Brazil":      "#2563EB",
    "Netherlands": "#D97706",
    "Canada":      "#16A34A",
}

LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="sans-serif", size=12),
    margin=dict(l=10, r=10, t=40, b=10),
)


def governance_chart(stats: dict) -> go.Figure:
    """Horizontal grouped bar: top 8 governance categories across all countries."""
    all_cats = {}
    for s in stats.values():
        for cat, n in s["governance_counts"].items():
            all_cats[cat] = all_cats.get(cat, 0) + n
    top8 = [c for c, _ in sorted(all_cats.items(), key=lambda x: -x[1])
            if c not in ("other_water", "not_water_related")][:8]

    fig = go.Figure()
    countries = list(stats.keys())
    for country in countries:
        vals = [stats[country]["governance_counts"].get(c, 0) for c in top8]
        labels = [GOVERNANCE_LABELS.get(c, c) for c in top8]
        fig.add_trace(go.Bar(
            name=country,
            y=labels,
            x=vals,
            orientation="h",
            marker_color=COUNTRY_COLORS[country],
        ))

    fig.update_layout(
        **LAYOUT,
        title="Top Governance Categories by Country",
        barmode="group",
        height=380,
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
    )
    return fig


def outcomes_chart(stats: dict) -> go.Figure:
    """Stacked bar: user_wins / utility_wins / mixed / not_coded per country."""
    categories = ["user_wins", "utility_wins", "mixed", "not_coded"]
    colors = ["#16A34A", "#DC2626", "#D97706", "#9CA3AF"]
    labels = ["User wins", "Utility wins", "Mixed", "Not coded"]

    countries = list(stats.keys())
    fig = go.Figure()

    for cat, color, label in zip(categories, colors, labels):
        vals = []
        for country in countries:
            s = stats[country]
            if cat == "not_coded":
                coded = s["user_wins"] + s["utility_wins"] + s.get("mixed", 0)
                vals.append(s["total"] - coded)
            elif cat == "mixed":
                vals.append(s.get("coded_outcomes", 0) - s["user_wins"] - s["utility_wins"])
            else:
                vals.append(s[cat])
        fig.add_trace(go.Bar(name=label, x=countries, y=vals, marker_color=color))

    fig.update_layout(
        **LAYOUT,
        title="Case Outcomes by Country",
        barmode="stack",
        height=320,
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
    )
    return fig


def year_trend_chart(trend_df: pd.DataFrame, countries: list[str]) -> go.Figure:
    """Line chart: cases filed per year per country."""
    fig = go.Figure()
    for country in countries:
        if country in trend_df.columns:
            fig.add_trace(go.Scatter(
                x=trend_df.index,
                y=trend_df[country],
                mode="lines+markers",
                name=country,
                line=dict(color=COUNTRY_COLORS.get(country, "#6B7280"), width=2),
                marker=dict(size=4),
            ))
    fig.update_layout(
        **LAYOUT,
        title="Cases Filed per Year",
        height=300,
        xaxis_title="Year",
        yaxis_title="Cases",
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
    )
    return fig


def hr_chart(stats: dict) -> go.Figure:
    """Bar: human rights language usage count and rate per country."""
    countries = list(stats.keys())
    counts = [stats[c]["hr_language"] for c in countries]
    rates  = [stats[c]["hr_language"] / stats[c]["total"] * 100 for c in countries]
    colors = [COUNTRY_COLORS[c] for c in countries]

    fig = go.Figure(go.Bar(
        x=countries,
        y=rates,
        text=[f"{r:.2f}%" for r in rates],
        textposition="outside",
        marker_color=colors,
        customdata=counts,
        hovertemplate="%{x}: %{customdata} cases (%{y:.2f}%)<extra></extra>",
    ))
    fig.update_layout(
        **LAYOUT,
        title="Human Rights Language Usage",
        yaxis_title="% of cases",
        height=280,
    )
    return fig
