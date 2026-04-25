from langchain_text_splitters import RecursiveCharacterTextSplitter

def splitDocs(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1600,
        chunk_overlap=200
    )

    return splitter.split_documents(documents)