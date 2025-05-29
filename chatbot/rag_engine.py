# from langchain.vectorstores import FAISS
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.chains import RetrievalQA
# from langchain.llms import HuggingFacePipeline
# from transformers import pipeline
# import os

# # Load the embedding and FAISS index
# embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
# db = FAISS.load_local("vectorstore", embedding)

# # Setup local LLM (GPT-Neo, GPT-J, etc.)
# generator = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B", max_new_tokens=256)
# llm = HuggingFacePipeline(pipeline=generator)

# # Retrieval chain
# qa_chain = RetrievalQA.from_chain_type(
#     llm=llm,
#     retriever=db.as_retriever(),
#     return_source_documents=True
# )

# def ask_question(query):
#     result = qa_chain(query)
#     return result["result"]
