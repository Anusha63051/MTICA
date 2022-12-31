def fun(str1):
    print(str1)
fun("I'm first call to user defined function!")
fun("Again second call to the same function")


def printme(str1,n):
    n[0]='Anusha'
    print(str1,n)
    return

x=['Anusha','Sridhar']
printme("Wakeup",x)
print('x:',x)
