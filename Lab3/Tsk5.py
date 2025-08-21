def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    # Convert input to Celsius first
    if from_unit == 'C':
        celsius = value
    elif from_unit == 'F':
        celsius = (value - 32) * 5/9
    elif from_unit == 'K':
        celsius = value - 273.15
    else:
        raise ValueError("Invalid from_unit. Use 'C', 'F', or 'K'.")

    # Convert from Celsius to target unit
    if to_unit == 'C':
        return celsius
    elif to_unit == 'F':
        return celsius * 9/5 + 32
    elif to_unit == 'K':
        return celsius + 273.15
    else:
        raise ValueError("Invalid to_unit. Use 'C', 'F', or 'K'.")

# Example usage:
print("100 Celsius to Fahrenheit:", convert_temperature(100, 'C', 'F'))
print("32 Fahrenheit to Celsius:", convert_temperature(32, 'F', 'C'))
print("0 Celsius to Kelvin:", convert_temperature(0, 'C', 'K'))