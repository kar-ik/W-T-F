def scan_sql_injection(url, depth):
    """Simulates SQL Injection scanning based on depth level."""
    if depth == 1:
        return "Basic SQL Injection Check (Fast Mode)"
    elif depth == 2:
        return "Medium-Level SQL Injection Testing"
    elif depth == 3:
        return "Deep SQL Injection Testing (Slow & Comprehensive)"
