import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load content from JSON files
def load_docs():
    base_path = "data"  # or "." if in root
    discourse_file = os.path.join(base_path, "discourse_posts.json")
    course_file = os.path.join(base_path, "course_content.json")

    with open(discourse_file, "r", encoding="utf-8") as f:
        discourse_data = json.load(f)
    with open(course_file, "r", encoding="utf-8") as f:
        course_data = json.load(f)

    return discourse_data + course_data  # Combine both

# Preload documents (avoid reloading every time)
ALL_DOCS = load_docs()
ALL_TEXTS = [doc["title"] + " " + doc["content"] for doc in ALL_DOCS]

# TF-IDF vectorizer
VECTORIZER = TfidfVectorizer(stop_words="english").fit(ALL_TEXTS)
DOC_EMBEDDINGS = VECTORIZER.transform(ALL_TEXTS)

def retrieve_docs(question: str, top_k=3):
    query_vec = VECTORIZER.transform([question])
    similarities = cosine_similarity(query_vec, DOC_EMBEDDINGS).flatten()
    top_indices = similarities.argsort()[-top_k:][::-1]

    results = []
    for i in top_indices:
        doc = ALL_DOCS[i]
        content = f"{doc.get('title', '')}\n{doc.get('content', '')}"
        if "url" in doc:
            content += f"\nLink: {doc['url']}"
        results.append(content)

    return results
