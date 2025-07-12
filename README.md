# RAG Pipeline – Retrieval-Augmented Generation

Based on *“RAG (Retrieval‑Augmented Generation): Make LLMs Smarter with Your Own Data”* :contentReference[oaicite:2]{index=2}

## 🔍 Overview

This repository demonstrates how to build a simple RAG pipeline using:
- LangChain
- FAISS
- OpenAI LLMs

It loads PDF documents, creates a searchable vector index, and allows question-answering grounded in your own data.

## 🚀 Setup

1. Clone the repo:
   ```bash
   git clone <https://github.com/Hemanth-Mydugolam/MediumArticle-RAG>
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
    python main.py
    ```
5. Query the index:
    ```bash
    python query.py --question "What is the company's work-from-home policy for part-time employees?"
    ```
