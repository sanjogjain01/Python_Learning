# Any function that calls itself in its body repeatedly until a particular condition becomes false and the target
# task is done is called a "Recursive function" and this procedure is called "Recursion".

# program to find factorial using recursion
def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)


# Example usage:
result = factorial(5)
print("Factorial of 5:", result)
