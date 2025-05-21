from datasets import load_dataset
from sentence_transformers import SentenceTransformer
import pandas as pd
import json
from tqdm import tqdm

print("🔄 Loading dataset...")
dataset = load_dataset("solomonk/reddit_mental_health_posts")["train"]
posts = dataset.to_pandas()

# Clean data: rename, filter, and drop missing texts
posts = posts[["body", "subreddit"]].dropna().head(4678)
posts = posts.rename(columns={"body": "text"})

# Reset index after dropping
posts.reset_index(drop=True, inplace=True)

print("🚀 Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2") # 384 dimensions

print("🔁 Generating embeddings in batch...")
embeddings = model.encode(
    posts["text"].tolist(),
    batch_size=32,
    show_progress_bar=True,
    convert_to_numpy=True
)

# Add embeddings
posts["embedding"] = [e.tolist() for e in embeddings]

# Export to JSON
output_path = "embedded_mental_health_posts.json"
posts.to_json(output_path, orient="records", lines=True)
print(f"✅ Saved embedded posts to {output_path}")