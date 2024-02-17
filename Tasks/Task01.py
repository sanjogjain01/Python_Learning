# Program to print Odd Number and even number

number_range = int(input("enter the range upto you want odd number "))

for i in range(1,number_range):
    if i % 2 != 0:
        print("Odd Numbers are  ", i)
    else:
        print("even number are", i)
