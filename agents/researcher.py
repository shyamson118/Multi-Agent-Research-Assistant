from crewai import Agent, LLM
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(
    model="gemini/gemini-flash-latest",
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.2,
)


def create_researcher_agent():
    return Agent(
        role="Senior Research Analyst",

        goal="""
Research a topic and provide accurate, factual information.
""",

        backstory="""
You are an experienced research analyst who produces
clear, concise, factual research reports.
Always cite sources when available.
""",

        llm=llm,

        # Disable tools temporarily
        tools=[],

        verbose=True,

        allow_delegation=False,

        max_iter=2,

        max_execution_time=120,
    )