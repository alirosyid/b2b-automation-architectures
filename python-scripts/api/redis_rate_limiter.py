import time

class RedisRateLimiter:
    def __init__(self, requests_per_minute):
        self.limit = requests_per_minute
        # Mocking Redis connection
        self.redis_cache = {} 

    def check_rate_limit(self, client_ip):
        print(f"[API Ops] Verifying sliding-window rate limit for IP: {client_ip}")
        
        current_time = int(time.time())
        window_start = current_time - 60
        
        # Simulate Redis ZREMRANGEBYSCORE and ZCARD
        request_timestamps = self.redis_cache.get(client_ip, [])
        valid_requests = [ts for ts in request_timestamps if ts > window_start]
        
        if len(valid_requests) >= self.limit:
            print(f"[!] 🛑 429 TOO MANY REQUESTS. Rate limit exceeded for {client_ip}.")
            return False
            
        valid_requests.append(current_time)
        self.redis_cache[client_ip] = valid_requests
        print(f"[+] Request authorized. ({len(valid_requests)}/{self.limit} used this minute).")
        return True

if __name__ == "__main__":
    limiter = RedisRateLimiter(requests_per_minute=5)
    limiter.check_rate_limit("192.168.1.100")
