# query_bot.py

import os
from langchain.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

# Load API Key
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Load FAISS index
embedding_model = OpenAIEmbeddings()
vectorstore = FAISS.load_local("faiss_index", embedding_model,allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# Load LLM
llm = ChatOpenAI(
    model_name="gpt-4o",
    temperature=0.3,
    max_tokens=1000
)

# Build RAG pipeline
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

# Example query
query = "What is the company's work-from-home policy for part-time employees?"
response = qa_chain(query)

# Print results
print("\n🧠 Answer:\n", response["result"])
print("\n📚 Sources:")
for i, doc in enumerate(response["source_documents"]):
    print(f"\n--- Source {i+1} ---\n{doc.page_content[:400]}...")
