import os
import re

REPORTS_DIR = "reports"

def sanitize_filename(url):
    """Removes special characters from a URL to use as a valid filename."""
    return re.sub(r'\W+', '_', url)  

def save_html_report(results, url):
    """Save scan results to an HTML file named after the target URL."""
    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)

    filename = sanitize_filename(url) + ".html"
    report_path = os.path.join(REPORTS_DIR, filename)

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

    with open(report_path, "w") as file:
        file.write(html_content)

    print(f"HTML Report saved: {report_path}")
