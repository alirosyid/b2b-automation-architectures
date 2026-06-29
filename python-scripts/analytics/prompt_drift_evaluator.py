def evaluate_prompt_drift(baseline_score, current_outputs):
    print("[Analytics] Evaluating production LLM outputs against baseline quality...")
    
    # Mock scoring logic (e.g., using BLEU/ROUGE or LLM-as-a-judge)
    current_average_score = sum(current_outputs) / len(current_outputs)
    drift_variance = baseline_score - current_average_score
    
    if drift_variance > 0.15:
        print(f"[!] PROMPT DRIFT DETECTED. Quality dropped by {drift_variance*100:.1f}%.")
        print("    -> Alerting Prompt Engineering team for template optimization.")
        return "Drift Detected"
        
    print("[+] Model output quality is stable.")
    return "Stable"

if __name__ == "__main__":
    # Baseline was 0.95. Current recent scores dropped to ~0.75
    evaluate_prompt_drift(0.95, [0.72, 0.76, 0.70, 0.81])
