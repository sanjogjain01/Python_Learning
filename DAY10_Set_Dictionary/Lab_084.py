# Change Value in Dictionary

MyDict = {"empid": 101, "X": 102, "Y": 105}

MyDict["empid"] = 110
print(MyDict)

# Reading item from Dict using Loop

for i in MyDict:
    print(i)  # it prints only key but not value

for i in MyDict:
    print(MyDict[i])  # return also values


for x,y in MyDict.items():
    print(x,y)  # print both key and value