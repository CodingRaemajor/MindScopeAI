import json
from pymongo import MongoClient

# MongoDB atlas connection
connection_string = "mongodb+srv://iparth2166:dPhjugMr8WdfV8XK@cluster0.cglmv0e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string)
db = client["mindscope"]
collection = db["posts"]

# clear old data
collection.delete_many({})
print("Cleared previous documents in 'posts' collection.")

# Load embedded JSON
with open("embedded_mental_health_posts.json", "r", encoding="utf-8") as f:
    batch = []
    for i, line in enumerate(f, 1):
        batch.append(json.loads(line))
        if i % 1000 == 0:
            collection.insert_many(batch)
            print(f"Uploaded batch {i//1000}")
            batch = []
    if batch:
        collection.insert_many(batch)
        print("Uploaded final batch")

print("Upload to MongoDB complete.")