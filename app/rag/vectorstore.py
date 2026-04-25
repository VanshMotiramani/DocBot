from langchain_community.vectorstores import Chroma

def createVectorStore(chunks, embeddings, persist_dir):
    return Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_dir
    )

def loadVectorStore(embeddings, persist_dir):
    return Chroma(
        embedding_function=embeddings,
        persist_directory=persist_dir
    )