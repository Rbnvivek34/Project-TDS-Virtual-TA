from fastapi import FastAPI, Request
from pydantic import BaseModel
from model.responder import generate_answer
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="TDS Virtual TA", description="Answer student questions using TDS course content and Discourse data.")

# ✅ Allow CORS from any domain (safe for this project)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to just the submission site
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
