import google.generativeai as genai
from config import *
# from Pycodes.Code_Doc_Agent.config import (
#     GEMINI_API_KEY,
#     MODEL_NAME
# )

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(MODEL_NAME)

SYSTEM_PROMPT = """
You are a senior software architect. Your task is to analyze the provided code and give structured summary report covering the following aspects:

1. Purpose
2. Main functionality
3. Important functions/classes
4. Dependencies
5. Execute the code and summarize the output.
6. Create key insights about purchase behavior based on the output.
7. Explain how this data helps businesses make informed decisions.

Return the response in plain text with .doc or .docx formatting. Make sure spacing, indents & all format is properly maintained. Use bullet points, headings, and subheadings where appropriate to enhance readability.
"""

def analyze_code(code_chunk):

    prompt = f"""
    {SYSTEM_PROMPT}

    CODE:
    {code_chunk}
    """

    response = model.generate_content(prompt)

    return response.text