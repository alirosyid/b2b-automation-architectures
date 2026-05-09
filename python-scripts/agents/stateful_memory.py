import hashlib
import sqlite3
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class StatefulAgentMemory:
    """
    Upgrades the automation architecture from stateless to stateful.
    Tracks processed URLs, generated payloads, and conversation context across 
    multiple decoupled n8n webhook executions to prevent duplicate processing.
    """
    def __init__(self, db_path: str = "agent_state.db"):
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self):
        """Creates the state tracking table if it doesn't exist."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS execution_state (
                    state_hash TEXT PRIMARY KEY,
                    entity_id TEXT,
                    status TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')

    def is_already_processed(self, entity_id: str, payload_data: str) -> bool:
        """
        Cryptographically verifies if a specific data payload has already 
        been processed by the AI pipeline.
        """
        unique_string = f"{entity_id}_{payload_data}"
        state_hash = hashlib.sha256(unique_string.encode()).hexdigest()
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT status FROM execution_state WHERE state_hash = ?", 
                (state_hash,)
            )
            result = cursor.fetchone()
            
            if result:
                logger.info(f"State hit: Entity {entity_id} already processed. Skipping to save API costs.")
                return True
                
            # Log the new state to prevent future duplicate processing
            conn.execute(
                "INSERT INTO execution_state (state_hash, entity_id, status) VALUES (?, ?, ?)",
                (state_hash, entity_id, "processed")
            )
            return False

    def get_context_history(self, entity_id: str) -> Optional[str]:
        """Placeholder for retrieving past AI interactions for ongoing threads."""
        pass
