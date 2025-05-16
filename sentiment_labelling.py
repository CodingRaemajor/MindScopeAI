import pandas as pd
from textblob import TextBlob

df = pd.read_csv("cleaned_mental_health_posts.csv")


def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return 'positive'
    elif polarity < -0.1:
        return 'negative'
    else:
        return 'neutral'
    

df['sentiment'] = df['body'].apply(get_sentiment)

#Preview
print(df[['body', 'sentiment']].head())
print(f"\n Sentiment labeling complete:\n{df['sentiment'].value_counts()}")

#Save updated dataset
df.to_csv("Labeled_mental_health_posts.csv", index=False)