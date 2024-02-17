#  program to get the Fibonacci series between 0 and 50
# Method 1

num = int(input("Enter the number of terms for Fibonacci series: "))
a, b = 0, 1
print(a, end=" ")
while b <= num:
    print(b, end=" ")
    a, b = b, a + b

# Method 2

num = 10
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3)

# Method 3

num = int(input("Enter the number of terms for Fibonacci series: "))

a, b = 0, 1

print(a, end=" ")
for _ in range(num):
    a, b = b, a + b
    print(b, end=" ")
