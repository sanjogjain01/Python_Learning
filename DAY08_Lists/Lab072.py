# Remove List Items

# using remove method()

list1 = ["Rohan", "Physics", 21, 69.75]
print ("Original list: ", list1)

list1.remove("Physics") #  removes the object given as argument
print ("List after removing: ", list1)

# Using the pop() Method >>
list1 = ["Rohan", "Physics", 21, 69.75]
print ("Original list: ", list1)

list1.pop(1)  # pop() removes an item at the given index.
print ("List after removing: ", list1)

# Using delete keyword

list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
del list1[2]
print ("List after deleting: ", list1)