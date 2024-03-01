# Abstract Class and method
from abc import ABC, abstractmethod


class XYZ(ABC):
    @abstractmethod
    def M1(self):
        pass

    @abstractmethod
    def M2(self):
        pass


class Y(XYZ):
    def M1(self):
        print("This is M1 ")


# ob = Y()
# ob.M1() # show error Can't instantiate abstract class Y without an implementation for abstract method 'M2'

class Z(Y):
    def M2(self):
        print("this is M2 of abstract method")


Ob = Z()
Ob.M2()
Ob.M1()


# Example

class Cal(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def Add(self):
        pass

    @abstractmethod
    def Sub(self):
        pass


class C(Cal):
    def Add(self):
        print(self.value + 100)

    def Sub(self):
        print(self.value - 10)


ob = C(200)
ob.Add()
ob.Sub()
