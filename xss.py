import subprocess

def scan_xss(url):
    print(f"[*] Scanning for XSS vulnerabilities on {url}...")
    command = f"python3 XSStrike/xsstrike.py -u {url}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout
