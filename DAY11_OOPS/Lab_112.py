# Multiple Inhritance >> multiple parents for single child Class

# Multi level Inheritance

class A:  # Class parent
    x, y = 40, 50

    def M1(self):
        print(self.x + self.y)


class B:  # Class B parent
    a, b = 500, 200

    def M2(self):
        print(self.a - self.b)


class C(A, B):  # Multiple Inheritance
    i, j = 5, 6

    def M3(self):
        print(self.i * self.j)


ob = C()
ob.M1()
ob.M2()
ob.M3()
