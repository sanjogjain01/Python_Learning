# Override Concept >> when we have the same method in child with different implementation
# Calling parent class method using super keyword
class A:
    def M1(self):
        print("This is M1 method of Class A")


class B(A):
    def M1(self):  # same method as parent but with different implementation
        print("This is M1 method of Class B")
        super().M1()  # also invoke parent class method


ob = B()
ob.M1()


# Accessing Variable in Child Class

class A:
    x, y = 10, 20


class B(A):
    i, j = 20, 30

    def M1(self, a, b):  # same method as parent but with different implementation
        print(a + b)
        print(self.x + self.y)
        print(self.i + self.j)


ob = B()
ob.M1(300,400)

