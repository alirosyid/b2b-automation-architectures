import sqlite3
import json
import logging

logger = logging.getLogger(__name__)

class ResilientDLQ:
    """
    Self-healing Dead Letter Queue (DLQ).
    Captures failed n8n webhook payloads during downstream CRM outages and 
    securely stores them in a local SQLite database for autonomous replay.
    """
    def __init__(self, db_path: str = "dlq_state.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS dead_letters 
                             (id INTEGER PRIMARY KEY, payload TEXT, retries INTEGER DEFAULT 0)''')

    def enqueue_failure(self, payload: dict):
        self.conn.execute("INSERT INTO dead_letters (payload) VALUES (?)", (json.dumps(payload),))
        self.conn.commit()
        logger.error("Pipeline failure detected. Payload secured in Dead Letter Queue.")

    def fetch_for_replay(self, max_retries: int = 3) -> list:
        cursor = self.conn.execute("SELECT id, payload FROM dead_letters WHERE retries < ?", (max_retries,))
        return [{"id": row[0], "payload": json.loads(row[1])} for row in cursor.fetchall()]
