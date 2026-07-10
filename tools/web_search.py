from crewai.tools import tool
from duckduckgo_search import DDGS
from bs4 import BeautifulSoup
import requests


@tool("Web Search")
def web_search(query: str) -> str:
    """
    Search the web using DuckDuckGo.
    """
    try:
        results = []

        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=5):
                results.append(
                    f"""
Title : {r.get('title')}

URL : {r.get('href')}

Snippet :
{r.get('body')}

----------------------------------
"""
                )

        if not results:
            return "No search results found."

        return "\n".join(results)

    except Exception as e:
        return f"Search Error : {e}"


@tool("Web Scraper")
def web_scraper(url: str) -> str:
    """
    Scrape text content from a webpage.
    """
    try:

        headers = {
            "User-Agent":
            "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        for tag in soup([
            "script",
            "style",
            "header",
            "footer",
            "nav",
            "aside"
        ]):
            tag.decompose()

        text = soup.get_text(
            separator="\n",
            strip=True
        )

        return text[:5000]

    except Exception as e:
        return f"Scraping Error : {e}"