# while

# Calculate the sum of numbers until user enters 0

num = int(input("enter the numbers"))
total = 0
while num != 0:
    total = total + num  # total += num
    num = int(input("enter the numbers"))
print('The sum is', total)

