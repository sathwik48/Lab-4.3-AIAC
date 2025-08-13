def count_vowels(s):
    """
    Counts the number of vowels in a string.
    Vowels are: a, e, i, o, u (both uppercase and lowercase).
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Example usage:
if __name__ == "__main__":
    test_strings = ["hello", "Sky"]
    for s in test_strings:
        print(f'Number of vowels in "{s}": {count_vowels(s)}')

    # Or prompt user input
    user_input = input("Enter a string: ")
    print(f'Number of vowels in "{user_input}": {count_vowels(user_input)}')
