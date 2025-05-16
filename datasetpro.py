from datasets import load_dataset

dataset = load_dataset("solomonk/reddit_mental_health_posts")
df = dataset["train"].to_pandas()
df.head()

import re

# Keep only text and subreddit columns
df = df[['body', 'subreddit']]

# Define cleaning function
def clean_text(text):
    text = str(text)
    text = re.sub(r'http\S+', '', text)                  # Remove URLs
    text = re.sub(r'\s+', ' ', text).strip()             # Normalize whitespace
    text = re.sub(r'[^\x00-\x7F]+', '', text)            # Remove emojis/non-ASCII
    return text.lower()

# Apply cleaning
df['body'] = df['body'].apply(clean_text)

# Remove posts shorter than 20 characters
df = df[df['body'].str.len() > 20]

# Reset index
df = df.reset_index(drop=True)

# Check results
print(df.head())
print(f"\n✅ Cleaned dataset has {len(df)} posts.")
df.to_csv("cleaned_mental_health_posts.csv", index=False)