def summarize_execution_error(stack_trace):
    print("[Ops] Parsing raw execution stack trace...")
    
    # Mocking LLM summarization logic
    if "ECONNRESET" in stack_trace:
        summary = "The third-party CRM server forcibly closed the connection. Likely a rate limit or server outage on their end."
        fix = "Implement exponential backoff in the n8n HTTP Request node."
    else:
        summary = "Unknown execution error."
        fix = "Manual inspection required."
        
    alert_payload = f"🚨 **N8N Failure Alert**\n**Issue:** {summary}\n**Action:** {fix}"
    print(f"[Ops] Dispatching summary to SRE Slack channel...\n{alert_payload}")
    return alert_payload

if __name__ == "__main__":
    raw_error = "Error: write ECONNRESET at WriteWrap.onWriteComplete [as oncomplete] (internal/stream_base_commons.js:94:16)"
    summarize_execution_error(raw_error)
