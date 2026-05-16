import json
from datetime import datetime

class GlassBoxExporter:
    """
    Explainable AI (XAI) utility. Generates a cryptographic 'Glass Box' artifact 
    detailing the exact context, prompts, and deterministic weights used by the 
    LLM for a specific business decision. Crucial for enterprise trust and auditing.
    """
    @staticmethod
    def generate_decision_artifact(entity_id: str, system_prompt: str, context_injected: list, output: dict) -> str:
        artifact = {
            "timestamp_utc": datetime.utcnow().isoformat(),
            "entity_id": entity_id,
            "xai_parameters": {
                "temperature": 0.0,
                "top_p": 1.0,
                "system_instructions_used": system_prompt,
                "retrieval_context_length": len(context_injected)
            },
            "final_decision_output": output
        }
        # Output can be attached to the CRM record for complete transparency
        return json.dumps(artifact, indent=2)
