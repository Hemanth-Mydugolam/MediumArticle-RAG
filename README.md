# RAG Pipeline – Retrieval-Augmented Generation
📌 **Note**: This repository is a working example that complements the concepts discussed in the [Medium article](https://medium.com/@hemanth.mydugolam/rag-retrieval-augmented-generation-make-llms-smarter-with-your-own-data-08e21835af21) titled *"RAG (Retrieval‑Augmented Generation): Make LLMs Smarter with Your Own Data"*.

## 🔍 Overview

This repository demonstrates how to build a simple RAG pipeline using:
- LangChain
- FAISS
- OpenAI LLMs

It loads PDF documents, creates a searchable vector index, and allows question-answering grounded in your own data.

## 🚀 Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/Hemanth-Mydugolam/MediumArticle-RAG
   cd MediumArticle-RAG
   ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set your OpenAI API key in the `.env` file:
    ```bash
    OPENAI_API_KEY=<your_api_key>
    ```
4. Run the script to build the index:
    ```bash
    python build_index.py
    ```
5. Query the index:
    ```bash
    python query.py --question "What is the company's work-from-home policy for part-time employees?"
    ```
