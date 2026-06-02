import sqlite3
import logging
from fastapi import Request, HTTPException

logger = logging.getLogger(__name__)

class ResendEventWebhook:
    """
    Real-Time Lead Intent Tracker.
    Listens for asynchronous webhook events from the Resend API (e.g., opens, clicks).
    Statefully updates the B2B lead score in the internal database to trigger 
    downstream sales orchestration when prospect intent is high.
    """
    def __init__(self, db_path: str = "lead_scoring.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS lead_scores 
                             (lead_id TEXT PRIMARY KEY, engagement_score INTEGER)''')

    async def process_event(self, request: Request):
        payload = await request.json()
        
        event_type = payload.get("type")
        lead_id = payload.get("data", {}).get("tags", {}).get("lead_id")
        
        if not lead_id:
            logger.warning("Resend event missing lead_id tag. Dropping payload.")
            raise HTTPException(status_code=400, detail="Missing lead identification.")
            
        points = 0
        if event_type == "email.opened":
            points = 5
        elif event_type == "email.clicked":
            points = 15
            
        if points > 0:
            self._update_score(lead_id, points)
            logger.info(f"Lead {lead_id} engaged ({event_type}). Added {points} points.")
            
        return {"status": "event_processed"}

    def _update_score(self, lead_id: str, points: int):
        cursor = self.conn.execute("SELECT engagement_score FROM lead_scores WHERE lead_id = ?", (lead_id,))
        row = cursor.fetchone()
        
        new_score = (row[0] if row else 0) + points
        self.conn.execute("INSERT OR REPLACE INTO lead_scores (lead_id, engagement_score) VALUES (?, ?)", 
                          (lead_id, new_score))
        self.conn.commit()
