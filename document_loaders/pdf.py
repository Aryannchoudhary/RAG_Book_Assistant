from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


data = PyPDFLoader("document_loaders/GRU.pdf")

docs = data.load()


splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=1)

chunks = splitter.split_documents(docs)

print(len(chunks))
print(chunks[0].page_content)
