# Python program to find the sum of natural using recursive function.

def sum(n):
    if n < 1:
        return n
    else:
        return n + sum(n - 1)


num = -8
if num < 0:

    print("enter positive no.")
else:
    print("the sum is ", sum(num))
