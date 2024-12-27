def list_sum(numbers):
    return sum(numbers)

def list_average(numbers):
    return sum(numbers) / len(numbers)

def list_max(numbers):
    return max(numbers)

def reverse_list(my_list):
    return my_list[::-1]

# Example usage
numbers = [1, 5, 3, 8, 2]
print(f"Sum: {list_sum(numbers)}")  # Output: Sum: 19
print(f"Average: {list_average(numbers)}")  # Output: Average: 3.8
print(f"Maximum: {list_max(numbers)}")  # Output: Maximum: 8

my_list = ['a', 'b', 'c']
print(reverse_list(my_list))  # Output: ['c', 'b', 'a']
