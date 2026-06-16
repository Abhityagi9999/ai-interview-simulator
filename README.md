# 🧠 AI Interview Simulator

An **AI-powered interview platform** that evaluates candidate answers using **semantic intelligence** instead of rigid keyword matching — improving fairness and realism in technical assessments.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🧠 **Semantic Similarity** | Encodes questions & answers into dense vector embeddings using Sentence Transformers and performs high-speed similarity search via FAISS |
| 📈 **Dynamic Difficulty** | Automatically progresses candidates across Easy → Medium → Hard → Advanced levels based on real-time performance |
| 🔍 **Grammar Correction** | Analyzes and corrects grammar using Flan-T5 large model, scoring original vs corrected text similarity |
| 📊 **Fluency Scoring** | Measures language fluency using GPT-2 perplexity scoring — lower perplexity = more natural language |
| 🎯 **Keyword Relevance** | Checks presence of domain-specific keywords in candidate responses |
| 🎨 **Stunning UI** | Modern glassmorphism interface with animated backgrounds and real-time score visualization |

---

## 🏗️ Architecture

```
User Answer
    │
    ▼
┌──────────────────────────────────────┐
│       Multi-Dimensional Scoring      │
│                                      │
│  ┌────────────┐  ┌────────────────┐  │
│  │  Semantic   │  │   Grammar      │  │
│  │  Similarity │  │   Correction   │  │
│  │  (FAISS +   │  │   (Flan-T5)    │  │
│  │  SentenceT) │  │                │  │
│  └────────────┘  └────────────────┘  │
│                                      │
│  ┌────────────┐  ┌────────────────┐  │
│  │  Fluency    │  │   Keyword      │  │
│  │  Scoring    │  │   Relevance    │  │
│  │  (GPT-2     │  │   Matching     │  │
│  │  Perplexity)│  │                │  │
│  └────────────┘  └────────────────┘  │
│                                      │
│         Final Weighted Score         │
│   (40% Semantic + 30% Keyword +      │
│    15% Grammar + 15% Fluency)        │
└──────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

- **Python** — Core language
- **FastAPI** — Web framework & API
- **FAISS** — Vector similarity search
- **Sentence Transformers** (`all-MiniLM-L6-v2`) — Embedding generation
- **Hugging Face Transformers** — Grammar correction (Flan-T5) & Fluency (DistilGPT-2)
- **PyTorch** — Deep learning backend

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/Abhityagi9999/ai-interview-simulator.git
cd ai-interview-simulator

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Open your browser at **http://localhost:8000** 🎉

> **Note:** The first launch will download ML models (~1-2 GB). Subsequent launches will be faster as models are cached.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Serves the Web UI |
| `GET` | `/questions/{difficulty}` | Get questions by difficulty level |
| `POST` | `/evaluate` | Evaluate a candidate answer |

### Example API Request

```json
POST /evaluate
{
  "difficulty": "easy",
  "question_index": 0,
  "user_answer": "Reinforcement learning is a type of machine learning where an agent learns to make decisions by interacting with an environment and receiving rewards."
}
```

### Example Response

```json
{
  "question": "What is reinforcement learning?",
  "user_answer": "...",
  "evaluation_results": {
    "final_score": 78.5,
    "semantic_score": 85.2,
    "grammar_score": 95.0,
    "fluency_score": 62.3,
    "keyword_score": 80.0,
    "corrected_text": "..."
  }
}
```

---

## 📂 Project Structure

```
ai-interview-simulator/
├── app.py              # FastAPI server & routes
├── evaluator.py        # AI evaluation engine (FAISS, NLP models)
├── data.py             # Interview Q&A dataset
├── requirements.txt    # Python dependencies
├── vercel.json         # Vercel deployment config
├── static/
│   ├── index.html      # Web UI
│   ├── styles.css      # Glassmorphism styling
│   └── script.js       # Frontend logic
└── README.md
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">Built with ❤️ using Python, FAISS, and Hugging Face Transformers</p>
