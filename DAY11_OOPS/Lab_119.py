# Concept of Abstraction class and method
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass


class Tiger(Animal):
    def eat(self):
        print("eat non veg")


class Cow(Animal):
    def eat(self):
        print("eat veg")


ob = Tiger()
ob.eat()

ob1 = Cow()
ob1.eat()

# Example 2

from abc import ABC, abstractmethod

class democlass(ABC):
    @abstractmethod
    def method1(self):
        print("abstract method")
        return

    def method2(self):
        print("concrete method")

class concreteclass(democlass):
    def method1(self):
        super().method1()
        return


obj = concreteclass()
obj.method1()
obj.method2()
