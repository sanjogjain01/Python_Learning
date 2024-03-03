# 4. Split Method >>Splits a string into a list of substrings based on a specified delimiter

my_string = "apple,orange,banana"
fruits_list = my_string.split(",")
print("List of fruits:", fruits_list)


# join() method:
# Joins elements of an iterable (e.g., a list) into a single string using the specified separator.
fruits_list = ["apple", "orange", "banana"]
joined_string = ", ".join(fruits_list)
print("Joined string:", joined_string)