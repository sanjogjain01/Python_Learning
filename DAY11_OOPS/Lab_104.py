# when do We have the same variables name (global, local, class) using global() function

a, b = 10, 20


class MyClass1:
    a, b = 30, 40

    def add(self, a, b):
        print(a + b)  # x,y are local Variables
        print(self.a + self.b)  # a,b are class variable
        print(
            globals()['a'] + globals()['b'])  # we use global() function to use global variable if variable name is same


ob1 = MyClass1()
ob1.add(100, 200)
