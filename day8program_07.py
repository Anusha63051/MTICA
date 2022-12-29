num1=input("Enter a number:")
num2=input("Enter a number:")

try:
    res=int(num1)/int(num2)
except (ZeroDivisionError,ValueError):
    print("Exception handled by Anu")

except Exception as ob:
    print(ob)
else:
    print(num1, '/',num2, '=',res)
finally:
    print('Thanks')

print("visit again for python class at MTICA")
        
