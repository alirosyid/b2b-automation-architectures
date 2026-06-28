import time
import random

def execute_with_exponential_backoff(target_func, max_retries=5, base_delay=1.0):
    for attempt in range(max_retries):
        try:
            print(f"[API] Attempting webhook execution (Try {attempt + 1})...")
            return target_func()
        except Exception as e:
            if attempt == max_retries - 1:
                print(f"[API] ❌ Max retries reached. Execution failed: {e}")
                raise
                
            # Exponential backoff with jitter to prevent thundering herd problem
            delay = (base_delay * (2 ** attempt)) + random.uniform(0, 1)
            print(f"[API] ⚠️ Execution failed. Retrying in {delay:.2f} seconds...")
            time.sleep(delay)

def mock_flaky_webhook():
    if random.random() < 0.7:
        raise ConnectionError("503 Service Unavailable")
    return "200 OK"

if __name__ == "__main__":
    try:
        execute_with_exponential_backoff(mock_flaky_webhook)
    except Exception:
        pass
