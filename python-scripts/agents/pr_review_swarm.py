def execute_swarm_code_review(pr_diff_text):
    print("[Swarm] Pull Request opened. Engaging Multi-Agent Code Review Swarm...")
    
    # Swarm Agent 1: Security
    if "eval(" in pr_diff_text or "os.system(" in pr_diff_text:
        sec_approval = False
        print("    -> 🛡️ Security Agent: REJECTED. Unsafe evaluation of arbitrary code detected.")
    else:
        sec_approval = True
        
    # Swarm Agent 2: Logic & Efficiency
    if "for i in range(len(list))" in pr_diff_text:
        logic_comment = "Logic Agent: Consider using `enumerate()` for more Pythonic iteration."
        print(f"    -> ⚙️ {logic_comment}")
        
    if sec_approval:
        print("[+] Swarm consensus reached. Approving PR with non-blocking suggestions.")
        return True
    else:
        print("[-] 🛑 Swarm consensus blocked. Blocking merge until security flaws are resolved.")
        return False

if __name__ == "__main__":
    mock_diff = "def process_data(data):\n    eval(data['command'])"
    execute_swarm_code_review(mock_diff)
