sample_dict = {
    "name": "Anu",
    "age":21,
    "salary":7000,
    "city": "New York"}
keys = ["name","salary"]


d=dict()
for i in sample_dict.keys()-keys:
    d[i]=sample_dict[i]
print(d)
    


