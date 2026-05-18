import logging
from typing import Dict

logger = logging.getLogger(__name__)

class DynamicPersonaEngine:
    """
    Hyper-Personalization Engine for B2B Outreach.
    Dynamically adjusts the LLM's system prompt and tone based on the 
    target lead's seniority and inferred psychological profile (DISC).
    """
    PERSONAS = {
        "c_level_driver": "Direct, data-driven, ROI-focused. Zero fluff. Max 3 sentences.",
        "vp_analytical": "Detailed, process-oriented, focused on integration and security.",
        "manager_amiable": "Collaborative, team-focused, conversational tone."
    }

    @classmethod
    def select_persona(cls, job_title: str, industry: str) -> str:
        title_lower = job_title.lower()

        if any(role in title_lower for role in ["ceo", "cfo", "founder"]):
            logger.info(f"Target is C-Level ({job_title}). Applying 'Driver' persona.")
            return cls.PERSONAS["c_level_driver"]

        if "vp" in title_lower or "director" in title_lower:
            logger.info(f"Target is Executive ({job_title}). Applying 'Analytical' persona.")
            return cls.PERSONAS["vp_analytical"]

        logger.info("Target is Mid-Level. Applying 'Amiable' persona.")
        return cls.PERSONAS["manager_amiable"]
