# Python program to sort the characters in a string

input_string = input("Enter a string: ")

# Use sorted() to sort the characters
sorted_string = ''.join(sorted(input_string))

print("Original string:", input_string)
print("Sorted string:", sorted_string)
