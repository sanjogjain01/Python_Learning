# Generally, we restrict our data outside in encapsulation
#  It can be achieved by declaring data member and method of a class as Private

# Example 1 of Private Modifier >> not accessbile outside class

class Finance:
    def __init__(self):
        self.__revenue = 50000  # Private data using __
        self._no_of_sale = 200  # Protected data using _


f1 = Finance()


class HR:
    def __init__(self):
        self.no_of_emp = 300
        print(f1.__revenue)  # finance daat can not be accessible in HR class


h1 = HR()  # return error


# Example 2: How we can access Private data >> through method

class Finance:
    def __init__(self):
        self.__revenue = 50000  # Private data using __
        self.__no_of_sale = 200  # private data using __

    def display(self):
        print(f"revenue : {self.__revenue} and sale:{self.__no_of_sale}")


f1 = Finance()
f1.display()
