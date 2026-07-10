#  Multi-Agent Research Assistant

A production-ready AI-powered research assistant built using **CrewAI**, **FastAPI**, and **Google Gemini**. The system leverages multiple AI agents to perform web research, analyze information, and generate comprehensive research reports automatically.

---

##  Features

-  Multi-Agent Architecture using CrewAI
-  Automated Web Research
-  Research Analysis
-  Professional Report Generation
-  FastAPI REST API
-  Google Gemini Integration
- Markdown Research Reports
- Health Monitoring Endpoint
-  Modular & Scalable Project Structure

---

##  System Architecture

```
                User
                 │
                 ▼
          FastAPI Backend
                 │
                 ▼
          CrewAI Orchestrator
                 │
      ┌──────────┼──────────┐
      ▼          ▼          ▼
 Researcher   Analyst    Writer
    Agent      Agent      Agent
                 │
                 ▼
            Gemini LLM
                 │
                 ▼
      Final Research Report
```

---

##  Project Structure

```
Multi-Agent-Research-Assistant/

├── agents/
│   ├── researcher.py
│   ├── analyst.py
│   └── writer.py
│
├── api/
│   └── main.py
│
├── tasks/
│   └── research_tasks.py
│
├── tools/
│   └── web_search.py
│
├── test.py
├── requirements.txt
├── .env
└── README.md
```

---

##  Tech Stack

- Python
- FastAPI
- CrewAI
- Google Gemini
- Uvicorn
- Requests
- BeautifulSoup
- DuckDuckGo Search

---

# Installation

## Clone Repository

```bash
git clone https://github.com/shyamson118/Multi-Agent-Research-Assistant.git

cd Multi-Agent-Research-Assistant
```

## Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

# Running the Project

## Start FastAPI Server

```bash
uvicorn api.main:app --reload
```

Server

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Test the API

```bash
python test.py
```

Example Request

```json
{
    "topic": "Artificial Intelligence in Healthcare"
}
```

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Application Info |
| GET | /health | Health Check |
| GET | /agents | List Available Agents |
| POST | /research | Generate Research Report |

---

# Workflow

1. User submits a research topic.
2. Research Agent gathers information.
3. Analysis Agent evaluates findings.
4. Writer Agent generates the final report.
5. FastAPI returns the report as JSON.

---

# Future Enhancements

- Live Web Search
- PDF Report Export
- DOCX Export
- Retrieval-Augmented Generation (RAG)
- Authentication
- Conversation Memory
- Database Integration
- Frontend Dashboard

---

# License

MIT License

---

# Author

**Shyam Son**

GitHub: https://github.com/shyamson118