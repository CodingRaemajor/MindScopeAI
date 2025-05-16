import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np
from pymongo import MongoClient
import os

st.set_page_config(page_title="MindScope AI", layout="centered")

st.title("🧠 MindScope AI")
st.markdown("Enter a mental health concern or feeling, and we'll find the most similar real Reddit posts using semantic search powered by MongoDB Atlas Vector Search.")
user_input = st.text_input("What are you feeling right now?", "")

if user_input:
    model = SentenceTransformer("all-mpnet-base-v2")
    embedding = model.encode(user_input).tolist()

    connection_string = "mongodb+srv://iparth2166:dPhjugMr8WdfV8XK@cluster0.cglmv0e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(connection_string)
    db = client["mindscope"]
    collection = db["posts"]

    pipeline = [
        {
            "$vectorSearch": {
                "index": "vector_index",
                "path": "embedding",
                "queryVector": embedding,
                "numCandidates": 100,
                "limit": 5
            }
        }
    ]

    results = list(collection.aggregate(pipeline))

    st.markdown("### 🔍 Top Matching Posts:")
    for i, doc in enumerate(results, 1):
        score = float(doc.get('score', 0))
        text = doc.get('text', '')
        st.markdown(f"{i}. ({score:.4f}) {text}")