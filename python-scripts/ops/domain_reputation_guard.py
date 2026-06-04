import sqlite3
import logging

logger = logging.getLogger(__name__)

class DomainReputationGuard:
    """
    Deliverability Ops & Infrastructure Protection.
    Maintains a stateful ledger of email bounce rates and spam flags. 
    Autonomously severs the outbound pipeline if a B2B campaign's failure rate 
    breaches safe thresholds, mathematically protecting corporate sender reputation.
    """
    def __init__(self, db_path: str = "reputation_state.db", max_bounce_rate: float = 0.05):
        self.conn = sqlite3.connect(db_path)
        self.max_bounce_rate = max_bounce_rate
        self.conn.execute('''CREATE TABLE IF NOT EXISTS campaign_metrics 
                             (campaign_id TEXT PRIMARY KEY, attempts INTEGER, bounces INTEGER)''')

    def log_attempt(self, campaign_id: str, is_bounce: bool) -> bool:
        cursor = self.conn.execute("SELECT attempts, bounces FROM campaign_metrics WHERE campaign_id = ?", (campaign_id,))
        row = cursor.fetchone()
        
        attempts = (row[0] if row else 0) + 1
        bounces = (row[1] if row else 0) + (1 if is_bounce else 0)
        
        self.conn.execute("INSERT OR REPLACE INTO campaign_metrics (campaign_id, attempts, bounces) VALUES (?, ?, ?)", 
                          (campaign_id, attempts, bounces))
        self.conn.commit()
        
        if attempts > 20 and (bounces / attempts) > self.max_bounce_rate:
            logger.critical(f"REPUTATION ALERT: Campaign {campaign_id} exceeded bounce limits. Halting outbound orchestration.")
            return False # Signal to stop pipeline
            
        return True
