import logging

logger = logging.getLogger(__name__)

class PipelineProgressBroadcaster:
    """
    Publishes real-time pipeline execution statuses to frontend dashboards via WebSockets.
    Eliminates 'black box' waiting periods for B2B end-users during massive data extractions.
    """
    @staticmethod
    def broadcast_progress(job_id: str, total_items: int, current_item: int):
        percentage = (current_item / total_items) * 100
        payload = {
            "job_id": job_id,
            "status": "processing",
            "progress_percentage": round(percentage, 2)
        }
        # Production: Push to Redis Pub/Sub or directly to WebSocket clients
        if current_item % 100 == 0 or current_item == total_items:
            logger.info(f"WebSocket Broadcast: Job {job_id} is {percentage:.1f}% complete.")
        return payload
