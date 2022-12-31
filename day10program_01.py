dict1={'Name': 'Anu', 'Age' :21, 'Class':'Mca'}
print(dict1.keys())
print(dict1.items())
print(dict1.values())
print("Values:")
for i in dict1.values():
    print(i,end=' ')
print("Keys:")
for i in dict1.keys():
    print(i,end=' ')
    print("Items")
for i,j in dict1.items():
    print(i,j)
