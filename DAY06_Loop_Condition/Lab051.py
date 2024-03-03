# Checking Prime Factors

num = int(input("Accept input from user"))
print("prime factor of ",num)
d = 2
while num > 1:
    if num % d == 0:
        print(d)
        num = num / d
        continue
    d = d + 1
