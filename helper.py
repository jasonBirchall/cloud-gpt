import
def check_key(key):
    """Check for existence of key"""
    if key not in os.environ:
        print(f"Please set {key}.")
        sys.exit(1)
