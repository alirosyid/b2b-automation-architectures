import numpy as np

def forecast_end_of_month_spend(daily_spend_history, allocated_budget):
    print("[FinOps] Running ARIMA time-series model on cloud expenditure telemetry...")
    
    # Mocking ARIMA (AutoRegressive Integrated Moving Average) prediction
    current_spend = sum(daily_spend_history)
    predicted_trajectory = np.mean(daily_spend_history[-7:]) * 15 # Extrapolating last 7 days to next 15 days
    
    projected_eom_cost = current_spend + predicted_trajectory
    
    print(f"    -> Current Spend: ${current_spend:.2f}")
    print(f"    -> Projected End of Month Spend: ${projected_eom_cost:.2f} (Budget: ${allocated_budget})")
    
    if projected_eom_cost > allocated_budget:
        overage = projected_eom_cost - allocated_budget
        print(f"[!] ⚠️ FinOps Alert: Projected to exceed budget by ${overage:.2f}.")
        print("[+] Triggering autonomous downscaling of non-critical analytics nodes to enforce budget.")
        return {"action": "downscale_infrastructure", "projected_overage": overage}
        
    print("[+] Cost trajectory is stable and within bounds.")
    return {"action": "none"}

if __name__ == "__main__":
    historical_spend = [45, 48, 52, 50, 89, 95, 90] # Spike in last few days
    forecast_end_of_month_spend(historical_spend, allocated_budget=1500)
