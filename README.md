# MultiResearch AI Agent

A Streamlit research assistant that searches the web with Tavily, reads a relevant source, drafts a structured report with Groq, and provides critic feedback.

## Run locally

```cmd
uv venv
.venv\Scripts\activate
uv pip install -r requirements.txt
python -m streamlit run app.py
```

Copy `.env.example` to `.env` and provide:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## Deploy on Streamlit Community Cloud

1. Push this repository to GitHub.
2. Open https://share.streamlit.io and select **Create app**.
3. Choose:
   - Repository: `Labheshm21/multiresearch-ai-agent`
   - Branch: `main`
   - Main file path: `app.py`
4. In **Advanced settings**, select Python 3.12 and add:

```toml
GROQ_API_KEY = "your_groq_api_key"
TAVILY_API_KEY = "your_tavily_api_key"
```

5. Click **Deploy**.

Never commit `.env` or `.streamlit/secrets.toml`.
