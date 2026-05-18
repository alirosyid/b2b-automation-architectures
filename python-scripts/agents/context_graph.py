import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class CrossAgentContextGraph:
    """
    Centralized Memory State for Agentic Swarms.
    Provides a shared, real-time knowledge graph where specialized AI agents 
    can deposit and retrieve context about a specific B2B account, preventing 
    hallucinations and redundant processing.
    """
    def __init__(self):
        # In production, this maps to Redis or a Graph Database (Neo4j)
        self.account_memory = {}

    def update_node(self, account_id: str, agent_name: str, extracted_insight: dict):
        if account_id not in self.account_memory:
            self.account_memory[account_id] = {"insights": [], "last_updated": None}

        self.account_memory[account_id]["insights"].append({
            "source_agent": agent_name,
            "data": extracted_insight,
            "timestamp": datetime.utcnow().isoformat()
        })
        self.account_memory[account_id]["last_updated"] = datetime.utcnow().isoformat()
        logger.info(f"Context Graph updated for account {account_id} by {agent_name}.")

    def retrieve_context(self, account_id: str) -> list:
        return self.account_memory.get(account_id, {}).get("insights", [])
