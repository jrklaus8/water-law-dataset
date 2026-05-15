"""
Multi-agent research pipeline for the Legal Last Mile Research Assistant.

Architecture (inspired by Scott Cunningham's gradient-decay principle):
  - One focused Country Agent per detected jurisdiction — smaller context, higher fidelity
  - One Theory Agent that reads only the country summaries (not raw data)
  - One Synthesis Agent that produces the final answer from theory + country outputs

Keeping each agent's context narrow avoids the performance decay that comes from
stuffing all jurisdictions, all cases, and all analytical tasks into a single prompt.
"""

import anthropic

COUNTRY_AGENT_SYSTEM = """You are a specialist in {country} water law. Your only job is to analyse
the {country} portion of the Global Water Law Dataset (83,596 decisions, Brazil/Netherlands/Canada)
and answer the research question from a {country}-specific perspective.

Rules:
- Use only the statistics and cases provided. Do not invent cases or statistics.
- Be precise: quote numbers, categories, and outcome codes directly from the data.
- Flag any coding limitation (e.g., win_loss = not_coded for most cases).
- Write 150–250 words. Plain English. Active voice. No legalese.
- End with one sentence flagging the key limitation of the {country} data for this question."""

THEORY_AGENT_SYSTEM = """You are a Legal Last Mile theory specialist.

The Legal Last Mile theory (Claudio Klaus) holds that administrative law acts as a gatekeeper
between physical water infrastructure and enforceable legal entitlement. Even when pipes exist,
residents can be excluded by tariff disputes, connection refusals, lack of formal address, or
permit denials. The "Administrative Ghost" is the household physically close to infrastructure
but legally invisible to it.

You will receive short jurisdiction summaries produced by country specialists. Your job:
1. Identify where the Legal Last Mile theory is supported by the evidence.
2. Identify where the evidence does NOT fit the theory — note that honestly.
3. Highlight cross-jurisdictional contrasts that are theoretically significant.
4. Write 150–200 words. Do not repeat the country specialists' statistics — synthesise them.
5. Distinguish de lege lata (what the law does) from de lege ferenda (what it should do)."""

SYNTHESIS_AGENT_SYSTEM = """You are a senior legal researcher producing a final research response.

You will receive:
- Country-specific analyses from jurisdiction specialists
- A theory application note from a Legal Last Mile theory specialist

Your job: write a coherent, evidence-grounded answer to the original research question.

Rules:
1. Integrate the country analyses and theory note into one flowing response.
2. Do not repeat all the statistics — select the most important ones for the argument.
3. Structure: answer the question directly in the first sentence, then support it.
4. Acknowledge uncertainty and data limitations where the specialists flagged them.
5. 300–450 words. Plain English. Active voice. No legalese.
6. End with one research implication — what this finding suggests for future study or policy."""


def run_country_agent(
    client: anthropic.Anthropic,
    country: str,
    question: str,
    country_context: str,
) -> str:
    system = COUNTRY_AGENT_SYSTEM.format(country=country)
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=600,
        system=system,
        messages=[
            {
                "role": "user",
                "content": (
                    f"Research question: {question}\n\n"
                    f"{country} data:\n\n{country_context}"
                ),
            }
        ],
    )
    return response.content[0].text


def run_theory_agent(
    client: anthropic.Anthropic,
    question: str,
    country_summaries: dict[str, str],
) -> str:
    summaries_block = "\n\n".join(
        f"## {country} specialist:\n{text}"
        for country, text in country_summaries.items()
    )
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=500,
        system=THEORY_AGENT_SYSTEM,
        messages=[
            {
                "role": "user",
                "content": (
                    f"Research question: {question}\n\n"
                    f"Country specialist summaries:\n\n{summaries_block}"
                ),
            }
        ],
    )
    return response.content[0].text


def run_synthesis_agent(
    client: anthropic.Anthropic,
    question: str,
    country_summaries: dict[str, str],
    theory_note: str,
) -> str:
    summaries_block = "\n\n".join(
        f"### {country}:\n{text}" for country, text in country_summaries.items()
    )
    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=1200,
        system=SYNTHESIS_AGENT_SYSTEM,
        messages=[
            {
                "role": "user",
                "content": (
                    f"Research question: {question}\n\n"
                    f"Country analyses:\n\n{summaries_block}\n\n"
                    f"Theory application:\n\n{theory_note}"
                ),
            }
        ],
    )
    return response.content[0].text


def run_pipeline(
    client: anthropic.Anthropic,
    question: str,
    country_contexts: dict[str, str],
    progress_callback=None,
) -> dict:
    """
    Run the full multi-agent pipeline and return all intermediate outputs.

    progress_callback(step: str) — called before each agent fires so the UI
    can update a status indicator without blocking on the result.
    """
    countries = list(country_contexts.keys())

    # Stage 1: Country agents (one per jurisdiction)
    country_summaries = {}
    for country in countries:
        if progress_callback:
            progress_callback(f"Running {country} specialist agent…")
        country_summaries[country] = run_country_agent(
            client, country, question, country_contexts[country]
        )

    # Stage 2: Theory agent reads only the country summaries
    if progress_callback:
        progress_callback("Applying Legal Last Mile theory…")
    theory_note = run_theory_agent(client, question, country_summaries)

    # Stage 3: Synthesis agent produces the final answer
    if progress_callback:
        progress_callback("Synthesising final answer…")
    final_answer = run_synthesis_agent(client, question, country_summaries, theory_note)

    return {
        "country_summaries": country_summaries,
        "theory_note": theory_note,
        "final_answer": final_answer,
    }
