💬 AI RAG Chatbot using Endee
📌 Project Overview

This project demonstrates a Retrieval-Augmented Generation (RAG) chatbot that uses a vector database for semantic search and intelligent information retrieval.

The system stores text data as vector embeddings and retrieves the most relevant information based on user queries.

🎯 Objective
Build an AI/ML project using a vector database
Demonstrate a real-world use case of RAG
Implement semantic search using embeddings
Develop an interactive chatbot interface
🧠 Technologies Used
Python
Streamlit – for building the web interface
Sentence Transformers – for generating embeddings
ChromaDB – vector database for storing and retrieving embeddings
Endee – used as a reference vector database
⚙️ System Architecture
Data Input
Text data is stored in data.txt
Embedding Generation
Sentence Transformer converts text into vector embeddings
Vector Storage
Embeddings are stored in ChromaDB (chroma_db)
Query Processing
User query is converted into embedding
Similarity Search
Top matching results are retrieved using vector similarity
Output Display
Results are shown in terminal or Streamlit UI
🚀 Features
Semantic search
Fast vector-based retrieval
Simple chatbot interface
Lightweight and efficient
Easy to extend with LLMs
📂 Project Structure
ai-rag-chatbot/
│── app.py
│── embed_store.py
│── query.py
│── data.txt
│── requirements.txt
│── README.md
│── chroma_db/   (auto-generated)
🔧 Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/ai-rag-chatbot.git
cd ai-rag-chatbot
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Store Data in Vector Database
python embed_store.py

👉 This step converts text into embeddings and stores them in chroma_db

4️⃣ Run Chatbot (Terminal)
python query.py
5️⃣ Run Web Application
streamlit run app.py
📊 Example Query

Input:
What is RAG?

Output:
RAG stands for Retrieval-Augmented Generation

📌 Use Cases
AI-based search engines
FAQ chatbots
Knowledge retrieval systems
Document search applications
🔗 Endee Requirement

As per project requirements:

⭐ Starred the Endee repository
🍴 Forked the Endee repository
Used it as a reference for vector database implementation
🚧 Future Enhancements
Integrate LLM (OpenAI / Ollama) for better responses
Add file/document upload support
Improve UI with chat interface
Deploy the application online
👨‍💻 Author

Sathya K
