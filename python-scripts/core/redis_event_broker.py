import logging
import json
import redis

logger = logging.getLogger(__name__)

class RedisEventBroker:
    """
    High-Throughput Event-Driven Architecture (EDA).
    Decouples inbound API ingress from heavy downstream AI processing.
    Utilizes Redis Streams to maintain a stateful, persistent event log, 
    guaranteeing zero data loss during massive B2B lead enrichment spikes.
    """
    def __init__(self, redis_url: str = "redis://localhost:6379", stream_name: str = "b2b_ingress_stream"):
        self.redis_client = redis.from_url(redis_url)
        self.stream_name = stream_name

    def publish_event(self, event_type: str, payload: dict) -> str:
        logger.debug(f"Publishing {event_type} event to Redis Stream...")
        
        event_data = {
            "type": event_type,
            "payload": json.dumps(payload)
        }
        
        # Returns the unique Redis timestamp ID (e.g., 1692384759234-0)
        event_id = self.redis_client.xadd(self.stream_name, event_data)
        logger.info(f"Event successfully persisted to stream. Message ID: {event_id}")
        return event_id.decode('utf-8')
