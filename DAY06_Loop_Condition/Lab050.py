# Continue Statement
# Python continue statement is used to skip the execution of the program block
# and returns the control to the beginning of the current loop to start the next iteration
# The continue statement can be used in both while and for loops.

# Program to difference break and Continue

for i in range(7):
    if i == 5:
        continue
    print(i)

print("break statement")
for i in range(7):
    if i == 5:
        break
    print(i)