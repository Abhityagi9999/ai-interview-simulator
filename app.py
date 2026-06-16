from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from evaluator import get_evaluator
from data import qa_data
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI(
    title="AI Interview Simulator API",
    description="Evaluates candidate answers using semantic intelligence and multi-dimensional scoring."
)

class EvaluationRequest(BaseModel):
    difficulty: str
    question_index: int
    user_answer: str

@app.post("/evaluate")
def evaluate_candidate_answer(req: EvaluationRequest):
    if req.difficulty not in qa_data:
        raise HTTPException(status_code=400, detail="Invalid difficulty level. Try 'easy', 'medium', 'hard', or 'advanced'.")
    
    questions = qa_data[req.difficulty]
    if req.question_index < 0 or req.question_index >= len(questions):
        raise HTTPException(status_code=400, detail="Invalid question index.")
    
    question_dict = questions[req.question_index]
    
    # Load evaluator and compute
    evaluator = get_evaluator()
    results = evaluator.evaluate_answer(req.user_answer, question_dict)
    
    return {
        "question": question_dict["question"],
        "user_answer": req.user_answer,
        "evaluation_results": results
    }

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/questions/{difficulty}")
def get_questions(difficulty: str):
    if difficulty not in qa_data:
        raise HTTPException(status_code=400, detail="Invalid difficulty level.")
    
    questions = qa_data[difficulty]
    return {"questions": [{"index": i, "question": q["question"]} for i, q in enumerate(questions)]}

@app.get("/")
def serve_ui():
    return FileResponse("static/index.html")

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
