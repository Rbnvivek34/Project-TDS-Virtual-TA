import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_docs():
    base_path = "data"  # Update if your JSON files are elsewhere

    # Load course content documents
    with open(os.path.join(base_path, "course_content.json"), "r", encoding="utf-8") as f:
        course_data = json.load(f)
        course_docs = [
            {
                "title": item["title"],
                "content": item["content"],
                "url": None  # Course content has no direct URLs
            }
            for item in course_data
        ]

    # Load discourse posts documents
    with open(os.path.join(base_path, "discourse_posts.json"), "r", encoding="utf-8") as f:
        discourse_data = json.load(f)
        discourse_docs = [
            {
                "title": f"Discourse Topic {item['topic_id']}",
                "content": item["raw"],
                "url": item.get("url")
            }
            for item in discourse_data
        ]

    return course_docs + discourse_docs

# Pre-load docs and create TF-IDF embeddings once
ALL_DOCS = load_docs()
ALL_TEXTS = [doc["title"] + " " + doc["content"] for doc in ALL_DOCS]

VECTORIZER = TfidfVectorizer(stop_words="english").fit(ALL_TEXTS)
DOC_EMBEDDINGS = VECTORIZER.transform(ALL_TEXTS)

def retrieve_docs(question: str, top_k=3):
    query_vec = VECTORIZER.transform([question])
    similarities = cosine_similarity(query_vec, DOC_EMBEDDINGS).flatten()
    top_indices = similarities.argsort()[-top_k:][::-1]

    results = []
    for i in top_indices:
        doc = ALL_DOCS[i]
        content = f"{doc['title']}\n{doc['content']}"
        if doc.get("url"):
            content += f"\nLink: {doc['url']}"
        results.append(content)

    return results
