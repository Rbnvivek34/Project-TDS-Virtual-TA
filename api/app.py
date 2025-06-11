from fastapi import FastAPI, Request
from pydantic import BaseModel
from model.responder import generate_answer
import uvicorn

app = FastAPI(title="TDS Virtual TA", description="Answer student questions using TDS course content and Discourse data.")

class QuestionInput(BaseModel):
    question: str
    image: str = None  # Optional base64 image if provided

@app.get("/")
def home():
    return {"message": "TDS Virtual TA is running. Use POST / to ask a question."}

@app.post("/")
async def answer_question(input_data: QuestionInput):
    question = input_data.question
    image = input_data.image

    answer, links = generate_answer(question, image)
    
    return {
        "answer": answer,
        "links": links
    }

# Optional: enable running locally
if __name__ == "__main__":
    uvicorn.run("api.app:app", host="0.0.0.0", port=8000, reload=True)
