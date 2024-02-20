# Types of argument

# Default Argument - arguments that will be used if no arguments are passed to the function call.

# program to show the default argument of a function

def printinfo(name="sanjog", age=35):
    # "This prints passed info into this function"
    print("Name: ", name)
    print("Age ", age)
    return


# Now we can call print info function
printinfo(age=50, name="miki")

printinfo(name="miki")
printinfo()  # return by default
