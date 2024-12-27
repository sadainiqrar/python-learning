def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Example usage
temperature_c = 25
temperature_f = celsius_to_fahrenheit(temperature_c)
print(f"{temperature_c} Celsius is {temperature_f} Fahrenheit")  # Output: 25 Celsius is 77.0 Fahrenheit

temperature_f = 77
temperature_c = fahrenheit_to_celsius(temperature_f)
print(f"{temperature_f} Fahrenheit is {temperature_c} Celsius")  # Output: 77 Fahrenheit is 25.0 Celsius
