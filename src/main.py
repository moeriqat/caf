import os

from .qdrant.vector_store import  vectorstore, embedding, COLLECTION_NAME
from .chunker.chuker import  load_split_text
from .html_processing.cleaning_html import process_all_html_files
from dotenv import load_dotenv

load_dotenv()



TEXT_DATA_PATH = "src/data/cleaned_text"
DATA_PATH = "src/data/fetched_html"

loaded_text = load_split_text(TEXT_DATA_PATH)



if __name__ == "__main__":
    process_all_html_files(DATA_PATH)
    vectorstore.add_documents(loaded_text)