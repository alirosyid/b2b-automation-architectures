import time

def trace_workflow_execution(workflow_id, execution_steps):
    print(f"[Ops] Initializing OpenTelemetry tracing for workflow: {workflow_id}")
    
    total_latency = 0
    bottlenecks = []
    
    for step in execution_steps:
        # Mocking distributed tracing spans
        step_latency = step.get("latency_ms", 0)
        total_latency += step_latency
        
        if step_latency > 500:
            print(f"    ⚠️ Warning: High latency detected in span '{step['name']}' ({step_latency}ms)")
            bottlenecks.append(step['name'])
            
    print(f"[+] Trace complete. Total Execution Time: {total_latency}ms")
    
    if bottlenecks:
        print(f"[!] Alerting SRE team. Optimize the following nodes: {bottlenecks}")
        return {"status": "degraded", "bottlenecks": bottlenecks}
        
    return {"status": "optimal"}

if __name__ == "__main__":
    spans = [
        {"name": "Webhook Ingress", "latency_ms": 45},
        {"name": "LLM Entity Extraction", "latency_ms": 1200}, # Bottleneck
        {"name": "CRM Sync", "latency_ms": 110}
    ]
    trace_workflow_execution("B2B_Lead_Routing_v2", spans)
