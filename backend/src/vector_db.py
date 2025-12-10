from qdrant_client import QdrantClient
from backend.src.config import settings

QDRANT_URL = settings.QDRANT_URL

client = QdrantClient(url=QDRANT_URL)

async def get_qdrant_client():
    return client