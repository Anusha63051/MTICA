def div(a,b):
    assert( isinstance(a,int) or isinstance(a,float)),\
                'First Argument should be either Integer or Float'
    assert( isinstance(b,int) or isinstance(b,float)),\
                'Second Argument should be either Integer or Float'
           
    assert(b!=0),"Divison by zero is not defined"
    return a/b
    
try:
    print(div(55,0))
except AssertionError as ob:
    print(ob)
try:
    print(div(20,3))
except AssertionError as ob:
    print(ob)
try:
    print(div('hello',20))
except AssertionError as ob:
    print(ob)
try:
    print(div(20,'hello'))
except AssertionError as ob:
    print(ob)
