# Explain Decorator
# are a very powerful and useful tool in Python since it allows programmers to modify
# the behavior of a function or class. Decorators allow us to wrap another function
# in order to extend the behavior of the wrapped function, without permanently modifying it.
# In normal function, we pass parameter but in decorator we pass the function. like def fun(fun 1):
# we will use decorator when we need to change the behaviour of a function without modifying the function irself
# we can also use we need to run the same code on multiple function


# def decor(func):  # func is a parameter
#     def inner():
#         func()
#         print("Welcome 3")
#
#     return inner
#
#
# def printer():
#     print("Welcome 1")
#     print("Welcome 2")
#
#
# printer = decor(printer)
# printer()

# The above can be used with @ symabol
def decor(func):  # func is a parameter
    def inner():
        func()
        print("Welcome 3")

    return inner


@decor
def printer():
    print("Welcome 1")
    print("Welcome 2")


printer()
