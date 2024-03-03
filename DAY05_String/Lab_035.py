# Python program to remove duplicate characters from a string

input_string = input("Enter a string: ")

result_string = ""
for char in input_string:
    if char not in result_string:
        result_string += char

print("Original string:", input_string)
print("String with duplicates removed:", result_string)

# Mehtod 2- Using Set

input_string = input("Enter a string: ")

# Use a set to remove duplicate characters
unique_characters = set(input_string)

# Join the unique characters to form a string
result_string = ''.join(unique_characters)

print("Original string:", input_string)
print("String with duplicates removed:", result_string)