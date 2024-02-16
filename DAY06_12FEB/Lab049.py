# break Statement
# Python break statement is used to terminate
# the current loop and resumes execution at the next statement

# Program

for letter in 'Python':
    if letter == 'h':
        break
    print('Current Letter :', letter)

# Program 2: Given a list of strings, write a program that prints the first string that starts with the letter "A".
words = ["banana", "cherry", "apricot", "coconut", "kiwi", "avocado", "apple"]

for word in words:
    if word.startswith('A') or word.startswith('a'):
        print(word)
        break
