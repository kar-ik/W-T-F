import subprocess

def scan_xss(url, depth=2):
    """Simulates XSS scanning based on depth level."""
    if depth == 1:
        return "Basic XSS Scan (Fast Mode)"
    elif depth == 2:
        return "Medium-Level XSS Testing"
    elif depth == 3:
        return "Deep XSS Testing (Slow & Comprehensive)"
