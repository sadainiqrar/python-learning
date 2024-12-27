def calculator(num1, num2, operator):
    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2
    }
    return operations.get(operator, "Invalid operator")

# Example usage
result = calculator(5, 3, '*')
print(result)  # Output: 8
