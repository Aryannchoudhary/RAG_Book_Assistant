from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

data= TextLoader("document_loaders/notes.txt").load()


splitter = CharacterTextSplitter(
    separator="",
    chunk_size=10,
    chunk_overlap=1
    )
docs = splitter.split_documents(data)

print(len(docs))


for i in docs:
    print(i.page_content)
    print()
    print()
    print()


