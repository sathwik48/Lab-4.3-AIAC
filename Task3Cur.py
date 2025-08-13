def format_name(full_name):
    """
    Formats a full name as 'Last,First'.
    Assumes the full name consists of two parts: First Last.
    """
    parts = full_name.strip().split()
    if len(parts) != 2:
        return "Invalid input. Please enter a first and last name."
    first, last = parts
    return f"{last},{first}"

# Example usage:
if __name__ == "__main__":
    name = input("Enter full name (First Last): ")
    formatted = format_name(name)
    print(formatted)
