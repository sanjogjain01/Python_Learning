# Program 2: Python program to calculate the sum of all sum numbers from 1 to a given number range.

given_number = int(input("enter the range of Number"))
even_sum = 0
odd_sum = 0
for i in range(1, given_number):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("Sum of even number ", even_sum)
print("Sum of even number ", odd_sum)