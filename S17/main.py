MyDict = {"Name":"Ali", 
          "Family":"Hosseini", 
          "STID": 403521078}

# print(MyDict["Name"])

# keyList = MyDict.keys()
# print(keyList)

for key in MyDict:
    print(key," : ", MyDict[key])

MyDict["Age"] = 30
print(MyDict)
MyDict["Age"] = 50
print(MyDict)

a = MyDict.pop("Name")
print(a)
print(MyDict)

del MyDict["Family"]
print(MyDict)

