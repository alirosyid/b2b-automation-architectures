def detect_cost_anomalies(daily_moving_average, current_daily_spend):
    print(f"[FinOps] Analyzing cloud infrastructure spend. DMA: ${daily_moving_average:.2f}")
    
    variance = (current_daily_spend - daily_moving_average) / daily_moving_average
    
    if variance > 0.15:
        spike_amount = current_daily_spend - daily_moving_average
        print(f"[!] 💸 FINOPS ANOMALY: Spend spiked by {variance*100:.1f}% (+${spike_amount:.2f}).")
        print("    -> Triggering PagerDuty/Slack alert for immediate compute audit.")
        return True
        
    print(f"[+] Cloud costs stable. Current spend: ${current_daily_spend:.2f}")
    return False

if __name__ == "__main__":
    detect_cost_anomalies(daily_moving_average=145.00, current_daily_spend=195.50)
