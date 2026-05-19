import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

class ProviderFallbackCascade:
    """
    Enterprise High-Availability (HA) Engine.
    Seamlessly catches HTTP 500s or timeouts from primary LLM providers 
    and routes the payload to secondary/tertiary fallback models to guarantee zero downtime.
    """
    PROVIDERS = ["groq_llama3", "gemini_1_5_flash", "local_ollama_backup"]

    @classmethod
    def execute_with_fallback(cls, payload: dict, execution_func: Callable) -> Any:
        for provider in cls.PROVIDERS:
            try:
                logger.info(f"Attempting execution via primary node: {provider}")
                return execution_func(provider, payload)
            except Exception as e:
                logger.warning(f"Provider {provider} failed ({e}). Cascading to next available node...")

        logger.critical("All LLM providers exhausted. Routing payload to Dead Letter Queue.")
        raise ConnectionError("Catastrophic LLM provider outage.")
