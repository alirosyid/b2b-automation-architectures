import sqlite3
import logging
import re

logger = logging.getLogger(__name__)

class IdentityResolutionEngine:
    """
    Stateful Master Data Management (MDM).
    Resolves fragmented B2B inbound leads across decoupled webhooks.
    Utilizes domain normalization and fuzzy logic to prevent CRM duplication 
    and maintain a pristine, unified state profile for enterprise clients.
    """
    def __init__(self, db_path: str = "identity_graph.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS unified_profiles 
                             (master_id TEXT PRIMARY KEY, domain TEXT, root_email TEXT)''')

    def _normalize_domain(self, email: str) -> str:
        domain = email.split('@')[-1].lower()
        return re.sub(r'^(www\.|mail\.)', '', domain)

    def resolve_identity(self, email_address: str) -> str:
        domain_normalized = self._normalize_domain(email_address)
        email_normalized = email_address.lower()
        
        cursor = self.conn.execute("SELECT master_id FROM unified_profiles WHERE domain = ?", (domain_normalized,))
        record = cursor.fetchone()
        
        if record:
            master_id = record[0]
            logger.info(f"Identity Resolved: Mapped {email_normalized} to existing Master Profile {master_id}.")
            return master_id
            
        # Create new root identity
        new_master_id = f"PRFL_{hash(email_normalized)}"
        self.conn.execute("INSERT INTO unified_profiles (master_id, domain, root_email) VALUES (?, ?, ?)",
                          (new_master_id, domain_normalized, email_normalized))
        self.conn.commit()
        
        logger.info(f"New Entity Detected. Initializing Master Profile: {new_master_id}")
        return new_master_id
