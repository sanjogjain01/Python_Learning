# Return Statement - return keyword as the last statement in function definition
# indicates an end of function block, and the program flow goes back to the calling function

# Program: write function to accept input and return sum

def add(x, y):
    z = x + y
    return z  # 12
    return  # print none as output


result = add(7, 5)
print(result)


# program tto print even or odd number using function

def odd_even(num):
    if num % 2 == 0:
        print(num, "is even number")
    else:
        print(num, "is odd number")

    return


odd_even(78)
