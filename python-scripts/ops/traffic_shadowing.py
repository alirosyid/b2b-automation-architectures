import asyncio
import logging
from copy import deepcopy
from typing import Callable, Any

logger = logging.getLogger(__name__)

class TrafficShadowingMiddleware:
    """
    Enterprise 'Dark Launching' Architecture.
    Intercepts live production B2B payloads. Routes the primary payload to the 
    live n8n orchestrator synchronously, while asynchronously dispatching a 
    'shadow' copy to a staging/experimental LLM cluster. 
    Enables zero-risk A/B testing of new AI models on real production data.
    """
    def __init__(self, shadow_endpoint_active: bool = True):
        self.shadow_active = shadow_endpoint_active

    async def route_traffic(self, payload: dict, live_processor: Callable, shadow_processor: Callable) -> Any:
        logger.info("Routing payload to primary production orchestrator.")

        # 1. Execute live production pipeline synchronously
        live_result = await live_processor(payload)

        # 2. Fire-and-forget the shadow pipeline asynchronously to prevent latency
        if self.shadow_active:
            shadow_payload = deepcopy(payload)
            logger.debug("Duplicating live payload for silent staging execution (Dark Launch).")
            asyncio.create_task(self._execute_shadow(shadow_payload, shadow_processor))

        return live_result

    async def _execute_shadow(self, payload: dict, shadow_processor: Callable):
        try:
            # Executes the new, experimental LLM logic without affecting production
            await shadow_processor(payload)
            logger.info("Shadow execution complete. Telemetry logged for CTO review.")
        except Exception as e:
            logger.warning(f"Shadow execution failed: {e}. (Production remains unaffected).")
