# Python program to create a list of 5 random integers.

import random
L1 = []
for i in range(5):
   x = random.randint(0, 100)
   L1.append(x)
print (L1)