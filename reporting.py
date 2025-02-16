import json
import os

REPORTS_DIR = "reports"

def save_report(results, url):
    """Save scan results to a JSON file."""
    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)

    report_path = os.path.join(REPORTS_DIR, "results.json")

    # Read existing data if file exists
    if os.path.exists(report_path):
        with open(report_path, "r") as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = {}
    else:
        existing_data = {}

    existing_data[url] = results  # Store results under the target URL

    # Write updated data
    with open(report_path, "w") as file:
        json.dump(existing_data, file, indent=4)

    print(f"✅ Report saved: {report_path}")
