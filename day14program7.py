class A:
    def first_method(self):
        print("method of class A...")
class B:
    def second_method(self):
        print("method of class B...")
class c(B,A):
    def third_method(self):
        print("method of class B...")


if __name__=="__main__":
    ob=c()
    ob.first_method()
    #ob.second_method()
    ob.third_method()
