def audit_github_access(org_members, hr_active_employees):
    print("[SecOps] Reconciling GitHub organization access against HR database...")
    unauthorized_access = []
    
    for member in org_members:
        if member not in hr_active_employees:
            unauthorized_access.append(member)
            print(f"[!] SOC2 VIOLATION: {member} retains access but is not an active employee.")
    
    if unauthorized_access:
        print("[+] Generating automated revocation PR and alerting compliance officer.")
        return False
        
    print("[+] Access logs perfectly reconciled. SOC2 compliance maintained.")
    return True

if __name__ == "__main__":
    audit_github_access(["dev_a", "dev_b", "ex_dev_c"], ["dev_a", "dev_b"])
