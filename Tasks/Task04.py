# Python program to find the factorial of a given number.

given_number = int(input("enter the range of Number"))

factorial = 1  # since 1 is a factor of all number set the factorial to 1
for i in range(1,given_number):
    factorial *= i

print("The factorial of ", given_number, " is ", factorial)
