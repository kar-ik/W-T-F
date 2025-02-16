import requests

def check_csrf(url):
    print(f"[*] Checking for CSRF vulnerabilities on {url}...")
    response = requests.get(url)
    if "csrf" not in response.text.lower():
        return "⚠️ Potential CSRF vulnerability detected!"
    return "✅ CSRF protection detected."
