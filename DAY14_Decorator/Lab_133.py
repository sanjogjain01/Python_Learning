
# # Multiple Decorator on a single function
def decor1(fun):
    def inner():
        return fun().upper()

    return inner


def decor2(fun):
    def inner():
        return fun().split()

    return inner


@decor2
@decor1

def get_name():
    name = input("Enter first name")
    sirname = input("Enter sirname")
    full_name = name + "" + sirname


    return full_name


print(get_name())
