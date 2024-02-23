# Add List Items
# There are two methods of the list class
# append() and insert(), that are used to add items to an existing list.

# Program 1 :  append() method adds only one item at the end of an existing list.

list1 = ["a", "b", "c", "d"]
print("Original list: ", list1)
list1.append('e')
print("List after appending: ", list1)

# Program 2 :insert() method inserts the item at a specified index in the list.

list1 = ["Rohan", "Physics", 21, 69.75]
print("Original list ", list1)

list1.insert(2, 'Chemistry')
print("List after appending: ", list1)

list1.insert(-1, 'Pass')
print("List after appending: ", list1)

# Program 3: Appending multiple items to a list using “extend

my_list = [1, 2, 3]
new_items = [4, 5, 6]

my_list.extend(new_items)

print(my_list)
