import hashlib
import sqlite3
import logging

logger = logging.getLogger(__name__)

class IdempotentBillingGuard:
    """
    Stateful Revenue Protector.
    Ensures that B2B clients are strictly charged once per unique API request, 
    even during aggressive network retries or downstream n8n orchestrator timeouts.
    """
    def __init__(self, db_path: str = "billing_state.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS billing_ledger 
                             (transaction_hash TEXT PRIMARY KEY, status TEXT)''')

    def authorize_charge(self, client_id: str, idempotency_key: str) -> bool:
        tx_hash = hashlib.sha256(f"{client_id}_{idempotency_key}".encode()).hexdigest()

        cursor = self.conn.execute("SELECT status FROM billing_ledger WHERE transaction_hash = ?", (tx_hash,))
        if cursor.fetchone():
            logger.warning(f"Idempotency hit: Transaction {idempotency_key} already billed. Blocking duplicate charge.")
            return False

        self.conn.execute("INSERT INTO billing_ledger (transaction_hash, status) VALUES (?, ?)", (tx_hash, "billed"))
        self.conn.commit()
        return True
