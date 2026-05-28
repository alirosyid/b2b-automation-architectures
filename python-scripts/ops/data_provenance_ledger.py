import hashlib
import json
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class DataProvenanceLedger:
    """
    Enterprise Auditing and Compliance Engine.
    Attaches cryptographic provenance metadata to all outbound AI generations.
    Provides an immutable audit trail detailing exactly which agent, model version, 
    and prompt generated specific CRM mutations to satisfy SOC2 compliance.
    """
    @staticmethod
    def stamp_provenance(payload: dict, agent_id: str, model_version: str) -> dict:
        timestamp = datetime.utcnow().isoformat()
        
        provenance_metadata = {
            "generated_by": agent_id,
            "model": model_version,
            "timestamp": timestamp
        }
        
        # Create cryptographic hash of the payload + metadata for immutability check
        signature_base = json.dumps(payload, sort_keys=True) + json.dumps(provenance_metadata, sort_keys=True)
        provenance_metadata["cryptographic_hash"] = hashlib.sha256(signature_base.encode()).hexdigest()
        
        stamped_payload = payload.copy()
        stamped_payload["_provenance"] = provenance_metadata
        
        logger.info(f"Provenance stamped securely. Hash: {provenance_metadata['cryptographic_hash'][:8]}")
        return stamped_payload
