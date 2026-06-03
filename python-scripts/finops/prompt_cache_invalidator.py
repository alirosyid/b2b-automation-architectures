import sqlite3
import logging
import hashlib

logger = logging.getLogger(__name__)

class PromptCacheInvalidator:
    """
    Stateful Prompt Cache Management.
    Tracks the cryptographic hash of source B2B documents. Autonomously invalidates 
    LLM prompt caches if the underlying CRM data is modified, ensuring zero 
    staleness while maximizing FinOps caching discounts.
    """
    def __init__(self, db_path: str = "cache_state.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS document_hashes 
                             (doc_id TEXT PRIMARY KEY, content_hash TEXT)''')

    def requires_cache_invalidation(self, doc_id: str, new_content: str) -> bool:
        new_hash = hashlib.sha256(new_content.encode()).hexdigest()
        
        cursor = self.conn.execute("SELECT content_hash FROM document_hashes WHERE doc_id = ?", (doc_id,))
        record = cursor.fetchone()
        
        if record and record[0] == new_hash:
            logger.debug(f"Document {doc_id} unchanged. Utilizing FinOps Prompt Cache.")
            return False
            
        logger.info(f"Data modification detected for {doc_id}. Forcing cache invalidation.")
        self.conn.execute("INSERT OR REPLACE INTO document_hashes (doc_id, content_hash) VALUES (?, ?)", 
                          (doc_id, new_hash))
        self.conn.commit()
        return True
