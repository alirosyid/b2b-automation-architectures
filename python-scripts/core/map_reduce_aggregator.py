import asyncio
import logging
from typing import List, Callable, Any

logger = logging.getLogger(__name__)

class MapReduceAIAggregator:
    """
    High-Concurrency Processing Architecture.
    Solves context-window degradation by chunking massive B2B documents. 
    Fanning out the chunks to asynchronous worker nodes for parallel LLM extraction, 
    then fanning in (aggregating) the results into a unified, hallucination-free JSON.
    """
    @staticmethod
    async def fan_out(chunks: List[str], worker_func: Callable) -> List[Any]:
        logger.info(f"Fanning out {len(chunks)} document chunks to asynchronous AI workers...")
        tasks = [worker_func(chunk) for chunk in chunks]
        results = await asyncio.gather(*tasks)
        return results

    @staticmethod
    def fan_in(results: List[dict]) -> dict:
        logger.info("Fanning in parallel results for structural aggregation...")
        aggregated_data = {"extracted_entities": [], "summary_points": []}
        
        for res in results:
            if "entities" in res:
                aggregated_data["extracted_entities"].extend(res["entities"])
            if "summary" in res:
                aggregated_data["summary_points"].append(res["summary"])
                
        # Deduplicate entities
        aggregated_data["extracted_entities"] = list(set(aggregated_data["extracted_entities"]))
        logger.info("MapReduce execution complete. Unified payload generated.")
        return aggregated_data
