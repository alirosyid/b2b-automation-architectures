class WebhookDebouncer:
    def __init__(self):
        # Mocks a Redis distributed cache with TTL
        self.processed_event_ids = set()

    def is_duplicate(self, event_id):
        print(f"[API Gateway] Verifying idempotency for event: {event_id}...")
        
        if event_id in self.processed_event_ids:
            print(f"[!] 🛑 DUPLICATE DETECTED. Dropping payload to prevent pipeline corruption.")
            return True
            
        print(f"[+] Event is unique. Registering {event_id} to idempotency cache.")
        self.processed_event_ids.add(event_id)
        return False

if __name__ == "__main__":
    debouncer = WebhookDebouncer()
    debouncer.is_duplicate("evt_stripe_9942a") # First pass
    debouncer.is_duplicate("evt_stripe_9942a") # Network retry (Dropped)
