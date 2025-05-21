# 🧠 MindScope AI

**MindScope AI** is an intelligent mental health support tool that semantically searches real Reddit posts based on user-submitted concerns. Built using MongoDB Atlas Vector Search and Sentence Transformers, it matches user input with contextually similar experiences from real people.

![MindScope Banner](https://img.shields.io/badge/Mental%20Health-AI%20Support-purple?style=flat&logo=github)
![Built with Python](https://img.shields.io/badge/Built%20With-Python-blue?logo=python)
![MongoDB Atlas](https://img.shields.io/badge/Database-MongoDB%20Atlas-green?logo=mongodb)
![Streamlit App](https://img.shields.io/badge/Frontend-Streamlit-orange?logo=streamlit)

---

## 🌟 Features

- 🔍 **Semantic Search** using MongoDB Atlas Vector Search
- 🤗 **Embeddings** generated with `all-MiniLM-L6-v2` for optimized performance
- 🧵 **Real Reddit Posts** (4.6K+ records) for relatable mental health support
- 🖥️ **Streamlit Interface** for smooth user interaction
- ☁️ **Deployable** on Streamlit Cloud with lightweight compute

---

## 🚀 Demo

> 📍**Live App**: [Streamlit Deployment](https://your-streamlit-url-here)

Enter a concern like:
```text
I feel anxious and alone.

And MindScopeAI will return the top 5 most relevant Reddit posts, like this:

1. (0.84) I've been struggling with anxiety for a while...
2. (0.82) I feel isolated and it's getting worse...
And Continue

🧩 Tech Stack
Component	      Tool/Framework
Embeddings	    🤗 SentenceTransformers (MiniLM)
Vector Search	  🔎 MongoDB Atlas Vector Index
Backend	        🐍 Python
Frontend	      🎨 Streamlit
Deployment	    ☁️ Streamlit Cloud


📁 File Structure

MindScopeAI/
│
├── generate_embeddings.py     # Load dataset & generate vector embeddings
├── upload_to_mongodb.py       # Upload JSON docs with embeddings to MongoDB
├── mindscope_app.py           # Streamlit frontend + query pipeline
├── embedded_mental_health_posts.json  # Output of embedding phase
└── requirements.txt           # Python dependencies


🧠 How it Works
1. Input is embedded using MiniLM sentence transformer
2. Embedding is sent to MongoDB Atlas for vector similarity search
3. Matching Reddit posts are returned and displayed in the app

🛠️ Local Setup

git clone https://github.com/CodingRaemajor/MindScopeAI.git
cd MindScopeAI
pip install -r requirements.txt
# Run the app
streamlit run mindscope_app.py


🧬 Dataset
4,678 Reddit mental health posts from solomonm/mental-health-reddit
Cleaned and embedded into 384-dimensional vectors

💡 Future Improvements
Sentiment-based filtering of results
Mobile-responsive UI
Topic-based clustering of results
Real-time support suggestions


Built with ❤️ by Parth Patel
If you like the project, consider ⭐️ starring it on GitHub!


📄 License
This project is licensed under the terms of the MIT License.

---

Let me know if you'd like a **light or dark theme preview**, or want me to include your **Streamlit URL**. Ready to push this to your repo?
