import pandas as pd
from sentence_transformers import SentenceTransformer

# Load labeled dataset
df = pd.read_csv("labeled_mental_health_posts.csv")

# Load model (auto-detect GPU)
model = SentenceTransformer("all-mpnet-base-v2", device="cuda")

# Generate embeddings in batch
print("🔄 Generating embeddings in batch mode using GPU...")
embeddings = model.encode(
    df['body'].tolist(),
    batch_size=32,                # ✅ Safer for 6GB GPU
    show_progress_bar=True,
    convert_to_numpy=True
)

# Store embeddings
df['embedding'] = [e.tolist() for e in embeddings]

# Save to file for MongoDB
df.to_json("embedded_mental_health_posts.json", orient="records", lines=True)

print("✅ Embeddings generated and saved to embedded_mental_health_posts.json")