# In this we try to access Module A and Module B of inside Pack A

import sys

sys.path.append("D:/Python_Learning/DAY12_Module_Package/Pack1")

import ModuleA
import ModuleB

ModuleA.display()
ModuleB.show()

# approach 2

from ModuleA import *
from ModuleB import *


display()
show()
