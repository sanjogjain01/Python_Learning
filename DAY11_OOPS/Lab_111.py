# Hirarchy Level Inhritance

# Multi level Inheritance

class A:
    x, y = 40, 50

    def M1(self):
        print(self.x + self.y)


class B(A):  # Inheritance Class A to B Class
    a, b = 500, 200

    def M2(self):
        print(self.a - self.b)


class C(A):  # Hierarchy inheritance >> single parent with multiple Child
    i, j = 5, 6

    def M3(self):
        print(self.i * self.j)


Ob = B()
Ob.M1()
Ob.M2()
Ob1 = C()
Ob1.M3()


