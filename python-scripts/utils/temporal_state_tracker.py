from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class TemporalLeadTracker:
    """
    Tracks time-series mutations in B2B lead data.
    Enables highly context-aware outreach by triggering automations based on 
    the exact duration since a specific corporate event (e.g., 'Series B Funding').
    """
    def __init__(self):
        self.state_history = {}

    def log_state_change(self, lead_id: str, new_event: str):
        timestamp = datetime.utcnow()
        if lead_id not in self.state_history:
            self.state_history[lead_id] = []

        self.state_history[lead_id].append({"event": new_event, "time": timestamp})
        logger.info(f"Temporal event logged for {lead_id}: {new_event} at {timestamp.isoformat()}")

    def get_days_since_event(self, lead_id: str, target_event: str) -> int:
        # Logic to calculate time elapsed to trigger specific n8n follow-up campaigns
        pass
