from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from datetime import datetime
import uvicorn
import os
import traceback

from crewai import Crew, Process

from agents.researcher import create_researcher_agent
from agents.analyst import create_analyst_agent
from agents.writer import create_writer_agent
from tasks.research_tasks import create_research_tasks

load_dotenv()

app = FastAPI(
    title="CogniResearch AI",
    version="2.0.0",
    description="Multi-Agent Research Assistant using CrewAI + Gemini"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ResearchRequest(BaseModel):
    topic: str


@app.get("/")
def home():
    return {
        "application": "CogniResearch AI",
        "version": "2.0.0",
        "status": "Running",
        "timestamp": datetime.now().isoformat(),
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "google_api_key_loaded": bool(os.getenv("GOOGLE_API_KEY")),
    }


@app.get("/agents")
def agents():
    return {
        "agents": [
            {
                "name": "Senior Research Analyst",
                "role": "Research"
            },
            {
                "name": "Research Analyst",
                "role": "Analysis"
            },
            {
                "name": "Technical Report Writer",
                "role": "Writing"
            }
        ]
    }


@app.post("/research")
async def research(request: ResearchRequest):

    try:

        print("=" * 80)
        print("Starting CrewAI Research")
        print("Topic:", request.topic)
        print("=" * 80)

        researcher = create_researcher_agent()
        analyst = create_analyst_agent()
        writer = create_writer_agent()

        tasks = create_research_tasks(
            topic=request.topic,
            researcher=researcher,
            analyst=analyst,
            writer=writer,
        )

        crew = Crew(
            agents=[researcher, analyst, writer],
            tasks=tasks,
            process=Process.sequential,
            verbose=True,
        )

        print("Running Crew...")

        result = await crew.kickoff_async()

        print("Crew Finished Successfully")

        return {
            "status": "success",
            "topic": request.topic,
            "report": str(result),
            "generated_at": datetime.now().isoformat(),
        }

    except Exception as e:

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


if __name__ == "__main__":
    uvicorn.run(
        "api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )