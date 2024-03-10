# single decorator on multiple function

def decor(fun):
    def inner(*args):
        for num in args[1:]:
            if num == 0:
                return "can not divide by zero"
        return fun(*args)

    return inner


@decor
def div1(a, b):
    return a / b


@decor
def div2(a, b, c):
    return a / b / c


print(div2(10, 5, 5))
print(div1(10, 2))
