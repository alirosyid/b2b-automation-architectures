import logging
from jsonschema import validate, ValidationError

logger = logging.getLogger(__name__)

class DataContractEnforcer:
    """
    Enforces strict data contracts for all incoming B2B webhooks.
    Detects 'Schema Drift' (unannounced payload changes by client CRMs) 
    to prevent pipeline crashes, API errors, and database corruption.
    """
    # Define the immutable contract for incoming leads
    B2B_LEAD_SCHEMA = {
        "type": "object",
        "properties": {
            "client_id": {"type": "string"},
            "lead_email": {"type": "string", "format": "email"},
            "company_size": {"type": "integer"}
        },
        "required": ["client_id", "lead_email"]
    }

    @classmethod
    def validate_payload(cls, payload: dict) -> bool:
        try:
            validate(instance=payload, schema=cls.B2B_LEAD_SCHEMA)
            logger.info("Data contract validation passed. Payload is safe to process.")
            return True
        except ValidationError as e:
            logger.critical(f"Schema Drift Detected! Contract violation: {e.message}")
            # Production: Trigger high-priority n8n webhook to alert the DevOps team
            return False
