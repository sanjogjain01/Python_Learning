# Overloading >> In Python it is not possible to perform method overloading.
# When you have a class with method of one name defined more than one
# but with different argument types and/or return type, it is a case of method overloading.
class example:
    def add(self, a, b):
        x = a + b
        return x

    def add(self, a, b, c):
        x = a + b + c
        return x


obj = example()

print(obj.add(10, 20, 30))
print(obj.add(10, 20))

# return error