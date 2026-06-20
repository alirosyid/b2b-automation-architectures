class GlobalRateLimiter:
    def __init__(self, max_requests_per_minute):
        self.max_requests = max_requests_per_minute
        self.current_requests = 0 # In production, this syncs with a Redis cluster

    def request_execution_token(self, worker_id):
        if self.current_requests < self.max_requests:
            self.current_requests += 1
            print(f"[Integrations] Token granted to {worker_id}. ({self.current_requests}/{self.max_requests} used)")
            return True
        else:
            print(f"[Integrations] RATE LIMIT REACHED. {worker_id} request queued to prevent 429 errors.")
            return False

if __name__ == "__main__":
    limiter = GlobalRateLimiter(max_requests_per_minute=100)
    limiter.current_requests = 99
    limiter.request_execution_token("n8n_worker_1")
    limiter.request_execution_token("n8n_worker_2") # This will be blocked
