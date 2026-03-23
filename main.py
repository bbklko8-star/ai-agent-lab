from fastapi import FastAPI
import google.generativeai as genai

app = FastAPI()

genai.configure(api_key="AIzaSyC2-CArnZdUhmgVMRJjsGH167ywSBhFyxE")

model = genai.GenerativeModel("gemini-pro")

@app.get("/")
def home():
    return {"message": "AI Exam Coach Running 🚀"}

@app.get("/ask")
def ask(question: str):
    response = model.generate_content(question)
    
    return {
        "question": question,
        "answer": response.text
    }