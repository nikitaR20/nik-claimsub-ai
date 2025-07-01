import fitz  # PyMuPDF
import os

def load_document(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(path)
    elif ext == ".txt":
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        raise ValueError("Unsupported file type: " + ext)

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def ask_question(provider, question, doc=None):
    if provider == "openai":
        from .openai_engine import ask_openai
        return ask_openai(question, doc)
    elif provider == "gemini":
        from .gemini_engine import ask_gemini
        return ask_gemini(question, doc)
    else:
        raise ValueError("Unsupported provider")