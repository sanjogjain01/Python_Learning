# elif Statement
# allows you to check multiple expressions for TRUE and
# execute a block of code as soon as one of the conditions evaluates to TRUE

# Program 1
Amount = int(input("enter the amount"))
if (Amount > 3000) and (Amount < 4000):
    print("No Discount applied and  Payable amount : ", Amount)
elif (Amount > 5000) and (Amount < 6000):
    discount = Amount * 10 / 100
elif (Amount > 6000) and (Amount < 8000):
    discount = Amount * 20 / 100
else:
    discount = 0

print("Payable amount : ", (Amount - discount))

# Program 2

amount = int("enter the amount")
print('Amount = ', amount)
if amount > 10000:
    discount = amount * 20 / 100
elif amount > 5000:
    discount = amount * 10 / 100
elif amount > 1000:
    discount = amount * 5 / 100
else:
    discount = 0

print('Payable amount = ', amount - discount)

# Problem  Find the Max between 3 numbers
num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
num3 = int(input("Enter num3"))

# max_num = max(num1, num2, num3)
# print(max_num)


if num1 > num2 and num1 > num3:
    print("Max is ", num1)
elif num2 > num1 and num2 > num3:
    print("Max is ", num2)
else:
    print("Max is ", num3)