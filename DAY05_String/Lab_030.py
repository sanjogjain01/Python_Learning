# String- Strings in Python are sequences of characters,
# and Python provides various methods to manipulate and work with strings
# A string is a non-numeric data type. Obviously, we cannot use arithmetic operators with string operands
# String is immutable
var="HELLO PYTHON"
var[7]="y"
print (var)  # it returns type error because string is immutable




#  String Methods
# 1. len() method:

my_string = "Hello, World!"
length = len(my_string)
print(f"Length of the string: {length}")

#  F-strings allow you to embed expressions inside string literals, using curly braces {}

# 2. count() method:
my_string = "banana"
count_a = my_string.count("a")
print("Number of 'a' in the string:", count_a)

# 3. replace() method:

my_string = "Hello, World!"
new_string = my_string.replace("Hello", "Hi")
print("Updated string:", new_string)
