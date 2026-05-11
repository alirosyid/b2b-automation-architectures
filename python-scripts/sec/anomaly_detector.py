import logging

logger = logging.getLogger(__name__)

class APIAbuseDetector:
    """
    Heuristic-based anomaly detection. Monitors incoming webhook traffic for 
    suspicious spikes that indicate compromised client credentials or DDoS attempts.
    """
    def __init__(self, spike_threshold_multiplier: float = 5.0):
        self.threshold = spike_threshold_multiplier

    def analyze_traffic(self, client_id: str, current_rpm: int, average_rpm: int) -> bool:
        if average_rpm > 0 and (current_rpm / average_rpm) >= self.threshold:
            logger.critical(f"SECURITY ALERT: Traffic anomaly detected for {client_id}. Freezing API access.")
            # Trigger n8n webhook to alert SecOps via Telegram
            return True # Anomaly detected
        return False
