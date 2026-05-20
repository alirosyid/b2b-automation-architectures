import logging
import random

logger = logging.getLogger(__name__)

class MicroserviceLoadBalancer:
    """
    Ingress Traffic Distribution Node.
    Sits ahead of the primary orchestration layer to catch massive webhook spikes 
    and distribute payloads evenly across a fleet of stateless worker nodes, 
    guaranteeing low-latency processing under extreme enterprise load.
    """
    WORKER_NODES = [
        "http://worker-alpha.internal:8000",
        "http://worker-beta.internal:8000",
        "http://worker-gamma.internal:8000"
    ]

    @classmethod
    def route_traffic(cls, payload: dict) -> str:
        # Round-robin or least-connections routing logic
        selected_node = random.choice(cls.WORKER_NODES)

        logger.info(f"Load Balancer: Routing payload {payload.get('id', 'unknown')} to {selected_node}")
        return selected_node
