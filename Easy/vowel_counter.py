def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in input_string if char in vowels)

# Example usage
input_string = "aeiouAEIOU"
vowel_count = count_vowels(input_string)
print(vowel_count)  # Output: 3
