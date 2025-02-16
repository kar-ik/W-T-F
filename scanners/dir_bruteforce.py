import subprocess

def brute_force_dirs(url):
    print(f"[*] Running directory brute force attack on {url}...")
    command = f"python3 dirsearch/dirsearch.py -u {url} -e php,html,js"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout
