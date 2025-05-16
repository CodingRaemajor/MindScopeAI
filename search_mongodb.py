from pymongo import MongoClient
from sentence_transformers import SentenceTransformer
import pprint

#loading embedding model 
model = SentenceTransformer("all-mpnet-base-v2")

#MongoDB connection
connection_string = "mongodb+srv://iparth2166:dPhjugMr8WdfV8XK@cluster0.cglmv0e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string)
collection = client["mindscope"]["posts"]

#step 1: take user query
query_text = input("Enter your mental health concern:\n> ")

#step 2: generate embedding
query_vector = model.encode(query_text).tolist()

#step 3: MongoDB Vector Search
pipeline = [
    {
        "$vectorSearch": {
            "index": "vector_index",
            "path": "embedding",
            "queryVector": query_vector,
            "numCandidates": 100,
            "limit": 5,
            "similarity": "Cosine"
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

#step 4: Show results
print("\n Top Matching POsts:\n")
for i, res in enumerate(results, 1):
    print(f"{i}. ({res['similarity']:.4f}) {res['body']}\n")