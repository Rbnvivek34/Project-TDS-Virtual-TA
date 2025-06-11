import os
import openai
from model.retriever import retrieve_docs

# ✅ Load from Render environment
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_answer(question: str, image=None):
    context_docs = retrieve_docs(question)

    # If context_docs is list of strings:
    if isinstance(context_docs, list):
        context_text = "\n\n".join(context_docs)
    else:
        context_text = str(context_docs)

    prompt = f"""
You are a helpful Teaching Assistant. Use the context below to answer the student question clearly and concisely.

Context:
{context_text}

Question: {question}
Answer:
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    answer = response.choices[0].message["content"].strip()

    # Extract links from full context
    links = [{"url": url, "text": "Relevant context"} for url in extract_links(context_text)]
    return answer, links

def extract_links(text):
    import re
    if isinstance(text, list):
        text = "\n".join(text)
    return re.findall(r'(https?://[^\s]+)', text)
