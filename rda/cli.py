import argparse
import yaml
import asyncio
from rda.core.registry import load_all_modules
from rda.core.runner import AsyncAuditRunner
from rda.core.reporters import console_output, generate_sarif

def main():
    parser = argparse.ArgumentParser(description="Red Dragon Audit (RDA) - Enterprise Security Orchestrator")
    parser.add_argument("-c", "--config", required=True, help="Path to target configuration YAML")
    parser.add_argument("--confirm-auth", action="store_true", help="CRITICAL: Confirm you have legal authorization to scan targets")
    parser.add_argument("--sarif", action="store_true", help="Output results in SARIF format for GitHub Security integration")
    
    args = parser.parse_args()

    # The Authorization Gate
    if not args.confirm_auth:
        print("\n[!] FATAL: Authorization Required.")
        print("[!] You must supply the --confirm-auth flag to verify you have explicit, legal permission to audit these targets.")
        print("[!] RDA is a defensive auditing tool. Unauthorized scanning is strictly prohibited.\n")
        exit(1)

    # 1. Load config
    with open(args.config, "r") as f:
        config = yaml.safe_load(f)

    # 2. Dynamically load all modules in the /modules folder
    load_all_modules()

    # 3. Execute Async Runner
    runner = AsyncAuditRunner(config)
    results = asyncio.run(runner.run_all())

    # 4. Report
    if args.sarif:
        generate_sarif(results)
    else:
        console_output(results)

if __name__ == "__main__":
    main()
