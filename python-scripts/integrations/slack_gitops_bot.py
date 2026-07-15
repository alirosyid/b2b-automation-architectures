def execute_slack_deployment(user_id, command_text, authorized_users):
    print(f"[ChatOps] Inbound deployment command received from @{user_id}: '{command_text}'")
    
    if user_id not in authorized_users:
        print("[-] 🛑 Authorization failed. User lacks deployment privileges.")
        return "You are not authorized to trigger production deployments."
        
    if "deploy to production" in command_text.lower():
        print("[+] Authorization verified. Initiating GitOps production rollout...")
        
        # Mocking CI/CD trigger (e.g., GitHub Actions API)
        print("    -> Running test suite...")
        print("    -> Merging 'staging' into 'main'...")
        print("    -> Invalidating Cloudflare cache...")
        
        success_message = "✅ Deployment successful. Production infrastructure is now running the latest commit."
        print(f"[+] Outputting success logs to Slack channel.")
        return success_message

if __name__ == "__main__":
    execute_slack_deployment("lead_engineer", "/ops deploy to production", ["lead_engineer", "cto"])
