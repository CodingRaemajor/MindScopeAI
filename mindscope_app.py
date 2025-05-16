import streamlit as st
from sentence_transformers import SentenceTransformer
from pymongo import MongoClient

# Load embedding model
model = SentenceTransformer("all-mpnet-base-v2", device = "cpu")

# MongoDB Atlas connection
connection_string = "mongodb+srv://iparth2166:dPhjugMr8WdfV8XK@cluster0.cglmv0e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string)
collection = client["mindscope"]["posts"]

st.set_page_config(page_title="MindScope AI", layout="centered")
st.title("🧠 MindScope AI")
st.markdown("""
Enter a mental health concern or feeling, and we'll find the most similar real Reddit posts using semantic search powered by MongoDB Atlas Vector Search.
""")

query_text = st.text_input("What are you feeling right now?")

if query_text:
    with st.spinner("Searching for similar posts..."):
        query_vector = model.encode(query_text).tolist()

        pipeline = [
            {
                "$vectorSearch": {
                    "index": "vector_index",
                    "path": "embedding",
                    "queryVector": query_vector,
                    "numCandidates": 100,
                    "limit": 5,
                    "similarity": "cosine"
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "body": 1,
                    "similarity": {"$meta": "vectorSearchScore"}
                }
            }
        ]

        results = list(collection.aggregate(pipeline))

    st.markdown("---")
    st.subheader("🔍 Top Matching Posts:")
    for i, res in enumerate(results, 1):
        st.markdown(f"**{i}.** ({res['similarity']:.2f})\n{res['body']}")