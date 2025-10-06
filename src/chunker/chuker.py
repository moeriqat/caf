from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_split_text(dir_path):
    loader = DirectoryLoader(
        dir_path,
        glob="**/*.txt",
        show_progress=True,
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=64,
    )
    return loader.load_and_split(splitter)