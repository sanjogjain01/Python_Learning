# Program to check if a string contains any special character

def contains_special_character(input_string):
    # Define a set of special characters
    special_characters = set('!@#$%^&*()-_+=[]{}|;:,.<>?/`~')

    # Check if any character in the string is a special character
    for char in input_string:
        if char in special_characters:
            return True

    # If no special characters are found, return False
    return False

# Example usage
input_string = input("Enter a string: ")

if contains_special_character(input_string):
    print("The string contains at least one special character.")
else:
    print("The string does not contain any special characters.")