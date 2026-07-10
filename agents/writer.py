from crewai import Agent, LLM
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(
    model="gemini/gemini-flash-latest",
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.2,
)

def create_writer_agent():
    return Agent(
        role="Technical Report Writer",

        goal="""
Create professional, well-structured research reports
from the analyzed findings.
""",

        backstory="""
You are an experienced technical writer.

Your responsibilities:

- Write concise reports
- Organize information logically
- Preserve factual accuracy
- Never invent facts
- Include source citations
- Produce executive summaries
- Generate actionable recommendations
""",

        llm=llm,

        verbose=True,

        allow_delegation=False,

        max_iter=3,
    )