# Multiple Decorator

# Note - This is not showing the desired output

num1 = None
num2 = None


def decor_sub(calculator):
    def inner():
        calculator()
        sub = num2 - num1
        return sub

    return inner


def decor_mul(calculator):
    def inner():
        calculator()
        mul = num2 * num1
        return mul

    return inner


@decor_mul
@decor_sub
def calculator():
    global num1
    global num2
    result = (num1 + num2)
    return result


num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
print(f"Calculations are: {calculator()}")
