def triage_slack_to_github(slack_message, reporter):
    print(f"[ChatOps] Parsing engineering channel message from @{reporter}...")
    
    # Keywords indicating a bug report rather than casual conversation
    if "error" in slack_message.lower() or "traceback" in slack_message.lower() or "bug" in slack_message.lower():
        print("[+] Bug context detected. Auto-generating GitHub Issue...")
        
        # Mocking LLM extraction and GitHub API Push
        github_issue = {
            "title": f"Auto-Triage: Bug reported by {reporter}",
            "body": f"**Reporter:** @{reporter}\n**Raw Log:**\n```\n{slack_message}\n```\n**Suggested Labels:** `bug`, `needs-triage`",
            "assignee": "on-call-engineer"
        }
        
        print(f"[+] Successfully pushed to GitHub: Issue #1042 created on active sprint board.")
        return github_issue
        
    return None

if __name__ == "__main__":
    msg = "Getting a 500 error on the /enrich endpoint. Traceback shows a Redis connection timeout."
    triage_slack_to_github(msg, "dev_josh")
