# Unpacking Tuples
# "unpacking" refers to the process of parsing tuple items in individual variables

# Program To store tuple items in individual variables

tup1 = (10, 20, 30)
x, y, z = tup1
print("x: ", x, "y: ", "z: ", z)

# If the number of variables is more or less than the length of tuple Prefix "* is used

tup1 = (10,20,30)
x, *y = tup1
print ("x: ", "y: ", y)

# What if we add "*" to the first variable?

tup1 = (10,20,30, 40, 50, 60)
*x, y, z = tup1
print ("x: ",x, "y: ", y, "z: ", z)