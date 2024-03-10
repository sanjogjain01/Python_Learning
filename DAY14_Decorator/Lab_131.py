# Example 3 of decorator function


def decor(addition):
    def inner():
        result = addition()
        num3 = int(input("Enter 3rd number"))
        result = result + num3
        return result

    return inner


@decor
def addition():
    num1 = int(input("Enter 1st number"))
    num12 = int(input("Enter 2nd number"))
    result = (num1 + num12)
    return result


addition = decor(addition)

print(f"Addition of number is : {addition()}")
