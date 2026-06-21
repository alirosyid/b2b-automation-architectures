import jsonschema
from jsonschema import validate

def validate_inbound_webhook(payload):
    # Strict enterprise schema definition
    b2b_schema = {
        "type": "object",
        "properties": {
            "client_id": {"type": "string"},
            "intent_score": {"type": "number"},
            "action": {"type": "string"}
        },
        "required": ["client_id", "action"]
    }
    
    try:
        validate(instance=payload, schema=b2b_schema)
        print("[N8N Gatekeeper] Payload validated successfully. Proceeding to automation queue.")
        return True
    except jsonschema.exceptions.ValidationError as err:
        print(f"[N8N Gatekeeper] 🚫 CRITICAL: Malformed payload blocked. Error: {err.message}")
        return False

if __name__ == "__main__":
    mock_payload = {"client_id": "ENT-001", "intent_score": 85.5, "action": "trigger_invoice"}
    validate_inbound_webhook(mock_payload)
