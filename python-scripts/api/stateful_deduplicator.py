import hashlib
import sqlite3
import logging
import json

logger = logging.getLogger(__name__)

class StatefulDeduplicator:
    """
    Stateful Architecture Guardian.
    Maintains a cryptographic ledger of processed webhooks across decoupled 
    n8n executions. Prevents duplicate API processing and double-billing 
    by mathematically verifying payload uniqueness.
    """
    def __init__(self, db_path: str = "pipeline_state.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute('CREATE TABLE IF NOT EXISTS processed_events (hash TEXT PRIMARY KEY)')

    def is_unique_event(self, payload: dict) -> bool:
        payload_hash = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()

        cursor = self.conn.execute("SELECT 1 FROM processed_events WHERE hash = ?", (payload_hash,))
        if cursor.fetchone():
            logger.info("State hit: Payload previously processed. Bypassing execution to save compute.")
            return False

        self.conn.execute("INSERT INTO processed_events (hash) VALUES (?)", (payload_hash,))
        self.conn.commit()
        return True
