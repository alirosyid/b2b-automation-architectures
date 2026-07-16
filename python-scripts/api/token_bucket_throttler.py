import time

class TokenBucketThrottler:
    def __init__(self, bucket_capacity, refill_rate_per_sec):
        self.capacity = bucket_capacity
        self.tokens = bucket_capacity
        self.refill_rate = refill_rate_per_sec
        self.last_refill = time.time()

    def request_tokens(self, tokens_needed, client_tier):
        now = time.time()
        time_passed = now - self.last_refill
        
        # Refill bucket
        self.tokens = min(self.capacity, self.tokens + (time_passed * self.refill_rate))
        self.last_refill = now
        
        if self.tokens >= tokens_needed:
            self.tokens -= tokens_needed
            print(f"[API Gateway] ✅ Access granted for {client_tier} client. Tokens remaining: {int(self.tokens)}")
            return True
            
        print(f"[API Gateway] 🛑 429 TOO MANY REQUESTS. {client_tier} client throttled. Bucket empty.")
        return False

if __name__ == "__main__":
    throttler = TokenBucketThrottler(bucket_capacity=100, refill_rate_per_sec=10)
    throttler.request_tokens(90, "Standard") # Pass
    throttler.request_tokens(20, "Standard") # Throttle
