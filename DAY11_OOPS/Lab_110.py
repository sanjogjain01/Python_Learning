# Multi level Inheritance

class A:
    x, y = 40, 50

    def M1(self):
        print(self.x + self.y)


class B(A):  # Inheritance Class A to B Class
    a, b = 500, 200

    def M2(self):
        print(self.a - self.b)


class C(B):  # Multilevel inheritance
    i, j = 5, 6

    def M3(self):
        print(self.i * self.j)


Ob = C()
Ob.M3()
Ob.M2()
Ob.M1()
