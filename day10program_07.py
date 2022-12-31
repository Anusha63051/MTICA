fo=open(r"D:\pythonpractice03\day10\abc.txt","a")
for i in range(5):
    inpstr=input("Enter string:")
    fo.write(inpstr+'\n')
fo.close()
print("Written to file")
    
                 
