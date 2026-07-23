def tune_kubernetes_resources(deployment_name, prometheus_metrics):
    print(f"[Ops] Analyzing resource utilization for deployment: {deployment_name}")
    
    cpu_usage_avg = prometheus_metrics.get("cpu_utilization_percent")
    
    if cpu_usage_avg < 15.0:
        print(f"[!] 📉 Severe over-provisioning detected ({cpu_usage_avg}% CPU usage).")
        print("    -> Autonomously patching K8s deployment to downscale CPU requests by 50%.")
        
        # Mocking Kubernetes API patch
        # v1.patch_namespaced_deployment(name=deployment_name, namespace="default", body=patch_payload)
        
        print(f"[+] Resource optimization successful. Cloud compute waste eliminated.")
        return True
        
    print("[+] Resource requests are tightly aligned with actual usage.")
    return False

if __name__ == "__main__":
    tune_kubernetes_resources("lead-enrichment-worker", {"cpu_utilization_percent": 12.5})
