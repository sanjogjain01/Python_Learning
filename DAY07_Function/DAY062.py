#  Arbitrary Arguments
# define a function that is able to accept arbitrary or variable number of arguments
# An argument prefixed with a single asterisk * for arbitrary positional arguments.
# An argument prefixed with two asterisks ** for arbitrary keyword arguments.

def add(*x):
    s = 0
    for i in x:
        s = s + i
    return s


result = add(10, 20, 30, 60)
print(result)


# Program 2

def addr(**kwargs):
    for k, v in kwargs.items():
        print("{}:{}".format(k, v))


print("pass two keyword args")
addr(Name="John", City="Mumbai")
print("pass four keyword args")

# pass four keyword args
addr(Name="Raam", City="Mumbai", ph_no="9123134567", PIN="400001")
