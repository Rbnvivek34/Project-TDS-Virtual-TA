import faiss
import pickle
import os
from openai.embeddings_utils import get_embedding

# Prebuilt from scraped data
INDEX_PATH = "vector.index"
DOCS_PATH = "docs.pkl"

def load_vector_index():
    if not os.path.exists(INDEX_PATH):
        raise FileNotFoundError("FAISS index not found. Please build it using scraped data.")
    index = faiss.read_index(INDEX_PATH)
    with open(DOCS_PATH, "rb") as f:
        docs = pickle.load(f)
    return {"index": index, "docs": docs}

def search_documents(query, store, top_k=3):
    embedding = get_embedding(query, engine="text-embedding-ada-002")
    D, I = store["index"].search([embedding], top_k)
    return [store["docs"][i] for i in I[0]]
