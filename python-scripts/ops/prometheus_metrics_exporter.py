import time

class PrometheusExporter:
    def __init__(self):
        # Mocking Prometheus Gauge/Histogram registries
        self.api_latency_metric = []
        self.llm_call_count = 0

    def record_llm_latency(self, duration_ms):
        print(f"[Ops] Exporting SRE telemetry: LLM API Latency = {duration_ms}ms")
        self.api_latency_metric.append(duration_ms)
        self.llm_call_count += 1
        
        if duration_ms > 2000:
            print("[!] ⚠️ HIGH LATENCY DETECTED. Flagging telemetry for Grafana alerting.")
            
        return True

if __name__ == "__main__":
    exporter = PrometheusExporter()
    
    # Simulating API execution
    start = time.time()
    time.sleep(0.4) # Simulated network call
    end = time.time()
    
    exporter.record_llm_latency(int((end - start) * 1000))
