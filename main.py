import argparse
from scanners.sql_injection import scan_sql_injection
from scanners.xss import scan_xss
from scanners.csrf import check_csrf
from scanners.headers import check_headers
from scanners.dir_bruteforce import brute_force_dirs
from reporting import save_report

def main():
    parser = argparse.ArgumentParser(description="Website Security Testing Tool")
    parser.add_argument("url", help="Target URL to scan")
    parser.add_argument("--sql", action="store_true", help="Scan for SQL Injection")
    parser.add_argument("--xss", action="store_true", help="Scan for XSS vulnerabilities")
    parser.add_argument("--csrf", action="store_true", help="Check for CSRF vulnerabilities")
    parser.add_argument("--headers", action="store_true", help="Check for missing security headers")
    parser.add_argument("--brute", action="store_true", help="Bruteforce hidden directories")
    parser.add_argument("--report", action="store_true", help="Save scan results to a report")

    args = parser.parse_args()
    
    url = args.url
    scan_results = {"target": url, "results": {}}

    if args.sql:
        scan_results["results"]["SQL Injection"] = scan_sql_injection(url)
    
    if args.xss:
        scan_results["results"]["XSS"] = scan_xss(url)
    
    if args.csrf:
        scan_results["results"]["CSRF"] = check_csrf(url)
    
    if args.headers:
        scan_results["results"]["Security Headers"] = check_headers(url)
    
    if args.brute:
        scan_results["results"]["Directory Bruteforce"] = brute_force_dirs(url)

    # Save report if requested
    if args.report:
        save_report(scan_results, url)

if __name__ == "__main__":
    main()
