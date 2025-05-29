# Chatbot-LLM-rag-django-streamlit (RAG Chatbot Project)
Create a RAG-based Chatbot with Langchain, Django, and Streamlit using Open-Source LLM.

## Overview
This project implements a Retrieval-Augmented Generation (RAG) chatbot that uses a local knowledge base to answer questions.  
It consists of two main components:
- **Backend**: A Django REST API serving embeddings and managing vector search
- **Frontend**: A Streamlit app UI for users to interact with the chatbot

The backend uses Langchain and HuggingFace models for vector search and language generation.

---

## Features
- Similarity search over a custom knowledge base (FAISS + HuggingFace embeddings)
- Text generation with an open-source LLM (e.g., Flan-T5)
- Streamlit frontend for an interactive Q&A experience
- Fast and lightweight; no reliance on external internet search for responses

---

## Prerequisites

- Python 3.10 or higher
- `pip` package manager
- Virtual environment (recommended)

---

## Create and activate a virtual environment:

```
cd /rag_chatbot
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

## Install dependencies:

```

pip install -r requirements.txt
```

## Run the Django backend server:

```
python3 manage.py runserver

#By default, it runs at:
http://127.0.0.1:8000/

```

## Start the Frontend UI
Run the Streamlit app:
```
streamlit run streamlit_app.py

#Once started, open your browser to:

Local URL: http://localhost:8501
Network URL: http://<your-local-ip>:8501
```
