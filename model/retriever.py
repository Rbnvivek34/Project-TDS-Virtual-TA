import json
from difflib import get_close_matches

def load_docs():
    with open("data/discourse_posts.json") as f:
        discourse = json.load(f)
    # Optionally add course content
    try:
        with open("data/course_content.json") as f:
            course = json.load(f)
    except FileNotFoundError:
        course = []
    return discourse + course

def retrieve_docs(query):
    docs = load_docs()
    matches = []
    for doc in docs:
        text = doc.get("raw", "") or doc.get("content", "")
        if any(word in text.lower() for word in query.lower().split()):
            matches.append(text)
    return "\n---\n".join(matches[:3])  # Return top 3 results
