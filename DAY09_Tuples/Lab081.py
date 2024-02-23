# join Tuples

T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
T3 = T1+T2 # Using + operator
print ("Joined Tuple:", T3)

# Program 2

T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
L1 = list(T1)
L2 = list(T2)
L1.extend(L2)  # Using exxtend method
T1 = tuple(L1)
print ("Joined Tuple:", T1)

# Program 3

T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
T3 = sum((T1, T2), ())
print ("Joined Tuple:", T3)