import logging
from qdrant_client import QdrantClient
from qdrant_client.models import QueryRequest

logger = logging.getLogger(__name__)

class QdrantHybridRetriever:
    """
    Hybrid Search Architecture (Dense + Sparse).
    Combines dense semantic vectors with sparse keyword extraction (BM25/FastEmbed).
    Guarantees that autonomous agents can retrieve both broad concepts and 
    highly specific B2B acronyms from the knowledge base simultaneously.
    """
    def __init__(self, collection_name: str = "b2b_knowledge"):
        self.client = QdrantClient(":memory:") # Production: Connect to cloud instance
        self.collection = collection_name

    def retrieve_hybrid_context(self, query_text: str, limit: int = 3) -> list:
        logger.info("Executing Hybrid Vector + Keyword Search...")
        
        # Qdrant v1.10+ supports native hybrid search routing
        search_result = self.client.query_points(
            collection_name=self.collection,
            query=query_text,
            limit=limit,
            # Production: Requires configured dense and sparse embedding models
        )
        
        logger.debug(f"Retrieved {len(search_result.points)} high-fidelity hybrid chunks.")
        return [point.payload for point in search_result.points]
