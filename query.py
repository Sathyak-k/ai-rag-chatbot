from sentence_transformers import SentenceTransformer
import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

# 🔥 IMPORTANT: use get_collection (NOT create)
collection = client.get_collection(name="rag_collection")

model = SentenceTransformer("all-MiniLM-L6-v2")

query = input("Enter your question: ")

query_embedding = model.encode([query]).tolist()

results = collection.query(
    query_embeddings=query_embedding,
    n_results=2
)

print("\n🔍 Results:")
for doc in results["documents"][0]:
    print("-", doc)