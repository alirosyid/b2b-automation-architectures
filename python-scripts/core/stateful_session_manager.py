import sqlite3
import json
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class StatefulSessionManager:
    """
    Distributed Workflow Resilience.
    Checkpoints long-running B2B pipeline states. Enables n8n orchestrators 
    to seamlessly recover and resume massive asynchronous executions from the 
    exact point of failure following a server crash or container redeployment.
    """
    def __init__(self, db_path: str = "workflow_states.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS session_checkpoints 
                             (workflow_id TEXT PRIMARY KEY, state_data TEXT)''')

    def save_checkpoint(self, workflow_id: str, state: dict):
        state_json = json.dumps(state)
        self.conn.execute("INSERT OR REPLACE INTO session_checkpoints (workflow_id, state_data) VALUES (?, ?)", 
                          (workflow_id, state_json))
        self.conn.commit()
        logger.debug(f"Workflow {workflow_id} state checkpointed securely.")

    def load_checkpoint(self, workflow_id: str) -> Optional[dict]:
        cursor = self.conn.execute("SELECT state_data FROM session_checkpoints WHERE workflow_id = ?", (workflow_id,))
        row = cursor.fetchone()
        if row:
            logger.info(f"Resuming workflow {workflow_id} from saved state.")
            return json.loads(row[0])
        return None
