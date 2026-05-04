import time
from typing import Dict

START_TIME = time.time()

def get_system_health() -> Dict[str, str]:
    """
    Returns system health metrics for B2B SLA monitoring.
    """
    uptime_seconds = time.time() - START_TIME
    return {
        "status": "healthy",
        "uptime_seconds": round(uptime_seconds, 2),
        "active_services": "OCR, Data Extraction, Telegram Bot",
        "sla_tier": "Enterprise 99.9%"
    }
