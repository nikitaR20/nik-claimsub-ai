import os
from dotenv import load_dotenv

# Load .env file
load_dotenv(dotenv_path=".env")

# Get AI provider
AI_PROVIDER = os.getenv("AI_PROVIDER", "openai").strip().lower()
if AI_PROVIDER not in ["openai", "gemini"]:
    raise ValueError(f"Invalid AI_PROVIDER: {AI_PROVIDER}. Must be 'openai' or 'gemini'.")

# Load only the API key for the selected provider
if AI_PROVIDER == "openai":
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GEMINI_API_KEY = None
elif AI_PROVIDER == "gemini":
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    OPENAI_API_KEY = None
