def analyze_ai_voice_telemetry(call_logs):
    print("[Analytics] Processing conversational telemetry for AI SDR Agents...")
    
    total_calls = len(call_logs)
    interruptions = sum(1 for call in call_logs if call["human_interrupted"] == True)
    avg_duration = sum(call["duration_seconds"] for call in call_logs) / total_calls
    
    interruption_rate = (interruptions / total_calls) * 100
    
    print("--- AI SDR Performance Matrix ---")
    print(f"Average Call Duration: {avg_duration:.1f} seconds")
    print(f"Human Interruption Rate: {interruption_rate:.1f}%")
    
    if interruption_rate > 30.0:
        print("[!] 🚨 High interruption rate detected. Latency or prompt design is failing the Turing Test.")
        print("    -> Flagging system prompt for immediate engineering review.")
        return "Needs Optimization"
        
    print("[+] AI SDR performance is optimal and conversational.")
    return "Stable"

if __name__ == "__main__":
    logs = [
        {"duration_seconds": 120, "human_interrupted": False},
        {"duration_seconds": 15, "human_interrupted": True},
        {"duration_seconds": 22, "human_interrupted": True}
    ]
    analyze_ai_voice_telemetry(logs)
