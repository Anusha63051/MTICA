def sum_num(x):
    res=0
    for i in range(x+1):
        res=res +i
        yield("i=",i,"res=",res)
    return res
ob=sum_num(5)
for i in range(6):
    print(next(ob))
