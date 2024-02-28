# Abstraction-Abstraction is a fundamental concept in object-oriented programming (OOP)
# that allows us to represent complex systems by simplifying and hiding unnecessary details
# Abstract Class contains one or more methods
# Abstract method is a method declared only but no implementation

# Example of abstract class
from abc import ABC, abstractmethod


class A(ABC):  # ABC is to define abstract class
    @abstractmethod  # to define abstract method
    def display(self):
        None


class B(A):
    def display(self):
        print("this is display method of abstract class")


obj = B()  # We cant create an object of abstract class. SO creating object of subclass
obj.display()

