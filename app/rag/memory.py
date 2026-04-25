from langchain_classic.memory import ConversationBufferMemory
from sqlalchemy import true

def getMemory():
    return ConversationBufferMemory(
        return_messages=True,
        memory_key="chat_history",
        output_key="answer" 
    )