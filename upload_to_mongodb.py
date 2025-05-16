import json
from pymongo import MongoClient

# MongoDB connection string
connection_string = "mongodb+srv://iparth2166:dPhjugMr8WdfV8XK@cluster0.cglmv0e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB Atlas
client = MongoClient(connection_string)
db = client["mindscope"]
collection = db["posts"]

# Load your embedded dataset
with open("embedded_mental_health_posts.json", "r") as file:
    data = [json.loads(line) for line in file]

# ✅ Upload only the first 40,000 records
subset = data[:40000]

# Upload in batches to avoid overload
batch_size = 1000
for i in range(0, len(subset), batch_size):
    batch = subset[i:i + batch_size]
    collection.insert_many(batch)
    print(f"✅ Uploaded batch {i // batch_size + 1}")

print("🎉 Upload complete! You're under the 512MB limit.")