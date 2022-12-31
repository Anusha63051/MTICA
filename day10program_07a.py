fo1=open(r"D:\pythonpractice03\day10\abc.txt","r")
fo2=open(r"D:\pythonpractice03\day10\abc.txt","w+")

temp=fo1.read()
fo2.write(temp)

fo1.close()
fo2.close()
print("File Copied")
                 

