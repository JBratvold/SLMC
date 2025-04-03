# filters.py

def get_type_name(type_id, TYPE_NAMES):
    return TYPE_NAMES.get(type_id, f"Unknown Item (ID: {type_id})")

def format_number(value, decimals=2):
    try:
        return f"{value:,.{decimals}f}"
    except ValueError:
        return value  # If the value isn't a number, return it as-is
