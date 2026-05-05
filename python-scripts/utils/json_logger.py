import logging
import json
from datetime import datetime

class StructuredJSONLogger:
    """
    Enterprise telemetry logger. Outputs logs in JSON format for easy ingestion 
    into Datadog, Splunk, or ELK stacks for live business dashboards.
    """
    @staticmethod
    def log_event(level: str, event_name: str, payload: dict):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": level.upper(),
            "event": event_name,
            "data": payload
        }
        print(json.dumps(log_entry))

# Usage: StructuredJSONLogger.log_event("info", "lead_extracted", {"company": "Acme", "value": 5000})
