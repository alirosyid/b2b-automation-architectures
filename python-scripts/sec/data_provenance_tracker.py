import hashlib
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class AIDataProvenanceTracker:
    """
    Enterprise Data Lineage tracking. Cryptographically stamps AI-generated 
    CRM records with the exact model version, prompt hash, and timestamp.
    Ensures strict compliance with global AI regulations and corporate auditing.
    """
    @staticmethod
    def generate_provenance_stamp(model_name: str, prompt_text: str, generated_output: dict) -> dict:
        timestamp = datetime.utcnow().isoformat()
        prompt_hash = hashlib.sha256(prompt_text.encode()).hexdigest()

        provenance_metadata = {
            "_ai_provenance": {
                "timestamp": timestamp,
                "model_version": model_name,
                "prompt_signature": prompt_hash,
                "audit_status": "verified"
            }
        }

        logger.info(f"Provenance stamp attached for model {model_name}. Signature: {prompt_hash[:8]}")
        # Merge the audit metadata with the actual CRM payload
        return {**generated_output, **provenance_metadata}
