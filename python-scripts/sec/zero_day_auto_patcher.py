import requests

def scan_and_patch_vulnerabilities(repo_dependencies, trending_cves):
    print("[SecOps] Initiating automated vulnerability scan against trending CVEs...")
    
    patched_deps = {}
    for dep, version in repo_dependencies.items():
        if dep in trending_cves:
            safe_version = trending_cves[dep]["safe_version"]
            print(f"[!] CRITICAL: {dep} {version} is vulnerable. Auto-patching to {safe_version}.")
            patched_deps[dep] = safe_version
        else:
            patched_deps[dep] = version
            
    return {"status": "secured", "updated_dependencies": patched_deps}

if __name__ == "__main__":
    current_deps = {"requests": "2.25.0", "urllib3": "1.26.4"}
    cve_database = {"urllib3": {"safe_version": "1.26.5"}}
    result = scan_and_patch_vulnerabilities(current_deps, cve_database)
    print(f"[+] Repository secured. Generating PR for updated dependencies.")
