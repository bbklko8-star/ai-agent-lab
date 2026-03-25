
from fastapi import FastAPI
import google.generativeai as genai
import os
from dotenv import load_dotenv
# Load environment variables
load_dotenv()

app = FastAPI()

# Configure Gemini API
genai.configure(api_key=os.getenv("AIzaSyC2-CArnZdUhmgVMRJjsGH167ywSBhFyxE"))

# Use latest working model
model = genai.GenerativeModel("gemini-1.5-flash")

# Home route
@app.get("/")
def home():
    return {"message": "AI Exam Coach Running 🚀"}

# Ask route (REAL AI)
@app.get("/ask")
def ask(question: str):
    try:
        response = model.generate_content(
            question,
            generation_config={
                "max_output_tokens": 150
            }
        )

        answer = response.text if response.text else "No response from AI"

    except Exception as e:
        answer = f"Error: {str(e)}"

    return {
        "question": question,
        "answer": answer
    }
