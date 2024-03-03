# Check only Key exists in dict or not

MyDict = {"empid": 101, "X": 102, "Y": 105}

if "empid" in MyDict:
    print("exist")
else:
    print("not exist")

# Adding item to dict

MyDict = {"empid": 101, "X": 102, "Y": 105}

MyDict["color"]= "red"
print(MyDict)

# remove item using pop ()

MyDict.pop("color")
print(MyDict)

MyDict.popitem()  # remove last item from Dict
print(MyDict)