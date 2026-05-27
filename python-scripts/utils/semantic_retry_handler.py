import logging
import re
from typing import Callable, Any

logger = logging.getLogger(__name__)

class SemanticRetryStrategy:
    """
    Context-Aware Pipeline Resilience.
    Analyzes downstream API error signatures (e.g., HTTP 400 Bad Request). 
    Dynamically mutates the outbound payload to correct schema violations 
    (like stripping invalid unicode or truncating long strings) before retrying.
    """
    @classmethod
    def execute_with_semantic_healing(cls, api_call: Callable, payload: dict) -> Any:
        try:
            return api_call(payload)
        except Exception as e:
            error_msg = str(e).lower()
            logger.warning(f"API Execution failed: {error_msg}. Analyzing semantic signature...")
            
            if "invalid character" in error_msg or "emoji" in error_msg:
                logger.info("Applying Semantic Fix: Stripping non-ASCII characters.")
                healed_payload = {k: re.sub(r'[^\x00-\x7F]+', '', str(v)) for k, v in payload.items()}
                return api_call(healed_payload)
                
            if "too long" in error_msg or "max length" in error_msg:
                logger.info("Applying Semantic Fix: Truncating string fields.")
                healed_payload = {k: str(v)[:255] for k, v in payload.items()}
                return api_call(healed_payload)
                
            raise e
