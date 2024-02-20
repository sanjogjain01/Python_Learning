# Creation of List
# 1. Creation of empty lis

list_ob = []
print(list_ob)

# 2.
ob = [10, 20, 30, 40, "s", "%"]
print(ob)

# 3. with dynamic input

list_ob = eval(input("Enter ist: ")) # The eval() function evaluates the specified expression, if the expression is a legal Python statement, it will be

print(list_ob)

# with list function

l = list(range(0, 10, 2))
print(l)

s= "sanjog"
l= list(s)
print(l)

# with Split() function

l1 = input("Enter list 1 (e.g., 1, 2, 3): ").split(',')
l2 = input("Enter list 2 (e.g., 'a', 'b', 'c'): ").split(',')

print(l1)
print(l2)
