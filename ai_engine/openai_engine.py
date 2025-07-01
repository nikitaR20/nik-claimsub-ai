from openai import OpenAI
from .config import OPENAI_API_KEY

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=OPENAI_API_KEY)

def ask_openai(question, document=None):
    messages = [{"role": "user", "content": question}]
    
    if document:
        # Add the document as system context before the user question
        messages.insert(0, {"role": "system", "content": f"Use this document:\n{document}"})
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
    )
    
    # Return the assistant's reply text
    return response.choices[0].message.content
