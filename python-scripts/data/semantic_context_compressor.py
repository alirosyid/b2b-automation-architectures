import logging
import numpy as np
from typing import List, Dict

logger = logging.getLogger(__name__)

class SemanticContextCompressor:
    """
    Advanced Token Reduction Architecture.
    Analyzes dense B2B documents and calculates the semantic relevance of individual 
    sentences against the core orchestration objective. Dynamically drops low-density 
    information to compress context windows, drastically reducing API token costs.
    """
    @staticmethod
    def _calculate_density_score(sentence_embedding: list, target_embedding: list) -> float:
        return float(np.dot(sentence_embedding, target_embedding) / 
                    (np.linalg.norm(sentence_embedding) * np.linalg.norm(target_embedding)))

    @classmethod
    def compress_context(cls, raw_sentences: List[Dict[str, Any]], target_objective_embedding: list, compression_ratio: float = 0.3) -> str:
        logger.info(f"Initiating context compression on {len(raw_sentences)} text segments...")
        
        scored_sentences = []
        for item in raw_sentences:
            score = cls._calculate_density_score(item["embedding"], target_objective_embedding)
            scored_sentences.append({"text": item["text"], "score": score})
            
        # Sort by relevance and slice based on the compression ratio
        scored_sentences.sort(key=lambda x: x["score"], reverse=True)
        retention_count = max(1, int(len(scored_sentences) * compression_ratio))
        
        compressed_output = " ".join([seg["text"] for seg in scored_sentences[:retention_count]])
        
        logger.info(f"Compression complete. Reduced payload from {len(raw_sentences)} segments to {retention_count}.")
        return compressed_output
