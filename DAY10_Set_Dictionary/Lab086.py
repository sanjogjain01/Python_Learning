# Adding item to Set using Add() >> adding only single item to set at a time
# and  update() >> add  multiple item in a set using update

MySet = {"apple", "Cat", "banana", "grapes"}

MySet.add("Dog")
print(MySet)
MySet.update(["mango", "tiger"])
print(MySet)

# Number of items is a set
MySet = {"apple", "Cat", "banana", "grapes"}
print(len(MySet))

# remove item from set using Remove
MySet = {"apple", "Cat", "banana", "grapes"}
MySet.remove("grapes")
print(MySet)
# Note- if we try to remove  item which is not availble in set then it return key error

# remove item from set using discard
MySet = {"apple", "Cat", "banana", "grapes"}
#MySet.discard("grapes")
MySet.discard("XYZ") # it will not retrn key error

# Note>> The  main diference remove() and discrad(), discrad() function not return any error while accessing
# non existence of the item of set while remove () return error of key error