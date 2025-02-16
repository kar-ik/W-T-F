import requests

def check_headers(url):
    print(f"[*] Checking HTTP security headers on {url}...")
    response = requests.get(url)
    headers = response.headers

    missing_headers = []
    required_headers = ["Content-Security-Policy", "X-Frame-Options", "Strict-Transport-Security"]

    for header in required_headers:
        if header not in headers:
            missing_headers.append(header)

    if missing_headers:
        return f"⚠️ Missing security headers: {', '.join(missing_headers)}"
    return "✅ All essential security headers are present."
