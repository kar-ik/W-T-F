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
from reporting import save_report, save_html_report

BANNER = """\033[1;32m
=========================================
      __    __        __    __ 
     |  \  /  \      |  \  /  \
     | $$ /  $$      | $$ /  $$
     | $$/  $$       | $$/  $$ 
     | $$  $$        | $$  $$  
     | $$$$$\        | $$$$$\  
     | $$ \$$\       | $$ \$$\ 
     | $$  \$$\      | $$  \$$\
      \$$   \$$       \$$   \$$

  🔥 Website Security Scanner v1.0 🔥  
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

def progress_task(task_name, func, *args):
    """Shows a progress bar while running a task in a separate thread."""
    print(f"\n\033[1;34m[*] Running {task_name}...\033[0m")

    result = None  
    def run_func():
        nonlocal result
        result = func(*args)

    thread = threading.Thread(target=run_func)
    thread.start()

    with tqdm(total=100, desc=f"{task_name}", bar_format="{l_bar}{bar} {n_fmt}/{total_fmt}") as pbar:
        while thread.is_alive():
            time.sleep(0.5) 
            pbar.update(10 if pbar.n < 90 else 100 - pbar.n) 

    thread.join()  
    print(f"\033[1;32m[✔] {task_name} Completed!\033[0m\n")
    return result

def main():
    print(BANNER)  

    parser = argparse.ArgumentParser(description="Website Security Testing Tool")
    parser.add_argument("url", nargs="?", help="Target URL to scan")
    parser.add_argument("--sql", action="store_true", help="Scan for SQL Injection")
    parser.add_argument("--xss", action="store_true", help="Scan for XSS vulnerabilities")
    parser.add_argument("--csrf", action="store_true", help="Check for CSRF vulnerabilities")
    parser.add_argument("--headers", action="store_true", help="Check for missing security headers")
    parser.add_argument("--brute", action="store_true", help="Bruteforce hidden directories")
    parser.add_argument("--report", action="store_true", help="Save scan results to a report")
    parser.add_argument("--update", action="store_true", help="Update the tool to the latest version")

    args = parser.parse_args()
    
    if args.update:
        update_tool()
        return  

    if not args.url:
        print("\033[1;31m[!] Please provide a target URL.\033[0m")
        parser.print_help()
        return

    url = args.url
    scan_results = {"target": url, "results": {}}

    if args.sql:
        scan_results["results"]["SQL Injection"] = progress_task("SQL Injection Scan", scan_sql_injection, url)

    if args.xss:
        scan_results["results"]["XSS"] = progress_task("XSS Scan", scan_xss, url)

    if args.csrf:
        scan_results["results"]["CSRF"] = progress_task("CSRF Check", check_csrf, url)

    if args.headers:
        scan_results["results"]["Security Headers"] = progress_task("Security Headers Check", check_headers, url)

    if args.brute:
        scan_results["results"]["Directory Bruteforce"] = progress_task("Directory Bruteforcing", brute_force_dirs, url)

    if args.report:
        save_report(scan_results, url)
        save_html_report(scan_results, url)

if __name__ == "__main__":
    main()
