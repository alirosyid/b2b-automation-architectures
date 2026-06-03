import sqlite3
import logging
from typing import List

logger = logging.getLogger(__name__)

class VectorTombstoneTracker:
    """
    Stateful RAG Consistency Engine.
    Tracks deleted or deprecated enterprise documents using 'Tombstones'. 
    Filters out ghost vectors during retrieval to ensure AI agents do not 
    hallucinate based on outdated B2B knowledge base entries.
    """
    def __init__(self, db_path: str = "tombstones.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS vector_tombstones 
                             (vector_id TEXT PRIMARY KEY, deprecated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

    def mark_deleted(self, vector_id: str):
        self.conn.execute("INSERT OR IGNORE INTO vector_tombstones (vector_id) VALUES (?)", (vector_id,))
        self.conn.commit()
        logger.info(f"Vector {vector_id} marked with tombstone. Excluded from future RAG queries.")

    def filter_active_vectors(self, retrieved_vectors: List[dict]) -> List[dict]:
        safe_vectors = []
        for vec in retrieved_vectors:
            cursor = self.conn.execute("SELECT 1 FROM vector_tombstones WHERE vector_id = ?", (vec["id"],))
            if not cursor.fetchone():
                safe_vectors.append(vec)
            else:
                logger.debug(f"Ghost vector intercepted: {vec['id']}")
                
        return safe_vectors
