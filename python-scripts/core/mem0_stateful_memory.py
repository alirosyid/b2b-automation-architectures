import logging
from mem0 import Memory

logger = logging.getLogger(__name__)

class Mem0AgenticMemory:
    """
    Long-Term Stateful Memory Architecture.
    Utilizes the Mem0 vector framework to persist contextual interactions 
    across completely decoupled pipeline runs, enabling hyper-personalized 
    B2B sales cadences.
    """
    def __init__(self):
        # Production: Configure with Qdrant/Milvus backend
        self.memory = Memory()

    def store_interaction(self, lead_id: str, interaction_text: str):
        logger.info(f"Committing stateful memory episode for lead {lead_id}...")
        self.memory.add(interaction_text, user_id=lead_id)
        logger.debug("Memory successfully persisted.")

    def retrieve_context(self, lead_id: str, current_query: str) -> str:
        logger.info(f"Retrieving historical context for lead {lead_id}...")
        relevant_memories = self.memory.search(query=current_query, user_id=lead_id)
        
        context = " ".join([m["text"] for m in relevant_memories])
        return context
