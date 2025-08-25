from ai_engine.base import load_document, ask_question
from ai_engine.config import AI_PROVIDER
from dotenv import load_dotenv
pdfPath = r"\ai-integration\requirement_docs\HLBR_Adj_0001-ACT-113_HLBR_Adj_0001 Previous claims amount paid accumulation.pdf"

# Load .env BEFORE importing config
load_dotenv(dotenv_path=".env")

doc = load_document(pdfPath)  # change from .txt to .pdf
question = "What information is required from the user for submitting a health insurance claim?"

answer = ask_question(AI_PROVIDER, question, doc)
print(f"[{AI_PROVIDER.upper()} Response]\n", answer)
