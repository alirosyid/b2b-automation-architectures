import logging
import numpy as np
from typing import Optional, Dict

logger = logging.getLogger(__name__)

class SemanticCache:
    """
    FinOps Optimization Layer.
    Utilizes local, lightweight vector embeddings to identify semantically identical 
    B2B queries (e.g., "pricing" vs "cost"). Bypasses the LLM entirely if a 
    historical match exceeds the confidence threshold, saving massive API compute.
    """
    def __init__(self, similarity_threshold: float = 0.92):
        self.threshold = similarity_threshold
        # Production: Connect to Redis/Qdrant
        self.vector_store: Dict[str, dict] = {} 

    def _cosine_similarity(self, vec1: list, vec2: list) -> float:
        return float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))

    def check_cache(self, query_embedding: list) -> Optional[str]:
        for cached_id, data in self.vector_store.items():
            similarity = self._cosine_similarity(query_embedding, data["embedding"])
            if similarity >= self.threshold:
                logger.info(f"Semantic Cache Hit (Confidence: {similarity:.2f}). Bypassing LLM.")
                return data["response"]
                
        logger.debug("Semantic Cache Miss. Routing to LLM API.")
        return None
