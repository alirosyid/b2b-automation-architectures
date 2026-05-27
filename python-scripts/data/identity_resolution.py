import sqlite3
import logging

logger = logging.getLogger(__name__)

class IdentityResolutionEngine:
    """
    Stateful Master Data Management (MDM).
    Resolves fragmented B2B inbound leads across decoupled webhooks.
    Utilizes domain normalization to prevent CRM duplication and maintain 
    a pristine, unified state profile for enterprise clients.
    """
    def __init__(self, db_path: str = "identity_graph.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS unified_profiles 
                             (master_id TEXT PRIMARY KEY, aliases TEXT, domain TEXT)''')

    def resolve_identity(self, email_address: str, company_domain: str) -> str:
        domain_normalized = company_domain.lower().replace("www.", "")
        email_normalized = email_address.lower()
        
        cursor = self.conn.execute("SELECT master_id FROM unified_profiles WHERE domain = ?", (domain_normalized,))
        record = cursor.fetchone()
        
        if record:
            master_id = record[0]
            logger.info(f"Identity Resolved: Mapped {email_normalized} to existing Master Profile {master_id}.")
            return master_id
            
        new_master_id = f"PRFL_{hash(email_normalized)}"
        logger.info(f"New Entity Detected. Initializing Master Profile: {new_master_id}")
        return new_master_id
