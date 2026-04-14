import streamlit as st
from sentence_transformers import SentenceTransformer
import chromadb

# Load DB
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection(name="rag_collection")

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

st.title("💬 RAG Chatbot")

# User input
query = st.text_input("Ask something:")

if query:
    # Convert query to embedding
    query_embedding = model.encode([query]).tolist()

    # Search DB
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=2
    )

    st.subheader("🔍 Retrieved Context:")
    for doc in results["documents"][0]:
        st.write("-", doc)