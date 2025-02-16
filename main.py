import argparse
import os
import subprocess
import threading
import time
from tqdm import tqdm
from scanners.sql_injection import scan_sql_injection
from scanners.xss import scan_xss
from scanners.csrf import check_csrf
from scanners.headers import check_headers
from scanners.dir_bruteforce import brute_force_dirs
from reporting import save_html_report

BANNER = """\033[1;32m
=========================================
      ________________________________ 
     |               |                | 
     | $$    $$      | $$    $$       |
     | $$   $$       | $$   $$        |
     | $$  $$        | $$  $$         |
     | $$$$$         | $$$$$          |
     | $$  $$        | $$  $$         |
     | $$   $$       | $$   $$        |
     | $$    $$      | $$    $$       |
     
  🔥 Website Security Scanner v1.2 🔥  
  Automated Web Security Testing Tool  
=========================================
\033[0m"""

def update_tool():
    """Pulls the latest updates from GitHub."""
    print("\033[1;34m[*] Checking for updates...\033[0m")
    try:
        if not os.path.exists(".git"):
            print("\033[1;31m[!] This tool is not cloned from a Git repository. Cannot update.\033[0m")
            return
        
        subprocess.run(["git", "pull"], check=True)
        print("\033[1;32m[✔] Tool updated successfully!\033[0m")
    except Exception as e:
        print(f"\033[1;31m[!] Update failed: {e}\033[0m")

def run_scans_in_parallel(scan_tasks, depth):
    """Runs multiple security scans in parallel and prints results."""
    threads = []
    results = {}

    def scan_task(name, func, url):
        print(f"\n\033[1;34m[*] Running {name} (Depth: {depth})...\033[0m")
        results[name] = func(url, depth)  
        print(f"\033[1;32m[✔] {name} Completed!\033[0m")
        print(f"\033[1;33m[Result:]\033[0m {results[name]}")  

    for name, func, url in scan_tasks:
        thread = threading.Thread(target=scan_task, args=(name, func, url))
        threads.append(thread)
        thread.start()

    with tqdm(total=len(threads), desc="Running Scans", bar_format="{l_bar}{bar} {n_fmt}/{total_fmt}") as pbar:
        for thread in threads:
            thread.join() 
            pbar.update(1)

    return results

def main():
    print(BANNER)  

    parser = argparse.ArgumentParser(description="Website Security Testing Tool")
    parser.add_argument("url", nargs="?", help="Target URL to scan")
    parser.add_argument("--sql", action="store_true", help="Scan for SQL Injection")
    parser.add_argument("--xss", action="store_true", help="Scan for XSS vulnerabilities")
    parser.add_argument("--csrf", action="store_true", help="Check for CSRF vulnerabilities")
    parser.add_argument("--headers", action="store_true", help="Check for missing security headers")
    parser.add_argument("--brute", action="store_true", help="Bruteforce hidden directories")
    parser.add_argument("--report", action="store_true", help="Save scan results to an HTML report")
    parser.add_argument("--update", action="store_true", help="Update the tool to the latest version")

    parser.add_argument("--depth", type=int, choices=[1, 2, 3], default=2,
                        help="Set scan depth: 1 (Shallow), 2 (Medium - Default), 3 (Deep)")

    args = parser.parse_args()
    
    if args.update:
        update_tool()
        return  

    if not args.url:
        print("\033[1;31m[!] Please provide a target URL.\033[0m")
        parser.print_help()
        return

    url = args.url
    scan_tasks = []
    depth = args.depth  

    if args.sql:
        scan_tasks.append(("SQL Injection Scan", scan_sql_injection, url))
    if args.xss:
        scan_tasks.append(("XSS Scan", scan_xss, url))
    if args.csrf:
        scan_tasks.append(("CSRF Check", check_csrf, url))
    if args.headers:
        scan_tasks.append(("Security Headers Check", check_headers, url))
    if args.brute:
        scan_tasks.append(("Directory Bruteforcing", brute_force_dirs, url))

    scan_results = {"target": url, "results": run_scans_in_parallel(scan_tasks, depth)}

    if args.report:
        save_html_report(scan_results, url)

if __name__ == "__main__":
    main()

