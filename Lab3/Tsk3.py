# Step 1: Basic power bill calculation
def calculate_power_bill(units, rate_per_unit):
    """
    Calculate the power bill based on units consumed and rate per unit.
    """
    return units * rate_per_unit

# Step 2: Add minimum bill and fixed charge
def calculate_power_bill_with_fixed(units, rate_per_unit, fixed_charge=50, minimum_bill=100):
    """
    Calculate the power bill with a fixed charge and minimum bill amount.
    """
    bill = units * rate_per_unit + fixed_charge
    return max(bill, minimum_bill)

# Step 3: Add slab-wise billing
def calculate_power_bill_slab(units):
    """
    Calculate the power bill using slab rates:
    - First 100 units: 5 per unit
    - Next 100 units: 8 per unit
    - Above 200 units: 10 per unit
    Fixed charge: 50
    Minimum bill: 100
    """
    fixed_charge = 50
    minimum_bill = 100
    bill = 0

    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 8
    else:
        bill = 100 * 5 + 100 * 8 + (units - 200) * 10

    bill += fixed_charge
    return max(bill, minimum_bill)

# Example usage:
if __name__ == "__main__":
    try:
        units = float(input("Enter units consumed: "))
        print("Simple bill:", calculate_power_bill(units, 5))
        print("Bill with fixed charge:", calculate_power_bill_with_fixed(units, 5))
        print("Slab-wise bill:", calculate_power_bill_slab(units))
    except ValueError:
        print("Invalid input. Please enter a numeric value for units.")
