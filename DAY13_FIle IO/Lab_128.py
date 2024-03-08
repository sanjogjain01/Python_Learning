# readlines() method
#reads a single line from the file. If we want to read multiple lines, we can use a loop
f = open('Text File', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)

# Writeliness method()
# The writelines() method in Python writes a sequence of strings to a file.
# The sequence can be any iterable object, such as a list or a tuple.

f = open('Text File', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
print(f)
f.close()