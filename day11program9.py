sample_Dict = {
    "name": "Anu",
    "age":21,
    "salary":70000,
    "city": "New York"}
keys = ["name","salary"]


##newDict={}
##for i in keys:
##    newDict[i]=sample_Dict[i]
##print(newDict)
    
newDict={i:sample_Dict[i] for i in keys}
print(newDict)
