# Use 0f * Operator in String

str1 = "Hello"
str2 = "World"
print("String 1:", str1)
print("String 2:", str2)
str3 = str1 + str2 * 3
print("String 3:", str3)
str4 = (str1 + str2) * 3
print("String 4:", str4)


# Check String is Palindrome

user_input = input("Enter a string: ")

# Clean the input by removing spaces and converting to lowercase
cleaned_string = ''.join(user_input.split()).lower()

# Check if the cleaned string is equal to its reverse
if cleaned_string == cleaned_string[::-1]:
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')
