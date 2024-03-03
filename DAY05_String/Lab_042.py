# Python program to find the number of vowels in a given string.

Mystr = "All animals are equal. Some are more equal"
vowels = "aeiouAEIOU"
count = 0
for x in Mystr:
    if x in vowels:
        count += 1
print("Number of Vowels:", count)


# Using Function
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count


# Example usage
input_string = input("Enter a string: ")
result = count_vowels(input_string)

print("Number of vowels in the given string:", result)


