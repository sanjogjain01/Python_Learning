# Program 2: Python program to calculate the sum of all numbers from 1 to a given number.

Given_range = int(input("Enter the number range "))
sum = 0
for i in range(Given_range + 1):
    sum += i
print(sum)
