# 📚 RAG Book Assistant

A Retrieval-Augmented Generation (RAG) application built with **Streamlit**, **LangChain**, **Hugging Face Embeddings**, **ChromaDB**, and **Mistral AI**.

Upload any PDF book or document, create a vector database, and ask questions about its contents. The AI answers only using the information retrieved from the uploaded document.

---

## 🚀 Features

- 📄 Upload any PDF document
- ✂️ Automatically split the document into chunks
- 🧠 Generate embeddings using Hugging Face
- 💾 Store embeddings locally with ChromaDB
- 🔍 Retrieve relevant document chunks using MMR search
- 🤖 Answer questions using Mistral AI
- 🌐 Simple and interactive Streamlit interface

---

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- Hugging Face Embeddings
- ChromaDB
- Mistral AI
- PyPDFLoader

---

## 📂 Project Structure

```
RAG-Book-Assistant/
│
├── app.py
├── chroma_db/
├── requirements.txt
├── .env
├── README.md
└── sample.pdf
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/RAG-Book-Assistant.git

cd RAG-Book-Assistant
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

#### Linux / Mac

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create a `.env` file

Add your Mistral API key.

```env
MISTRAL_API_KEY=your_api_key_here
```

---

## ▶️ Run the application

```bash
streamlit run app.py
```

---

## 📖 How It Works

### Step 1

Upload a PDF document.

### Step 2

Click **Create Vector Database**.

The application:

- Loads the PDF
- Splits it into chunks
- Creates embeddings
- Stores them inside ChromaDB

### Step 3

Ask questions related to the uploaded document.

The application:

1. Retrieves the most relevant chunks using MMR.
2. Sends the retrieved context to Mistral AI.
3. Returns an answer based only on the document.

---

## 🧠 Embedding Model

The project uses:

```
sentence-transformers/all-MiniLM-L6-v2
```

- Embedding Dimension: **384**
- Fast and lightweight
- Suitable for Retrieval-Augmented Generation (RAG)

---

## 🔍 Retrieval Strategy

Retriever configuration:

```python
search_type="mmr"

k=4
fetch_k=10
lambda_mult=0.5
```

MMR (Maximal Marginal Relevance) retrieves documents that are both relevant and diverse, reducing redundant context.

---

## 🤖 Language Model

Model used:

```
mistral-small-2506
```

The model is instructed to answer **only** using the retrieved context.

If the information is unavailable, it responds:

> "I could not find the answer in the document."

---

## 📦 Dependencies

- streamlit
- langchain
- langchain-community
- langchain-huggingface
- langchain-mistralai
- chromadb
- pypdf
- python-dotenv
- sentence-transformers

---

## 📸 Application Workflow

```
Upload PDF
      │
      ▼
Load PDF
      │
      ▼
Split into Chunks
      │
      ▼
Generate Embeddings
      │
      ▼
Store in ChromaDB
      │
      ▼
User Question
      │
      ▼
Retriever (MMR)
      │
      ▼
Retrieved Context
      │
      ▼
Mistral AI
      │
      ▼
Answer
```

---

## 🔮 Future Improvements

- Chat history
- Multiple PDF support
- Hybrid search (BM25 + Vector Search)
- Source citations
- Streaming responses
- Conversation memory
- Support for DOCX and TXT files
- Cloud vector databases (Pinecone, Weaviate, Qdrant)

---

## 👨‍💻 Author

Your Name

---

## 📄 License

This project is licensed under the MIT License.