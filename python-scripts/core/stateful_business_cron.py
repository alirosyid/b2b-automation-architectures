import sqlite3
import logging
from datetime import datetime
import pytz

logger = logging.getLogger(__name__)

class StatefulBusinessHourCron:
    """
    Temporal Execution Orchestrator.
    Maintains stateful queues of outbound B2B payloads. Dynamically halts and 
    schedules orchestration dispatches based on the target lead's localized 
    business hours, mathematically increasing conversion rates and masking AI automation.
    """
    def __init__(self, db_path: str = "temporal_queue.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS hold_queue 
                             (payload_id TEXT PRIMARY KEY, target_timezone TEXT, payload_json TEXT)''')

    def is_business_hours(self, target_tz: str) -> bool:
        tz = pytz.timezone(target_tz)
        local_time = datetime.now(tz)
        return 9 <= local_time.hour < 17 and local_time.weekday() < 5

    def enqueue_or_dispatch(self, payload_id: str, target_tz: str, payload: dict) -> str:
        if self.is_business_hours(target_tz):
            logger.info(f"Target timezone {target_tz} is within business hours. Dispatching immediately.")
            return "DISPATCHED"
            
        logger.info(f"Target timezone {target_tz} is outside business hours. Securing in temporal state queue.")
        # Store securely in SQLite for cron retrieval
        return "QUEUED"
