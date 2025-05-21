import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np
from pymongo import MongoClient

st.set_page_config(page_title="MindScope AI", layout="centered")

st.title("🧠 MindScope AI")
st.markdown("Enter a mental health concern or feeling and we will find the most similar real Reddit posts using semantic search powered by MongoDB Atlas Vector Search.")


user_input = st.text_area("What are you feeling right now?", "")

st.markdown("Press Ctrl + Enter to submit your feelings.")

if user_input:
    # Load updated model(384-Dim)
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    embedding = model.encode(user_input).tolist()

    # Connect to MongoDB
    connection_string = "mongodb+srv://iparth2166:dPhjugMr8WdfV8XK@cluster0.cglmv0e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(connection_string)
    db = client["mindscope"]
    collection = db["posts"]

    # Vector search query
    pipeline = [
        {
            "$vectorSearch": {
                "index": "vector_index",
                "path": "embedding",
                "queryVector": embedding,
                "numCandidates": 100,
                "limit": 5
            }
        },
        {
            "$project": {
                "_id": 0,
                "text": 1,
                "score": {"$meta": "vectorSearchScore"}
            }
        }
    ]

    results = list(collection.aggregate(pipeline))

    st.markdown("### 🔍 Top Matching Posts:")
    for i, doc in enumerate(results, 1):
        score = float(doc.get('score', 0.0))
        text = doc.get('text') or doc.get('body', '') or "No content found."
        st.markdown(f"{i}. ({score:.4f}) {text}")