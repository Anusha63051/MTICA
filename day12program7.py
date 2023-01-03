class Student:
    college='MTICA'
    cource='MCA'
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def displayStudent(self):
        print("Name : "+self.name.title()+'\nRoll.no : '\
              +str(self.rollno))
        print('college : '+self.college+'\ncource : '+self.cource)
lstOb=[]
for i in range(2):
    n=input()
    r=int(input())
    temp='Ob'+str(i)
    temp=Student(n,r)
    lstOb.append(temp)
for i in lstOb:
    i.displayStudent()

