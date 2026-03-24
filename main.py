from fastapi import FastAPI
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

app = FastAPI()

# Secure API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

@app.get("/")
def home():
    return {"message": "AI Exam Coach Running 🚀"}

@app.get("/ask")
def ask(question: str):
    try:
        response = model.generate_content(
            question,
            generation_config={"max_output_tokens": 150}
        )

        answer = response.text if response.text else "No response"

    except Exception as e:
        answer = f"Error: {str(e)}"

    return {
        "question": question,
        "answer": answer
    }
