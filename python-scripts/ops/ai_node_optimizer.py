import psutil
import time

def monitor_and_scale_nodes(cpu_threshold=10.0, idle_time_limit=300):
    idle_time = 0
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        if cpu_usage < cpu_threshold:
            idle_time += 1
            print(f"[Ops] Low traffic detected. Idle time: {idle_time}s")
        else:
            idle_time = 0
            
        if idle_time >= idle_time_limit:
            print("[Ops] 📉 Idle limit reached. Scaling down inactive compute nodes to save costs.")
            _trigger_cloud_scale_down()
            idle_time = 0
            
        time.sleep(1)

def _trigger_cloud_scale_down():
    # Placeholder for AWS Auto Scaling / Kubernetes API call
    pass

if __name__ == "__main__":
    print("[Ops] Booting AI Server Cost Optimizer...")
    # monitor_and_scale_nodes() # Uncomment to run daemon
