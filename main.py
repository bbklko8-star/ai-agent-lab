from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Exam Coach Running 🚀"}

@app.get("/ask")
def ask(question: str):
    
    # Simple AI logic (rule-based)
    if "ai" in question.lower():
        answer = "AI (Artificial Intelligence) is the simulation of human intelligence in machines."
    
    elif "python" in question.lower():
        answer = "Python is a popular programming language used in AI, web development, and automation."
    
    elif "network" in question.lower():
        answer = "A network connects multiple devices to share data and resources."
    
    else:
        answer = "Good question! I will answer this properly when we connect real AI."

    return {
        "question": question,
        "answer": answer
    }
