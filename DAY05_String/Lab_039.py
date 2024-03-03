# Reverse the words in the given string program

def reverse_words(input_string):
    words = input_string.split()  # Split the string into a list of words
    reversed_words = ' '.join(reversed(words))  # Reverse the order of words
    return reversed_words


input_string = "Hello World! Python is awesome."
result = reverse_words(input_string)
print(result)
