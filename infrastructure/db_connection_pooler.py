import time

class ConnectionPooler:
    def __init__(self, max_connections=50):
        self.max_connections = max_connections
        self.active_connections = 0

    def request_connection(self, worker_id):
        while self.active_connections >= self.max_connections:
            print(f"[Infra] Pool exhausted. {worker_id} is waiting in queue...")
            time.sleep(0.5) # Wait for a connection to free up
            
        self.active_connections += 1
        print(f"[Infra] Connection granted to {worker_id}. ({self.active_connections}/{self.max_connections} active)")
        return True

    def release_connection(self, worker_id):
        self.active_connections = max(0, self.active_connections - 1)
        print(f"[Infra] Connection released by {worker_id}.")

if __name__ == "__main__":
    pool = ConnectionPooler(max_connections=2)
    pool.request_connection("Serverless_Node_1")
    pool.request_connection("Serverless_Node_2")
    # pool.request_connection("Serverless_Node_3") # This would block until release
    pool.release_connection("Serverless_Node_1")
