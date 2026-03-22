from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Exam Coach Running 🚀"}

@app.get("/questions")
def get_questions():
    conn = sqlite3.connect("database/questions.db")
    cursor = conn.cursor()

    cursor.execute("SELECT question, option1, option2, option3, option4, answer FROM questions LIMIT 10")
    rows = cursor.fetchall()

    conn.close()

    result = []
    for row in rows:
        result.append({
            "question": row[0],
            "options": [row[1], row[2], row[3], row[4]],
            "answer": row[5]
        })

    return result
