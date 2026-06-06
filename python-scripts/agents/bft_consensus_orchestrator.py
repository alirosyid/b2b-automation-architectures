import asyncio
import logging
from typing import List, Callable, Any, Dict
from collections import Counter
import hashlib

logger = logging.getLogger(__name__)

class BFTConsensusOrchestrator:
    """
    Enterprise Reliability Architecture.
    Enforces Byzantine Fault Tolerance across multi-agent swarms. 
    Requires a cryptographic majority consensus from disparate LLM providers 
    before executing high-stakes B2B database mutations.
    """
    @staticmethod
    async def _execute_node(node_func: Callable, payload: dict) -> str:
        try:
            return await node_func(payload)
        except Exception as e:
            logger.error(f"Consensus node failure: {e}")
            return "NODE_FAILURE"

    @classmethod
    async def execute_consensus(cls, payload: dict, execution_nodes: List[Callable]) -> Dict[str, Any]:
        logger.info(f"Deploying BFT consensus across {len(execution_nodes)} independent AI nodes...")
        
        tasks = [cls._execute_node(node, payload) for node in execution_nodes]
        results = await asyncio.gather(*tasks)
        
        # Filter out failed nodes
        valid_results = [r for r in results if r != "NODE_FAILURE"]
        if not valid_results:
            raise RuntimeError("Catastrophic Swarm Failure: All BFT nodes offline.")
            
        # Hash results for strict equality checking
        hashed_results = [hashlib.md5(str(r).encode()).hexdigest() for r in valid_results]
        response_counts = Counter(hashed_results)
        majority_hash, count = response_counts.most_common(1)[0]
        
        if count >= (len(execution_nodes) // 2) + 1:
            logger.info(f"BFT Consensus achieved. Mathematical majority ({count}/{len(execution_nodes)}) verified.")
            # Retrieve the actual payload corresponding to the winning hash
            winning_index = hashed_results.index(majority_hash)
            return {"status": "consensus_reached", "data": valid_results[winning_index]}
            
        logger.critical("BFT Consensus failed. Models hallucinated disparate outputs. Operation aborted.")
        raise ValueError("Agentic swarm failed to reach majority consensus.")
