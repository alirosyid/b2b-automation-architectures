import logging
import agentops
from typing import Callable, Any

logger = logging.getLogger(__name__)

class AgentOpsTelemetryLogger:
    """
    AI Financial Auditing and Observability.
    Wraps critical B2B enrichment functions with AgentOps telemetry.
    Automatically logs token consumption, latency, and exact API costs to a 
    centralized dashboard to strictly monitor agency profit margins.
    """
    def __init__(self, agentops_api_key: str):
        # Initializes the global session tracker
        agentops.init(agentops_api_key, tags=["b2b_enrichment_pipeline"])
        logger.info("AgentOps observability session initialized.")

    @staticmethod
    def track_execution(func: Callable, *args, **kwargs) -> Any:
        # AgentOps automatically instruments LLM calls within this block
        logger.debug(f"Tracking agentic execution for {func.__name__}...")
        
        try:
            result = func(*args, **kwargs)
            logger.info("Execution complete. Telemetry flushed to AgentOps dashboard.")
            return result
        except Exception as e:
            logger.error(f"Tracked execution failed. Error logged to observability sink: {e}")
            raise
        finally:
            agentops.end_session("Success")
