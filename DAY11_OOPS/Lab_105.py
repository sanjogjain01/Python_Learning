# Constructor:
# Constructor name is fixed :-   __init__(self)
# Contractor can take argument, and parameter
# Contractor will be called at the time of object creation
# Contractor will not return any value

# Example

class MyClass:
    def __init__(self):
        print("this is a contractor")

    def myfun(self):
        print("this is a method")


ob = MyClass()  # invoke the contructor automatically
ob.myfun()  # for method, we need to call explicit using an object


# Example 2 : Parameter constructor

class MyClass:
    name = "XYZ"

    def __init__(self, name):
        print(name)  # Local variable
        print(self.name)  # Class variable


ob = MyClass("sanjog")  # passing parameter to constructor

