# Program: Class name- Emp
# contractor :eid, ename, sal
# display all the values using another method

class Emp:
    def __init__(self, eid, ename, sal):
        self.eid = eid  # now all  these variables are class variable
        self.ename = ename
        self.sal = sal

    def myfun(self):
        print(self.eid, self.ename, self.sal)


ob = Emp("23", "sonu", 25000)
ob.myfun()
ob2 = Emp("23", "sonu", 25001)
ob2.myfun()

