
import streamlit as st
import os
import shutil
import time 
import uuid

from config import GOOGLE_API_KEY, TMP_DIR, VECTOR_DB_DIR
from app.rag.loader import loadDocuments
from app.rag.splitter import splitDocs
from app.rag.embeddings import getEmbeddings
from app.rag.vectorstore import loadVectorStore, createVectorStore
from app.rag.retriever import getRetriever
from app.rag.memory import getMemory
from app.rag.chain import create_chain

st.title("RAG Chatbot")

if "chain" not in st.session_state:
    st.session_state.chain = None

uploaded_files = st.file_uploader(
    "Upload files",
    accept_multiple_files=True
)

if st.button("Process"):

    if os.path.exists(TMP_DIR):
        shutil.rmtree(TMP_DIR)
    os.makedirs(TMP_DIR, exist_ok=True)

    st.session_state.chain = None

    for file in uploaded_files:
        with open(os.path.join(TMP_DIR, file.name), "wb") as f:
            f.write(file.read())

    docs = loadDocuments(TMP_DIR)
    chunks = splitDocs(docs)

    if len(chunks) == 0:
        st.error("❌ No content extracted")
        st.stop()

    embeddings = getEmbeddings()

    session_db = os.path.join(VECTOR_DB_DIR, str(uuid.uuid4()))

    vs = createVectorStore(chunks, embeddings, session_db)

    retriever = getRetriever(vs)
    memory = getMemory()

    st.session_state.chain = create_chain(
        retriever, memory, GOOGLE_API_KEY
    )

    st.success("✅ Documents processed successfully!")

query = st.text_input("Ask your query")

if query:
    if st.session_state.chain is None:
        st.warning("⚠️ Process documents first")
    else:
        response = st.session_state.chain.invoke({"question": query})
        st.write(response["answer"])