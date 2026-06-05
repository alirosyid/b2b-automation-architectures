import logging
import numpy as np
from typing import Dict, List, Tuple

logger = logging.getLogger(__name__)

class SemanticIntentRouter:
    """
    High-Speed Semantic Routing Engine.
    Utilizes local vector embeddings to classify inbound B2B payloads instantly.
    Bypasses expensive cloud LLM inferences for basic intent classification, 
    routing traffic directly to the appropriate downstream orchestration nodes.
    """
    def __init__(self, threshold: float = 0.85):
        self.threshold = threshold
        # Production: Load actual reference embeddings from a local lightweight model
        self.reference_intents: Dict[str, List[float]] = {
            "sales_routing": [0.12, 0.88, 0.05],
            "support_routing": [0.05, 0.11, 0.92]
        }

    def _cosine_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        return float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))

    def route_payload(self, payload_embedding: List[float]) -> str:
        best_match: Tuple[str, float] = ("default_queue", 0.0)
        
        for route, ref_vec in self.reference_intents.items():
            similarity = self._cosine_similarity(payload_embedding, ref_vec)
            if similarity > best_match[1]:
                best_match = (route, similarity)
                
        if best_match[1] >= self.threshold:
            logger.info(f"Semantic match found. Routing to {best_match[0]} (Confidence: {best_match[1]:.2f})")
            return best_match[0]
            
        logger.debug("No semantic threshold met. Routing to default queue.")
        return "default_queue"
