import sqlite3
import logging

logger = logging.getLogger(__name__)

class ExecutionState:
    """
    Lightweight SQLite cache to track processed URLs or IDs.
    Prevents duplicate workflow executions.
    """
    def __init__(self, db_path: str = "execution_state.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS processed_items (item_id TEXT PRIMARY KEY, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)"
        )

    def is_processed(self, item_id: str) -> bool:
        cursor = self.conn.execute("SELECT 1 FROM processed_items WHERE item_id = ?", (item_id,))
        return cursor.fetchone() is not None

    def mark_processed(self, item_id: str):
        try:
            self.conn.execute("INSERT INTO processed_items (item_id) VALUES (?)", (item_id,))
            self.conn.commit()
        except sqlite3.IntegrityError:
            logger.warning(f"Item {item_id} already marked as processed.")
