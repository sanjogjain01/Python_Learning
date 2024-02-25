# To simulate "method overloading" (Polymorhism),
# we can use a workaround by defining default value to method arguments as None,
# so that it can be used with one, two or three arguments.

# Example:1 Overloading(Polymorphism)

class Human:
    def Hello(self, name=None):
        if name is not None:
            print("Hello" + name)
        else:
            print("hello")


ob = Human()
ob.Hello("sonu")
ob.Hello()


# Example 2: Overloading

class Cal:
    def Calculation(self, a=0, b=0, c=0):
        print(a + b + c)


ob = Cal()
ob.Calculation()
ob.Calculation(10, 20)
ob.Calculation(10, 20, 30)
