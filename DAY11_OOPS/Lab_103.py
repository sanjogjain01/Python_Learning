# Variables are : Global, Class and Local Variables

# Class Variable

class MyClass:
    a, b = 10, 20  # Class Variable

    def add(self):
        print(self.a + self.b)  # we can use class variable inside method using self
        # print(a,b)  # return error, we cant directly access class variable inside method


ob = MyClass()
ob.add()

# Exercise 2

i, j = 10, 20


class MyClass1:
    a, b = 30, 40

    def add(self, x, y):
        print(x + y)              # x,y are local Variables
        print(self.a + self.b)  # a,b are class variable
        print(i + j)


ob1 = MyClass1()
ob1.add(100,200)
