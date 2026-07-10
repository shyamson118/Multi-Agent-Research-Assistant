from crewai import Agent, LLM
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(
    model="gemini/gemini-flash-latest",
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.2,
)

def create_analyst_agent():
    return Agent(
        role="Research Analyst",

        goal="""
Analyze research findings, identify patterns,
evaluate credibility, and generate insights.
""",

        backstory="""
You are a senior data analyst.

Responsibilities:
- Analyze research results
- Compare multiple sources
- Identify trends
- Detect inconsistencies
- Assign confidence levels
- Produce actionable insights
""",

        llm=llm,

        verbose=True,

        allow_delegation=False,

        max_iter=4,
    )