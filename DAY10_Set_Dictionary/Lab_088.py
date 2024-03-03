# Remove duplicates values  from Dictionary

# Note - Dictionaries in Python cannot have duplicate keys, but if you want to remove duplicate values,
# you can create a new dictionary by iterating over the items of the original dictionary.

original_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

# Create a new dictionary with unique values
unique_dict = {}
for key, value in original_dict.items():
    if value not in unique_dict.values():
        unique_dict[key] = value

print("Original dictionary:", original_dict)
print("Dictionary with duplicate values removed:", unique_dict)

dict1 = {'c': 45, 'b': 95, 'a': 35}

#  sorting dictionary by keys
print(sorted(dict1.items()))
# Output [('a', 35), ('b', 95), ('c', 45)]
#
#  sort dict eys
print(sorted(dict1))
# # output ['a', 'b', 'c']
#
# # sort dictionary values
print(sorted(dict1.values()))
# # output [35, 45, 95]
