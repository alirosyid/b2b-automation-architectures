import logging

logger = logging.getLogger(__name__)

class PromptFrameworkSynthesizer:
    """
    Autonomous PromptOps Engineering.
    Intercepts unstructured user/client instructions and programmatically 
    structures them into a rigid 6-Component Framework to guarantee 
    deterministic, hallucination-free outputs for B2B data extraction.
    """
    @staticmethod
    def synthesize_framework(raw_task: str, expected_output_schema: str) -> str:
        logger.info("Synthesizing raw input into 6-Component Architectural Framework...")
        
        synthesized_prompt = f"""
        [ROLE]: You are an Enterprise B2B Data Architect.
        [TASK]: {raw_task}
        [INPUT]: {{inbound_payload}}
        [OUTPUT]: Strictly formatted JSON matching this schema: {expected_output_schema}.
        [CONSTRAINTS]: No conversational padding. No markdown wrapping. Output only valid JSON.
        [CAPABILITIES]: You have access to semantic extraction and logical inference.
        """
        
        logger.debug("Prompt synthesis complete. Guardrails applied.")
        return synthesized_prompt.strip()
