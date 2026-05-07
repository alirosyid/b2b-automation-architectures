import hashlib
from datetime import datetime

class SystemAuditLogger:
    """
    Menyediakan jejak audit (audit trail) yang tidak dapat diubah untuk semua 
    perubahan status dalam pipeline B2B. Sangat penting untuk kepatuhan SOC2.
    """
    @staticmethod
    def log_state_change(entity_id: str, old_state: str, new_state: str, actor: str = "n8n_webhook"):
        timestamp = datetime.utcnow().isoformat()
        audit_string = f"{timestamp}|{entity_id}|{old_state}|{new_state}|{actor}"
        audit_hash = hashlib.sha256(audit_string.encode()).hexdigest()

        # This should be written to an append-only log file or secure DB
        audit_entry = f"[{timestamp}] Entity: {entity_id} | Transition: {old_state} -> {new_state} | Actor: {actor} | Hash: {audit_hash}"
        print(audit_entry)
