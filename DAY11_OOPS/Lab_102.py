# function inside Class called as methods
# 2 types of method inside the class
# Instance Method (we can call only through an object) and Static method (directly call using class)

# Example 1: Instance Method
class MyClass:
    def myfun(self):  # self is the by default parameter when we create a method inside class.
        # self means this particular method belongs to this class
        pass  # Pass means none it means we are not implementing anything in this function

    def display(self):
        print("Sanjog")


ob = MyClass()  # >> ob is object variables but in actual MyClass() is an object

ob.myfun()  # return nothing since three is no implementation inside this function
ob.display()  # return sanjog
MyClass().display()  # it also returns sanjog


# Example 2: Static Method >> this method is common for all the objects of the Class

class Myfun2:
    def m1(self, age):
        print(age)

    @staticmethod  # in static method sef keyword is not required
    def m2(self, name):  # self is not by default in static method it is an argument
        print(self, name)


ob = Myfun2()
ob.m1("70")
# ob.m2("sanjog") # return error since here self is also treated as an agreement, so we need to pass two values
# ob.m2("sanjog", "kumar")

Myfun2.m2("sanjog", "jain")  # invoking Static method directly with class without any object
