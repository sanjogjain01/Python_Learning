# Position Argument :argument passed to function in correct postion

def sub(a, b):
    print(a - b)


sub(100, 200)  # argument and position must be matched

#sub(200, 100, 80)  # if we change no. of argument it will show error
sub(200, 100)

#sub("hell0", 100) # Data type of corresponding actual and formal arguments must match.