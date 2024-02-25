# Single Inheritance

class A:
    x, y = 40, 50

    def M1(self):
        print(self.x + self.y)


class B(A):  # Inheritance Class A to B Class
    a, b = 500, 200

    def M2(self):
        print(self.a-self.b)


ob = B()  # Create an object for B Class
ob.M2()  # accessing method for Class B
ob.M1()  # accessing method for Class A
