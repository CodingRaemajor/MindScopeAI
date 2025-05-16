import streamlit as st
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer
import numpy as np

# Use secrets for connection string
connection_string = st.secrets["MONGODB_URI"]
client = MongoClient(connection_string)

# Connect to your collection
db = client["mindscope"]
collection = db["posts"]

# Load embedding model
model = SentenceTransformer("all-mpnet-base-v2")

# Streamlit UI
st.markdown("<h1 style='color:#f63366;'>🧠 MindScope AI</h1>", unsafe_allow_html=True)
st.write("Enter a mental health concern or feeling, and we'll find the most similar real Reddit posts using semantic search powered by MongoDB Atlas Vector Search.")

query = st.text_input("What are you feeling right now?", "")

if query:
    query_vector = model.encode(query).tolist()

    pipeline = [
        {
            "$vectorSearch": {
                "index": "vector_index",
                "path": "embedding",
                "queryVector": query_vector,
                "numCandidates": 100,
                "limit": 5
            }
        },
        {
            "$project": {
                "text": 1,
                "score": {"$meta": "vectorSearchScore"}
            }
        }
    ]

    results = list(collection.aggregate(pipeline))

    st.markdown("## 🔎 Top Matching Posts:")
    for i, doc in enumerate(results, 1):
        st.markdown(f"{i}. ({doc['score']:.4f}) {doc['text']}")