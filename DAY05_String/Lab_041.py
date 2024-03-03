# Python program to drop all digits from a string.

def remove_digits(input_string):
    result_string = ''

    for char in input_string:
        if not char.isdigit():
            result_string += char

    return result_string

input_string = input("Enter a string: ")
result = remove_digits(input_string)

print("String with digits removed:", result)
