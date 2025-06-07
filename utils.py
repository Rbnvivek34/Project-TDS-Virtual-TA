import pytesseract
from PIL import Image
import io
import base64
import openai
import os

from vector_store import search_documents

openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_text_from_base64_image(b64_string):
    image_data = base64.b64decode(b64_string)
    image = Image.open(io.BytesIO(image_data))
    return pytesseract.image_to_string(image)

def generate_answer_with_references(question, vector_index):
    relevant_docs = search_documents(question, vector_index)
    context = "\n\n".join([doc['text'] for doc in relevant_docs])

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a helpful TA for an IIT Madras course."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{question}"}
        ]
    )

    links = [{"url": doc["url"], "text": doc.get("summary", "See this post.")} for doc in relevant_docs]
    return response["choices"][0]["message"]["content"], links
