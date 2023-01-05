class Wolf:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print("Grr...")
class Dog(Wolf):
    def bark(self):
        print("woof")
pet1=Dog("Munna","White")
pet1.bark()
pet2=Wolf("Tommy","Brown")
pet2.bark()
Dog("abc","xyz").bark()
