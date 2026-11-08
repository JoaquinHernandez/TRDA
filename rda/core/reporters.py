import json

def generate_sarif(results, output_file="rda_results.sarif"):
    sarif_log = {
        "version": "2.1.0",
        "$schema": "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json",
        "runs": [
            {
                "tool": {
                    "driver": {
                        "name": "Red Dragon Audit (RDA)",
                        "informationUri": "https://github.com/your-org/red-dragon-audit",
                        "rules": []
                    }
                },
                "results": []
            }
        ]
    }

    for finding in results:
        # Map RDA status to SARIF levels
        level = "warning" if finding.get("status") == "WARN" else "error"
        if finding.get("status") == "OK":
            continue # Skip clean checks in SARIF

        sarif_log["runs"][0]["results"].append({
            "ruleId": finding.get("check_id", "rda_generic_rule"),
            "level": level,
            "message": {
                "text": f"[{finding.get('module')}] {finding.get('details', 'Misconfiguration detected')}"
            },
            "locations": [{
                "physicalLocation": {
                    "artifactLocation": {"uri": finding.get("target", "global_config")}
                }
            }]
        })

    with open(output_file, 'w') as f:
        json.dump(sarif_log, f, indent=2)
    print(f"[+] SARIF DevSecOps report generated: {output_file}")

def console_output(results):
    for r in results:
        indicator = "✅" if r.get("status") == "OK" else "⚠️" if r.get("status") == "WARN" else "❌"
        print(f"{indicator} [{r.get('module')}] {r.get('check_id')}: {r.get('details')}")
