# Consider this is a operation module 2

#  Approach 1
'''
import Lab_122

Lab_122.add(10,30)
Lab_122.mul(2,6)
'''


# Approach 2
from DAY12_Module_Package.Lab_122 import add,mul
add(30,50)
mul(4,6)


# Approach 3

from Lab_122 import *
add(40,50)