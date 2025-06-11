import os
import openai
from model.retriever import retrieve_docs

openai.api_key = os.getenv("OPENAI_API_KEY")
def generate_answer(question: str, image=None):
    context_docs = retrieve_docs(question)

    prompt = f"""
You are a helpful Teaching Assistant. Use the context below to answer the student question clearly and concisely.

Context:
{context_docs}

Question: {question}
Answer:
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",  # or gpt-3.5-turbo-0125
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    answer = response.choices[0].message["content"].strip()

    # Extracting any links from context
    links = [{"url": url, "text": "Relevant context"} for url in extract_links(context_docs)]
    return answer, links

def extract_links(text):
    import re
    return re.findall(r'(https?://[^\s]+)', text)
