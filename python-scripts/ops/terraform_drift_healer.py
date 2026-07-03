import subprocess
import os

def check_and_heal_terraform_drift(github_repo):
    """Runs terraform plan, detects drift, and auto-generates a healing PR."""
    result = subprocess.run(["terraform", "plan", "-detailed-exitcode"], capture_output=True, text=True)
    
    if result.returncode == 2: # 2 means drift detected
        print("Terraform drift detected! Generating remediation patch...")
        drift_details = result.stdout
        
        # Here you would pass 'drift_details' to an LLM to generate the updated .tf code
        # For safety, the LLM creates a PR rather than auto-applying
        
        pr_branch = "auto-heal-tf-drift"
        os.system(f"git checkout -b {pr_branch}")
        # Assuming LLM updated the main.tf file
        os.system("git add main.tf && git commit -m 'chore: auto-heal terraform drift'")
        os.system(f"git push origin {pr_branch}")
        
        # Create PR via GitHub CLI
        os.system('gh pr create --title "Automated TF Drift Remediation" --body "Detected manual cloud changes. Please review code sync."')
        print("Remediation PR created.")
    else:
        print("Infrastructure matches state. No drift detected.")
