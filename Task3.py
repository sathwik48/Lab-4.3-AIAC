def format_name(full_name):
    parts = full_name.strip().split()
    if len(parts) < 2:
        return full_name  # Return as is if not enough parts
    first = parts[0]
    last = parts[-1]
    return f"{last}, {first}"

# Example usage
names = ["Sathwik Modem", "Nani Puli"]
for name in names:
    print(format_name(name))