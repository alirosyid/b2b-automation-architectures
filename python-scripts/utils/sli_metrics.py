class SLIMetricsTracker:
    """
    Melacak Service Level Indicators (SLI) secara real-time untuk memvalidasi
    bahwa Service Level Agreements (SLA) B2B terpenuhi secara hukum.
    """
    def __init__(self):
        self.total_requests = 0
        self.failed_requests = 0

    def record_request(self, success: bool):
        self.total_requests += 1
        if not success:
            self.failed_requests += 1

    def get_current_sli(self) -> float:
        if self.total_requests == 0:
            return 100.0
        success_rate = ((self.total_requests - self.failed_requests) / self.total_requests) * 100
        return round(success_rate, 4)
