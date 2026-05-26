import sqlite3
import json
import logging
from typing import List

logger = logging.getLogger(__name__)

class StatefulMemoryManager:
    """
    Long-Term Agentic Memory Store.
    Upgrades the architecture from stateless webhooks to stateful memory.
    Maintains conversational context across decoupled pipeline executions to 
    enable highly personalized, context-aware B2B outreach.
    """
    def __init__(self, db_path: str = "agent_memory.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS session_memory 
                             (entity_id TEXT PRIMARY KEY, history_json TEXT)''')

    def append_context(self, entity_id: str, new_interaction: dict):
        history = self.get_context(entity_id)
        history.append(new_interaction)

        self.conn.execute("INSERT OR REPLACE INTO session_memory (entity_id, history_json) VALUES (?, ?)",
                          (entity_id, json.dumps(history)))
        self.conn.commit()
        logger.debug(f"Stateful memory updated for entity {entity_id}.")

    def get_context(self, entity_id: str) -> List[dict]:
        cursor = self.conn.execute("SELECT history_json FROM session_memory WHERE entity_id = ?", (entity_id,))
        row = cursor.fetchone()
        return json.loads(row[0]) if row else []
