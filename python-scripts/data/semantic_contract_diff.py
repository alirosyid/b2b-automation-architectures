import logging
import numpy as np
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class SemanticContractDiffEngine:
    """
    AI-Driven Procurement & Legal Ops.
    Replaces brittle string-matching diffs with semantic embedding comparisons.
    Analyzes multi-version B2B contracts to autonomously highlight critical 
    business logic alterations while completely ignoring benign phrasing changes.
    """
    def __init__(self, semantic_threshold: float = 0.95):
        self.threshold = semantic_threshold

    def _cosine_similarity(self, vec1: list, vec2: list) -> float:
        return float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))

    def calculate_semantic_diff(self, original_clauses: List[Dict[str, Any]], updated_clauses: List[Dict[str, Any]]) -> List[Dict[str, str]]:
        logger.info(f"Executing semantic diff between contract versions ({len(original_clauses)} clauses)...")
        critical_changes = []

        # Assuming clauses are aligned by ID for complex B2B documents
        for orig, updated in zip(original_clauses, updated_clauses):
            similarity = self._cosine_similarity(orig["embedding"], updated["embedding"])
            
            if similarity < self.threshold:
                logger.warning(f"Semantic Drift Detected in Clause {orig['id']} (Similarity: {similarity:.2f})")
                critical_changes.append({
                    "clause_id": orig["id"],
                    "original_text": orig["text"],
                    "updated_text": updated["text"],
                    "drift_score": similarity
                })
                
        logger.info(f"Diff complete. Isolated {len(critical_changes)} critical semantic alterations.")
        return critical_changes
