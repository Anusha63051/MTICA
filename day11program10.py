sample_dict = {
    "name": "Anu",
    "age":21,
    "salary":7000,
    "city": "New York"}
keys = ["city","age"]


res = dict()
for k in keys:
   res.update({k: sample_dict[k]})
print(res)
    


