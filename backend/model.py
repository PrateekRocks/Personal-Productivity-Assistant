import os
from langchain.vectorstores import  Chroma
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain.chat_models import ChatOllama
from langchain.chains import RetrievalQA
from langchain.chains.question_answering import load_qa_chain


embeddings = OllamaEmbeddings(model="nomic-embed-text")
vector_db =  Chroma(embedding_function=embeddings,persist_directory="DataBase")
retriever = vector_db.as_retriever()

llm = Ollama(model = "llama3" ,base_url = "http://localhost:11434")

qa_chain = load_qa_chain(
    llm = llm,
    chain_type="stuff"
)


def get_response(query):
    docs = retriever.get_relevant_documents(query)
    return qa_chain.run(input_documents=docs, question=query)
