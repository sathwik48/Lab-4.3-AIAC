def cm_to_inches(cm):
    """
    Convert centimeters to inches.
    1 cm = 0.39 inches (rounded, more precisely 1 cm = 0.3937 inches)
    """
    return cm * 0.39

# Example usage:
try:
    cm_value = float(input("Enter length in centimeters: "))
    inches = cm_to_inches(cm_value)
    print(f"{cm_value} cm is equal to {inches} inches.")
except ValueError:
    print("Please enter a valid number.")
