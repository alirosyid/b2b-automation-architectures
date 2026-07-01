def reconcile_payroll_vs_commits(developer_username, billed_hours, github_client):
    commits = github_client.get_user(developer_username).get_commits()
    commit_count_this_month = sum(1 for c in commits) # Simplified metric
    
    # Establish a baseline ratio (e.g., at least 1 commit per billed hour)
    expected_commits = billed_hours * 1.0 
    
    if commit_count_this_month < (expected_commits * 0.5):
        return f"FLAGGED: {developer_username} billed {billed_hours}h but only made {commit_count_this_month} commits."
    
    return "APPROVED: Velocity matches billed hours."
