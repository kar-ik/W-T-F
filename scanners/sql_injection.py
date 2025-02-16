import subprocess

def scan_sql_injection(url):
    print(f"[*] Running SQL Injection scan on {url}...")
    command = f"sqlmap -u {url} --batch --dbs"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout
