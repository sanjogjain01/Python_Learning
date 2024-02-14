# if Statement >> If the boolean expression evaluates to TRUE,
# then the block of statement(s) inside the if statement is executed.
# If boolean expression evaluates to FALSE, then the first set of code after the end of the if statement(s) is executed.
"""
Syntax
if expression:
  statement(s) """

# Program 1

amount = int(input("enter the purchase amount"))
discount = int(input("enter the percentage of discount that you apply"))
discount = amount * 10 / 100
if amount > 5000:
    print("selling price=", (amount-discount))






