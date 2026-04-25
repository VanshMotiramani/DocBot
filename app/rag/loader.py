import os
from langchain_community.document_loaders import (
    PyPDFLoader, TextLoader, CSVLoader, Docx2txtLoader
)

def loadDocuments(directory):
    docs = []

    for file in os.listdir(directory):
        path = os.path.join(directory, file)

        if path.endswith(".pdf"):
            docs.extend(PyPDFLoader(path).load())
        elif path.endswith(".txt"):
            docs.extend(TextLoader(path).load())
        elif path.endswith(".csv"):
            docs.extend(CSVLoader(path).load())
        elif path.endswith(".docx"):
            docs.extend(Docx2txtLoader(path).load())

    return docs
