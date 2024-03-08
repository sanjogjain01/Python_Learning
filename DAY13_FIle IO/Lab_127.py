# Opening of a file

f = open('Text File', 'r')

# open() function to open a file. It takes two arguments:
# the name of the file and the mode in which the file should be opened.
# The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.


# READING A FILE

f = open('Text File', 'r')
print(f)
text = f.read()
print(text)
f.close()

# WRITING A FILE

f = open('Text File', 'a')
# append (a): This mode opens the file for appending only and creates a new file if the file does not exist.
f.write('Hello, world!')
f.close()

with open('Text File', 'a') as f:
    f.write("Hey I am inside with")

# we can use it the "with" statement to automatically close the file after you are done with it
