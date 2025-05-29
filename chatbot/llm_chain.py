
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from transformers import pipeline, logging as hf_logging
import torch
import re, os
from django.conf import settings
# --- Suppress warnings ---
hf_logging.set_verbosity_error()

# --- Constants ---
KNOWLEDGE_PATH = "data/knowledge.txt"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "google/flan-t5-base"
TOP_K = 3
STOP_TOKENS = ["\nQuestion:", "\n\nQuestion:", "Question:", "Q:"]

# --- Load vector DB ---
def build_vector_db(path: str) -> FAISS:
    documents = TextLoader(path).load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50)
    chunks = splitter.split_documents(documents)
    embeddings = HuggingFaceEmbeddings(model_name= EMBEDDING_MODEL)
    return FAISS.from_documents(chunks, embeddings)

# --- Load FLAN-T5 generator ---
def load_generator():
    device = 0 if torch.cuda.is_available() else -1
    return pipeline(
        "text2text-generation",
        model= LLM_MODEL,
        device=device,
        max_new_tokens=1024,
        temperature=0.3,
        top_p=0.9,
        repetition_penalty=1.1,
    )

# --- Clean Output ---
def clean_output(generated: str) -> str:
    answer = generated.strip()

    for stop in STOP_TOKENS:
        if stop in answer:
            answer = answer.split(stop)[0].strip()
            break

    answer = re.split(r"(\.|\n)+", answer)[0].strip()

    # Capitalize first character if not already
    if answer:
        answer = answer[0].upper() + answer[1:]

    return answer


# --- Detect poor or generic responses ---
def is_response_trash(answer: str) -> bool:
    trash_values = {"python", "iii", "flask", "vector database", ""}
    return answer.lower().strip() in trash_values or len(answer.strip()) < 10

# --- Main ---
db = build_vector_db(KNOWLEDGE_PATH)
generator = load_generator()

def get_rag_response(query: str) -> str:
    docs = db.similarity_search(query, k= TOP_K)
    if not docs:
        return f"Sorry, no relevant information found in the knowledge base for: '{query}'."

    context = "\n\n".join(doc.page_content for doc in docs)
    prompt = (
        f"Answer the following question based on the context provided. Write a detailed response.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {query}"
    )

    result = generator(prompt)[0]
    generated_text = result.get("generated_text") or result.get("text", "")
    answer = clean_output(generated_text)

    if is_response_trash(answer):
        return f"Sorry, I couldn't generate a useful answer from the knowledge base for: '{query}'."

    return answer
