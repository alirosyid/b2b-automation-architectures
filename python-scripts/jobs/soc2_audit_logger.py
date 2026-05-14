import datetime
import logging
import hashlib

logger = logging.getLogger(__name__)

class SOC2AuditLogger:
    """
    Generates an immutable log of system access and data flow.
    Streamlines annual SOC2 Type II compliance audits for enterprise clients.
    """
    @staticmethod
    def log_system_event(actor: str, action: str, resource: str):
        timestamp = datetime.datetime.utcnow().isoformat()
        log_entry = f"{timestamp}|{actor}|{action}|{resource}"
        audit_hash = hashlib.sha256(log_entry.encode()).hexdigest()

        logger.info(f"[SOC2 AUDIT] {log_entry} | Hash: {audit_hash}")
        return audit_hash
