#  Python program to print all the even numbers within the given range.
given_range = int(input("enter given range"))

for i in range(10,given_range):
    if i % 2 == 0:
        print(i)
