import json
from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END
from langchain_ollama import ChatOllama


# 1. Shared State

class AgentState(TypedDict):
    company: str
    raw_data: Optional[dict]
    analysis: str

# 2. Utilities

def normalize_name(name: str) -> str:
    return name.strip().lower().replace(" ", "")


def load_company_data(company: str):
    try:
        with open("data/dummy_company_data.json", "r") as f:
            data = json.load(f)

        normalized_input = normalize_name(company)

        for key, value in data.items():
            if normalize_name(key) == normalized_input:
                return value

        return None
    except FileNotFoundError:
        return None


# 3. Agent 1: Data Collector

def data_collector_agent(state: AgentState):
    return {
        "raw_data": load_company_data(state["company"])
    }

# 4. Agent 2: Analyst (FAST + SAFE)

llm = ChatOllama(
    model="llama3",
    temperature=0.2,   # lower = faster + less hallucination
)

def analyst_agent(state: AgentState):
    company = state["company"]
    raw_data = state["raw_data"]

    if raw_data:
        prompt = f"""
Create a company intelligence report in STRICT markdown format.

RULES:
- Use EXACT headings: ## Overview, ## Key Strengths, ## Key Risks
- Use "-" for bullets only, no arrows
- Each bullet must be on its OWN line
- Do NOT combine bullets into a single line
- No emojis, no disclaimers, no extra titles
- Do not invent financial numbers

Company: {company}

Structured Data:
{raw_data}

FORMAT EXAMPLE:

## Overview
- Bullet 1
- Bullet 2

## Key Strengths
- Bullet 1
- Bullet 2

## Key Risks
- Bullet 1
- Bullet 2
"""
    else:
        prompt = f"""
Create a company intelligence report for a real company in STRICT markdown format.

RULES:
- Use EXACT headings: ## Overview, ## Key Strengths, ## Key Risks
- Use "-" for bullets only, no arrows
- Each bullet must be on its OWN line
- No emojis, no disclaimers, no extra titles
- Do not invent financial numbers

Company: {company}

FORMAT EXAMPLE:

## Overview of {company}
- Bullet 1
- Bullet 2

## Key Strengths
- Bullet 1
- Bullet 2

## Key Risks
- Bullet 1
- Bullet 2
"""

    response = llm.invoke(prompt)

    return {
        "analysis": response.content.strip()
    }

# 5. LangGraph Workflow

workflow = StateGraph(AgentState)

workflow.add_node("data_collector", data_collector_agent)
workflow.add_node("analyst", analyst_agent)

workflow.set_entry_point("data_collector")
workflow.add_edge("data_collector", "analyst")
workflow.add_edge("analyst", END)

app = workflow.compile()
