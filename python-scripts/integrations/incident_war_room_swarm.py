def orchestrate_war_room(incident_id, failing_service):
    print(f"[Ops] Sev-1 Incident {incident_id} detected. Booting diagnostic agent swarm...")
    
    war_room_channel = f"#incident-{incident_id.lower()}"
    print(f"[+] Slack channel {war_room_channel} created.")
    
    # Swarm data aggregation (Mocked)
    print("    -> Agent 1: Fetching K8s tail logs for latest crash loop...")
    print("    -> Agent 2: Querying Prometheus for CPU/Memory spikes...")
    print("    -> Agent 3: Extracting GitHub diffs for the last 24 hours...")
    
    diagnostic_dashboard = f"""
    🔥 **INCIDENT WAR ROOM: {incident_id}**
    **Service:** {failing_service}
    **Recent Commits:** 2 PRs merged in last 4 hours.
    **Telemetry:** 300% spike in Postgres connections detected prior to failure.
    **Logs:** OOMKilled state confirmed on worker nodes.
    """
    
    print("[+] Unified diagnostic context injected into Slack. Ready for human SRE remediation.")
    return diagnostic_dashboard

if __name__ == "__main__":
    orchestrate_war_room("INC-4921", "n8n-webhook-ingress")
