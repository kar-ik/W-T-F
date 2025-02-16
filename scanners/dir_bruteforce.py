def brute_force_dirs(url, depth=2):
    """Simulates directory bruteforcing based on depth level."""
    if depth == 1:
        return "Quick directory scan completed"
    elif depth == 2:
        return "Medium-Level directory bruteforcing"
    elif depth == 3:
        return "Deep directory bruteforcing (Slow & Comprehensive)"
