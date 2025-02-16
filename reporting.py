import json
import os

REPORTS_DIR = "reports"

def save_report(results, url):
    """Save scan results to a JSON file."""
    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)

    report_path = os.path.join(REPORTS_DIR, "results.json")

    if os.path.exists(report_path):
        with open(report_path, "r") as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = {}
    else:
        existing_data = {}

    existing_data[url] = results  

    with open(report_path, "w") as file:
        json.dump(existing_data, file, indent=4)

    print(f"✅ Report saved: {report_path}")

def save_html_report(results, url):
    """Save scan results to an HTML file."""
    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)

    html_content = f"""
    <html>
    <head>
        <title>Security Scan Report - {url}</title>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            h2 {{ color: #2E86C1; }}
            .section {{ margin-bottom: 20px; }}
            .vuln {{ color: red; font-weight: bold; }}
        </style>
    </head>
    <body>
        <h1>Security Scan Report</h1>
        <h2>Target: {url}</h2>
        <div class="section">
    """

    for test, result in results["results"].items():
        html_content += f"<h3>{test}</h3>"
        html_content += f"<pre>{result}</pre>"

    html_content += """
        </div>
    </body>
    </html>
    """

    report_path = os.path.join(REPORTS_DIR, "report.html")

    with open(report_path, "w") as file:
        file.write(html_content)

    print(f"✅ HTML Report saved: {report_path}")
