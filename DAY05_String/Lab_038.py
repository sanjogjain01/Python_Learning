# Python program to find uncommon words from two Strings

# Method 1 >>
def find_uncommon_words(str1, str2):
    words1 = set(str1.split())
    words2 = set(str2.split())

    uncommon_words = list(words1.symmetric_difference(words2))

    return uncommon_words
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

uncommon_words = find_uncommon_words(string1, string2)

print("Uncommon words:", uncommon_words)


# Method 2
def UncommonWords(A, B):
    A = A.split()
    B = B.split()
    x = []
    for i in A:
        if i not in B:
            x.append(i)
    for i in B:
        if i not in A:
            x.append(i)
    x = list(set(x))
    return x


# Driver Code
A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

# Print required answer
print(UncommonWords(A, B))
