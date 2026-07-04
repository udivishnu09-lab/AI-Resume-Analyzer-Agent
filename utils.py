# utils.py

def calculate_percentage(found, total):
    """Calculate percentage safely."""
    if total == 0:
        return 0
    return round((found / total) * 100)


def format_list(items):
    """Return list as comma-separated string."""
    if not items:
        return "None"
    return ", ".join(items)