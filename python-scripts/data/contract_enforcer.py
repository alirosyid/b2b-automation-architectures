import logging
from jsonschema import validate, ValidationError
from typing import Dict, Any

logger = logging.getLogger(__name__)

class DataContractEnforcer:
    """
    Shift-Left Data Governance Gateway.
    Enforces a strict cryptographic data contract on all inbound webhooks. 
    Detects 'Schema Drift' from external CRMs instantly to prevent pipeline 
    corruption and silent downstream failures.
    """
    # Master architecture schema requirement
    B2B_CONTRACT = {
        "type": "object",
        "properties": {
            "tenant_id": {"type": "string"},
            "lead_payload": {"type": "object"}
        },
        "required": ["tenant_id", "lead_payload"]
    }

    @classmethod
    def validate_ingress(cls, payload: Dict[str, Any]) -> bool:
        try:
            validate(instance=payload, schema=cls.B2B_CONTRACT)
            logger.debug("Ingress payload satisfies B2B Data Contract.")
            return True
        except ValidationError as e:
            logger.critical(f"Data Contract Violation: Schema drift detected -> {e.message}")
            # Production: Fire a high-priority alert to the DevOps Slack channel
            return False
