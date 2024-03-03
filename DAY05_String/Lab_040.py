# Python program to list unique characters with their count in a string

input_string = input("Enter a string: ")
char_count = {}

for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Unique characters with their count:")
for char, count in char_count.items():
    print(f"'{char}': {count}")


# Metjod 2 Using Function

def count_unique_characters(input_string):
    char_count = {}

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


input_string = input("Enter a string: ")
result = count_unique_characters(input_string)

print("Unique characters with their count:")
for char, count in result.items():
    print(f"'{char}': {count}")

# Method 3-using collections.Counter class

from collections import Counter

input_string = input("Enter a string: ")

char_count = Counter(input_string)

print("Unique characters with their count:")
for char, count in char_count.items():
    print(f"'{char}': {count}")
