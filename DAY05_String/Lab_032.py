# Modify Strings - a string (object of str class) is of an immutable type.
# Since String is Immutable but we can do it by converting String into List

# Example to show how we can modify String

Initial_string = "Hello World"
print(f"Original String : {Initial_string}")

L1 = list(Initial_string)

L1.insert(5, "L")
print(L1)

Initial_string = ''.join(L1)
print(f"Modified String :{Initial_string}")
