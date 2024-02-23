# Tuples is immutable i.e cant chane the tuples objects

#tup1 = ("a", "b", "c", "d")
#tup1[2] = 'Z'
#print("tup1: ", tup1)  # show error

# How to Update a Python Tuple?
# Using the list() function, convert the tuple to a list, perform the desired append/insert/remove operations and
# then parse the list back to a tuple object.

tup1 = ("a", "b", "c", "d")
print("Tuple before update", tup1)

list1 = list(tup1)
list1[2] = 'F'
list1.append('Z')
list1.sort()
print("updated list", list1)

tup1 = tuple(list1)
print("Tuple after update", tup1)
