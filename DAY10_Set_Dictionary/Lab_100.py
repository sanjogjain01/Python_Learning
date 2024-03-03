# calculate the square of each even number from a list and store in dict
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a dictionary to store square of even numbers
squares_dict = {}

for number in original_list:
    if number % 2 == 0:
        squares_dict[number] = number ** 2

print("Original list:", original_list)
print("Dictionary with squares of even numbers:", squares_dict)