def printDetail(name,marks):
    print("Name:",name)
    print("Marks:",marks)
    return None
#printDetail()#TypeError
#printDetail('Anusha')#TypeError
#printDetail('Anusha',80)

#printDetail(80,'Anusha')
printDetail(marks=80,name='Anusha')
