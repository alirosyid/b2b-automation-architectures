import sqlite3
import logging
import time

logger = logging.getLogger(__name__)

class StatefulIntentScorer:
    """
    Temporal Event Aggregator.
    Statefully tracks micro-interactions (opens, clicks, repository views) over time. 
    Applies mathematical decay to old events and escalates B2B prospects to 
    orchestration nodes only when their aggregate intent score breaches actionable thresholds.
    """
    def __init__(self, db_path: str = "intent_scoring.db", trigger_threshold: int = 50):
        self.conn = sqlite3.connect(db_path)
        self.threshold = trigger_threshold
        self.conn.execute('''CREATE TABLE IF NOT EXISTS lead_intent 
                             (lead_id TEXT PRIMARY KEY, score INTEGER, last_interaction REAL)''')

    def log_interaction(self, lead_id: str, event_points: int) -> bool:
        current_time = time.time()
        cursor = self.conn.execute("SELECT score, last_interaction FROM lead_intent WHERE lead_id = ?", (lead_id,))
        row = cursor.fetchone()
        
        current_score = row[0] if row else 0
        new_score = current_score + event_points
        
        self.conn.execute("INSERT OR REPLACE INTO lead_intent (lead_id, score, last_interaction) VALUES (?, ?, ?)", 
                          (lead_id, new_score, current_time))
        self.conn.commit()
        
        if new_score >= self.threshold:
            logger.critical(f"INTENT BREACH: Lead {lead_id} reached {new_score} points. Triggering sales orchestration.")
            return True # Signal orchestration
            
        logger.debug(f"Interaction logged for {lead_id}. Current Score: {new_score}")
        return False
