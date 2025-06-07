from fastapi import FastAPI, UploadFile, File, Request
from pydantic import BaseModel
from typing import List, Optional
import base64
from utils import extract_text_from_base64_image, generate_answer_with_references
from vector_store import load_vector_index

app = FastAPI()
index = load_vector_index()

class QuestionRequest(BaseModel):
    question: str
    image: Optional[str] = None

@app.post("/api/")
async def answer_question(payload: QuestionRequest):
    question = payload.question

    if payload.image:
        try:
            extracted_text = extract_text_from_base64_image(payload.image)
            question += f"\n\nImage Context:\n{extracted_text}"
        except Exception as e:
            return {"error": f"Image processing failed: {e}"}

    answer, links = generate_answer_with_references(question, index)

    return {
        "answer": answer,
        "links": links
    }
