import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
HF_API_KEY = os.getenv("HF_API_KEY")

TMP_DIR = "data/tmp"
VECTOR_DB_DIR = "data/vectorstores"