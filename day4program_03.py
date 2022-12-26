def greet(inpstr):
    outstr="GOOD MORNING"+" "+inpstr
    return outstr.title()

inp=input("Enter your name:")
print(greet(inp))
