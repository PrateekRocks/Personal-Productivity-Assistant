import os
from dotenv import load_dotenv
from langchain.vectorstores import  Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain.document_loaders import  TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
import gdown
from pathlib import Path


# Load Documents
doc = [
    Document(page_content="Meeting notes :Discuss Project X deliverrable"),
    Document(page_content="Reminder: submit report by friday"),
    Document(page_content="upcoming event: Tech conference next wednesday")

]

embeddings = OllamaEmbeddings(model="nomic-embed-text")

text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=50)
docs = text_splitter.split_documents(doc)

vector_db =  Chroma.from_documents(docs,embedding=embeddings,persist_directory="DataBase")

print("Document Successfully Indexed")