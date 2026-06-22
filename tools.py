from langchain_core.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv
load_dotenv()

tavily=TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query: str) -> str:
    """Search the web for recent, reliable information and return formatted results."""
    results = tavily.search(query=query, max_results=5)
    output = []

    for result in results.get("results", []):
        output.append(
            f"Title: {result.get('title', 'Untitled')}\n"
            f"URL: {result.get('url', '')}\n"
            f"Snippet: {result.get('content', '')[:500]}"
        )

    return "\n\n---\n\n".join(output)

@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"

if __name__ == "__main__":

    print(web_search.invoke("what are the recent news on middle east war?"))
