import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    LLM_MODEL_RESEARCHER = "llama-3.3-70b-versatile"
    LLM_MODEL_ANALYST = "llama-3.1-8b-instant"
    LLM_MODEL_WRITER = "llama-3.1-8b-instant"
    LLM_TEMPERATURE = 0.3
    MAX_ITERATIONS = 5
    VERBOSE = True
    API_HOST = "0.0.0.0"
    API_PORT = 8000

settings = Settings()