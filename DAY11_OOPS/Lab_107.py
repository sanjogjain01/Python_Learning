# Program: Class name- Emp
# contractor :eid, ename, sal
# display all the values using contructor

class Emp:
    def __init__(self, eid, ename, sal):
        self.eid = eid  # now all  these variables are class variable
        self.ename = ename
        self.sal = sal

    def __str__(self):
        return (self.ename, self.sal)  # it returns error since __str__ return only string value
        return (self.ename)  # return sonu


ob = Emp("23", "sonu", 25000)
print(ob)
