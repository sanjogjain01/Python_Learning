# Class is a group of objects which have common properties. No memory is allocated when class is createdand Objects
# Object-: an object is a real world entity, or we can say instance of a Class. Objects allocate memo

# Creating Class >> collection of method(behavoiur)  and variable (attributes)
class Students:
    name = "Sanjog"


# Creating Object >> for one class we can create a multiple object
ob = Students()  # ob is an object of class Students
ob1 = Students() # ob1 is another object
print(ob.name)
print(ob1.name)
