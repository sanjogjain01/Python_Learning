# Inheritance: Acquiring all the attributes(variables) and behaviour(method ) from one class to another class

# Class A >> variable a,b,c, methods m1,m2 >> A is the parent of B (superclass/base clas)
# Class B(A)>> variable x,y,x , method m3 >> B is the child of A (derived class/subclass)
# Types: Single , multi level, Heirarchy , Multiple


class A:
    def M1(self):
        print("this is class A")


class B(A):  # Inheritance Class A to B Class
    def M2(self):
        print("this is class B")


ob = B()  # Create an object for B Class
ob.M2()  # accessing method for Class B
ob.M1()  # accessing method for Class A
