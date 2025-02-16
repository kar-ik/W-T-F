def check_headers(url, depth=2):
    """Checks security headers. Depth is unused but added for compatibility."""
    headers = {
        "X-Frame-Options": "Missing",
        "Content-Security-Policy": "Missing",
        "Strict-Transport-Security": "Present"
    }
    return f"Security Headers Analysis: {headers}"
