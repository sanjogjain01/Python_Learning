# Python program to remove all non-alphabetic characters from a string

input_string = input("Enter a string: ")

# Use a loop to build a string with only alphabetic characters
filtered_string = ''
for char in input_string:
    if char.isalpha():
        filtered_string += char

print("Original string:", input_string)
print("String with non-alphabetic characters removed:", filtered_string)

# Method 2 >> Using Alpha method and filter function

input_string = input("Enter a string: ")

# Use filter and isalpha to keep only alphabetic characters
filtered_string = ''.join(filter(str.isalpha, input_string))

print("Original string:", input_string)
print("String with non-alphabetic characters removed:", filtered_string)


