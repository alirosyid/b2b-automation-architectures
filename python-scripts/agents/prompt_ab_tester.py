import logging
import random

logger = logging.getLogger(__name__)

class PromptABTester:
    """
    PromptOps Revenue Optimization.
    Dynamically routes inbound B2B payloads between competing System Prompts (Control vs. Variant) 
    to mathematically determine which instruction set yields higher data extraction 
    accuracy and downstream commercial conversion rates.
    """
    PROMPTS = {
        "control_v1": "You are a data extractor. Pull the company name.",
        "variant_v2": "Strict JSON extraction. Target: B2B Organization Name."
    }

    @classmethod
    def get_variant(cls, lead_id: str) -> str:
        # Deterministic routing based on lead ID for consistent session tracking
        hash_val = sum(ord(c) for c in lead_id)

        if hash_val % 2 == 0:
            logger.info(f"A/B Test: Routing lead {lead_id} to Control Group (v1).")
            return cls.PROMPTS["control_v1"]
        else:
            logger.info(f"A/B Test: Routing lead {lead_id} to Variant Group (v2).")
            return cls.PROMPTS["variant_v2"]
