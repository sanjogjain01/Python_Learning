# Encapsulation: It describes the idea of wrapping data and the methods that work on data within one unit. This puts
# restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
# Ex - data for sections such as sales, finance, and accounts are hidden from all other sections.

# With the help of Access Modifier, We restrict our Data 1. Public Access Modifier - all daat are accessible from any
# 2. Private members - Accessible within class.Accessible via method
# 3. Protected member - Accessible within class and its subclass
# Example of Public Access Modifier

class Finance:
    def __init__(self):
        self.revenue = 50000
        self.no_of_sale = 200


f1 = Finance()


class HR:
    def __init__(self):
        self.no_of_emp = 300
        print(f1.revenue)  # finance daat can be accessible in HR class


h1 = HR()

# print(f1.revenue) # print revenue of Finance Class which should be there in a pratical world

# To private own data, we use protected modifier to restrict  our data
