from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.chains import ConversationalRetrievalChain

def create_chain(retriever, memory, api_key):

    llm = ChatGoogleGenerativeAI(
        google_api_key=api_key,
        model="gemini-2.5-flash",
        temperature=0.5
    )

    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True
    )