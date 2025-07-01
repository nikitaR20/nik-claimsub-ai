import google.generativeai as genai
from .config import GEMINI_API_KEY

# Configure the Gemini client
genai.configure(api_key=GEMINI_API_KEY)

def ask_gemini(question, document=None):
    try:
        model = genai.GenerativeModel('gemini-2.5-pro')
        prompt = f"{document}\n\nQuestion: {question}" if document else question

        response = model.generate_content(prompt)

        return response.text.strip()
    
    except Exception as e:
        return f"❌ Gemini API Error: {str(e)}"
