from sentence_transformers import SentenceTransformer
import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

# 🔥 Create fresh collection
collection = client.create_collection(name="rag_collection")

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Endee is a vector database",
    "RAG stands for Retrieval Augmented Generation",
    "Streamlit is used for building web apps"
]

embeddings = model.encode(documents).tolist()

collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=[str(i) for i in range(len(documents))]
)

print("✅ Data stored successfully!")