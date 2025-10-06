from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore

from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

from dotenv import load_dotenv

load_dotenv()


QDRANT_URL = "http://localhost:6333"  # or your Qdrant Cloud URL
EMBEDDING_MODEL = "text-embedding-004"  # or your preferred model
COLLECTION_NAME = "afcon_vectors"  # or your preferred collection name
EMBEDDING_MODEL_DIMENSION = 768  # Dimension for text-embedding-004
COLLECTION_NAME = COLLECTION_NAME

client = QdrantClient(QDRANT_URL)  # or your Qdrant Cloud URL
embedding = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)

if not client.collection_exists(COLLECTION_NAME):
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=EMBEDDING_MODEL_DIMENSION, distance=Distance.COSINE),
    )

vectorstore = QdrantVectorStore(
    embedding=embedding,
    client=client,  # or your Qdrant Cloud URL
    collection_name=COLLECTION_NAME,
)
