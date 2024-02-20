# Access List Items
# Each object in the list is accessible with its index

# write a program to enter a lists and access to it

l1 = eval(input("enter list 1 :"))
l2 = eval(input("enter list 2 :"))

l3 = input("Enter list 1 (e.g., 1, 2, 3): ").split(',')
l4 = input("Enter list 2 (e.g., 'a', 'b', 'c'): ").split(',')
# When we use the input function, it takes user input as a string.
# Therefore, we need to convert the input to a list using the eval function or by manually splitting the input string.
print("Item at 0th index in list1: ", l1[0])
print("Item at 0th index in list1: ", l2[2])
print("Item at 0th index in list1: ", l1[-2])
print("Item at 0th index in list1: ", l2[-2])

# Program 2

list1 = ["a", "b", "c", "d"]
list2 = [25.50, True, -55, 1+2j]
list4 = ["Rohan", "Physics", 21, 69.75]
list3 = [1, 2, 3, 4, 5]

print ("Items from index 1 to last in list1: ", list1[1:])
print ("Items from index 0 to 1 in list2: ", list2[:2])
print ("Items from index 2 to last in list3", list3[2:-1])
print ("Items from index 0 to index last in list4", list4[:])