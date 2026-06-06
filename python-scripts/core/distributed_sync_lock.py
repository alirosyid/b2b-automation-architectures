import sqlite3
import hashlib
import json
import logging

logger = logging.getLogger(__name__)

class DistributedSyncLock:
    """
    Stateful Idempotency Architecture.
    Maintains a cryptographic ledger of processed B2B payloads.
    Mathematically prevents duplicate CRM injections and redundant LLM API 
    compute during aggressive network retries or orchestration glitches.
    """
    def __init__(self, db_path: str = "sync_locks.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS processed_locks 
                             (payload_hash TEXT PRIMARY KEY, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')

    def acquire_lock(self, payload: dict) -> bool:
        payload_hash = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
        
        try:
            self.conn.execute("INSERT INTO processed_locks (payload_hash) VALUES (?)", (payload_hash,))
            self.conn.commit()
            logger.debug("Sync lock acquired. Payload is unique and cleared for processing.")
            return True
            
        except sqlite3.IntegrityError:
            logger.warning("Stateful Lock Hit: Duplicate payload detected. Execution bypassed.")
            return False
